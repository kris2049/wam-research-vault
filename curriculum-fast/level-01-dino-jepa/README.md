# Level 1：DINOv2 + JEPA 预测

> **学了什么**：冻结特征 + 潜在空间预测 = 世界模型的一半
> **硬件**：6G VRAM 足够 | **时间**：2 天

---

## 🎯 核心问题

世界模型的本质是：**给定当前状态 + 动作 → 预测下一状态**。

但"状态"是什么？不是像素。是一个压缩的**表示向量**。

谁来产生这个表示？可以用一个**已经训练好的模型**——比如 DINOv2。

---

## 📖 概念 1：DINOv2 是什么

DINOv2 是 Meta 的一个**自监督视觉模型**。给它一张图 → 输出一个向量。

```
输入: 一张猫的图片 (224×224)
输出: z ∈ ℝ^384  （384 个数字的向量）

相似的图片 → 相似的向量
不同的图片 → 不同的向量
```

**为什么 DINOv2 的表示"好"？**

因为它是在 1.42 亿张图片上训练的。它见过：
- 各种路面（公路、停车场 → 和 CarRacing 的路面很像）
- 各种草地（草坪、公园 → 和 CarRacing 的草地很像）
- 各种边缘和纹理（路缘石、标线）

所以它已经**知道怎么"看"**。我们不需要重新训练它。

---

## 📖 概念 2：JEPA 预测

JEPA 的核心思想只有一句话：**不预测像素，预测表示**。

```
不好：看到当前帧 → 画出下一帧的每一个像素（浪费算力，预测噪声）
好：  看到当前帧 → 预测下一帧的"表示向量"（只预测语义信息）
```

**最简单的 JEPA 预测器**：

```python
# 当前帧 → DINOv2(冻结) → z_curr [384]
# 动作 a_t [3]

# 预测器：小型 MLP
z_next_pred = Predictor(z_curr, a_t)   # [384]

# 目标（训练时）：下一帧的真实表示
with torch.no_grad():
    z_next_true = DINOv2(next_frame)    # [384]

# Loss：预测和真实越接近越好
loss = (z_next_pred - z_next_true).pow(2).mean()
```

---

## 🔬 实验 1.1：用 DINOv2 看 CarRacing

**目标**：加载 DINOv2，提取一帧赛车画面的表示，验证"相似画面→相似向量"。

```python
"""实验 1.1: DINOv2 特征提取"""
import torch
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

# 1. 加载 DINOv2
dinov2 = torch.hub.load("facebookresearch/dinov2", "dinov2_vits14")
dinov2.eval()

# 2. 启动 CarRacing，收集几帧
env = gym.make("CarRacing-v2", render_mode="rgb_array")
frames = []
for _ in range(3):
    obs, _ = env.reset()
    for _ in range(20):
        obs, _, _, _, _ = env.step(env.action_space.sample())
        frames.append(obs)

# 3. 预处理：84×84 → 224×224 → DINOv2
def extract(obs):
    img = torch.FloatTensor(obs).permute(2,0,1) / 255.0    # [3,96,96]
    img = torch.nn.functional.interpolate(img.unsqueeze(0), size=224, mode='bilinear')
    with torch.no_grad():
        return dinov2(img).squeeze(0)                       # [384]

features = torch.stack([extract(f) for f in frames])        # [N, 384]

# 4. 计算相似度
sim = features @ features.T                                 # [N, N]
print("特征相似度矩阵 (越近的对角线应该越相似):")
print(sim[:5, :5].numpy().round(2))

# 5. 验证：相邻帧应该非常相似
for i in range(len(frames)-1):
    cos = torch.cosine_similarity(features[i], features[i+1], dim=0)
    print(f"帧{i}→帧{i+1} 余弦相似度: {cos:.3f}")

env.close()
print("\n✅ 如果相邻帧相似度 > 0.95，DINOv2 对 CarRacing 有效")
```

---

## 🔬 实验 1.2：迷你 JEPA 预测器

**目标**：训练一个最简单的预测器——从当前帧的 DINOv2 特征 + 动作 → 预测下一帧的 DINOv2 特征。

```python
"""实验 1.2: 迷你 JEPA 预测器"""
import torch
import torch.nn as nn
import gymnasium as gym
import numpy as np

# 1. 冻结编码器
dinov2 = torch.hub.load("facebookresearch/dinov2", "dinov2_vits14").eval()

def encode(obs_batch):
    """obs_batch: [B, 3, 96, 96] → [B, 384]"""
    obs_224 = nn.functional.interpolate(obs_batch, size=224, mode='bilinear')
    with torch.no_grad():
        return dinov2(obs_224)

# 2. 预测器（只有这个要训练！）
predictor = nn.Sequential(
    nn.Linear(384 + 3, 256),  # DINOv2 特征 [384] + 动作 [3]
    nn.ReLU(),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Linear(128, 384),      # 预测下一帧的特征
)

# 3. 收集数据
env = gym.make("CarRacing-v2", render_mode="rgb_array")
data = []
obs, _ = env.reset()
for _ in range(1000):
    action = env.action_space.sample()
    next_obs, _, _, _, _ = env.step(action)
    data.append((obs, action, next_obs))
    obs = next_obs
env.close()
print(f"收集了 {len(data)} 条数据")

# 4. 训练
opt = torch.optim.Adam(predictor.parameters(), lr=1e-3)

for epoch in range(50):
    batch = np.random.choice(len(data), 64, replace=False)
    obs_b = torch.FloatTensor(np.stack([data[i][0] for i in batch])).permute(0,3,1,2) / 255.0
    act_b = torch.FloatTensor(np.stack([data[i][1] for i in batch]))
    nxt_b = torch.FloatTensor(np.stack([data[i][2] for i in batch])).permute(0,3,1,2) / 255.0
    
    z_curr = encode(obs_b)                              # [64, 384]
    z_true = encode(nxt_b)                              # [64, 384]
    z_pred = predictor(torch.cat([z_curr, act_b], -1))  # [64, 384]
    
    loss = (z_pred - z_true).pow(2).mean()
    opt.zero_grad(); loss.backward(); opt.step()
    
    if epoch % 10 == 9:
        print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")

print("\n✅ 如果 Loss 从 ~1.0 降到 ~0.1，预测器学会了预测下一帧的语义特征")
```

---

## ✅ Level 1 检查清单

- [ ] 理解了 DINOv2 是什么，为什么不需要训练
- [ ] 跑通实验 1.1，验证相邻帧相似度 > 0.95
- [ ] 跑通实验 1.2，Loss 从 1.0 降到 0.1
- [ ] 能回答：为什么预测 DINOv2 特征比预测像素更好？

---

## 📚 如果想深入了解

| 问题 | 资源 |
|------|------|
| DINOv2 是怎么训练的？ | 论文：Oquab et al., "DINOv2" (2023)，只需读 Section 2-3 |
| JEPA 为什么不预测像素？ | 2402.11337 "Learning by Reconstruction Produces Uninformative Features" |
