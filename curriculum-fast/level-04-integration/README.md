# Level 4：全部集成 → CarRacing 完整世界模型

> **学了什么**：把所有模块拼起来，跑通完整的训练和规划循环
> **硬件**：8G VRAM | **时间**：3 天

---

## 🎯 目标

把 Level 1-3 学到的所有概念整合成一个可运行的 CarRacing 世界模型：

```
DINOv2(冻结) → Encoder → WorldModel(JEPA) → CostHead + Configurator → CEM规划
```

---

## 📖 架构复习

```
一帧画面 (84×84, cropped)
    │
    ▼
DINOv2-small (冻结, 22M)
    │ z ∈ ℝ^384
    ▼
Projection: Linear(384→256) + GRU(256+3, 256)
    │ s_t ∈ ℝ^256, h_t ∈ ℝ^256
    │
    ├──► Configurator: 256→128→4 → scene_id → cost_weights + sigma_steer
    │
    ├──► CostHead: 256→128→64→4 → [progress, track, speed, energy]
    │
    └──► WorldModel: [s_t, h_t, a_t] → 3层MLP → ŝ_{t+1}, ĥ_{t+1}
              │
              │ 训练Loss: L_pred + 0.1×KL_gaussian + 0.05×L_straighten
              │
              └──► CEM: 世界模型中展开8步 → Cost打分 → 选最优动作
```

---

## 🔬 集成实验：完整训练

把 `carracing/` 目录下的代码按最佳实践改造：

**关键改动 vs 当前代码**：

| 组件 | 当前（旧） | 最佳实践（新） |
|------|----------|--------------|
| 编码器 | CNN 1.4M，端到端训练 | DINOv2-small 22M，冻结 |
| 防坍缩 | EMA Target Encoder | 高斯正则化 KL(N(z), N(0,I)) |
| 时间拉直 | 无 | L_straighten |
| 物理随机化 | 无 | 每次 reset 随机化摩擦力/颜色 |

**改动后的 `models.py` 核心部分**：

```python
class FastWorldModel(nn.Module):
    """CarRacing 最佳实践世界模型"""
    
    def __init__(self, dino_name="dinov2_vits14", s_dim=256):
        super().__init__()
        # 冻结编码器
        self.dino = torch.hub.load("facebookresearch/dinov2", dino_name)
        for p in self.dino.parameters():
            p.requires_grad = False
        
        # 可训练部分
        self.proj = nn.Linear(384, s_dim)
        self.gru = nn.GRUCell(s_dim + 3, s_dim)
        self.predictor = nn.Sequential(
            nn.Linear(s_dim * 2 + 3, 512), nn.LayerNorm(512), nn.ReLU(),
            nn.Linear(512, 512), nn.LayerNorm(512), nn.ReLU(),
            nn.Linear(512, 512), nn.LayerNorm(512), nn.ReLU(),
        )
        self.head_s = nn.Linear(512, s_dim)
        self.head_h = nn.Linear(512, s_dim)
        self.head_r = nn.Linear(512, 1)
        self.head_d = nn.Linear(512, 1)
    
    def encode(self, frame, prev_action, prev_hidden=None):
        B = frame.shape[0]
        frame_224 = F.interpolate(frame, size=224, mode='bilinear')
        with torch.no_grad():
            z = self.dino(frame_224)
        s_t = self.proj(z)
        gru_in = torch.cat([s_t, prev_action], -1)
        if prev_hidden is None:
            prev_hidden = torch.zeros(B, s_t.shape[-1], device=frame.device)
        h_t = self.gru(gru_in, prev_hidden)
        return s_t, h_t
    
    def forward(self, s_t, h_t, a_t):
        x = torch.cat([s_t, h_t, a_t], -1)
        x = self.predictor(x)
        return self.head_s(x), self.head_h(x), self.head_r(x), self.head_d(x)
    
    def compute_loss(self, s_t, h_t, a_t, s_target, h_target, r_true, d_true,
                     s_prev=None, lambda_kl=0.1, lambda_st=0.05):
        s_pred, h_pred, r_pred, d_pred = self(s_t, h_t, a_t)
        
        # 1. 预测 Loss
        loss_pred = F.mse_loss(s_pred, s_target) + 0.05 * F.mse_loss(h_pred, h_target)
        loss_aux  = 0.1 * F.mse_loss(r_pred, r_true) + 0.1 * F.binary_cross_entropy_with_logits(d_pred, d_true)
        
        # 2. 高斯正则化（防坍缩）
        m, v = s_pred.mean(0), s_pred.var(0, unbiased=False)
        loss_kl = 0.5 * (v + m.pow(2) - 1 - v.log()).sum() / s_pred.shape[-1]
        
        # 3. 时间拉直
        loss_st = 0.0
        if s_prev is not None:
            d1 = s_pred - s_t
            d2 = s_target - s_pred
            loss_st = (d1 - d2).pow(2).mean()
        
        return loss_pred + loss_aux + lambda_kl * loss_kl + lambda_st * loss_st
```

---

## ✅ Level 4 检查清单

- [ ] 理解完整架构图，能画出数据流
- [ ] 替换 Perception 为冻结 DINOv2
- [ ] 用高斯正则化替代 EMA Target Encoder
- [ ] 加入时间拉直 Loss
- [ ] 加入物理随机化 wrapper
- [ ] 跑通 Phase 1-5 完整训练
- [ ] 评估分数达到 800+

---

## 📚 论文速查表

当你需要深入某个概念时，直接看对应论文：

| 我想理解... | 看这篇 |
|-----------|--------|
| DINOv2 为什么好 | Oquab et al., "DINOv2", 2023 |
| JEPA 为什么不预测像素 | 2402.11337 "Reconstruction Produces Uninformative Features" |
| 高斯正则化替代 EMA | 2511.08544 "LeJEPA" |
| 时间拉直 | 2603.12231 "Temporal Straightening" |
| 冻结特征 + 训练预测器 | 2411.04983 "DINO-WM" |
| 端到端 JEPA 世界模型 | 2603.19312 "LeWorldModel" |
| 在想象中训练的误差分析 | 2605.06732 "On Training in Imagination" |
| CEM vs 梯度规划 | 2602.00475 "Parallel Stochastic Gradient Planning" |
