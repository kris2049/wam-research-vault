# CarRacing × LeCun World Model — 理论架构分析

> 将 LeCun 六模块架构映射到 Gym CarRacing 任务。逐模块分析可行性、难点和计算需求。

---

## 1. 任务分析

### CarRacing-v2 规格

| 维度 | 值 |
|------|-----|
| 观测空间 | 96×96×3 RGB（自顶向下视角） |
| 动作空间 | 3 维连续：[转向 -1..1, 油门 0..1, 刹车 0..1] |
| 奖励 | 每帧 -0.1，超过一个赛道 tile +1000/N（N=tiles总数） |
| 终止条件 | 所有 tile 被访问完成 或 1200 步上限 |
| 难度 | 赛道随机生成，含弯道和直道 |

### 为什么适合测试 World Model？

✅ **视觉输入**：需要 Perception 模块从像素提取表示
✅ **物理动力学**：惯性、转向不足、速度限制 → 需要 World Model 学习
✅ **需要规划**：赛车线选择、入弯刹车点 → 需要 Actor + Cost
✅ **可复现性**：Gym 标准环境，有基线分数
✅ **计算可行**：96×96 分辨率 → 8-12G VRAM 可训练

---

## 2. 六模块架构映射

### 模块 1：Perception（感知）

**输入**：96×96×3 RGB 帧
**输出**：潜在状态向量 s_t ∈ ℝ^256（或其他维度）

```
┌─────────────────────────────────────┐
│           Perception Encoder         │
│                                      │
│  96×96×3 ──► Conv Stem ──► ViT/CNN  │
│              (下采样 4×)    Backbone  │
│              24×24×64     24×24×256   │
│                                      │
│  ──► Global Pool ──► s_t ∈ ℝ^256    │
└─────────────────────────────────────┘
```

**挑战**：
- 赛道是稀疏特征（灰色路面 + 绿色草地 + 红色/白色路缘）→ CNN 的局部感受野足够
- 不需要 ViT 级别的全局注意力（赛道结构简单）
- **结论**：用 CNN backbone（~2M 参数），不需要 ViT

**推荐架构**：Mini CNN-JEPA 风格（参考 2408.07514）
- 3 层 stride-2 卷积：96→48→24（输出 24×24×64）
- 2 层残差块（不降采样）
- 全局平均池化 → 256 维向量

---

### 模块 2：World Model（JEPA 预测器）

这是核心模块。接收当前状态 + 动作，预测未来状态。

```
                    s_t (当前视觉表示)
                         │
                    ┌────▼────┐
                    │  Action  │ ← a_t = [steer, gas, brake]
                    │ Embedding│
                    └────┬────┘
                         │
              ┌──────────▼──────────┐
              │   Dynamics Predictor │
              │   (Transformer or    │
              │    GRU over latents) │
              └──────────┬──────────┘
                         │
                    ŝ_{t+1} (预测的下一帧表示)
                         │
                    ┌────▼────┐
                    │  Loss:  │
                    │  L2(ŝ, s)│ ← 和真实下一帧的 JEPA 表示对齐
                    └─────────┘
```

**两种实现路线**：

#### 路线 A：JEPA 风格（纯潜在空间预测）

```
优点：计算高效，不浪费算力在像素重建上
缺点：需要 EMA + Stop-Gradient 防止坍缩，训练可能不稳定
适合：CarRacing 的视觉简单性可能让 JEPA 训练更稳定
```

**架构**：
- 输入：s_t（256 维）+ a_t（3 维→嵌入 32 维）= 288 维
- Dynamics：2 层 Transformer / GRU → 256 维 → Linear → 256 维
- 输出：ŝ_{t+1}（256 维）
- Loss：||ŝ_{t+1} - sg(s_{t+1})||²（sg = stop-gradient on target encoder）

#### 路线 B：Dreamer/RSSM 风格（随机状态 + 确定状态混合）

```
优点：更成熟，有现成的规划算法（MPC）
缺点：包含重建损失（浪费），但 CarRacing 的 96×96 分辨率不高，可接受
适合：如果你想要一个 100% 能跑的方案而不是研究 JEPA 本身
```

**两种路线的比较**：

| | JEPA 路线 | Dreamer 路线 |
|---|---|---|
| 是否重建像素 | ❌ | ✅（但可以关掉，像 Dreamer-CDP） |
| 训练稳定性 | 需要技巧 | 更稳定 |
| 规划能力 | 需要额外设计 | 内置 MPC |
| 计算量 | 更低 | 中等（含解码器） |
| 对齐 LeCun 理论 | ✅ 完全对齐 | 🟡 部分对齐 |
| 实现难度 | 中等 | 低（有开源代码） |

**推荐**：先 Dreamer 路线验证可行性，再替换为 JEPA 路线验证理论。

---

### 模块 3：Cost（成本函数）

这是 CarRacing 最有意思的部分。Cost 告诉 Agent "当前状态有多好/多坏"。

**CarRacing 的自然 Cost 分解**：

```
Cost(s_t, a_t) = w₁ × ProgressCost    （前进进度）
               + w₂ × TrackCost        （是否在赛道上）
               + w₃ × SpeedCost        （速度是否合理）
               + w₄ × SmoothnessCost   （动作是否平滑）
               + w₅ × EnergyCost       （是否高效）
```

**具体设计**：

```
ProgressCost(s_t, s_{t-1}) = -d_progress  （负号：前进越多 Cost 越低）

  d_progress = 赛车沿赛道方向前进的距离
  怎么计算？从 Perception 的潜在表示中解码出"赛道位置"：
  ┌──────────────┐
  │  Cost Head    │ ← 一个小 MLP，接在 Perception 编码器后面
  │  预测:        │
  │  - on_track   │   二分类：赛车在路面上吗？
  │  - progress   │   回归：距离上一个 tile 的进度（0..1）
  │  - speed_norm │   回归：当前速度是否合理（0..1）
  └──────────────┘
```

**关键设计选择**：
- **Intrinsic vs Extrinsic**：环境给的外部奖励 ≠ Cost。LeCun 的 Cost 应该是**可学习的、内在的**——Agent 自己对"好坏"的判断
- **为什么不用环境奖励当 Cost？**：因为环境奖励是稀疏的（只有过 tile 才给分），而 Cost 需要在每一帧都给出密集信号
- **怎么训练 Cost？**：从成功/失败的 episode 中学习。成功轨迹 → 低 Cost，失败轨迹（如冲出赛道）→ 高 Cost

---

### 模块 4：Actor（行动器）

Actor 的任务：找到一个动作序列，最小化 World Model 预测的未来 Cost。

```
算法：Model Predictive Control (MPC) in Latent Space

┌──────────────────────────────────────────────────────┐
│  在每一步 t：                                          │
│                                                       │
│  1. 编码当前帧 s_t = Perception(frame_t)               │
│                                                       │
│  2. 在 World Model 中"想象"H 步未来：                    │
│     for τ in 1..H:                                    │
│       采样 K 个候选动作序列 {a⁽¹⁾, a⁽²⁾, ..., a⁽ᴷ⁾}     │
│       for each a⁽ᵏ⁾:                                  │
│         用 World Model 展开 H 步                       │
│         ŝ_{t+τ} = WorldModel(ŝ_{t+τ-1}, a⁽ᵏ⁾_τ)       │
│         计算累积 Cost: Σ Cost(ŝ_{t+τ})                  │
│                                                       │
│  3. 选择 Cost 最低的动作序列的第一个动作                    │
│                                                       │
│  4. 执行动作，观测真实下一帧，更新 World Model              │
└──────────────────────────────────────────────────────┘
```

**CarRacing 的特殊性**：
- 规划视野 H 不需要太长：5-10 步足够（赛道曲率不会突变）
- 候选动作数 K 可以很小：5-10 个（连续动作空间，可以用 CEM 优化）
- 动作空间连续 → 用 Cross-Entropy Method (CEM) 而非随机采样

**CEM 规划（轻量版）**：
```
1. 初始化：动作分布 N(μ=当前最优猜测, σ=探索范围)
2. 采样 K 个动作序列
3. 在 World Model 中评估每个序列的 Cost
4. 保留 Cost 最低的 M 个序列（精英）
5. 用精英序列的均值和方差更新分布
6. 重复 2-5 共 N 轮
7. 执行最终分布均值的第一帧动作
```

---

### 模块 5：Configurator（配置器/注意力路由器）

CarRacing 需要 Configurator 吗？**需要，但可以很简单。**

**CarRacing 的自然层级**：

```
高层 Configurator："当前赛段是直道还是弯道？"
  │
  ├── 如果是直道：
  │     ├── World Model 聚焦"速度预测"
  │     ├── Cost 关注"最大化前进速度"
  │     └── Actor 动作分布偏向"大油门、小转向"
  │
  └── 如果是弯道：
        ├── World Model 聚焦"转向动力学"
        ├── Cost 关注"不冲出赛道 + 找到 apex"
        └── Actor 动作分布偏向"刹车入弯 + 转向"
```

**简化实现**：Configurator 可以退化为一个**场景分类器 + 条件模块**。

```
┌────────────────────────────────────┐
│  Scene Classifier (轻量 MLP)        │
│  输入: s_t (256维潜在状态)           │
│  输出: c ∈ {straight, left_turn,    │
│            right_turn, chicane}     │
│                                    │
│  每种场景有独立的 Actor 参数偏置      │
│  Actor(s_t | c=straight)           │
│  Actor(s_t | c=turn)               │
└────────────────────────────────────┘
```

**不做 Configurator 会怎样？**：一个单一 Actor 可能在直道和弯道之间"平均"，导致弯道太激进或直道太保守。加入场景条件相当于给了 Actor 一个"顶层指令"。

---

### 模块 6：Short-Term Memory（短期记忆）

**CarRacing 需要多少记忆？**

考虑这个场景：你正在过一个 S 弯。刚过了左弯，现在要过右弯。你需要记住"我刚才在左弯"才能调整右弯的策略。

```
时间线：
t-3: 直道末尾
t-2: 开始左转 ← 需要这个信息
t-1: 左转中
t:   开始右转 ← 在这里做决策时，需要知道 t-2 的状态
```

**实现**：
- 最简单：堆叠最近 3-4 帧作为 Perception 输入（类似于 DQN 的做法）
- 中等：在 World Model 的 Dynamics 里使用 GRU 而非 Transformer，GRU 自带隐状态记忆
- 复杂：用 Transformer 的 causal attention 关注过去 N 帧

**推荐**：GRU 方式（和 Dreamer 的 RSSM 一致），隐状态维度 256 足够。

---

## 3. 完整架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                     LeCun × CarRacing                            │
└─────────────────────────────────────────────────────────────────┘

  Camera (96×96×3)
       │
       ▼
┌──────────────────┐
│   Perception      │  CNN Encoder (3层 stride-2 conv + 2残差块)
│   96×96×3 → 256   │  → s_t (256维)
└────────┬─────────┘
         │ s_t
    ┌────▼────┐
    │ Memory  │  GRU: h_t = f(h_{t-1}, s_t, a_{t-1})
    │ (GRU)   │  → (s_t, h_t) 联合状态
    └────┬────┘
         │ (s_t, h_t)
         │
    ┌────▼─────────────────────────────────────┐
    │           Configurator                    │
    │  Scene Classifier: straight / turn / S    │
    │  ──► 选择 Actor 模式 + Cost 权重           │
    └────┬─────────────────────────────────────┘
         │
    ┌────▼────┐        ┌──────────┐
    │  World   │◄───────│  Action  │  a_t
    │  Model   │        └──────────┘
    │ (JEPA)   │
    │          │  ŝ_{t+1} = Dynamics(s_t, h_t, a_t)
    │          │  Loss = L2(ŝ_{t+1}, sg(s_{t+1}))
    └────┬────┘
         │ ŝ_{t+1} (预测的下一帧表示)
         │
    ┌────▼────┐        ┌──────────────┐
    │  Cost    │        │   Actor       │
    │  Head    │        │  (CEM MPC)    │
    │          │        │               │
    │ Cost(ŝ)= │◄───────│ 在 World Model │
    │ -progress│        │ 中想象 H 步    │
    │ +offtrack│        │ 找到最优 a_t   │
    │ -speed   │        │               │
    └─────────┘        └──────┬────────┘
                              │ a_t = [steer, gas, brake]
                              ▼
                         Environment
```

---

## 4. 训练流程

### Phase 1：随机探索 + 收集数据（1-2 小时）

```
for episode in 1..100:
    重置环境
    for step in 1..1000:
        a_t = 随机动作（或加噪声的 PID 控制器）
        执行 a_t，观测 frame_{t+1}, reward, done
        存储 (frame_t, a_t, frame_{t+1}, reward, done) 到 Replay Buffer
```

### Phase 2：训练 World Model（3-5 小时，🟡 8-12G）

```
for epoch in 1..100:
    从 Replay Buffer 采样 batch
    s_t     = Perception(frame_t)
    s_{t+1} = TargetEncoder(frame_{t+1})  # Stop-Gradient
    ŝ_{t+1} = WorldModel(s_t, a_t)
    Loss = MSE(ŝ_{t+1}, s_{t+1})
    反向传播（只更新 Perception + WorldModel）
    EMA 更新 TargetEncoder
```

### Phase 3：训练 Cost Head（1 小时）

```
从成功 episode 中采样：label = "好状态"（低 Cost）
从失败 episode 中采样：label = "坏状态"（高 Cost，冲出赛道/太慢）
训练 Cost Head: MSE(Cost(s), label)
```

### Phase 4：在想象中训练 Actor + 在线微调（2-4 小时）

```
# 在 World Model 里"做梦"训练 Actor
for iteration in 1..1000:
    从随机状态开始 s_0
    for t in 1..H:
        a_t = CEM_plan(WorldModel, Cost, s_t, H=10)
        s_{t+1} = WorldModel(s_t, a_t)
        Loss = Cost(s_{t+1})  # Actor 目标：最小化未来 Cost
        用 Loss 更新 Actor 参数

# 在线微调（与真实环境交互）
for episode in 1..50:
    for step in 1..1000:
        执行 Actor 动作 + 小噪声
        用新数据更新 World Model
```

**总体训练时间**：~10-15 小时（单卡 8-12G），取决于能否一次训稳定。

---

## 5. 预期可行性分析

### ✅ 可行的部分

| 模块 | 可行性 | 原因 |
|------|--------|------|
| Perception (CNN) | ✅ 高 | CarRacing 视觉简单，CNN 足够 |
| World Model (JEPA) | 🟡 中 | 需要调参防坍缩，但赛道动力学不复杂 |
| Cost (Progress) | ✅ 高 | 可以从视觉特征直接回归"在赛道上"和"前进进度" |
| Actor (CEM MPC) | ✅ 高 | CEM 在连续控制中成熟，Dreamer 已验证 |
| Short-Term Memory | ✅ 高 | GRU 即可 |

### ⚠️ 挑战

| 挑战 | 严重程度 | 应对 |
|------|---------|------|
| **JEPA 训练坍缩** | 中 | 调大 EMA decay（0.999）、减小学习率、加 Sub-JEPA 正则化 |
| **Cost 没有 ground truth** | 中 | 从成功/失败 episode 中学习，或用"是否在赛道上"作为 proxy |
| **长期规划不足** | 中 | CEM 的 H=10 可能不够看到远处弯道，加长到 H=20 或加"转弯检测"提前减速 |
| **赛道随机生成** | 低 | 同一 episode 内赛道不变，World Model 不需要泛化到新赛道结构 |
| **奖励稀疏** | 低 | Cost 提供密集信号，环境奖励仅用于最终评估 |

### ❌ 不太可行/不太必要

| 问题 | 原因 |
|------|------|
| 完全端到端 JEPA 无重建 | 可能不稳定，建议先用 Dreamer 路线验证，再替换 |
| 真正的多层 H-JEPA | CarRacing 不需要三层抽象，两层（Scenes + Actions）足够 |

---

## 6. 和现有方案的比较

| 方案 | 方法 | CarRacing 表现 | 与 LeCun 路线的差距 |
|------|------|---------------|-------------------|
| DQN/PPO (无世界模型) | 端到端 RL | ~800-900 分 | 无预测/规划，纯反应式 |
| DreamerV2 | RSSM + MPC | ~900+ | 有重建损失，非 JEPA |
| **本文方案** | JEPA + CEM | 理论预期 ~800-900 | ✅ 完全对齐 LeCun 理论 |
| 人类 | — | ~900-1000 | — |

**理论预期分数**：如果 Cost 设计合理、世界模型不坍缩 → 应该能达到 800+ 分（完成一圈以上）。

---

## 7. 最小可行版本（MVP）

如果只能做一个最简版本验证理论，应该做什么？

### MVP 范围

```
✅ 包含：
   - CNN Perception（96×96 → 256维）
   - JEPA World Model（预测 s_{t+1}）
   - 简单 Cost（"是否在赛道上"的二分类头）
   - CEM 规划（H=5, K=10）

❌ 不包含：
   - Configurator（单一 Actor 对所有场景）
   - 完整的进度/速度 Cost（只有 on-track 判断）
   - 在线微调（只在想象中训练）

硬件需求：8G VRAM
预期训练时间：~6 小时
预期分数：~500-700（能开一段但不太快）
```

**MVP 的验证价值**：
1. 证明 JEPA 能在控制任务中学习动力学 → ✅/❌
2. 证明 CEM 在潜在空间规划可行 → ✅/❌
3. 识别实际训练中的坍缩风险 → 为完整版做准备

---

## 8. 结论

**可以吗？** ✅ **可以。**

CarRacing 是测试 LeCun 世界模型的**理想中等复杂度任务**：
- 视觉输入但不复杂（不需要 ViT 级别）
- 有物理动力学但不混沌（CNN 能学）
- 需要规划但规划视野短（CEM 够用）
- 有明确的 Cost 信号（是否在赛道上）

**建议路线**：
1. 先用 Dreamer 路线验证 CarRacing 能用世界模型解决（1-2 周）
2. 把 Dreamer 的重建损失替换为 JEPA 风格（1 周）
3. 如果 JEPA 坍缩，用 Sub-JEPA 正则化修复（参考 2605.09241）
4. 加入 Configurator（直道/弯道分类）→ 提升弯道表现

**最大风险**：JEPA 坍缩。但 CarRacing 的视觉简单性（大面积纯色 + 清晰特征）可能让训练比 ImageNet 上容易得多。

---

*分析完成。如需实现，从 MVP 开始，先在 8G 卡上跑通 World Model + CEM 的基本流程。*
