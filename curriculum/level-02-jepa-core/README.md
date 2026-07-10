# Level 2: JEPA Core

> **Duration**: 2 weeks | **Compute**: 🟡 8-12G VRAM | **Papers**: 2 close-read + 1 skim

---

## 🎯 Learning Objectives

1. Implement the I-JEPA architecture from scratch (simplified)
2. Understand the context→target→predictor pipeline
3. Grasp WHY stop-gradient and EMA prevent collapse
4. Reproduce the core insight: predicting latents > predicting pixels

---

## 📖 Close-Read Papers

### Paper 1: I-JEPA (Meta, 2023)

- **arXiv**: [2301.08243](https://arxiv.org/abs/2301.08243)
- **Time**: 3 hours
- **Hardware**: 🟡 8-12G for experiment; paper reading needs none

**Reading Guide — Focus on these equations/sections:**

| Section | Key Content | Time |
|---------|-------------|------|
| §3.1 | Context/Target block masking | 20 min |
| §3.2 | Encoder architecture (ViT) | 15 min |
| §3.3 | Predictor network | 20 min |
| §3.4 | Loss function: why L2 in latent space? | 15 min |
| §4.1 | Training dynamics: stop-gradient + EMA | 30 min |
| §5.1 | Why multi-block masking matters | 15 min |
| Figure 2 | The architecture diagram — memorize this | 10 min |

**After reading, answer:**
1. Why does I-JEPA use L2 loss in latent space rather than cross-entropy on pixels?
2. What would happen if you removed the stop-gradient on the target encoder?
3. Why multi-block masking (4 blocks) rather than a single big mask?
4. How does the predictor network differ from a standard transformer decoder?

---

### Paper 2: Connecting JEPA with Contrastive SSL (2024)

- **arXiv**: [2410.19560](https://arxiv.org/abs/2410.19560)
- **Time**: 1 hour — skim
- **Why**: Bridges JEPA to contrastive learning. Helps understand JEPA as "implicit contrastive learning."

**Key takeaway**: JEPA is contrastive learning where negative samples are implicit (all possible representations in the latent space, not a finite batch).

---

## 🔬 Experiment: Mini I-JEPA on CIFAR-10

**Hardware**: 🟡 8-12G VRAM (RTX 3060/4060 or better)
**Time**: ~4 hours training on single GPU
**Goal**: Build a simplified I-JEPA and train on CIFAR-10, then evaluate representations.

### Architecture (simplified for 8G VRAM):

```
CIFAR-10 Image (32×32)
      ↓
┌─────────────────────┐
│  Context Encoder     │ ← processes visible patches
│  (Small ViT, ~5M)    │
└──────────┬──────────┘
           ↓ context_latent
┌─────────────────────┐
│  Predictor           │ ← predicts target latent FROM context latent
│  (Small Transformer) │    (+ positional embeddings for masked positions)
└──────────┬──────────┘
           ↓ predicted_target_latent
           ‖  ← L2 loss
           ↓ actual_target_latent
┌─────────────────────┐
│  Target Encoder      │ ← processes masked patches
│  (EMA of Context)    │    STOP-GRADIENT
└─────────────────────┘
```

### Key simplifications from the real I-JEPA:
1. **CIFAR-10 instead of ImageNet** (32×32 vs 224×224)
2. **Small ViT**: 4 layers, 256 dim, 4 heads (~5M params vs ~630M)
3. **Batch size 256** instead of 2048
4. **Single GPU training** instead of 16+ GPUs

### Experiment Steps:

```python
# experiment_01_mini_jepa.py

"""
Mini I-JEPA on CIFAR-10
Hardware: 8-12G VRAM (RTX 3060+)
Time: ~4 hours for 100 epochs
"""

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as T

# ============================================
# Step 1: Define the Context/Target masking
# ============================================
def create_masks(image_size=32, patch_size=4, num_target_blocks=4):
    """
    Split 32x32 image into 8x8=64 patches (each 4x4).
    Select 4 random target blocks + their context (everything else).
    
    Returns:
      context_mask: [64] bool — True where context sees the patch
      target_mask:  [64] bool — True where target predicts
    """
    n_patches = (image_size // patch_size) ** 2  # 64
    # Randomly select target blocks
    target_blocks = torch.randperm(n_patches)[:num_target_blocks]
    context_mask = torch.ones(n_patches, dtype=torch.bool)
    target_mask = torch.zeros(n_patches, dtype=torch.bool)
    context_mask[target_blocks] = False
    target_mask[target_blocks] = True
    return context_mask, target_mask

# ============================================
# Step 2: Build the Small ViT Encoder (~5M params)
# ============================================
class SmallViT(nn.Module):
    """Tiny ViT for CIFAR-10: 4 layers, 256 dim, 4 heads."""
    def __init__(self, patch_size=4, dim=256, depth=4, heads=4):
        super().__init__()
        self.patch_size = patch_size
        n_patches = (32 // patch_size) ** 2
        
        self.patch_embed = nn.Linear(patch_size * patch_size * 3, dim)
        self.pos_embed = nn.Parameter(torch.randn(1, n_patches, dim))
        self.cls_token = nn.Parameter(torch.randn(1, 1, dim))
        
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=dim, nhead=heads, dim_feedforward=dim*4,
            batch_first=True, norm_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=depth)
        
    def forward(self, x, mask=None):
        # x: [B, 3, 32, 32] → patches → [B, 64, dim]
        B = x.shape[0]
        # Patchify
        patches = x.unfold(2, self.patch_size, self.patch_size) \
                   .unfold(3, self.patch_size, self.patch_size)
        patches = patches.permute(0, 2, 3, 1, 4, 5).reshape(B, -1, self.patch_size**2 * 3)
        x = self.patch_embed(patches)  # [B, 64, dim]
        
        if mask is not None:
            x = x[:, mask, :]  # Only keep unmasked patches
        
        x = x + self.pos_embed[:, :x.shape[1], :]
        cls = self.cls_token.expand(B, -1, -1)
        x = torch.cat([cls, x], dim=1)
        x = self.transformer(x)
        return x[:, 0, :]  # CLS token

# ============================================
# Step 3: Build the Predictor
# ============================================
class Predictor(nn.Module):
    """Predicts target latents given context latent + position info."""
    def __init__(self, dim=256, n_targets=4):
        super().__init__()
        self.target_tokens = nn.Parameter(torch.randn(1, n_targets, dim))
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=dim, nhead=4, dim_feedforward=dim*4,
                                        batch_first=True, norm_first=True),
            num_layers=2
        )
    
    def forward(self, context_latent):
        # context_latent: [B, dim]
        B = context_latent.shape[0]
        # Concatenate context with learnable target query tokens
        ctx = context_latent.unsqueeze(1)  # [B, 1, dim]
        targets = self.target_tokens.expand(B, -1, -1)  # [B, 4, dim]
        x = torch.cat([ctx, targets], dim=1)
        x = self.transformer(x)
        return x[:, 1:, :]  # [B, 4, dim] — predicted target latents

# ============================================
# Step 4: Training Loop
# ============================================
def train_mini_jepa(epochs=100, batch_size=256, lr=1e-3):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using: {device} | VRAM: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f}G")
    
    # Data
    transform = T.Compose([T.ToTensor(), T.Normalize((0.5,)*3, (0.5,)*3)])
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=4)
    
    # Models
    context_encoder = SmallViT().to(device)
    target_encoder = SmallViT().to(device)
    predictor = Predictor().to(device)
    
    # EMA for target encoder
    ema_decay = 0.996
    for param_t, param_c in zip(target_encoder.parameters(), context_encoder.parameters()):
        param_t.data.copy_(param_c.data)
        param_t.requires_grad = False  # Never backprop through target
    
    optimizer = torch.optim.AdamW(list(context_encoder.parameters()) + list(predictor.parameters()), lr=lr)
    
    for epoch in range(epochs):
        total_loss = 0
        for images, _ in trainloader:
            images = images.to(device)
            B = images.shape[0]
            
            # Create masks
            ctx_mask, tgt_mask = create_masks()
            
            # Forward
            with torch.no_grad():
                tgt_latent = target_encoder(images, mask=tgt_mask)  # [B, dim]
                # For simplicity: use CLS. Real I-JEPA predicts per-block.
            
            ctx_latent = context_encoder(images, mask=ctx_mask)  # [B, dim]
            pred_latent = predictor(ctx_latent)  # [B, 4, dim]
            
            # Loss: L2 in latent space
            # Simplified: match the CLS token. Full I-JEPA matches per-block latents.
            loss = nn.functional.mse_loss(pred_latent.mean(dim=1), tgt_latent)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            # Update target encoder via EMA
            with torch.no_grad():
                for param_t, param_c in zip(target_encoder.parameters(), context_encoder.parameters()):
                    param_t.data = ema_decay * param_t.data + (1 - ema_decay) * param_c.data
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(trainloader)
        print(f"Epoch {epoch+1}/{epochs} | Loss: {avg_loss:.4f}")
        
        # Check for collapse (loss ≈ 0 means collapsed)
        if avg_loss < 1e-4:
            print("⚠️  WARNING: Loss near zero — possible collapse!")

if __name__ == "__main__":
    train_mini_jepa()
```

### Expected Results:
- Loss should stabilize around 0.1-0.5 (not near 0, which would indicate collapse)
- Linear probe on CIFAR-10 should achieve ~65-70% accuracy (simplified model)
- Key insight: the model learns SEMANTIC representations without pixel reconstruction

---

## ✅ Level 2 Checklist

- [ ] Close-read I-JEPA — can explain every design choice
- [ ] Understand why stop-gradient + EMA prevent collapse
- [ ] Skimmed Contrastive-JEPA bridge paper
- [ ] Ran Mini I-JEPA experiment — non-collapsing loss
- [ ] Evaluated representations with linear probe
- [ ] Can explain how this scales to V-JEPA and MC-JEPA

---

## 📚 Supplementary

| Resource | Type | Link |
|----------|------|------|
| I-JEPA code (Meta) | GitHub | github.com/facebookresearch/ijepa |
| Understanding JEPA (Yannic Kilcher) | Video | YouTube explanation |
| BYOL paper | Paper | Understand EMA+stop-gradient origin |
