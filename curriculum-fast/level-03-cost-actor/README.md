# Level 3：Cost 函数 + CEM 规划

> **学了什么**：世界模型能预测未来了——但"哪个未来是好的"？
> **硬件**：无需额外 GPU | **时间**：1.5 天

---

## 🎯 核心问题

Level 2 结束，你有一个能"预见未来"的世界模型。

```
给定当前状态 + 动作序列 → 预测未来 8 步的状态

但 CEM 面临一个问题：
  候选 A 预测的未来：车在路面上，速度快
  候选 B 预测的未来：车冲上草地，速度慢
  
  怎么比较这两个未来？→ 需要一个"好坏评判标准" → Cost 函数
```

---

## 📖 概念 1：Cost 函数

**Cost 函数 = 给状态打分**。

```
Cost(s) → ℝ  （一个数字）
  数字越小 = 状态越好
  数字越大 = 状态越差

Cost 不是 World Model 的 Loss！
  世界模型 Loss：衡量"预测有多准"（训练信号）
  Cost：衡量"状态有多好"（决策信号）
```

**CarRacing 的四维 Cost**：

```python
Cost(s) = w₁×(-progress) + w₂×on_track + w₃×(-speed) + w₄×energy
          └─ 前进越多cost越低    └─ 在路面上？  └─ 速度            └─ 动作平滑

负号的含义：
  progress 大 → 好事 → 前面加负号 → cost 降低
  on_track=0（不在路面）→ 坏事 → 前面加正号 → cost 升高
```

**怎么训练 Cost？自动标注。**

```python
def auto_label_on_track(frame):
    """绿色=草地，灰色=路面。看画面中央像素的颜色。"""
    center = frame[42:52, 42:52]  # 中央 10×10
    green_ratio = (center[:,:,1] > center[:,:,0] * 1.2).mean()
    return 1.0 if green_ratio < 0.5 else 0.0  # 1=路面, 0=草地
```

---

## 📖 概念 2：CEM 规划

**CEM (Cross-Entropy Method)**：在动作空间中搜索最优解。

```
问题：在连续动作空间中找到最优动作序列
     动作 = [steer, gas, brake]，每一步都要决定这三个值
     规划 8 步 → 要决定 24 个数字 → 搜索空间巨大

CEM 解法：不暴力搜索，而是迭代收缩搜索范围

算法：
  1. 初始化：认为"最优动作"在 μ 附近，探索半径 σ
  2. 采样：从 N(μ, σ) 采样 K=64 个候选动作序列
  3. 评估：每个候选 → World Model 展开 → Cost 打分
  4. 选精英：保留 Cost 最低的 M=8 个
  5. 更新：μ = 精英的均值, σ = 精英的标准差
  6. 重复 2-5 共 3 轮
  
  最终：μ 的第一个动作为最优动作
```

**为什么有效？**

```
第 1 轮：σ 大 → 到处探索（"直行？左转？右转？"）
第 2 轮：σ 缩小 → 在"看起来不错"的区域精修
第 3 轮：σ 更小 → 精确找到最优
```

---

## 🔬 实验 3.1：Cost 函数的直觉

**目标**：手写几个状态的 Cost，理解四维代价的含义。

```python
"""实验 3.1: Cost 函数的直觉"""
import numpy as np

def compute_cost(progress, on_track, speed, smoothness,
                 w_prog=1.0, w_track=5.0, w_speed=0.5, w_smooth=0.1):
    return (-w_prog * progress + w_track * (1 - on_track)
            - w_speed * speed + w_smooth * (1 - smoothness))

# 场景 1：直道高速
c1 = compute_cost(progress=0.9, on_track=1.0, speed=0.9, smoothness=0.9)
print(f"直道高速:         Cost = {c1:.2f}")  # 应该很低（负数）

# 场景 2：冲上草地
c2 = compute_cost(progress=0.3, on_track=0.0, speed=0.3, smoothness=0.5)
print(f"冲上草地:         Cost = {c2:.2f}")  # 应该很高（正数）

# 场景 3：弯道低速但安全
c3 = compute_cost(progress=0.5, on_track=1.0, speed=0.3, smoothness=0.9,
                  w_track=10.0)  # ← Configurator 提高了 track 权重
print(f"弯道安全低速:     Cost = {c3:.2f}")

# 场景 4：弯道高速但危险
c4 = compute_cost(progress=0.7, on_track=1.0, speed=0.8, smoothness=0.5,
                  w_track=10.0)
print(f"弯道高速危险:     Cost = {c4:.2f}")

print("\n✅ 理解：Cost 越低越好。track 权重高时，安全 > 速度")
```

---

## 🔬 实验 3.2：CEM 规划可视化

**目标**：在一个简化的一维优化问题上跑 CEM，理解它如何收缩搜索范围。

```python
"""实验 3.2: CEM 在一维函数上的表现"""
import numpy as np
import matplotlib.pyplot as plt

def objective(x):
    """我们要最小化的函数：两个谷底"""
    return (x - 2)**2 + 3 * np.sin(3 * x) + 5

# CEM 参数
K, M, N = 64, 8, 3   # 候选数、精英数、迭代轮数
mu, sigma = 5.0, 3.0  # 初始猜测：最优在 5 附近，不确定范围 ±3

history = [(mu, sigma)]
x_plot = np.linspace(-3, 8, 500)

for n in range(N):
    # 1. 采样
    candidates = mu + sigma * np.random.randn(K)
    # 2. 评估
    scores = objective(candidates)
    # 3. 选精英
    elite_idx = np.argsort(scores)[:M]
    elites = candidates[elite_idx]
    # 4. 更新
    mu = elites.mean()
    sigma = elites.std()
    history.append((mu, sigma))

# 可视化
fig, axes = plt.subplots(1, N+1, figsize=(14, 3))
for i, (mu_i, sigma_i) in enumerate(history):
    ax = axes[i]
    ax.plot(x_plot, objective(x_plot), 'b-', alpha=0.3)
    ax.axvline(mu_i, color='r', linestyle='--', label=f'μ={mu_i:.2f}')
    ax.fill_between([mu_i-sigma_i, mu_i+sigma_i], 0, 20, alpha=0.2, color='red')
    ax.set_title(f'Round {i}' if i > 0 else 'Init')
    ax.set_ylim(0, 20)
plt.tight_layout()
plt.savefig("cem_demo.png")
print("📊 已保存 cem_demo.png")
print("✅ 观察：σ 越来越小，μ 收敛到最优值（x≈2）")
```

---

## 🔬 实验 3.3：CEM 在 World Model 中规划

**目标**：把 Level 2 的世界模型和 Level 3 的 CEM 组合，完成一次完整规划。

```python
"""实验 3.3: 完整规划"""
import torch
import torch.nn as nn
import numpy as np

# 假设 predictor 已经训练好（从 Level 2 加载）
# 这里用简化版

def plan_one_step(z_curr, predictor, H=8, K=64, M=8, N=3):
    """给定当前状态 z_curr，在 World Model 中规划最优动作"""
    D = 3  # [steer, gas, brake]
    
    # 初始分布
    mu = torch.zeros(H, D)
    mu[:, 1] = 0.5  # 默认：中等油门
    sigma = torch.full((H, D), 0.3)
    
    for _ in range(N):
        # 采样
        candidates = mu + sigma * torch.randn(K, H, D)
        candidates = torch.clamp(candidates,
                                 torch.tensor([-1., 0., 0.]),
                                 torch.tensor([1., 1., 1.]))
        # 评估
        costs = torch.zeros(K)
        for k in range(K):
            z = z_curr.clone()
            for t in range(H):
                a = candidates[k, t:k+1]
                z = predictor(torch.cat([z, a], -1))
                # 简化 Cost：离 z_curr 太远 = 不好（保守驾驶）
                costs[k] += 0.95**t * (z - z_curr).pow(2).mean()
        
        # 精英
        _, idx = torch.topk(costs, M, largest=False)
        elites = candidates[idx]
        mu = elites.mean(dim=0)
        sigma = elites.std(dim=0).clamp(min=0.01)
    
    return mu[0].numpy()  # 第一帧最优动作

# 测试
z_test = torch.randn(1, 384)  # 假状态
predictor = nn.Sequential(nn.Linear(387, 128), nn.ReLU(), nn.Linear(128, 384))
action = plan_one_step(z_test, predictor)
print(f"规划结果: steer={action[0]:.2f}, gas={action[1]:.2f}, brake={action[2]:.2f}")
print("\n✅ CEM 规划器可以输出连续动作")
```

---

## ✅ Level 3 检查清单

- [ ] 跑通实验 3.1，理解 Cost 的四维分解
- [ ] 跑通实验 3.2，理解 CEM 如何迭代收缩
- [ ] 跑通实验 3.3，理解 Cost + CEM + World Model 如何协同
- [ ] 能回答：Cost 和 World Model Loss 的区别是什么？
