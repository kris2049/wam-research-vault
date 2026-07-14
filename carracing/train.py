"""
CarRacing x LeCun World Model — Complete Training Script
Single GPU, 8-12GB VRAM

Usage:
    python train.py [--resume checkpoint.pt]

Phases:
    1. Collect data with random policy
    2. Train Perception + World Model (JEPA)
    3. Train Cost Head
    4. Train Configurator
    5. Joint fine-tuning with CEM planning
"""
import os, sys, time, math, random
from collections import deque
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import gymnasium as gym

from config import Config as C
from models import (
    Perception, WorldModel, CostHead, Configurator,
    update_ema, compute_on_track_label, compute_scene_label
)


# ═══════════════════════════════════════════════════════════════
#  Replay Buffer
# ═══════════════════════════════════════════════════════════════

class ReplayBuffer:
    def __init__(self, capacity=C.buffer_capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, frame, action, reward, next_frame, done, progress=0):
        """Store transition. frame/next_frame are 96×96×3 uint8."""
        self.buffer.append((
            frame.astype(np.uint8),
            action.astype(np.float32),
            np.float32(reward),
            next_frame.astype(np.uint8),
            np.float32(done),
            np.float32(progress),
        ))

    def sample(self, batch_size):
        idxs = np.random.choice(len(self.buffer), batch_size, replace=False)
        frames, actions, rewards, next_frames, dones, progresses = zip(
            *[self.buffer[i] for i in idxs]
        )
        # Convert HWC→CHW: stored as [96,96,3], model expects [3,96,96]
        frames_np = np.stack(frames)           # [B, H, W, C]
        next_np = np.stack(next_frames)        # [B, H, W, C]
        return (
            torch.FloatTensor(frames_np).permute(0, 3, 1, 2).div_(255.0),  # [B,C,H,W]
            torch.FloatTensor(np.stack(actions)),                            # [B,3]
            torch.FloatTensor(np.stack(rewards)).unsqueeze(1),               # [B,1]
            torch.FloatTensor(next_np).permute(0, 3, 1, 2).div_(255.0),     # [B,C,H,W]
            torch.FloatTensor(np.stack(dones)).unsqueeze(1),                 # [B,1]
            torch.FloatTensor(np.stack(progresses)).unsqueeze(1),            # [B,1]
        )

    def __len__(self):
        return len(self.buffer)

    def save(self, path="buffer_phase1.npz"):
        """Persist buffer to disk as compressed numpy archive."""
        frames, actions, rewards, next_frames, dones, progresses = zip(*self.buffer)
        np.savez_compressed(path,
            frames=np.stack(frames),
            actions=np.stack(actions),
            rewards=np.stack(rewards),
            next_frames=np.stack(next_frames),
            dones=np.stack(dones),
            progresses=np.stack(progresses),
        )
        size_mb = os.path.getsize(path) / 1024 / 1024
        print(f"  💾 Buffer saved: {path} ({size_mb:.1f} MB, {len(self.buffer)} transitions)")

    @classmethod
    def load(cls, path="buffer_phase1.npz"):
        """Restore buffer from disk."""
        data = np.load(path)
        buf = cls(capacity=len(data['frames']))
        frames = data['frames']
        actions = data['actions']
        rewards = data['rewards']
        next_frames = data['next_frames']
        dones = data['dones']
        progresses = data['progresses']
        for i in range(len(frames)):
            buf.push(frames[i], actions[i], rewards[i], next_frames[i], dones[i], progresses[i])
        print(f"  📂 Buffer loaded: {path} ({len(buf)} transitions)")
        return buf


# ═══════════════════════════════════════════════════════════════
#  CEM Planner
# ═══════════════════════════════════════════════════════════════

class CEMPlanner:
    """
    Cross-Entropy Method planner operating in latent space.
    Takes current state, uses WorldModel to imagine trajectories,
    CostHead to evaluate them, returns optimal action.
    """
    def __init__(self, world_model, cost_head, configurator=None):
        self.wm = world_model
        self.cost = cost_head
        self.conf = configurator
        self.device = next(world_model.parameters()).device

    @torch.no_grad()
    def plan(self, s_t, h_t, sigma_steer=None):
        """
        s_t: [1, 256], h_t: [1, 256]
        Returns: action [3] (steer, gas, brake)
        """
        H = C.plan_horizon
        K = C.cem_candidates
        M = C.cem_elites
        N = C.cem_iterations
        D = C.action_dim

        # Initialize action distribution
        # Mean: persist current guess (start with moderate gas, no steer/brake)
        mu = torch.zeros(H, D, device=self.device)
        mu[:, 1] = 0.5  # moderate gas
        sigma = torch.full((H, D), C.cem_sigma_init, device=self.device)

        # Adjust sigma per dimension
        sigma[:, 0] = sigma_steer if sigma_steer is not None else C.cem_sigma_init
        sigma[:, 1] = 0.3  # gas exploration
        sigma[:, 2] = 0.1  # brake exploration (rarely needed)

        # Get scene-conditioned cost weights
        if self.conf is not None:
            cost_w, _ = self.conf.get_scene_weights(s_t)
        else:
            cost_w = None

        # Action bounds as tensors
        bounds_low = torch.tensor([-1.0, 0.0, 0.0], device=self.device)
        bounds_high = torch.tensor([1.0, 1.0, 1.0], device=self.device)

        for _ in range(N):
            # 1. Sample candidates
            candidates = mu + sigma * torch.randn(K, H, D, device=self.device)
            candidates = torch.clamp(candidates, bounds_low, bounds_high)

            # 2. Evaluate all candidates in parallel via World Model
            s = s_t.expand(K, -1)   # [K, 256]
            h = h_t.expand(K, -1)   # [K, 256]
            total_costs = torch.zeros(K, device=self.device)

            for tau in range(H):
                a_tau = candidates[:, tau, :]  # [K, 3]
                s, h, _, _ = self.wm(s, h, a_tau)
                costs = self.cost.total_cost(s, cost_w)  # [K]
                total_costs += (C.cem_gamma ** tau) * costs

            # 3. Select elites
            _, elite_idx = torch.topk(total_costs, M, largest=False)
            elites = candidates[elite_idx]  # [M, H, D]

            # 4. Update distribution
            mu = elites.mean(dim=0)  # [H, D]
            sigma = elites.std(dim=0).clamp(min=0.01)

        # Return first action of final mean
        return mu[0].cpu().numpy()


# ═══════════════════════════════════════════════════════════════
#  Environment Wrapper: crop + frame skip + out-of-track detection
# ═══════════════════════════════════════════════════════════════

class EnvWrapper:
    """
    Wraps CarRacing-v2 with three optimizations:
    1. Image crop: remove bottom dashboard + side noise → 84×84
    2. Frame skip: repeat action for N steps, accumulate reward
    3. Out-of-track detection: penalty when car leaves road
    """
    def __init__(self, env, crop_top=0, crop_bottom=84, crop_left=6, crop_right=90,
                 frame_skip=5, out_penalty=-10.0):
        self.env = env
        self.action_space = env.action_space  # Expose for random action sampling
        self.crop_top = crop_top
        self.crop_bottom = crop_bottom
        self.crop_left = crop_left
        self.crop_right = crop_right
        self.frame_skip = frame_skip
        self.out_penalty = out_penalty

    def reset(self):
        frame, info = self.env.reset()
        # Skip initial meaningless frames (~45 frames)
        for _ in range(45):
            frame, _, _, _, _ = self.env.step(np.array([0.0, 0.0, 0.0]))
        frame = self._crop(frame)
        return frame, info

    def step(self, action):
        """Execute action for frame_skip steps, accumulate reward."""
        total_reward = 0.0
        final_frame = None
        out_of_track = False
        terminated = False
        truncated = False
        info = {}

        for _ in range(self.frame_skip):
            frame, reward, term, trunc, inf = self.env.step(action)
            total_reward += reward
            terminated = terminated or term
            truncated = truncated or trunc
            info.update(inf)

            # Check out-of-track
            if self._is_out_of_track(frame):
                out_of_track = True

            final_frame = frame
            if terminated or truncated:
                break

        # Apply out-of-track penalty
        if out_of_track:
            total_reward += self.out_penalty

        final_frame = self._crop(final_frame)
        return final_frame, total_reward, terminated, truncated, info

    def _crop(self, frame):
        """Crop frame: remove bottom dashboard and side margins."""
        return frame[self.crop_top:self.crop_bottom,
                     self.crop_left:self.crop_right, :]

    def _is_out_of_track(self, frame):
        """
        Detect if car has left the road.
        Checks green channel at row 75, columns 35-48 (adjusted for uncropped 96×96).
        After crop (top=0, left=6): row 75, cols 35-48 → row 75, cols 29-42 in cropped.
        We check on the ORIGINAL uncropped frame before cropping.
        """
        # Check green channel (index 1) at specific edge pixels
        # Row 75, columns 35:48 in original frame
        row = 75
        cols = slice(35, 48)
        green_vals = frame[row, cols, 1]  # Green channel values
        # Out of track if first 2 AND last 2 pixels are bright green (>200)
        front_two = (green_vals[:2] > 200).sum()
        back_two = (green_vals[-2:] > 200).sum()
        return (front_two + back_two) == 4

    def close(self):
        self.env.close()


# ═══════════════════════════════════════════════════════════════
#  Data Collection
# ═══════════════════════════════════════════════════════════════

def collect_data(env, perception, buffer, num_episodes, eps=1.0,
                 planner=None, device="cuda"):
    """
    Collect trajectories and store in replay buffer.
    If planner is None, use random actions.
    """
    perception.eval()
    total_steps = 0
    total_env_steps = 0  # Actual physical steps

    for ep in range(num_episodes):
        frame, _ = env.reset()
        done = False
        ep_reward = 0
        h_t = None
        prev_action = np.zeros(3, dtype=np.float32)
        steer_history = deque(maxlen=C.scene_history)

        while not done:
            # Frame is already cropped by EnvWrapper (84×84×3)
            frame_tensor = torch.FloatTensor(frame).permute(2,0,1).unsqueeze(0).to(device)
            frame_tensor = frame_tensor / 255.0

            with torch.no_grad():
                s_t, h_t = perception(
                    frame_tensor,
                    torch.FloatTensor(prev_action).unsqueeze(0).to(device),
                    h_t,
                )

            # Select action
            if planner is not None and random.random() > eps:
                action = planner.plan(s_t, h_t)
                # Add small noise for exploration
                action += np.random.randn(3) * 0.05
                action = np.clip(action, [-1,0,0], [1,1,1])
            else:
                action = env.action_space.sample()

            # Step environment (frame skip + out-of-track handled by EnvWrapper)
            next_frame, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            # Progress: with frame_skip=5, reward accumulates -0.5 base + tile bonus
            # If reward > 0, a tile was crossed (tile bonus dominates the -0.5 penalty)
            progress = 1.0 if reward > 0 else 0.0

            # Store
            buffer.push(frame, action, reward, next_frame, float(done), progress)

            frame = next_frame
            prev_action = action
            steer_history.append(action[0])
            ep_reward += reward
            total_steps += 1

        if (ep + 1) % 10 == 0:
            print(f"  Collect: ep {ep+1}/{num_episodes} | "
                  f"reward={ep_reward:.0f} | buffer={len(buffer)}")

    perception.train()
    return total_steps


# ═══════════════════════════════════════════════════════════════
#  Training Phases
# ═══════════════════════════════════════════════════════════════

def train_world_model(perception, target_perception, world_model,
                      buffer, optimizer, device, epochs=100, batch_size=None):
    """Phase 2: Train JEPA world model."""
    if batch_size is None:
        batch_size = C.batch_size
    
    print(f"\n{'='*60}")
    print("Phase 2: Training World Model (JEPA)")
    print(f"{'='*60}")
    
    for epoch in range(epochs):
        if len(buffer) < batch_size:
            print(f"  Buffer too small ({len(buffer)} < {batch_size}), skipping")
            break
        
        frames, actions, rewards, next_frames, dones, progresses = buffer.sample(batch_size)
        frames = frames.to(device)
        actions = actions.to(device)
        rewards = rewards.to(device)
        next_frames = next_frames.to(device)
        dones = dones.to(device)
        
        # Forward — context path
        # For training, we pass zero prev_action and None hidden (single-step training)
        s_t, h_t = perception(frames, torch.zeros_like(actions))
        
        # Forward — target path (stop-gradient)
        with torch.no_grad():
            s_target, h_target = target_perception(next_frames, actions)
        
        # World Model prediction
        s_pred, h_pred, r_pred, d_pred = world_model(s_t, h_t, actions)
        
        # Losses
        loss_jepa = F.mse_loss(s_pred, s_target)
        loss_hidden = F.mse_loss(h_pred, h_target)
        loss_reward = F.mse_loss(r_pred, rewards)
        loss_done = F.binary_cross_entropy_with_logits(d_pred, dones)
        
        total_loss = (loss_jepa +
                      0.05 * loss_hidden +
                      0.1 * loss_reward +
                      0.1 * loss_done)
        
        optimizer.zero_grad()
        total_loss.backward()
        torch.nn.utils.clip_grad_norm_(world_model.parameters(), C.grad_clip)
        torch.nn.utils.clip_grad_norm_(perception.parameters(), C.grad_clip)
        optimizer.step()
        
        # EMA update target encoder
        update_ema(target_perception, perception)
        
        if (epoch + 1) % 20 == 0:
            # Collapse detection
            if loss_jepa.item() < 1e-4:
                print(f"  ⚠️  WARNING: JEPA loss very low ({loss_jepa.item():.6f}) — possible collapse!")
            print(f"  Epoch {epoch+1:3d}/{epochs} | "
                  f"JEPA={loss_jepa.item():.4f} | "
                  f"Reward={loss_reward.item():.4f} | "
                  f"Done={loss_done.item():.4f}")


def train_cost_head(perception, cost_head, buffer, optimizer, device,
                    epochs=50, batch_size=None):
    """Phase 3: Train Cost Head with auto-labeled data."""
    if batch_size is None:
        batch_size = C.batch_size
    
    print(f"\n{'='*60}")
    print("Phase 3: Training Cost Head")
    print(f"{'='*60}")
    
    perception.eval()
    
    for epoch in range(epochs):
        if len(buffer) < batch_size:
            break
        
        frames, actions, rewards, next_frames, dones, progresses = buffer.sample(batch_size)
        frames = frames.to(device)
        
        with torch.no_grad():
            s_t, _ = perception(frames, torch.zeros(batch_size, 3, device=device))
        
        # Auto-labels
        on_track_label = compute_on_track_label(frames)  # [B, 1]
        
        # Cost prediction (4-dim)
        costs = cost_head(s_t)  # [B, 4]
        
        # Train each dimension
        # dim 0: progress → predict progress fraction
        # dim 1: on_track → predict binary on-track
        # dim 2: speed → predict normalized reward (proxy)
        # dim 3: energy → predict action smoothness (proxy via reward)
        
        loss_progress = F.mse_loss(costs[:, 0:1], progresses.to(device))
        loss_track = F.binary_cross_entropy_with_logits(costs[:, 1:2], on_track_label.to(device))
        loss_speed = F.mse_loss(costs[:, 2:3], torch.clamp(rewards.to(device) * 0.01 + 0.5, 0, 1))
        loss_energy = F.mse_loss(costs[:, 3:4], torch.zeros_like(costs[:, 3:4]))  # prior: smooth
        
        total_loss = loss_progress + loss_track + 0.1 * loss_speed + 0.01 * loss_energy
        
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 20 == 0:
            print(f"  Epoch {epoch+1:3d}/{epochs} | "
                  f"Track={loss_track.item():.4f} | "
                  f"Progress={loss_progress.item():.4f} | "
                  f"Total={total_loss.item():.4f}")
    
    perception.train()


def train_configurator(perception, configurator, buffer, optimizer, device,
                       epochs=30, batch_size=None):
    """Phase 4: Train Configurator (scene classifier)."""
    if batch_size is None:
        batch_size = C.batch_size
    
    print(f"\n{'='*60}")
    print("Phase 4: Training Configurator (Scene Classifier)")
    print(f"{'='*60}")
    
    perception.eval()
    
    for epoch in range(epochs):
        if len(buffer) < batch_size:
            break
        
        frames, actions, _, _, _, _ = buffer.sample(batch_size)
        frames = frames.to(device)
        actions = actions.to(device)
        
        with torch.no_grad():
            s_t, _ = perception(frames, torch.zeros(batch_size, 3, device=device))
        
        # Auto-label: scene from steering magnitude
        scene_labels = compute_scene_label(actions[:, 0].abs())  # [B]
        
        logits, _ = configurator(s_t)
        loss = F.cross_entropy(logits, scene_labels.to(device))
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 20 == 0:
            acc = (logits.argmax(dim=1) == scene_labels.to(device)).float().mean()
            print(f"  Epoch {epoch+1:3d}/{epochs} | "
                  f"Loss={loss.item():.4f} | Acc={acc.item():.2%}")


# ═══════════════════════════════════════════════════════════════
#  Evaluation
# ═══════════════════════════════════════════════════════════════

@torch.no_grad()
def evaluate(env, perception, planner, num_episodes=5, device="cuda", render=False):
    """Evaluate agent performance."""
    perception.eval()
    total_rewards = []

    for ep in range(num_episodes):
        frame, _ = env.reset()
        done = False
        ep_reward = 0
        h_t = None
        prev_action = np.zeros(3, dtype=np.float32)

        while not done:
            frame_tensor = torch.FloatTensor(frame).permute(2,0,1).unsqueeze(0).to(device)
            frame_tensor = frame_tensor / 255.0

            s_t, h_t = perception(
                frame_tensor,
                torch.FloatTensor(prev_action).unsqueeze(0).to(device),
                h_t,
            )
            action = planner.plan(s_t, h_t)
            action = np.clip(action, [-1,0,0], [1,1,1])

            frame, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            prev_action = action
            ep_reward += reward

        total_rewards.append(ep_reward)
        print(f"  Eval ep {ep+1}: reward={ep_reward:.0f}")

    perception.train()
    avg = np.mean(total_rewards)
    print(f"  Average reward: {avg:.0f}")
    return avg


# ═══════════════════════════════════════════════════════════════
#  Main Training Loop
# ═══════════════════════════════════════════════════════════════

def main():
    device = torch.device(C.device if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    if device.type == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)} | VRAM: {torch.cuda.get_device_properties(0).total_mem/1e9:.1f}G")

    # ── Create environment ──
    raw_env = gym.make(C.env_name, render_mode="rgb_array")
    env = EnvWrapper(raw_env,
                     crop_top=C.crop_top, crop_bottom=C.crop_bottom,
                     crop_left=C.crop_left, crop_right=C.crop_right,
                     frame_skip=C.frame_skip, out_penalty=C.out_of_track_penalty)
    raw_eval_env = gym.make(C.env_name, render_mode="rgb_array")
    eval_env = EnvWrapper(raw_eval_env,
                          crop_top=C.crop_top, crop_bottom=C.crop_bottom,
                          crop_left=C.crop_left, crop_right=C.crop_right,
                          frame_skip=C.frame_skip, out_penalty=C.out_of_track_penalty)

    # ── Create models ──
    perception = Perception().to(device)
    target_perception = Perception().to(device)
    world_model = WorldModel().to(device)
    cost_head = CostHead().to(device)
    configurator = Configurator().to(device)

    # Initialize target encoder with perception weights
    target_perception.load_state_dict(perception.state_dict())
    for p in target_perception.parameters():
        p.requires_grad = False

    # Count parameters
    total_params = sum(p.numel() for m in [perception, world_model, cost_head, configurator]
                       for p in m.parameters())
    print(f"Total parameters: {total_params/1e6:.2f}M")

    # ── Optimizers ──
    opt_wm = torch.optim.AdamW(
        list(perception.parameters()) + list(world_model.parameters()),
        lr=C.lr, weight_decay=C.weight_decay
    )
    opt_cost = torch.optim.AdamW(cost_head.parameters(), lr=C.lr)
    opt_conf = torch.optim.AdamW(configurator.parameters(), lr=C.lr)

    # ── Replay Buffer ──
    buffer_path = "buffer_phase1.npz"

    # ── Phase 1: Collect random data (or load from disk) ──
    if os.path.exists(buffer_path):
        print(f"\n{'='*60}")
        print("Phase 1: Loading saved buffer from disk")
        print(f"{'='*60}")
        buffer = ReplayBuffer.load(buffer_path)
    else:
        buffer = ReplayBuffer()
        print(f"\n{'='*60}")
        print("Phase 1: Collecting random exploration data")
        print(f"{'='*60}")
        collect_data(env, perception, buffer, num_episodes=200, eps=1.0, device=device)
        buffer.save(buffer_path)
        print(f"Buffer size: {len(buffer)}")

    # ── Phase 2: Train World Model ──
    train_world_model(perception, target_perception, world_model, buffer, opt_wm, device)

    # ── Phase 3: Train Cost Head ──
    train_cost_head(perception, cost_head, buffer, opt_cost, device)

    # ── Phase 4: Train Configurator ──
    train_configurator(perception, configurator, buffer, opt_conf, device)

    # ── Phase 5: Joint online fine-tuning with CEM ──
    print(f"\n{'='*60}")
    print("Phase 5: Online fine-tuning with CEM planning")
    print(f"{'='*60}")

    planner = CEMPlanner(world_model, cost_head, configurator)
    
    total_steps = 0
    best_reward = -float('inf')
    eps = C.eps_start

    while total_steps < C.total_env_steps:
        # Decay epsilon
        eps = max(C.eps_end, C.eps_start - (C.eps_start - C.eps_end) * total_steps / C.eps_decay_steps)

        # Collect one episode with CEM + noise
        steps = collect_data(env, perception, buffer, num_episodes=2,
                           eps=eps, planner=planner, device=device)
        total_steps += steps

        # Train World Model on new data
        if len(buffer) >= C.batch_size:
            train_world_model(perception, target_perception, world_model, buffer,
                            opt_wm, device, epochs=5, batch_size=min(C.batch_size, len(buffer)))
            train_cost_head(perception, cost_head, buffer, opt_cost, device,
                          epochs=5, batch_size=min(C.batch_size, len(buffer)))
            train_configurator(perception, configurator, buffer, opt_conf, device,
                             epochs=3, batch_size=min(C.batch_size, len(buffer)))

        # Evaluate
        if total_steps % C.eval_interval < steps + 200:
            print(f"\n  ── Evaluation at step {total_steps} ──")
            avg_reward = evaluate(eval_env, perception, planner, C.eval_episodes, device)

            if avg_reward > best_reward:
                best_reward = avg_reward
                torch.save({
                    'perception': perception.state_dict(),
                    'world_model': world_model.state_dict(),
                    'cost_head': cost_head.state_dict(),
                    'configurator': configurator.state_dict(),
                    'step': total_steps,
                    'best_reward': best_reward,
                }, 'checkpoint_best.pt')
                print(f"  ✅ New best: {best_reward:.0f}")

        # Periodic checkpoint
        if total_steps % C.save_interval < steps + 200:
            torch.save({
                'perception': perception.state_dict(),
                'world_model': world_model.state_dict(),
                'cost_head': cost_head.state_dict(),
                'configurator': configurator.state_dict(),
                'opt_wm': opt_wm.state_dict(),
                'opt_cost': opt_cost.state_dict(),
                'opt_conf': opt_conf.state_dict(),
                'step': total_steps,
                'best_reward': best_reward,
                'buffer': buffer,
            }, f'checkpoint_{total_steps}.pt')
            print(f"  📦 Checkpoint saved at step {total_steps}")

        print(f"\nStep {total_steps}/{C.total_env_steps} | eps={eps:.3f} | "
              f"buffer={len(buffer)} | best_reward={best_reward:.0f}")

    # ── Final evaluation ──
    print(f"\n{'='*60}")
    print("Final Evaluation")
    print(f"{'='*60}")
    final_reward = evaluate(eval_env, perception, planner, 10, device)
    print(f"\nFinal average reward: {final_reward:.0f}")
    print(f"Best reward during training: {best_reward:.0f}")

    env.close()
    eval_env.close()


if __name__ == "__main__":
    main()
