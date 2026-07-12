# Perception 模块：CNN 之外的 7 种选择

> 分析每种方案在 CarRacing + JEPA 场景下的理论适用性、计算开销和优缺点。

---

## 总览

| 方案 | 参数量 (96×96) | 推理速度 | 适合 CarRacing? | 对齐 JEPA 理论? |
|------|---------------|---------|----------------|----------------|
| **CNN (Baseline)** | ~2M | 快 | ✅ | 🟡 标准但无新意 |
| **ConvNeXt** | ~3M | 快 | ✅ | 🟡 现代 CNN |
| **ViT (Patch-based)** | ~5M | 中 | 🟡 | ✅ I-JEPA 原生架构 |
| **MLP-Mixer** | ~4M | 中 | 🟡 | 🟡 纯 MLP |
| **JEPA Native (Multi-block)** | ~2M | 中 | ✅ | ✅ 完全对齐 |
| **Random Projection** | 0 (无需训练!) | 极快 | 🟡 | ✅ 极端理论对齐 |
| **Predictive Coding Encoder** | ~2M | 中 | 🟡 | ✅ 神经科学启发 |

---

## 1. ConvNeXt（现代化 CNN）

**论文**：Liu et al., "A ConvNet for the 2020s" (2022)

### 架构
```
传统 ResNet: Conv → BN → ReLU
ConvNeXt:    Conv → LN → GELU  (更像 Transformer 的设计但保持卷积)
             更大的 kernel (7×7)
             更少的激活函数
             单独的降采样层
```

### CarRacing 优势
- 保留了 CNN 的局部性（适合检测路面/草地边界）
- 更大的 kernel 提供更好的感受野（看到更远的弯道）
- 更少的 FLOPs 比同参数量的 ViT

### 为什么比标准 CNN 好？
标准 CNN（如 Level 2 中的实现）用 3×3 kernel，感受野增长慢。ConvNeXt 用 7×7 → 6 层就看到 40×40 像素范围（半张图），对弯道检测更有用。

**计算**：🟡 8G VRAM 可训练，推理 ~3ms/帧。

---

## 2. ViT（Vision Transformer）

**论文**：Dosovitskiy et al., "An Image is Worth 16x16 Words" (2021)

### 架构
```
96×96 → 分成 6×6=36 个 16×16 patches
每个 patch 线性投影到 256 维
+ 位置编码
+ 4 层 Transformer Encoder
→ CLS token → 256 维表示
```

### I-JEPA 的选择

I-JEPA 原论文用的就是 ViT。这是有原因的：

```
JEPA 的 masking 操作在 patch 层面做：
┌──┬──┬──┬──┬──┬──┐
│██│  │  │██│  │  │   ██ = Target block (被遮住)
├──┼──┼──┼──┼──┼──┤   □  = Context block (可见)
│  │██│  │  │██│  │
├──┼──┼──┼──┼──┼──┤   Context Encoder 只看 □ patches
│  │  │██│  │  │██│   Target Encoder 只看 ██ patches
├──┼──┼──┼──┼──┼──┤
│██│  │  │██│  │  │   这种 patch-based masking 是 ViT 天然支持的
├──┼──┼──┼──┼──┼──┤   而 CNN 的卷积操作让 masking 变得困难
│  │██│  │  │██│  │   (卷积会"看到"相邻 patch)
├──┼──┼──┼──┼──┼──┘
│  │  │██│  │  │██│
└──┴──┴──┴──┴──┴──┘
```

### CarRacing 需要 ViT 吗？

**可能不需要**。CarRacing 的特征是局部性的：
- 路面 vs 草地（颜色对比）→ 局部信息足够
- 路缘石（红色/白色条纹）→ 局部纹理
- 弯道方向 → 需要一定感受野，但 CNN 的 7×7 kernel 够用

**但如果要做 JEPA masking**：ViT 的 patch 结构天然支持，不需要额外的 masking 适配。

**计算**：🟡 8G VRAM。ViT 推理比 CNN 慢 ~3-5 倍（注意力是 O(n²)）。

---

## 3. MLP-Mixer（无卷积，无注意力）

**论文**：Tolstikhin et al., "MLP-Mixer: An all-MLP Architecture" (2021)

### 架构
```
96×96 → 分成 8×8=64 个 12×12 patches
每个 patch → 256 维

交替执行：
  Token Mixing:   每个 patch 和其他 patch 通信（跨 patch 的 MLP）
  Channel Mixing: 每个 patch 内部特征变换（跨 channel 的 MLP）

× 4 层 → 全局池化 → 256 维
```

### 为什么考虑它？

MLP-Mixer 的核心思想是**在潜在空间做所有计算**——这恰好是 JEPA 的哲学："不需要像素级卷积，在表示空间处理一切"。

**优势**：
- 极简单：全是矩阵乘法，没有卷积、没有注意力
- 硬件友好：矩阵乘法在 GPU 上极度优化
- 理论纯粹：不预设任何空间结构先验

**劣势**：
- 没有平移不变性 → 需要更多数据才能学到
- 对于 96×96 分辨率，64 个 patch 的 Token Mixing 是 64² = 4096 次交互，和 ViT 的注意力复杂度一样

**计算**：🟡 8G VRAM。推理速度介于 CNN 和 ViT 之间。

---

## 4. JEPA Native Encoder（Multi-block 编码器）

### 架构：直接使用 I-JEPA 的原始设计

```
不是"先编码整张图再选择哪些表示用"，而是：
"只编码需要的部分"

┌─────────────────────────────────────┐
│  Context Encoder                     │
│  输入: 4 个随机 context block         │
│  每个 block: 16×16 patch → 256 维     │
│                                      │
│  ┌────┐  ┌────┐                      │
│  │ B1 │  │ B2 │  ViT (共享权重)        │
│  └────┘  └────┘  → z_context[B, 4, 256]
│  ┌────┐  ┌────┐                      │
│  │ B3 │  │ B4 │                      │
│  └────┘  └────┘                      │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  Target Encoder                      │
│  输入: 4 个 target block              │
│  同样架构，EMA 权重更新                 │
│  → z_target[B, 4, 256]               │
└─────────────────────────────────────┘

Predictor: z_context + pos_emb → z_pred[B, 4, 256]
Loss: L2(z_pred, z_target)
```

### CarRacing 的 Multi-block 设计

在赛车上，Context/Target 不应该随机分布——应该考虑驾驶相关的空间结构：

```
不是随机选择 block，而是按空间功能选择：

┌────────────────────────┐
│ 前方远 (tgt) │ 前方中 (ctx) │
│  预测远处路况  │  当前可见路况  │
├──────────────┼──────────────┤
│ 左侧 (tgt)   │ 右侧 (ctx)   │
│  预测左弯道    │  当前右路缘    │
├──────────────┼──────────────┤
│ 当前路面 (tgt)│ 当前路面 (ctx) │
│  预测路面变化  │  当前路面状态   │
└────────────────────────┘

Context = Agent 当前能看到的信息
Target  = Agent 需要预测的信息（下一帧或视线外）
```

**优势**：完全对齐 JEPA 理论，是最"正宗"的做法。
**劣势**：需要仔细设计 masking 策略；训练数据结构更复杂。

**计算**：🟡 8G VRAM。训练时每个 block 独立编码（并行），推理时只需 Context Encoder。

---

## 5. Random Projection（随机投影编码器）

### 思想来源：Reservoir Computing / Echo State Networks

**核心思想**：为什么 Encoder 一定要训练？如果随机投影就足够好了呢？

```
不训练 Encoder，而是用一个固定的、随机的非线性变换：

z = σ(W_random × flatten(frame) + b_random)

W_random ~ N(0, 1/d)  （高斯随机矩阵）
σ = ReLU 或 tanh
z ∈ ℝ^1024 （高维展开，保证线性可分）

只有 Predictor 和后续模块需要训练！
```

### 为什么理论上可行？

这是**核方法（kernel method）**的思想：
- 随机投影到高维空间 → 线性不可分的问题变得线性可分
- 类似 SVM 的 RBF kernel → 但不显式计算核，而是用随机特征近似
- 只要维度够高（>1000），随机投影的表示质量接近训练过的编码器

**在 CarRacing 上**：
- 输入 96×96×3 = 27648 维 → 投影到 2048 维
- 路面/草地的颜色分布在 2048 维中自然分离（不需要学习）
- World Model 只需要学习"这个高维向量会怎么变化"→ Predictor 的任务变简单了

**优势**：
- **零训练成本**：Encoder 不需要训练，节省 50% 以上的训练时间
- **无坍缩风险**：固定的 Encoder 不可能坍缩
- **极端对齐 LeCun 理论**：Encoder 只是"感知模块"，智能在 World Model + Cost + Actor 中

**劣势**：
- 表示质量不如训练过的 Encoder（但 CarRacing 的简单视觉可能够用）
- 更高的维度（2048 vs 256）→ World Model 和 Predictor 的参数量增加

**这是一个激进的理论实验**：如果随机投影就够了，说明 LeCun 的论点是正确的——智能不需要在"像素→表示"这一步浪费算力，随机投影的简单表示足以支撑 World Model。

**计算**：🟢 4-6G VRAM。不需要训练 Encoder，总训练时间减少 40%。

---

## 6. Predictive Coding Encoder（预测编码）

### 思想来源：Rao & Ballard (1999), Friston's Free Energy Principle

**核心思想**：感知 = 预测 + 修正。Encoder 不是被动"看"，而是主动"预测自己会看到什么"。

```
不训练一个前馈 Encoder，而是训练一个"预测→比较→修正"的循环：

         ┌──────────────┐
    ┌───►│  Prediction   │───┐
    │    │  自上而下的     │   │
    │    │  生成"预期"     │   │ pred_frame
    │    └──────────────┘   │
    │                       ▼
    │              ┌─────────────────┐
    │              │  Prediction Error │
    │              │  error = frame    │
    │              │        - pred     │
    │              └────────┬────────┘
    │                       │ error signal
    │    ┌──────────────┐   │
    └────│  Update       │◄──┘
         │  自底向上的    │
         │  修正表示      │
         └──────────────┘
              │
              ▼
          z_t (修正后的表示)

这个过程迭代 T 次（通常 5-10 次），
每次"预测→比较→修正"让表示越来越精确。
```

### 理论优势（为什么 LeCun 会喜欢这个）

1. **感知和预测统一**：Encoder 的"修正"步骤本质上就是 JEPA 的"预测"。感知模块和 World Model 用的是同一个预测机制。
2. **不需要重建**：只比较表示（error 在潜在空间），符合 JEPA 精神。
3. **主动感知**：Encoder 不被动接收数据，而是主动"询问" World Model："我预测会看到这个，实际呢？"——这就是 Configurator 的功能。

### CarRacing 的实现

```
迭代过程（T=3 轮）：
  Round 1: z₀ = 随机猜测 → pred₀ = WorldModel(z₀) → error₀ = real_frame - pred₀ → z₁ = z₀ + f(error₀)
  Round 2: pred₁ = WorldModel(z₁) → error₁ = real_frame - pred₁ → z₂ = z₁ + f(error₁)  
  Round 3: pred₂ = WorldModel(z₂) → 误差已很小 → z₃ 是最终表示

最终使用的 z₃ 就是 Perception 模块的输出
```

**优势**：一个模块同时实现了 Perception + World Model（预测）
**劣势**：推理时多次前向传播（T 轮），比 CNN 慢 T 倍；训练更复杂

**计算**：🟡-🔴。训练需要展开 T 轮的反向传播（类似 RNN），显存需求翻 T 倍；推理也慢 T 倍。对于 CarRacing 来说可能**过度设计**了。

---

## 7. 混合方案：CNN Stem + ViT Body

### 架构：取两者之长

```
输入: 96×96×3
     │
  ┌──▼──────────────┐
  │  CNN Stem        │  ← 保留 CNN 的局部特征提取 + 降采样
  │  2层 stride-2    │     96→48→12（8×降采样）
  │  Conv → 12×12×128│     避免了 ViT 的 16×16 大 patch
  └────────┬────────┘
           │ 12×12 = 144 个 token
  ┌────────▼────────┐
  │  ViT Body        │  ← 在降采样后的 token 上做注意力
  │  4层 Transformer │     全局感受野，但 token 数可控
  │  dim=256, 4 heads│
  └────────┬────────┘
           │
       CLS token → 256 维表示
```

### 为什么这个组合好？

| 组件 | 为什么用 | 解决什么问题 |
|------|---------|-------------|
| CNN Stem | 局部特征提取（边缘、纹理） | ViT 的大 patch 丢失了细粒度信息 |
| ViT Body | 全局注意力（弯道、远处路况） | CNN 的有限感受野看不到远处 |
| 降采样到 12×12 | Token 数可控（144） | 96×96 直接分 patch 是 36 个（太粗）或 576 个（太多） |

**这是 CarRacing 的最佳折中方案**：
- 卷积提取路面纹理 + 路缘石 → 精细
- Transformer 捕捉全局结构 + 弯道关系 → 广视野
- 144 个 token 的注意力开销小（比 36×36=1296 个全分辨率 token 少 9 倍）

**计算**：🟡 8G VRAM。推理速度 ~5ms/帧（比纯 ViT 快，比纯 CNN 慢一点）。

---

## 8. 决策矩阵

### 按目标选择

| 你的目标 | 推荐方案 | 原因 |
|---------|---------|------|
| **最快出结果** | CNN（原方案） | 最简单，100% 能跑，Dreamer 已用 CNN 验证过 |
| **最对齐 LeCun 理论** | Random Projection | 极简 Encoder，验证"智能不在感知模块" |
| **最高准确率** | CNN Stem + ViT Body | 局部+全局特征，12×12 token 高效 |
| **最适合 JEPA Masking** | JEPA Native | 原生支持 block masking，直接复用 I-JEPA 代码 |
| **最前沿/发论文** | Predictive Coding | 统一感知+预测，但实现复杂，可能过度设计 |
| **最省算力** | Random Projection | 零 Encoder 训练成本 |

### 我的推荐顺序

```
1. 先用 CNN 跑通整个流程（验证 World Model + CEM 能开车）
2. 测试 Random Projection 替代 CNN（验证"不需要训练 Encoder"）
3. 如果 Random Projection 也能开车 → 发论文（"世界模型的感知可以是随机的"）
4. 如果不行 → 换 CNN Stem + ViT Body（最佳质量）
```

第一步和第二步用了截然不同的假设，对比结果会非常有意思。

---

*分析完成。核心结论：CarRacing 的感知模块有 7 种可行方案，从极简随机投影到极复杂的预测编码。推荐先 CNN 跑通，再激进测试 Random Projection。*
