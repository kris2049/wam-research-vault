# Level 2：World Model 动力学 + 防坍缩 + 时间拉直

> **学了什么**：让预测器变成真正的世界模型——稳定、可展开、潜在空间是直的
> **硬件**：6G VRAM | **时间**：2 天

---

## 🎯 核心问题

Level 1 的预测器有一个致命缺陷：**如果循环展开多步，误差会爆炸**。

```
展开 1 步：预测误差 ≈ 0.01  ← 还行
展开 8 步：预测误差 ≈ 0.08  ← 开始不准
展开 50 步：预测误差 ≈ 5.0   ← 完全崩溃
```

Level 2 解决三个问题：
1. **防坍缩**：预测器不能把所有输入都预测成同一个值
2. **时间拉直**：潜在空间中的"运动"应该是直线
3. **循环稳定性**：展开 8 步不爆炸

---

## 📖 概念 1：为什么需要防坍缩

**问题**：如果我只用 L2 Loss 训练预测器，它可能学会"偷懒"。

```
偷懒方案：不管输入是什么，预测器都输出 "0 向量"
  → L2 Loss = ||0 - z_true||² 
  → 如果 z_true 的平均接近 0 → Loss 也不大
  → 预测器学不到任何有用的东西

这就是"表示坍缩" —— 所有预测都一样，失去了信息。
```

**I-JEPA 的解法（2023 年）**：EMA Target Encoder + Stop-Gradient。
- 维护一个"正确答案编码器"的副本，永远不更新（只通过 EMA 慢慢跟）
- 预测器不能"偷懒"——因为正确答案是 Target Encoder 给的，它改不了

**LeJEPA 的解法（2025 年，我们现在用的）**：高斯正则化。
- 更简单：不需要副本，只加一项 Loss

```
L_total = L_prediction + λ × KL( N(z_batch), N(0, I) )

               └─ 预测误差           └─ 高斯正则化：整个 batch 的表示必须
                                      接近标准高斯分布 N(0, I)
```

**为什么高斯正则化能防坍缩？**

```
如果预测器"偷懒"输出全零 → z_batch 的分布 = 全部集中在 0
→ 方差 ≈ 0
→ KL( N(0, ε), N(0, 1) ) → 巨大！
→ 预测器被惩罚，被迫保持多样性

如果预测器正常输出 → z_batch 的分布 ≈ N(0, I)
→ KL( N(0, I), N(0, 1) ) ≈ 0
→ 没有额外惩罚
```

---

## 📖 概念 2：时间拉直

**问题**：在自然训练的潜在空间中，状态的变化轨迹通常是弯曲的。

```
弯道中汽车的运动：
  真实世界：圆弧运动
  潜在空间：弯曲的轨迹

  CEM 规划时，它假设"沿着直线走"→ 在弯曲空间中走直线 = 偏离轨道
```

**解法**：加一项 Loss，强迫相邻两步的"变化量"保持一致。

```python
L_straighten = || (z_{t+1} - z_t) - (z_{t+2} - z_{t+1}) ||²

翻译：第一步的变化 应该 ≈ 第二步的变化
效果：潜在空间中的轨迹被"拉直"
      → CEM 规划时走直线 = 走在正确的轨迹上
```

---

## 📖 概念 3：循环展开

世界模型必须能**连续预测多步**，而不只是一步。

```python
# 单步预测（Level 1 做的）
z_next = predictor(z_curr, action)

# 多步展开（Level 2 需要的）
z = z_0
for t in range(H):
    z = predictor(z, action_seq[t])
# 现在 z = 第 H 步的预测状态
```

循环展开时，预测器必须足够稳定。时间拉直帮助稳定性（因为直线轨迹不容易发散）。

---

## 🔬 实验 2.1：可视化高斯正则化

**目标**：理解高斯正则化到底是干什么的。

```python
"""实验 2.1: 高斯正则化的效果"""
import torch
import numpy as np

def gaussian_kl(z_batch):
    """计算 batch 表示的 KL 散度 vs 标准高斯"""
    mean = z_batch.mean(dim=0)
    var  = z_batch.var(dim=0, unbiased=False)
    kl   = 0.5 * (var + mean.pow(2) - 1 - var.log()).sum()
    return kl.item()

# 场景 1：正常分布
normal = torch.randn(1000, 64)        # N(0,1)，64 维
print(f"正常分布 N(0,1):          KL = {gaussian_kl(normal):.2f}")

# 场景 2：坍缩分布（全部相同）
collapsed = torch.zeros(1000, 64)     # 全部是 0
print(f"坍缩分布（全零）:          KL = {gaussian_kl(collapsed):.2f}")

# 场景 3：方差很小的分布
small_var = torch.randn(1000, 64) * 0.01
print(f"小方差 N(0,ε):             KL = {gaussian_kl(small_var):.2f}")

# 场景 4：偏离中心的分布
shifted = torch.randn(1000, 64) + 3.0
print(f"偏离中心 N(3,1):          KL = {gaussian_kl(shifted):.2f}")

print("\n✅ 坍缩和小方差的 KL 远大于正常分布 → 高斯正则化有效")

# 可视化：三个分布的直方图
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, (data, title) in zip(axes, [
    (normal[:, 0], f"Normal KL={gaussian_kl(normal):.1f}"),
    (collapsed[:, 0], f"Collapsed KL={gaussian_kl(collapsed):.1f}"),
    (small_var[:, 0], f"Small var KL={gaussian_kl(small_var):.1f}"),
]):
    ax.hist(data.numpy(), bins=50, alpha=0.7)
    ax.set_title(title)
plt.savefig("gaussian_reg.png")
print("📊 已保存 gaussian_reg.png")
```

---

## 🔬 实验 2.2：稳定的循环世界模型

**目标**：用高斯正则化 + 时间拉直，训练一个能稳定展开 10 步的预测器。

```python
"""实验 2.2: 稳定的世界模型"""
import torch
import torch.nn as nn
import gymnasium as gym
import numpy as np

dinov2 = torch.hub.load("facebookresearch/dinov2", "dinov2_vits14").eval()

def encode(obs_batch):
    obs_224 = nn.functional.interpolate(obs_batch, size=224, mode='bilinear')
    with torch.no_grad():
        return dinov2(obs_224)

# 预测器（和 Level 1 一样，但训练方式不同）
predictor = nn.Sequential(
    nn.Linear(384 + 3, 256), nn.ReLU(),
    nn.Linear(256, 128), nn.ReLU(),
    nn.Linear(128, 384),
)

# 收集连续序列数据（每组 12 帧）
env = gym.make("CarRacing-v2", render_mode="rgb_array")
sequences = []
obs, _ = env.reset()
seq_frames, seq_actions = [], []
for _ in range(5000):
    action = env.action_space.sample()
    seq_frames.append(obs); seq_actions.append(action)
    obs, _, _, _, _ = env.step(action)
    if len(seq_frames) == 12:
        sequences.append((seq_frames, seq_actions))
        seq_frames, seq_actions = [], []
env.close()

opt = torch.optim.Adam(predictor.parameters(), lr=1e-3)
lambda_kl = 0.1        # 高斯正则化权重
lambda_st = 0.05       # 时间拉直权重

for epoch in range(100):
    batch_idx = np.random.choice(len(sequences), 16, replace=False)
    total_loss = 0
    
    for idx in batch_idx:
        frames, actions = sequences[idx]
        obs_b = torch.FloatTensor(np.stack(frames[:-1])).permute(0,3,1,2)[:,:,:84,6:90] / 255.0
        act_b = torch.FloatTensor(np.stack(actions[:-1]))
        nxt_b = torch.FloatTensor(np.stack(frames[1:])).permute(0,3,1,2)[:,:,:84,6:90] / 255.0
        
        z_curr = encode(obs_b)    # [11, 384]
        z_true = encode(nxt_b)    # [11, 384]
        z_pred = predictor(torch.cat([z_curr, act_b], -1))
        
        # 1. 预测 Loss
        loss_pred = (z_pred - z_true).pow(2).mean()
        
        # 2. 高斯正则化
        loss_kl = 0
        for z in [z_pred, z_true]:
            m, v = z.mean(0), z.var(0, unbiased=False)
            loss_kl += 0.5 * (v + m.pow(2) - 1 - v.log()).sum() / 384
        
        # 3. 时间拉直
        loss_st = 0
        for t in range(len(z_pred) - 2):
            d1 = z_pred[t+1] - z_pred[t]
            d2 = z_pred[t+2] - z_pred[t+1]
            loss_st += (d1 - d2).pow(2).mean()
        
        total_loss += loss_pred + lambda_kl * loss_kl + lambda_st * loss_st
    
    opt.zero_grad(); total_loss.backward(); opt.step()
    
    if epoch % 20 == 19:
        print(f"Epoch {epoch+1}: pred={loss_pred.item():.4f} "
              f"kl={loss_kl.item():.4f} st={loss_st.item():.4f}")

# 测试：循环展开 10 步，误差是否累积
with torch.no_grad():
    frames_test, actions_test = sequences[0]
    obs_t = torch.FloatTensor(frames_test[0]).permute(2,0,1).unsqueeze(0)[:,:,:84,6:90] / 255.0
    z_start = encode(obs_t)
    
    z = z_start
    errors = []
    for t in range(10):
        a = torch.FloatTensor(actions_test[t]).unsqueeze(0)
        z = predictor(torch.cat([z, a], -1))
        z_real = encode(torch.FloatTensor(frames_test[t+1]).permute(2,0,1).unsqueeze(0)[:,:,:84,6:90] / 255.0)
        err = (z - z_real).pow(2).mean().item()
        errors.append(err)
        print(f"  Step {t+1}: 累积误差 = {err:.4f}")

print("\n✅ 如果展开 10 步的误差 < 0.5，世界模型足够稳定")
```

---

## ✅ Level 2 检查清单

- [ ] 跑通实验 2.1，理解 KL 散度为什么能防坍缩
- [ ] 跑通实验 2.2，展开 10 步误差 < 0.5
- [ ] 能回答：高斯正则化和 EMA 哪种更简单？为什么 LeJEPA 选了高斯正则化？
- [ ] 能回答：时间拉直为什么对 CEM 规划有帮助？
