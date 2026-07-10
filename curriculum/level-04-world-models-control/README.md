# Level 4: World Models for Control

> **Duration**: 2 weeks | **Compute**: 🟢 4-6G VRAM | **Papers**: 1 close-read + 1 skim + 1 experiment

---

## 🎯 Learning Objectives

1. Understand how world models are used for ACTION (not just prediction)
2. Implement the Dreamer algorithm (simplified) for reinforcement learning
3. Grasp the connection between JEPA-style prediction and model-based RL
4. Run a world model that controls an agent in a simulated environment

---

## 📖 Close-Read Paper

### DayDreamer (2022)

- **arXiv**: [2206.14176](https://arxiv.org/abs/2206.14176)
- **Time**: 2.5 hours
- **Hardware**: 🟢 4-6G for experiment; paper reading needs none

**Reading Guide — This is the EMPIRICAL VALIDATION of the world model approach:**

| Section | Focus | Key Question |
|---------|-------|-------------|
| §2 | Dreamer algorithm recap | How does Dreamer use a world model for planning? |
| §3 | Real-robot challenges | Why is sim-to-real hard? What makes real robots different? |
| §4 | World model architecture | RSSM — what does the "S" (stochastic) add? |
| §5 | Actor-critic in imagination | How does the agent learn inside the world model? |
| Figure 1 | The Dreamer loop | Understand: act → observe → update world model → imagine → update policy |

**After reading, answer:**
1. What is the RSSM (Recurrent State-Space Model)? How does it differ from a plain RNN?
2. Why does Dreamer "dream" — i.e., why train the policy inside the world model rather than on real experience?
3. How does DayDreamer handle the fact that real robots are slow, noisy, and fragile?
4. What aspect of Dreamer does LeCun's JEPA seek to replace? (Hint: reconstruction loss)

---

## 👀 Skim Paper

### Dreamer-CDP (2026)
- **arXiv**: [2603.07083](https://arxiv.org/abs/2603.07083)
- **Time**: 30 min
- **Focus**: Removing reconstruction loss from Dreamer — moving toward JEPA
- **Key question**: What changes when you switch from stochastic states (RSSM) to continuous deterministic states?

---

## 🔬 Experiment: Mini Dreamer on CartPole

**Hardware**: 🟢 4-6G VRAM (GTX 1060 / RTX 2060)
**Time**: ~2 hours training
**Goal**: Implement a minimal Dreamer-style world model that learns to control CartPole.

### Why CartPole?
- 4-dimensional state (position, velocity, angle, angular velocity) — no vision needed
- Simple dynamics — world model can learn in minutes
- Clear success metric: balance the pole for 500 steps
- Demonstrates the FULL world model loop: act → observe → learn model → plan → act

### Architecture (simplified Dreamer):

```
Environment (CartPole)
      │
      │ action (left/right)
      ▼
┌──────────────────────────────────────────────┐
│                AGENT                          │
│                                               │
│  ┌─────────┐     ┌──────────────┐            │
│  │  World   │────▶│   Actor      │──▶ action  │
│  │  Model   │     │  (Policy)    │            │
│  │  (RSSM)  │     └──────────────┘            │
│  │          │                                  │
│  │  state → │     ┌──────────────┐            │
│  │  next_   │────▶│   Critic     │──▶ value   │
│  │  state   │     │  (Value Fn)  │            │
│  └─────────┘     └──────────────┘            │
│                                               │
│  Trained in IMAGINATION (inside world model)  │
└──────────────────────────────────────────────┘
```

### Key Code Sketch:

```python
"""
Mini Dreamer on CartPole
Hardware: Any GPU with 4G+ VRAM (or even CPU)
Time: ~2 hours (50K env steps)
"""

import torch
import torch.nn as nn
import gymnasium as gym
import numpy as np
from collections import deque

# ============================================
# Step 1: RSSM (Recurrent State-Space Model)
# ============================================
class RSSM(nn.Module):
    """
    Simplified RSSM — deterministic GRU state + stochastic latent.
    Predicts: next_state, reward, done from current state + action.
    """
    def __init__(self, state_dim=4, action_dim=2, hidden_dim=256, latent_dim=32):
        super().__init__()
        # Encoder: (state, action) → latent
        self.encoder = nn.Sequential(
            nn.Linear(state_dim + action_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim * 2)  # mean + logvar
        )
        # Dynamics: (latent, action) → next_latent
        self.gru = nn.GRUCell(latent_dim + action_dim, hidden_dim)
        self.dynamics_out = nn.Linear(hidden_dim, latent_dim * 2)
        # Decoders: latent → (next_state, reward)
        self.state_decoder = nn.Sequential(
            nn.Linear(latent_dim + hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, state_dim)
        )
        self.reward_decoder = nn.Sequential(
            nn.Linear(latent_dim + hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )
        self.hidden_dim = hidden_dim
        self.latent_dim = latent_dim
    
    def encode(self, state, action, hidden=None):
        """Encode (state, action) → latent + updated hidden state."""
        x = torch.cat([state, action], dim=-1)
        mean, logvar = self.encoder(x).chunk(2, dim=-1)
        latent = mean + torch.randn_like(mean) * torch.exp(0.5 * logvar)
        
        gru_input = torch.cat([latent, action], dim=-1)
        if hidden is None:
            hidden = torch.zeros(x.shape[0], self.hidden_dim, device=x.device)
        hidden = self.gru(gru_input, hidden)
        
        return latent, hidden
    
    def imagine(self, latent, hidden, action):
        """Predict next latent + hidden given action (no encoder needed)."""
        gru_input = torch.cat([latent, action], dim=-1)
        hidden = self.gru(gru_input, hidden)
        mean, logvar = self.dynamics_out(hidden).chunk(2, dim=-1)
        next_latent = mean + torch.randn_like(mean) * torch.exp(0.5 * logvar)
        
        # Decode
        dec_input = torch.cat([next_latent, hidden], dim=-1)
        next_state = self.state_decoder(dec_input)
        reward = self.reward_decoder(dec_input)
        
        return next_latent, hidden, next_state, reward

# ============================================
# Step 2: Actor-Critic (trained in imagination)
# ============================================
class ActorCritic(nn.Module):
    """Simple policy + value function."""
    def __init__(self, latent_dim=32, hidden_dim=256, action_dim=2):
        super().__init__()
        self.shared = nn.Sequential(
            nn.Linear(latent_dim + hidden_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU()
        )
        self.actor = nn.Linear(hidden_dim, action_dim)
        self.critic = nn.Linear(hidden_dim, 1)
    
    def forward(self, latent, hidden):
        x = self.shared(torch.cat([latent, hidden], dim=-1))
        logits = self.actor(x)
        value = self.critic(x)
        return torch.distributions.Categorical(logits=logits), value

# ============================================
# Step 3: Training Loop
# ============================================
def train_mini_dreamer(env_steps=50000, imagine_horizon=15, batch_size=64):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    env = gym.make("CartPole-v1")
    
    rssm = RSSM().to(device)
    ac = ActorCritic().to(device)
    
    opt_model = torch.optim.Adam(rssm.parameters(), lr=1e-3)
    opt_ac = torch.optim.Adam(ac.parameters(), lr=3e-4)
    
    replay_buffer = deque(maxlen=100000)
    state, _ = env.reset()
    total_reward = 0
    episode_rewards = []
    
    for step in range(env_steps):
        # Act (random at first, then from model)
        if step < 1000:
            action = env.action_space.sample()
        else:
            with torch.no_grad():
                s = torch.FloatTensor(state).unsqueeze(0).to(device)
                a = torch.zeros(1, 2).to(device)
                latent, hidden = rssm.encode(s, a)
                dist, _ = ac(latent, hidden)
                action = dist.sample().item()
        
        next_state, reward, done, truncated, _ = env.step(action)
        total_reward += reward
        
        replay_buffer.append((state, action, reward, next_state, done))
        state = next_state
        
        if done or truncated:
            episode_rewards.append(total_reward)
            state, _ = env.reset()
            total_reward = 0
        
        # Train world model (every step after initial collection)
        if step >= 1000 and len(replay_buffer) >= batch_size:
            # Sample batch
            batch = random.sample(list(replay_buffer), batch_size)
            states, actions, rewards, next_states, dones = zip(*batch)
            
            s = torch.FloatTensor(states).to(device)
            a = torch.zeros(batch_size, 2).to(device)  # one-hot actions
            a[range(batch_size), list(actions)] = 1
            r = torch.FloatTensor(rewards).unsqueeze(1).to(device)
            ns = torch.FloatTensor(next_states).to(device)
            
            latent, hidden = rssm.encode(s, a)
            _, _, pred_state, pred_reward = rssm.imagine(latent, hidden, a)
            
            model_loss = nn.functional.mse_loss(pred_state, ns) + \
                         nn.functional.mse_loss(pred_reward, r)
            
            opt_model.zero_grad()
            model_loss.backward()
            opt_model.step()
        
        # Train actor-critic in imagination (every 10 steps)
        if step >= 1000 and step % 10 == 0:
            # Imagine trajectories
            s_sample = torch.FloatTensor([b[0] for b in batch[:16]]).to(device)
            a_sample = torch.zeros(16, 2).to(device)
            latent, hidden = rssm.encode(s_sample, a_sample)
            
            total_imagined_reward = 0
            for t in range(imagine_horizon):
                dist, value = ac(latent.detach(), hidden.detach())
                action = dist.sample()
                a_onehot = torch.zeros(16, 2).to(device)
                a_onehot[range(16), action] = 1
                
                latent, hidden, _, reward = rssm.imagine(latent, hidden, a_onehot)
                total_imagined_reward += reward.mean()
            
            ac_loss = -total_imagined_reward  # Maximize imagined reward
            opt_ac.zero_grad()
            ac_loss.backward()
            opt_ac.step()
        
        if step % 5000 == 0:
            avg_reward = np.mean(episode_rewards[-10:]) if episode_rewards else 0
            print(f"Step {step} | Avg Reward (last 10 ep): {avg_reward:.1f}")
    
    env.close()
    return episode_rewards

if __name__ == "__main__":
    import random
    rewards = train_mini_dreamer()
    print(f"Final avg reward: {np.mean(rewards[-20:]):.1f}")
```

### Expected Results:
- CartPole solved (avg reward > 400) within 20K-30K environment steps
- The world model learns CartPole dynamics (pole angle, cart position) in <5K steps
- Key insight: the agent learns inside the world model (imagination) without interacting with the real environment during actor-critic training

---

## 🔬 Analysis Exercise: JEPA vs Dreamer

**Hardware**: None | **Time**: 1 hour

Compare the architectures:

| Aspect | Dreamer (RSSM) | JEPA |
|--------|---------------|------|
| Prediction target | Next state (pixels or features) | Latent of masked region |
| Reconstruction loss? | ✅ Yes (in standard Dreamer) | ❌ No |
| Action conditioning? | ✅ Actions input to dynamics | ❌ (currently; future direction) |
| Planning? | ✅ Imagination-based MPC | ❌ (future direction) |
| Collapse prevention | KL divergence to prior | Stop-gradient + EMA |

**Answer**: 
1. Which component of Dreamer would you REMOVE to make it more JEPA-like?
2. Which component of JEPA would you ADD to make it capable of planning?
3. Dreamer-CDP removes reconstruction. What else needs to change?

---

## ✅ Level 4 Checklist

- [ ] Close-read DayDreamer — understand the Dreamer loop
- [ ] Skimmed Dreamer-CDP — understand convergence toward JEPA
- [ ] Ran Mini Dreamer on CartPole — agent learns to balance pole
- [ ] Completed JEPA vs Dreamer comparison analysis
- [ ] Can explain the world model → planning → action pipeline

---

## 📚 Supplementary

| Resource | Type | Link |
|----------|------|------|
| Dreamer v3 paper | Paper | Hafner et al. 2023 |
| Dreamer code | GitHub | github.com/danijar/dreamer |
| World Models tutorial | Blog | Understanding RSSM in detail |
