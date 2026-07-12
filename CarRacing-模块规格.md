# CarRacing LeCun 世界模型 — 完整模块规格

> 每个模块的精确架构、超参数、输入输出维度、训练方案。可直接照着实现。

---

## 架构总览

```
┌──────────────────────────────────────────────────────────────────┐
│                        CarRacing × LeCun                          │
│                                                                   │
│  Frame (96×96×3)                                                  │
│       │                                                           │
│  ┌────▼──────────────────────────────┐                            │
│  │ PERCEPTION (CNN)                   │  §1                       │
│  │   → s_t (256d) + h_t (256d GRU)    │                            │
│  └────┬──────────────────────────────┘                            │
│       │ (s_t, h_t)                                                │
│  ┌────▼──────────────────────────────┐                            │
│  │ CONFIGURATOR (Scene Classifier)    │  §5                       │
│  │   → scene_id ∈ {straight, turn_L,  │                            │
│  │                  turn_R, chicane}  │                            │
│  └────┬──────────────────────────────┘                            │
│       │ scene_id                                                  │
│  ┌────▼──────────────────────────────┐                            │
│  │ WORLD MODEL (JEPA Dynamics)        │  §2                       │
│  │   (s_t, h_t, a_t) → (ŝ_{t+1}, ĥ_{t+1})                       │
│  │   + Reward Decoder: → r̂_t         │                            │
│  │   + Done Decoder:    → d̂_t         │                            │
│  └────┬──────────────────────────────┘                            │
│       │ ŝ_{t+1}                                                  │
│  ┌────▼──────┐  ┌────────────────────┐                            │
│  │ COST       │  │ ACTOR (CEM MPC)    │  §3, §4                   │
│  │ Head       │  │                    │                            │
│  │ Cost(ŝ) =  │  │ 在 WM 中想象 H=8 步 │                            │
│  │ w·features │  │ CEM: K=64, M=8,    │                            │
│  │            │  │       N_iter=3     │                            │
│  └────────────┘  └────────┬───────────┘                            │
│                           │ a_t = [steer, gas, brake]             │
│                           ▼                                       │
│                      Environment                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

## §1 Perception（CNN 编码器）

### 1.1 架构

```
输入: frame ∈ ℝ^{96×96×3} (uint8 → float32, /255)

┌─────────────────────────────────────────────────────┐
│ Layer          │ Output      │ Params               │
├────────────────┼─────────────┼──────────────────────┤
│ Conv2d 3→32    │ 96×96×32    │ k=3,s=1,p=1 + BN+ReLU│
│ Conv2d 32→64   │ 48×48×64    │ k=3,s=2,p=1 + BN+ReLU│
│ Conv2d 64→128  │ 24×24×128   │ k=3,s=2,p=1 + BN+ReLU│
│ Conv2d 128→256 │ 12×12×256   │ k=3,s=2,p=1 + BN+ReLU│
│ ResBlock ×2    │ 12×12×256   │ k=3,s=1,p=1 (残差)    │
│ GlobalAvgPool  │ 256         │ —                     │
│ Linear 256→256 │ 256         │ s_t (感知表示)          │
└─────────────────────────────────────────────────────┘

总参数量: ~1.4M
RFs (感受野): 第 1 层 3×3 → 第 3 层 15×15 → 第 5 层 35×35（看到半张图）
```

### 1.2 和 GRU Memory 的集成

```
Memory 不是一个独立模块，而是 Perception 的一部分：

  h_t = GRU(Linear([s_t, a_{t-1}]), h_{t-1})

  其中:
    s_t ∈ ℝ^256 (当前帧的视觉表示)
    a_{t-1} ∈ ℝ^3 (上一帧执行的动作)
    h_t ∈ ℝ^256 (GRU 隐状态)
    h_0 = zeros(256)

Memory 捕捉的内容:
  - 短期速度/方向: 最近几帧的位置变化
  - 赛道上下文: "我刚才在直道/弯道"
  - 这些信息编码在 h_t 中，不需要显式堆叠历史帧
```

### 1.3 Target Encoder（训练用）

```
Target Encoder = Perception 的 EMA 副本
  - 架构完全相同
  - 参数: θ_target = 0.999 × θ_target + 0.001 × θ_context
  - 永远不通过梯度更新（requires_grad=False + EMA）
  - 只在训练时存在，推理时删除
```

---

## §2 World Model（JEPA 动力学预测器）

### 2.1 核心架构

```
输入: (s_t, h_t, a_t)
  s_t ∈ ℝ^256  当前视觉表示
  h_t ∈ ℝ^256  GRU 隐状态（记忆）
  a_t ∈ ℝ^3    动作 [steer, gas, brake]

┌──────────────────────────────────────────────────────┐
│ Step 1: 动作嵌入                                     │
│   a_emb = Linear(3→64)(a_t)  ∈ ℝ^64                 │
│                                                      │
│ Step 2: 状态拼接                                     │
│   x = Concat[s_t, h_t, a_emb]  ∈ ℝ^576              │
│                                                      │
│ Step 3: Dynamics Predictor                           │
│   ┌─────────────────────────────────────┐            │
│   │ Linear 576→512 + LayerNorm + ReLU    │            │
│   │ Linear 512→512 + LayerNorm + ReLU    │            │
│   │ Linear 512→512 + LayerNorm + ReLU    │            │
│   └─────────────────────────────────────┘            │
│                                                      │
│ Step 4: 输出头                                       │
│   ŝ_{t+1} = Linear(512→256)(x)     下一帧视觉表示      │
│   ĥ_{t+1} = Linear(512→256)(x)     下一帧 GRU 状态     │
│   r̂_t     = Linear(512→1)(x)       预测奖励            │
│   d̂_t     = Linear(512→1)(x)       预测终止 (sigmoid)  │
└──────────────────────────────────────────────────────┘

总参数量: ~2.1M
```

### 2.2 为什么加了 Reward Decoder 和 Done Decoder？

这是**从 Dreamer 借来的实用改进**，不影响 JEPA 纯净性：

```
纯 JEPA:        只预测 ŝ_{t+1}，Loss = L2(ŝ, sg(s_target))
JEPA + 辅助任务: 同时预测 reward 和 done → 多任务学习

辅助任务的好处:
  1. Reward 预测提供额外梯度信号 → 世界模型学得更快
  2. Done 预测让 Agent 知道"什么时候会死"→ 规划时避开危险状态
  3. 这两个 decoder 是轻量的（各 512→1），不增加多少开销
  4. 和 JEPA 核心 Loss 完全不冲突（reward/done 用真实标签，不经过 Stop-Grad）
```

### 2.3 损失函数

```python
def world_model_loss(batch):
    # batch: (frame_t, a_t, frame_{t+1}, r_t, done_t)
    
    # Forward
    s_t, h_t = perception(frame_t, h_{t-1}, a_{t-1})
    
    with torch.no_grad():
        s_target, _ = target_encoder(frame_{t+1}, h_t, a_t)  # Stop-Grad
    
    s_next_pred, h_next_pred, r_pred, done_pred = world_model(s_t, h_t, a_t)
    
    # Losses
    loss_jepa   = F.mse_loss(s_next_pred, s_target)           # 核心 JEPA Loss
    loss_reward = F.mse_loss(r_pred, r_t)                      # 奖励预测
    loss_done   = F.binary_cross_entropy(done_pred, done_t)    # 终止预测
    loss_hidden = F.mse_loss(h_next_pred, h_t.detach())        # GRU 状态一致性
    
    total_loss = loss_jepa + 0.1*loss_reward + 0.1*loss_done + 0.05*loss_hidden
    
    return total_loss
```

### 2.4 超参数

```
优化器:      AdamW, lr=3e-4, weight_decay=1e-5
Batch size:  256 (需要 ~8G VRAM；如果不够就降到 128)
EMA decay:   0.999 (Target Encoder 更新速率)
训练 epochs: 100 (或直到 loss_jepa < 0.01)
梯度裁剪:    max_norm=1.0
```

---

## §3 Cost（成本函数）

### 3.1 架构

```
Cost Head 是一个轻量级 MLP，接在 Perception 输出后面：

输入: s_t ∈ ℝ^256

┌──────────────────────────────────────┐
│ CostHead:                            │
│   Linear(256→128) + ReLU              │
│   Linear(128→64) + ReLU               │
│   Linear(64→4)                        │
│                                       │
│ 输出: 4 维 Cost 分解                   │
│   [c_progress, c_track, c_speed,       │
│    c_energy]                          │
│                                       │
│ 总 Cost = Σ w_i × c_i                 │
│ 权重 w = [1.0, 5.0, 0.5, 0.1]        │
└──────────────────────────────────────┘
```

### 3.2 Cost 四个维度

| Cost 维度 | 含义 | 训练信号 | 权重 |
|-----------|------|---------|------|
| **c_progress** | 向前走了多远（0→1） | 用 tile 访问进度作 label | 1.0 |
| **c_track** | 在路面上吗？（0/1） | 用路面 mask 作 label（可从画面提取） | 5.0 |
| **c_speed** | 速度合理吗？ | 从连续帧的位置变化估算速度 | 0.5 |
| **c_energy** | 动作平滑吗？ | 相邻动作变化量 | 0.1 |

### 3.3 训练方案

**Phase 1："On-Track" 二分类（最简单，最关键）**

```
车道分割的简单近似：画面中绿色=草地，灰色=路面

on_track(frame) = mean((frame 的绿色通道 < 阈值) & (frame 的灰色通道 > 阈值)) > 0.3

这是一个弱监督信号——不需要人工标注，直接从画面颜色算。
然后训练 Cost Head 来预测这个信号：

loss_track = BCE(CostHead(s_t)[1], on_track_label)
```

**Phase 2：进度回归**

```
CarRacing 环境在每帧返回"已访问 tile 数 / 总 tile 数"。

可以直接用这个作为 c_progress 的 label：
loss_progress = MSE(CostHead(s_t)[0], progress_fraction)
```

**Phase 3：速度和能量（可选，最后加）**

```
c_speed  label: 从 (position_{t+1} - position_t) 的模长估算
c_energy label: 从 ||a_t - a_{t-1}|| 计算动作变化量

这两个是"锦上添花"的，先不加也可以。
```

### 3.4 Actor 如何使用 Cost

```
Actor 在 World Model 中展开 H=8 步时，每一步都调用 Cost：

  for τ in 1..H:
    ŝ_{t+τ} = WorldModel(ŝ_{t+τ-1}, a_τ)
    cost_τ  = CostHead(ŝ_{t+τ})   ← 预测这一状态的 Cost

  累积 Cost = Σ_{τ=1}^{H} γ^τ × cost_τ  (γ=0.95)

Actor 目标: 找到 a_{1:H} 使得累积 Cost 最小
```

---

## §4 Actor（CEM 规划器）

### 4.1 CEM 算法

```
CEM (Cross-Entropy Method) 在连续动作空间做优化：

输入: 当前状态 (s_t, h_t), 规划视野 H=8
输出: 最优动作 a_t

┌──────────────────────────────────────────────────────────┐
│ Algorithm: CEM_Plan(s_t, h_t, H, K, M, N_iter)           │
│                                                           │
│  动作维度: D = 3  [steer, gas, brake]                     │
│  动作范围: steer ∈ [-1,1], gas ∈ [0,1], brake ∈ [0,1]     │
│                                                           │
│  # 初始化动作分布                                          │
│  μ = repeat(previous_action, H)  ∈ ℝ^{H×3}               │
│  σ = 0.3 × ones(H, 3)                                    │
│                                                           │
│  for iter in 1..N_iter:                                   │
│    # 1. 采样 K=64 个候选动作序列                             │
│    candidates = μ + σ × randn(K, H, 3)                    │
│    candidates = clip(candidates, action_bounds)            │
│                                                           │
│    # 2. 在 World Model 中评估每个候选                        │
│    costs = []                                              │
│    for k in 1..K:                                         │
│      ŝ = s_t; ĥ = h_t                                    │
│      total_cost = 0                                        │
│      for τ in 1..H:                                       │
│        ŝ, ĥ = WorldModel(ŝ, ĥ, candidates[k,τ])          │
│        total_cost += γ^τ × CostHead(ŝ)                    │
│      costs.append(total_cost)                              │
│                                                           │
│    # 3. 保留精英 (M=8 个 Cost 最低的)                       │
│    elite_idx = argsort(costs)[:M]                          │
│    elite = candidates[elite_idx]  ∈ ℝ^{M×H×3}             │
│                                                           │
│    # 4. 更新分布                                            │
│    μ = mean(elite, dim=0)     ∈ ℝ^{H×3}                   │
│    σ = std(elite, dim=0)      ∈ ℝ^{H×3}                   │
│    σ = max(σ, 0.01)  # 防止 σ → 0                         │
│                                                           │
│  # 返回最终分布均值的第一个动作                                │
│  return μ[0, :]  ∈ ℝ^3                                    │
└──────────────────────────────────────────────────────────┘
```

### 4.2 超参数

```
H (规划视野):       8        ← 太短看不到弯道，太长噪声累积
K (候选数):         64       ← 越大越好，但受推理速度约束
M (精英数):         8        ← 保留前 12.5%
N_iter (CEM 轮数):  3        ← 3 轮通常足够收敛
γ (折扣因子):        0.95
σ_init (初始探索):   0.3      ← 第一轮探索范围大，后面自动缩小
```

### 4.3 推理效率

```
每步 CEM 需要的 World Model 前向次数:
  = N_iter × K × H = 3 × 64 × 8 = 1536 次

World Model 单次前向: ~0.3ms (纯 MLP, 512 维)
CEM 总推理时间: 1536 × 0.3ms ≈ 460ms

这个延迟太高了！需要优化。

优化方案: Batch 推理
  不逐个评估 64 个候选，而是一次性把所有候选喂给 World Model
  候选矩阵: [K×H, 256+256+64] = [512, 588]
  World Model 一次前向处理 512 个状态并行

优化后推理时间: ~5ms（GPU 并行，512 个状态 ≈ 1 个 batch 的时间）

加上 Perception (CNN) 的 ~2ms，总推理 ~7ms/帧
→ 约 140 FPS，远超 CarRacing 的实时需求
```

### 4.4 探索策略

```
训练时: 以概率 ε 执行随机动作（ε 从 1.0 → 0.1 衰减）
推理时: 直接执行 CEM 规划的最优动作

探索策略:
  ε = max(0.1, 1.0 - step/50000)  # 前 50K 步逐渐减少随机性
  
  当随机探索时:
    a_t = clip(μ_cem[0] + 0.2×randn(3), action_bounds)
    # 在 CEM 最优动作上加噪声，而非完全随机
```

---

## §5 Configurator（场景分类器）

### 5.1 架构

```
Configurator 是一个轻量分类器，接在 Perception 输出后面：

输入: s_t ∈ ℝ^256

┌────────────────────────────────────┐
│ Scene Classifier:                  │
│   Linear(256→128) + ReLU           │
│   Linear(128→4) + Softmax          │
│                                    │
│ 输出: 4 类场景概率                   │
│   [P(straight), P(turn_L),          │
│    P(turn_R), P(chicane)]          │
│                                    │
│ scene_id = argmax(probs)           │
└────────────────────────────────────┘
```

### 5.2 训练信号

**无监督聚类方案**（不需要人工标注）：

```
思路: 连续几帧的转向动作模式决定了场景类型

过去 T=10 帧的平均转向:
  avg_steer = mean(|steer_{t-9} ... steer_t|)

场景分类规则:
  if avg_steer < 0.1:
    label = "straight"
  elif 0.1 ≤ avg_steer < 0.4:
    label = "turn_L" or "turn_R" (根据方向)
  elif avg_steer ≥ 0.4:
    label = "chicane" (急弯)

用这些自动生成的 label 训练 Configurator:
  loss_scene = CrossEntropy(Configurator(s_t), label)

训练时间: 和 World Model 同时训练（多任务学习）
```

### 5.3 Configurator 如何影响其他模块

```
Configurator 的输出并不直接控制 Actor，而是：
  
  1. 调节 Cost 权重:
     if scene == "straight":
       w_speed = 1.0    ← 直道更关注速度
       w_track = 2.0    ← 直道不太担心冲出赛道
     elif scene == "turn":
       w_speed = 0.1    ← 弯道更关注不冲出赛道
       w_track = 10.0

  2. 调节 Actor 探索范围（CEM 的 σ_init）:
     if scene == "straight":
       σ_init = [0.1, 0.3, 0.05]  ← 转向和刹车探索小
     elif scene == "turn":
       σ_init = [0.5, 0.2, 0.3]   ← 转向和刹车探索大

  3. 调节规划视野:
     if scene == "straight":
       H = 8   ← 直道看远点
     elif scene == "turn":
       H = 5   ← 弯道看近点（快速响应）

这些都是"软"影响——不是硬切换，而是参数偏置。
```

---

## §6 训练流程

### 6.1 五阶段训练

```
Phase 1: 数据收集（随机策略）              [~1h, 单 GPU]
  for episode in 1..500:
    随机动作（ε=1.0）
    存储 (frame_t, a_t, r_t, frame_{t+1}, done_t)
    → Replay Buffer: 50,000 transitions

Phase 2: 训练 Perception + World Model    [~4h, 8G VRAM]
  for epoch in 1..100:
    从 Buffer 采样
    训练 JEPA Loss + 辅助任务
    检查坍缩（Loss < 1e-4 → 调大 EMA decay）
    → 世界模型学会预测下一帧表示

Phase 3: 训练 Cost Head                    [~1h, 8G VRAM]
  for epoch in 1..50:
    从 Buffer 采样
    用自动标注训练 on_track + progress
    → Cost Head 学会评估状态好坏

Phase 4: 训练 Actor（在想象中）             [~2h, 8G VRAM]
  for episode in 1..1000:
    从随机初始状态开始
    在 World Model 中展开 8 步
    用 CEM 选择动作
    用 Cost 评估结果
    更新 Actor（但 CarRacing 中 Actor = CEM 规划，无需训练）
  
  注意：在 CEM 方案中，Actor 没有可训练参数！
  Actor = 纯规划算法。不需要 Phase 4。
  但如果以后想换成一个学习到的 Policy Network，这里就要训练。

Phase 5: 在线微调                          [~2h, 8G VRAM]
  for episode in 1..100:
    用 CEM 规划执行动作（ε=0.1 探索）
    用新数据更新 World Model + Cost Head
    逐步减小 ε → 0.01
    → 世界模型适应 CEM 产生的状态分布
```

### 6.2 简化版（MVP）：合并 Phase 2+3+5

```
如果你不想分阶段训练，可以同时训练所有模块：

for epoch in 1..200:
  # 收集新数据
  for episode in 1..10:
    用当前 CEM 规划执行（ε 递减）
  
  # 从 Buffer 采样训练
  for iter in 1..100:
    batch = sample(Buffer)
    
    # 同时训练 World Model + Cost Head + Configurator
    loss = world_model_loss(batch)       # JEPA + reward + done
         + 0.5 * cost_loss(batch)        # on_track + progress
         + 0.1 * scene_loss(batch)       # 场景分类
  
  # 每个 epoch 评估一次
  avg_reward = evaluate(10 episodes)
```

---

## §7 完整超参数表

| 超参数 | 值 | 说明 |
|--------|-----|------|
| **Perception** | | |
| s_dim | 256 | 视觉表示维度 |
| h_dim | 256 | GRU 隐状态维度 |
| **World Model** | | |
| dynamics_hidden | 512 | 动力学预测器隐藏层维度 |
| dynamics_layers | 3 | MLP 层数 |
| ema_decay | 0.999 | Target Encoder EMA 速率 |
| loss_jepa_weight | 1.0 | JEPA Loss 权重 |
| loss_reward_weight | 0.1 | 辅助奖励预测权重 |
| loss_done_weight | 0.1 | 辅助终止预测权重 |
| **Cost** | | |
| cost_hidden | [128, 64] | Cost Head 隐藏层 |
| w_progress | 1.0 | 前进权重 |
| w_track | 5.0 | 路面权重（最重要！） |
| w_speed | 0.5 | 速度权重 |
| w_energy | 0.1 | 平滑权重 |
| **Actor (CEM)** | | |
| H | 8 | 规划视野 |
| K | 64 | 候选动作数 |
| M | 8 | 精英数 |
| N_iter | 3 | CEM 迭代轮数 |
| γ | 0.95 | 折扣因子 |
| **Configurator** | | |
| scene_classes | 4 | [直道, 左弯, 右弯, S弯] |
| scene_history | 10 | 用于自动标注的历史帧数 |
| **训练** | | |
| lr | 3e-4 | AdamW 学习率 |
| batch_size | 256 | 训练 batch |
| buffer_size | 50000 | Replay Buffer 容量 |
| total_env_steps | 100000 | 总交互步数 |
| grad_clip | 1.0 | 梯度裁剪 |

---

## §8 预期性能

```
World Model (JEPA):
  - Loss 从 1.0 → 0.05 (稳定，不坍缩)
  - 坍缩信号: loss < 1e-4 → 立即停止，调大 EMA decay + 减小 lr

Cost Head:
  - on_track 准确率 > 90%
  - progress 误差 < 0.1

CEM 规划:
  - 推理: ~7ms/帧 (Perception 2ms + CEM batch 5ms)
  - 规划质量: 直道选大油门，弯道提前刹车

Configurator:
  - 场景分类准确率 > 85%
  - 主要混淆: turn_L vs chicane（可接受）

总体:
  - 训练后 800+ 分 (完成 1-2 圈)
  - 训练时间: ~10 小时 / 8G VRAM
```

---

*所有模块规格已确定。可以直接开始实现。*
