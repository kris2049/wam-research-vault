# Level 3: Video & Multimodal JEPA

> **Duration**: 2 weeks | **Compute**: 🟡 8-12G VRAM | **Papers**: 1 close-read + 2 skim

---

## 🎯 Learning Objectives

1. Understand how JEPA extends from images (2D) to video (3D: 2D+time)
2. Grasp motion-content factorization in MC-JEPA
3. Understand the understanding+prediction+planning triad in V-JEPA 2
4. Implement a simplified video JEPA on synthetic data

---

## 📖 Close-Read Paper

### MC-JEPA (Meta, 2023)

- **arXiv**: [2307.12698](https://arxiv.org/abs/2307.12698)
- **Time**: 2.5 hours
- **Hardware**: 🔴 Heavy for full training; 🟡 for simplified experiment

**Reading Guide:**

| Section | Focus | Key Insight |
|---------|-------|-------------|
| §3.1 | Two-stream encoder (motion + content) | Why two streams instead of one? |
| §3.2 | Motion stream — uses optical flow | Weak supervision signal, not full flow |
| §3.3 | Content stream — uses spatial masking | Same as I-JEPA but on frames |
| §4 | Joint prediction | How do motion and content interact? |
| Figure 2 | Architecture diagram | Trace the data flow: frames → encoders → joint predictor |

**After reading, answer:**
1. Why use optical flow as a MOTION signal rather than learning it from scratch?
2. How does the motion-content factorization help downstream tasks?
3. What is the difference between MC-JEPA's predictor and I-JEPA's predictor?

---

## 👀 Skim Papers (30 min each)

### V-JEPA 2 (Meta, 2025)
- **arXiv**: [2506.09985](https://arxiv.org/abs/2506.09985)
- **Focus**: The understanding + prediction + planning triad
- **Key question**: How does V-JEPA 2 enable PLANNING (not just prediction)?

### A-JEPA (2023)
- **arXiv**: [2311.15830](https://arxiv.org/abs/2311.15830)
- **Focus**: JEPA for audio — proves modality generality
- **Key question**: What changes when switching from image patches to spectrogram patches?

---

## 🔬 Experiment: Moving MNIST Video JEPA

**Hardware**: 🟡 8-12G VRAM
**Time**: ~6 hours training
**Goal**: Build a minimal video JEPA that predicts future frame representations from past frames.

### Why Moving MNIST?
- 64×64 frames, 10 frames per sequence → fits in 8G
- Controlled dynamics (digits move and bounce)
- Clear separation of "content" (which digit) and "motion" (direction, speed)
- Perfect for demonstrating JEPA principles without massive compute

### Experiment Design:

```
Input: 10 frames of Moving MNIST (64×64)
Frame 0-4: CONTEXT (past)
Frame 5-9: TARGET  (future)

          CONTEXT frames (0-4)                TARGET frames (5-9)
                │                                     │
    ┌───────────▼───────────┐             ┌───────────▼───────────┐
    │  Context Encoder       │             │  Target Encoder       │
    │  (3D Conv + ViT)       │             │  (EMA of context)     │
    │  ~3M params            │             │  STOP-GRADIENT        │
    └───────────┬───────────┘             └───────────┬───────────┘
                │ ctx_latent [B, T, dim]               │ tgt_latent [B, T, dim]
                ▼                                     │
    ┌───────────────────────┐                         │
    │  Temporal Predictor    │                         │
    │  (Causal Transformer)  │◄────────────────────────┘
    │  ~2M params            │     L2 loss
    └───────────────────────┘
     predicts future latents
     from past latents
```

### Key Code Sketch:

```python
"""
Moving MNIST Video JEPA
Hardware: 8-12G VRAM (RTX 3060+)
Time: ~6 hours
"""

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

# ============================================
# Step 1: Generate Moving MNIST Data
# ============================================
def generate_moving_mnist(n_samples=10000, seq_len=10, img_size=64):
    """
    Generate sequences of 2 digits moving and bouncing.
    Each sample: [seq_len, 1, 64, 64]
    """
    from torchvision.datasets import MNIST
    mnist = MNIST(root='./data', train=True, download=True)
    
    samples = []
    for _ in range(n_samples):
        # Randomly select 2 digits
        digit1, _ = mnist[torch.randint(0, len(mnist), (1,)).item()]
        digit2, _ = mnist[torch.randint(0, len(mnist), (1,)).item()]
        
        # Random initial positions and velocities
        pos1 = torch.rand(2) * (img_size - 28)
        pos2 = torch.rand(2) * (img_size - 28)
        vel1 = torch.randn(2) * 2
        vel2 = torch.randn(2) * 2
        
        sequence = []
        for t in range(seq_len):
            frame = torch.zeros(1, img_size, img_size)
            # Place digit 1
            x1, y1 = pos1.int()
            x1, y1 = max(0, min(x1, img_size-28)), max(0, min(y1, img_size-28))
            frame[:, y1:y1+28, x1:x1+28] = digit1.squeeze()
            
            # Place digit 2
            x2, y2 = pos2.int()
            x2, y2 = max(0, min(x2, img_size-28)), max(0, min(y2, img_size-28))
            frame[:, y2:y2+28, x2:x2+28] = digit2.squeeze()
            
            sequence.append(frame)
            
            # Update positions with bouncing
            pos1 += vel1
            pos2 += vel2
            for pos, vel in [(pos1, vel1), (pos2, vel2)]:
                if pos[0] < 0 or pos[0] > img_size - 28: vel[0] *= -1
                if pos[1] < 0 or pos[1] > img_size - 28: vel[1] *= -1
        
        samples.append(torch.stack(sequence))
    
    return torch.stack(samples)  # [N, 10, 1, 64, 64]

# ============================================
# Step 2: 3D Context Encoder (video patch)
# ============================================
class VideoEncoder(nn.Module):
    """Encode a sequence of frames into temporal latents."""
    def __init__(self, dim=256, tubelet_size=(2, 8, 8)):
        super().__init__()
        # 3D conv to embed spacetime patches
        self.conv3d = nn.Conv3d(1, dim, kernel_size=tubelet_size, stride=tubelet_size)
        # After conv: [B, dim, T//2, 64//8, 64//8] = [B, 256, 5, 8, 8]
        # Flatten spatial dims → [B, 256, 5, 64]
        # Transformer over time
        self.temporal_transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=dim, nhead=4, dim_feedforward=dim*2,
                                        batch_first=True, norm_first=True),
            num_layers=2
        )
    
    def forward(self, x):
        # x: [B, T, 1, H, W]
        B, T = x.shape[:2]
        x = x.permute(0, 2, 1, 3, 4)  # [B, 1, T, H, W]
        x = self.conv3d(x)  # [B, dim, T', H', W']
        _, _, Tp, Hp, Wp = x.shape
        x = x.flatten(3).permute(0, 2, 3, 1)  # [B, T', H'*W', dim]
        x = x.reshape(B, Tp * Hp * Wp, -1)  # [B, N_tokens, dim]
        x = self.temporal_transformer(x)
        return x.mean(dim=1)  # [B, dim] — global representation

# ============================================
# Step 3: Training
# ============================================
def train_video_jepa(epochs=50, batch_size=32, lr=1e-3):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Generate data (or load pre-generated)
    print("Generating Moving MNIST...")
    data = generate_moving_mnist(n_samples=5000)
    loader = DataLoader(data, batch_size=batch_size, shuffle=True)
    
    ctx_enc = VideoEncoder().to(device)
    tgt_enc = VideoEncoder().to(device)
    predictor = nn.Sequential(
        nn.Linear(256, 512), nn.ReLU(), nn.Linear(512, 256)
    ).to(device)
    
    # EMA init
    ema = 0.996
    for pt, pc in zip(tgt_enc.parameters(), ctx_enc.parameters()):
        pt.data.copy_(pc.data)
        pt.requires_grad = False
    
    opt = torch.optim.AdamW(list(ctx_enc.parameters()) + list(predictor.parameters()), lr=lr)
    
    for epoch in range(epochs):
        total_loss = 0
        for batch in loader:
            batch = batch.to(device)  # [B, 10, 1, 64, 64]
            ctx_frames = batch[:, :5, ...]   # First 5 frames
            tgt_frames = batch[:, 5:, ...]   # Last 5 frames
            
            with torch.no_grad():
                tgt_latent = tgt_enc(tgt_frames)
            ctx_latent = ctx_enc(ctx_frames)
            pred_latent = predictor(ctx_latent)
            
            loss = nn.functional.mse_loss(pred_latent, tgt_latent)
            
            opt.zero_grad()
            loss.backward()
            opt.step()
            
            # EMA update
            with torch.no_grad():
                for pt, pc in zip(tgt_enc.parameters(), ctx_enc.parameters()):
                    pt.data = ema * pt.data + (1 - ema) * pc.data
            
            total_loss += loss.item()
        
        print(f"Epoch {epoch+1} | Loss: {total_loss/len(loader):.4f}")

if __name__ == "__main__":
    train_video_jepa()
```

### Expected Results:
- Loss should decrease and stabilize (not collapse to 0)
- The model learns to predict future DIGIT IDENTITIES and APPROXIMATE POSITIONS in latent space
- Heatmap visualization: cosine similarity between predicted vs actual latent across time steps

---

## 🔬 Experiment: Modality Extension Exercise

**Hardware**: 🟢 4-6G VRAM | **Time**: 2 hours

Take your Level 2 Mini I-JEPA code and swap CIFAR-10 images for:
1. **Spectrograms**: Convert audio (ESC-50 dataset) to mel-spectrograms → treat as "images"
2. **Observation**: Does JEPA still work without ANY architectural changes?

Key learning: JEPA is modality-agnostic. The architecture doesn't care if "patches" come from images, spectrograms, or point clouds.

---

## ✅ Level 3 Checklist

- [ ] Close-read MC-JEPA — understand motion-content factorization
- [ ] Skimmed V-JEPA 2 — understand the understanding+prediction+planning triad
- [ ] Skimmed A-JEPA — understand modality extension
- [ ] Ran Moving MNIST Video JEPA — non-collapsing temporal prediction
- [ ] (Optional) Ran spectrogram JEPA — verified modality agnosticism

---

## 📚 Supplementary

| Resource | Type | Link |
|----------|------|------|
| V-JEPA blog (Meta) | Blog | ai.meta.com/blog/v-jepa |
| MC-JEPA code | GitHub | github.com/facebookresearch/mc_jepa |
| Moving MNIST generator | GitHub | Standard benchmark in video prediction |
