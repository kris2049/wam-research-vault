# CarRacing × LeCun World Model — 代码详解

> 完整的技术文档，逐文件、逐函数、逐行解释。

---

## 目录

1. [文件结构](#1-文件结构)
2. [config.py — 超参数](#2-configpy--超参数)
3. [models.py — 神经网络模块](#3-modelspy--神经网络模块)
4. [train.py — 训练主程序](#4-trainpy--训练主程序)
5. [数据流全景图](#5-数据流全景图)
6. [常见问题与调参指南](#6-常见问题与调参指南)

---

## 1. 文件结构

```
carracing/
├── config.py          # 所有超参数集中管理
├── models.py          # 5个神经网络模块 + 2个自动标注工具
├── train.py           # 完整训练流程：数据收集、训练、规划、评估
├── requirements.txt   # 依赖：torch, gymnasium, numpy
├── buffer_phase1.npz  # (运行后自动生成) Phase 1 收集的数据缓存
├── checkpoint_best.pt # (运行后自动生成) 最优模型权重
└── README.md          # 本文件
```

---

## 2. config.py — 超参数

所有可调参数集中在 `Config` 类中，修改后全局生效。

### 2.1 环境参数

```python
env_name = "CarRacing-v2"   # Gymnasium 环境 ID
frame_size = 96              # 画面分辨率 96×96
action_dim = 3               # [steer, gas, brake]
action_bounds = [            # 各维度的取值范围
    (-1.0, 1.0),             # 方向盘：-1（最左）到 +1（最右）
    (0.0, 1.0),              # 油门：0 到 1
    (0.0, 1.0),              # 刹车：0 到 1
]
```

### 2.2 感知模块

```python
s_dim = 256                  # 视觉表示向量的维度（Perception 的输出）
h_dim = 256                  # GRU 隐状态的维度（短期记忆）
cnn_channels = [32,64,128,256]  # 四层卷积的通道数
cnn_kernel = 3               # 卷积核大小 3×3
cnn_stride = 2               # 步长 2（每层降采样一半）
res_blocks = 2               # 残差块数量
```

输入 96×96 → conv1(48×48×32) → conv2(24×24×64) → conv3(12×12×128) → conv4(6×6×256) → 2×残差块 → 全局平均池化 → 256 维。

### 2.3 世界模型 (JEPA)

```python
dynamics_hidden = 512        # 隐藏层宽度
dynamics_layers = 3          # MLP 层数
ema_decay = 0.999            # Target Encoder 的 EMA 衰减率（越大越稳定）
```

### 2.4 Cost Head

```python
cost_hidden = [128, 64]      # 两层隐藏层的维度
cost_dims = 4                # 四个维度：[前进进度, 是否在路面上, 速度, 动作平滑度]
w_track = 5.0                # "是否在路面上"的权重（最重要！）
```

### 2.5 Configurator

```python
scene_classes = 4            # [直道, 左弯, 右弯, S弯]
scene_history = 10           # 用过去 10 帧的转向统计自动标注
```

### 2.6 Actor (CEM 规划器)

```python
plan_horizon = 8             # CEM 向前看 8 步
cem_candidates = 64          # 每轮采样 64 个候选动作序列
cem_elites = 8               # 保留前 8 个最优候选
cem_iterations = 3           # 迭代 3 轮
cem_gamma = 0.95             # 折扣因子
```

CEM 每次规划的总推理量：3 轮 × 64 候选 × 8 步 = 1536 次世界模型前向（GPU 上 batch 并行，~5ms）。

### 2.7 训练参数

```python
lr = 3e-4                    # AdamW 学习率
batch_size = 128             # 训练批大小（8G 显存上限）
buffer_capacity = 50000      # 经验池容量
total_env_steps = 100000     # 总交互步数
grad_clip = 1.0              # 梯度裁剪
```

### 2.8 探索与评估

```python
eps_start = 1.0              # 初始全随机
eps_end = 0.05               # 最终 5% 随机
eps_decay_steps = 50000      # 线性衰减到这步
eval_interval = 2000         # 每 2000 步评估一次
eval_episodes = 5            # 每次评估跑 5 局
```

---

## 3. models.py — 神经网络模块

### 3.1 Perception（感知 + 短期记忆）

```
输入: frame [B, 3, 96, 96], prev_action [B, 3], prev_hidden [B, 256]
输出: s_t [B, 256], h_t [B, 256]
参数量: ~1.4M
```

**CNN 编码器**（第 27-59 行）：
- 4 层降采样卷积（3×3 kernel, stride=2），每层跟上 BatchNorm + ReLU
- 2 个残差块（保持 6×6 分辨率）
- 全局平均池化 → Linear 投影到 256 维

**GRU 记忆**（第 61-66 行）：
- 输入 = s_t（当前视觉表示）+ prev_action（上一帧动作）
- 隐状态 h_t 捕捉速度、方向、赛道上下文
- 初始状态 h_0 = 全零向量

**ResidualBlock**（第 70-83 行）：
- 标准残差块：Conv→BN→ReLU→Conv→BN→与输入相加→ReLU
- 通道数不变，分辨率不变

---

### 3.2 WorldModel（JEPA 动力学预测器）

```
输入: s_t [B,256], h_t [B,256], a_t [B,3]
输出: s_next [B,256], h_next [B,256], reward [B,1], done_logit [B,1]
参数量: ~2.1M
```

**动作嵌入**（第 102 行）：
- `a_t ∈ ℝ³` → Linear → `a_emb ∈ ℝ⁶⁴`

**主干网络**（第 104-114 行）：
- 输入拼接：`[s_t(256) + h_t(256) + a_emb(64)] = 576 维`
- 3 层 MLP（每层 512 维 + LayerNorm + ReLU）
- 4 个并行的输出头：
  - `head_s`：预测下一帧的视觉表示（核心 JEPA 任务）
  - `head_h`：预测下一帧的 GRU 状态
  - `head_r`：预测奖励
  - `head_d`：预测是否终止（sigmoid 二分类）

**imagine_trajectory**（第 130-142 行）：
- CEM 规划时调用
- 从 (s_0, h_0) 开始，沿动作序列 [B, H, 3] 展开 H 步
- 返回 H 步的预测表示：`[B, H, 256]`

---

### 3.3 CostHead（成本函数）

```
输入: s_t [B,256]
输出: costs [B,4]  (四维代价)
参数量: ~40K
```

**网络结构**（第 159-165 行）：
- 256 → 128 → 64 → 4（两个隐藏层，ReLU 激活）

**total_cost()**（第 170-185 行）：
- 将四维代价合并为标量
- 负号处理："前进越多" → cost 越低，"冲上草地" → cost 越高
- 支持场景条件权重（Configurator 传入）

---

### 3.4 Configurator（场景分类器）

```
输入: s_t [B,256]
输出: logits [B,4], probs [B,4]  (四类场景概率)
参数量: ~40K
```

**网络结构**（第 202-206 行）：
- 256 → 128 → 4（一个隐藏层）

**get_scene_weights()**（第 213-248 行）：
- 推理时被 CEM 调用
- 根据识别出的场景返回两个东西：
  - **cost_weights**：调整 Cost 的四个维度权重（直道重速度，弯道重路面）
  - **sigma_steer**：调整 Actor 的转向探索范围（弯道允许更大转向）

| 场景 | w_track | w_speed | sigma_steer |
|------|---------|---------|-------------|
| 直道 | 2.0 | 2.0 | 0.1（少转向） |
| 转弯 | 10.0 | 0.2 | 0.5（多转向） |
| S弯 | 15.0 | 0.1 | 0.6（激进转向） |

---

### 3.5 update_ema()（EMA 更新）

```python
def update_ema(target_net, source_net, decay=0.999):
    for tp, sp in zip(target_net.parameters(), source_net.parameters()):
        tp.data.copy_(decay * tp.data + (1 - decay) * sp.data)
```

JEPA 的核心机制。`target_net` 的参数永远不通过反向传播更新（`requires_grad=False`），只通过 EMA 慢慢跟随 `source_net`。`decay=0.999` 意味着每步只更新 0.1%，非常稳定。

---

### 3.6 自动标注工具

**compute_on_track_label(frame)**（第 266-285 行）：
```
原理：赛道画面中，灰色=路面，绿色=草地
操作：
  1. 取画面中央 20×20 像素
  2. 判断每个像素绿色通道是否 > 红/蓝通道 ×1.2
  3. 如果绿色比例 < 50% → 在路面上(label=1)；否则草地(label=0)
无需人工标注，纯物理规律推导。
```

**compute_scene_label(steer_history)**（第 288-303 行）：
```
原理：转向角的大小反映赛道曲率
操作：
  1. 计算过去 N 帧转向角的绝对值平均
  2. avg < 0.1   → class 0 (直道)
  3. 0.1 ≤ avg < 0.4 → class 1/2 (转弯)
  4. avg ≥ 0.4   → class 3 (急弯/S弯)
无需人工标注，纯车辆运动学推导。
```

---

## 4. train.py — 训练主程序

### 4.1 ReplayBuffer（经验池）

```
存储数据结构: (frame, action, reward, next_frame, done, progress)
frame/next_frame: uint8 [96,96,3]  (HWC格式，节省内存)
action: float32 [3]
其他: float32 标量
```

**key methods**:

| 方法 | 作用 |
|------|------|
| `push()` | 存入一条经验 |
| `sample(B)` | 随机采样 B 条 → 转 CHW 格式 + 归一化到 [0,1] |
| `save(path)` | 保存为压缩 `.npz` 文件（~50-100MB） |
| `load(path)` | 从 `.npz` 恢复（跳过 Phase 1 数据收集） |

---

### 4.2 CEMPlanner（CEM 规划器）

**plan(s_t, h_t)**（第 86-148 行）：完整的规划循环

```
输入: 当前状态 (s_t [1,256], h_t [1,256])
输出: 最优动作 [3] (steer, gas, brake)

流程:
  1. Configurator 判断场景 → 获取 cost_weights 和 sigma_steer
  2. 初始化动作分布: μ = "保持当前动作", σ = 0.3
  3. 迭代 3 轮:
     a. 采样 K=64 个候选序列 [64,8,3]
     b. 并行展开 8 步（WorldModel × 512 次，batch 并行）
     c. CostHead 打分 × 512 次 → 64 个总分
     d. 选前 M=8 个精英 → 更新 μ, σ
  4. 返回 μ 的第一个动作
```

**为什么 CEM 不训练**：CEM 是纯规划算法，没有可学习参数。它的"智能"来自 World Model（预测准不准）和 Cost Head（打分对不对）。

---

### 4.3 collect_data()（数据收集）

```
参数: env, perception, buffer, num_episodes, eps, planner, device
```

**两种模式**：

| eps | planner | 行为 |
|-----|---------|------|
| 1.0 | None | 纯随机动作（Phase 1） |
| 衰减中 | CEMPlanner | CEM 规划 + ε 概率随机探索（Phase 5） |

**每一步的流程**：
```
1. 预处理: frame [96,96,3] → tensor [1,3,96,96] / 255
2. Perception 前向: (s_t, h_t) = perception(frame, prev_action, h_t)
3. 选动作: 
   - 随机模式: env.action_space.sample()
   - CEM 模式: planner.plan(s_t, h_t) + 噪声
4. 执行: next_frame, reward, done = env.step(action)
5. 存储: buffer.push(frame, action, reward, next_frame, done, progress)
```

---

### 4.4 训练函数

三个训练函数结构类似，核心差异在**训练信号**：

#### train_world_model()（第 220-269 行）

```
Loss 组成:
  loss_jepa   = MSE(s_pred, s_target)       权重 1.0   ← 核心
  loss_hidden = MSE(h_pred, h_target)       权重 0.05  ← 辅助
  loss_reward = MSE(r_pred, reward_true)     权重 0.1   ← 辅助
  loss_done   = BCE(d_pred, done_true)       权重 0.1   ← 辅助

关键细节:
  - s_target 由 TargetEncoder（EMA 副本）计算，Stop-Gradient
  - 每一步都调用 update_ema() 让 Target 慢慢跟随 Context
  - 坍缩检测: loss_jepa < 1e-4 → 打印警告
```

#### train_cost_head()（第 272-316 行）

```
训练信号（自动标注）:
  loss_progress = MSE(cost[0], progress_true)      ← 环境给的 progress
  loss_track    = BCE(cost[1], on_track_label)      ← 颜色自动标注
  loss_speed    = MSE(cost[2], reward_normalized)   ← 代理信号
  loss_energy   = MSE(cost[3], 0)                   ← 先验：动作应平滑

注意: Perception 在这里是 eval() 模式，不更新参数。
```

#### train_configurator()（第 319-348 行）

```
训练信号（自动标注）:
  scene_label = compute_scene_label(steering.abs())
  loss = CrossEntropy(logits, scene_label)

注意: Perception 在这里是 eval() 模式，不更新参数。
```

---

### 4.5 evaluate()（评估）

```
不存储数据，不加噪声，纯前向推理。
跑 N 局，返回平均 Reward。
这是衡量"学得怎么样"的金标准。
```

---

### 4.6 main()（主流程）

```
入口: python train.py

1. 创建环境 + 模型 + 优化器 + 经验池
2. Phase 1: 收集数据（或从 buffer_phase1.npz 加载）
3. Phase 2: 训练 World Model (100 epochs)
4. Phase 3: 训练 Cost Head (50 epochs)
5. Phase 4: 训练 Configurator (30 epochs)
6. Phase 5: 在线微调循环 (直到 100K 步)
   - 收集 2 局（CEM 规划 + ε 探索）
   - 训练 World Model 5 epochs
   - 训练 Cost Head 5 epochs
   - 训练 Configurator 3 epochs
   - 每 2000 步评估一次
   - 创新高 → 保存 checkpoint_best.pt
7. 最终评估 10 局
```

---

## 5. 数据流全景图

```
训练时 (Phase 2-4):

  buffer.sample(128)
       │
  ┌────┴────┐
  │ frames   │──────► Perception ──► s_t ──┬──► WorldModel ──► s_pred ──┐
  │ actions  │                             │                              │
  │ next_fr  │──────► TargetPerc ──► s_target (stop-grad)               │
  └─────────┘                                                            │
       │                                                       L2 loss ◄─┘
       │
       ├──► CostHead(s_t) ──► costs ──► MSE/BCE with auto-labels
       │
       └──► Configurator(s_t) ──► logits ──► CE with steering labels


推理时 (Phase 5 规划):

  frame ──► Perception ──► s_t, h_t
                              │
                    ┌─────────┼──────────┐
                    ▼         ▼          ▼
              Configurator  CostHead   WorldModel (×1536)
              "这是弯道"    打分准备     想象 64×8 步轨迹
                    │         │          │
                    └────┬────┘          │
                         ▼               │
                  调整后的 Cost ◄─────────┘
                         │
                         ▼
                    CEM 选最优动作
                         │
                         ▼
                    [steer, gas, brake]
```

---

## 6. 常见问题与调参指南

### Q: 训练时显存不够？

- **症状**: CUDA out of memory
- **修复**: 改 `config.py`: `batch_size = 64`（甚至 32）

### Q: JEPA Loss 很快降到 ~0？

- **症状**: 第 5 个 epoch 就 loss≈0，但评估时车乱开
- **原因**: **坍缩了** — Target 和 Context 合谋输出零向量
- **修复**:
  1. 增大 `ema_decay`: 0.999 → 0.9995
  2. 减小 `lr`: 3e-4 → 1e-4
  3. 增大 `batch_size`（让坍缩更难）

### Q: CEM 太慢？

- **症状**: 每步推理超过 100ms
- **原因**: CEM 没有用 batch 推理
- **确认**: 检查 `self.wm(s, h, a_tau)` 的输入维度 — 应该是 [K, ...] 而不是 [1, ...]，一次处理 64 个候选

### Q: Cost Head 的 track 维度不收敛？

- **症状**: on_track BCE Loss 不下降
- **原因**: 自动标注不准确（颜色判断有噪声）
- **修复**:
  1. 调大 center crop 区域（20×20 → 30×30）
  2. 调整 green 阈值（1.2 → 1.5）

### Q: Configurator 分类不准？

- **症状**: 直道被分类为转弯
- **原因**: 转向角自动标注的阈值不适合你的赛道
- **修复**: 调整 `compute_scene_label()` 中的阈值（0.1, 0.4）

### Q: 想从 checkpoint 恢复训练？

```python
# 在 main() 的模型创建后加入：
ckpt = torch.load('checkpoint_10000.pt')
perception.load_state_dict(ckpt['perception'])
world_model.load_state_dict(ckpt['world_model'])
cost_head.load_state_dict(ckpt['cost_head'])
configurator.load_state_dict(ckpt['configurator'])
# 然后从 Phase 5 继续
```

### Q: 怎么只看 CEM 规划的效果（跳过随机收集）？

删掉 `Phase 1` 的代码块，直接 `buffer = ReplayBuffer.load("buffer_phase1.npz")`，然后从 Phase 2 开始训练 — Phase 5 就会用训练好的模型做 CEM 规划。

---

## 附录：参数量统计

| 模块 | 参数量 | 说明 |
|------|--------|------|
| Perception (CNN) | ~1.2M | 4 层卷积 + 2 残差块 |
| Perception (GRU) | ~0.2M | GRU + Linear 投影 |
| WorldModel | ~2.1M | 3 层 MLP + 4 个输出头 |
| CostHead | ~0.04M | 2 层 MLP |
| Configurator | ~0.04M | 1 层 MLP |
| **总计** | **~3.6M** | 8G 显存完全够用 |

---

*文档版本: 2026-07-09 | 对应代码 commit: 0590a3a*
