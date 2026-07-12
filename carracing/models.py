"""
CarRacing x LeCun World Model — Neural Network Modules
Perception + WorldModel + CostHead + Configurator
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from config import Config as C


# ═══════════════════════════════════════════════════════════════
# §1  Perception: CNN Encoder + GRU Memory
# ═══════════════════════════════════════════════════════════════

class Perception(nn.Module):
    """
    Encodes 96×96×3 frames into 256-dim latents.
    Maintains a GRU hidden state as short-term memory.
    
    Input:  frame [B,3,96,96], prev_action [B,3], prev_hidden [B,256]
    Output: s_t [B,256], h_t [B,256]
    """
    def __init__(self):
        super().__init__()
        # ── CNN stem ──
        ch = C.cnn_channels
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, ch[0], C.cnn_kernel, C.cnn_stride, 1), nn.BatchNorm2d(ch[0]), nn.ReLU()
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(ch[0], ch[1], C.cnn_kernel, C.cnn_stride, 1), nn.BatchNorm2d(ch[1]), nn.ReLU()
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(ch[1], ch[2], C.cnn_kernel, C.cnn_stride, 1), nn.BatchNorm2d(ch[2]), nn.ReLU()
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(ch[2], ch[3], C.cnn_kernel, C.cnn_stride, 1), nn.BatchNorm2d(ch[3]), nn.ReLU()
        )
        # ── Residual blocks ──
        self.res_blocks = nn.ModuleList([
            ResidualBlock(ch[3]) for _ in range(C.res_blocks)
        ])
        # ── Output projection ──
        self.out = nn.Linear(ch[3], C.s_dim)
        
        # ── GRU memory ──
        self.gru = nn.GRUCell(C.s_dim + C.action_dim, C.h_dim)

    def forward(self, frame, prev_action, prev_hidden=None):
        B = frame.shape[0]
        # CNN
        x = self.conv1(frame)           # 96→48, 32ch
        x = self.conv2(x)               # 48→24, 64ch
        x = self.conv3(x)               # 24→12, 128ch
        x = self.conv4(x)               # 12→6,  256ch
        for block in self.res_blocks:
            x = block(x)                # 6×6, 256ch
        x = x.mean(dim=[2, 3])          # global avg pool → 256
        s_t = self.out(x)               # → [B, 256]
        
        # GRU memory
        gru_input = torch.cat([s_t, prev_action], dim=-1)  # [B, 256+3]
        if prev_hidden is None:
            prev_hidden = torch.zeros(B, C.h_dim, device=frame.device)
        h_t = self.gru(gru_input, prev_hidden)
        
        return s_t, h_t


class ResidualBlock(nn.Module):
    """Standard residual block with 3×3 conv."""
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, 1, 1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, 1, 1)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        residual = x
        x = F.relu(self.bn1(self.conv1(x)))
        x = self.bn2(self.conv2(x))
        return F.relu(x + residual)


# ═══════════════════════════════════════════════════════════════
# §2  World Model (JEPA Dynamics Predictor)
# ═══════════════════════════════════════════════════════════════

class WorldModel(nn.Module):
    """
    Predicts next latent state given current (s_t, h_t, a_t).
    Also predicts reward and done as auxiliary tasks.
    
    Input:  s_t [B,256], h_t [B,256], a_t [B,3]
    Output: s_next [B,256], h_next [B,256], reward [B,1], done_logit [B,1]
    """
    def __init__(self):
        super().__init__()
        input_dim = C.s_dim + C.h_dim + 64  # s + h + action_embed
        
        self.action_embed = nn.Linear(C.action_dim, 64)
        
        layers = []
        in_dim = input_dim
        for _ in range(C.dynamics_layers):
            layers.extend([
                nn.Linear(in_dim, C.dynamics_hidden),
                nn.LayerNorm(C.dynamics_hidden),
                nn.ReLU(),
            ])
            in_dim = C.dynamics_hidden
        
        self.backbone = nn.Sequential(*layers)
        self.head_s = nn.Linear(C.dynamics_hidden, C.s_dim)
        self.head_h = nn.Linear(C.dynamics_hidden, C.h_dim)
        self.head_r = nn.Linear(C.dynamics_hidden, 1)
        self.head_d = nn.Linear(C.dynamics_hidden, 1)

    def forward(self, s_t, h_t, a_t):
        a_emb = self.action_embed(a_t)          # [B, 64]
        x = torch.cat([s_t, h_t, a_emb], dim=-1)
        x = self.backbone(x)
        s_next = self.head_s(x)                 # [B, 256]
        h_next = self.head_h(x)                 # [B, 256]
        reward = self.head_r(x)                 # [B, 1]
        done_logit = self.head_d(x)             # [B, 1]
        return s_next, h_next, reward, done_logit

    def imagine_trajectory(self, s_0, h_0, action_seq):
        """
        Roll out a trajectory in imagination.
        action_seq: [B, H, 3]  (H = planning horizon)
        Returns: s_seq [B, H, 256]  predicted latents
        """
        B, H, _ = action_seq.shape
        s_seq = []
        s, h = s_0, h_0
        for t in range(H):
            s, h, _, _ = self.forward(s, h, action_seq[:, t, :])
            s_seq.append(s)
        return torch.stack(s_seq, dim=1)  # [B, H, 256]


# ═══════════════════════════════════════════════════════════════
# §3  Cost Head
# ═══════════════════════════════════════════════════════════════

class CostHead(nn.Module):
    """
    Evaluates how "good" a state is.
    Decomposes into 4 dimensions: progress, on_track, speed, energy.
    
    Input:  s_t [B,256]
    Output: cost [B,4]  (per-dimension costs)
    """
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(C.s_dim, C.cost_hidden[0]),
            nn.ReLU(),
            nn.Linear(C.cost_hidden[0], C.cost_hidden[1]),
            nn.ReLU(),
            nn.Linear(C.cost_hidden[1], C.cost_dims),
        )

    def forward(self, s_t):
        return self.net(s_t)  # [B, 4]

    def total_cost(self, s_t, scene_weights=None):
        """
        Compute scalar cost with optional per-scene weighting.
        scene_weights: override the default [w_progress, w_track, w_speed, w_energy]
        """
        costs = self.forward(s_t)  # [B, 4]
        if scene_weights is None:
            w = torch.tensor([C.w_progress, C.w_track, C.w_speed, C.w_energy],
                           device=s_t.device)
        else:
            w = scene_weights
        # NOTE: cost should be LOW when state is GOOD
        # Our CostHead predicts raw values; we negate progress and speed
        # so that "more progress" → lower total cost
        weights = torch.tensor([-1.0, 1.0, -0.5, 0.1], device=s_t.device) * w
        return (costs * weights).sum(dim=-1)  # [B]


# ═══════════════════════════════════════════════════════════════
# §4  Configurator (Scene Classifier)
# ═══════════════════════════════════════════════════════════════

class Configurator(nn.Module):
    """
    Classifies the current driving scene.
    4 classes: straight, turn_L, turn_R, chicane.
    
    Input:  s_t [B,256]
    Output: scene_logits [B,4], scene_probs [B,4]
    """
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(C.s_dim, 128),
            nn.ReLU(),
            nn.Linear(128, C.scene_classes),
        )

    def forward(self, s_t):
        logits = self.net(s_t)
        probs = F.softmax(logits, dim=-1)
        return logits, probs

    def get_scene_weights(self, s_t):
        """
        Returns per-scene Cost weights and Actor exploration params.
        """
        _, probs = self.forward(s_t)
        scene_id = probs.argmax(dim=-1)  # [B]
        
        # Default weights
        w_progress = torch.ones_like(scene_id, dtype=torch.float) * C.w_progress
        w_track = torch.ones_like(scene_id, dtype=torch.float) * C.w_track
        w_speed = torch.ones_like(scene_id, dtype=torch.float) * C.w_speed
        w_energy = torch.ones_like(scene_id, dtype=torch.float) * C.w_energy
        
        # Steering sigma per scene
        sigma_steer = torch.ones_like(scene_id, dtype=torch.float) * C.cem_sigma_init
        
        # Straight: focus on speed, reduce steering exploration
        mask_straight = (scene_id == 0)
        w_speed[mask_straight] = 2.0
        w_track[mask_straight] = 2.0
        sigma_steer[mask_straight] = 0.1
        
        # Turn: focus on staying on track, increase steering exploration
        mask_turn = (scene_id == 1) | (scene_id == 2)
        w_track[mask_turn] = 10.0
        w_speed[mask_turn] = 0.2
        sigma_steer[mask_turn] = 0.5
        
        # Chicane: aggressive steering exploration, max track priority
        mask_chicane = (scene_id == 3)
        w_track[mask_chicane] = 15.0
        w_speed[mask_chicane] = 0.1
        sigma_steer[mask_chicane] = 0.6
        
        cost_weights = torch.stack([w_progress, w_track, w_speed, w_energy], dim=1)  # [B, 4]
        return cost_weights, sigma_steer


# ═══════════════════════════════════════════════════════════════
# §5  EMA updater
# ═══════════════════════════════════════════════════════════════

def update_ema(target_net, source_net, decay=C.ema_decay):
    """Update target network parameters via Exponential Moving Average."""
    with torch.no_grad():
        for tp, sp in zip(target_net.parameters(), source_net.parameters()):
            tp.data.copy_(decay * tp.data + (1 - decay) * sp.data)


# ═══════════════════════════════════════════════════════════════
# §6  Auto-labeling utilities
# ═══════════════════════════════════════════════════════════════

def compute_on_track_label(frame):
    """
    Heuristic: grass is green, road is gray.
    Returns 1 if center of frame is on road, 0 otherwise.
    frame: [B, 3, 96, 96] normalized to [0,1]
    """
    # Center crop: take middle 20×20 pixels
    h, w = frame.shape[2], frame.shape[3]
    center = frame[:, :, h//2-10:h//2+10, w//2-10:w//2+10]  # [B, 3, 20, 20]
    
    # Road = gray (R≈G≈B, medium brightness)
    # Grass = green (G > R, G > B)
    r, g, b = center[:, 0], center[:, 1], center[:, 2]
    
    # Simple heuristic: if green channel dominates, it's grass
    is_grass = (g > r * 1.2) & (g > b * 1.2)
    grass_ratio = is_grass.float().mean(dim=[1, 2])  # [B]
    
    on_track = (grass_ratio < 0.5).float()  # <50% grass → on road
    return on_track.unsqueeze(1)  # [B, 1]


def compute_scene_label(steer_history):
    """
    Auto-label scene from recent steering pattern.
    steer_history: [B, history_len]  or [B]
    Returns: scene_id [B] ∈ {0,1,2,3}
    """
    if steer_history.dim() == 1:
        avg_abs = steer_history.abs()
    else:
        avg_abs = steer_history.abs().mean(dim=1)  # [B]
    
    scene_id = torch.zeros_like(avg_abs, dtype=torch.long)
    scene_id[(avg_abs >= 0.1) & (avg_abs < 0.4)] = 1  # turn (direction determined later)
    scene_id[avg_abs >= 0.4] = 3                        # chicane
    
    return scene_id


def compute_progress_label(env):
    """Extract progress fraction from CarRacing environment."""
    # CarRacing-v2 tracks progress via tile visits
    # We approximate: reward > 0 means progress was made
    pass  # Used during data collection; label comes from env
