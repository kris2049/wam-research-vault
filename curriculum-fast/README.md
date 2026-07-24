# WAM 快速入门 — 4 级直达最佳实践

> **目标**：从零到理解 CarRacing 世界模型的全部核心概念。不读历史，只学必要的。
> **时间**：2 周（每天 2 小时）
> **前置**：Python、PyTorch 基础、`pip install torch gymnasium numpy matplotlib`

---

## 你需要学什么（只需 7 个概念）

```
Level 1 ── DINOv2（冻结特征）+ JEPA 预测（核心思想）
Level 2 ── World Model 动力学 + 高斯防坍缩 + 时间拉直
Level 3 ── Cost 函数 + CEM 规划
Level 4 ── 把所有模块拼起来，跑通 CarRacing
```

## 你不需要学什么

- ❌ 2022 年的 VICReg / Barlow Twins / BYOL 变体
- ❌ I-JEPA 的 multi-block masking 细节
- ❌ MC-JEPA 的光流运动分解
- ❌ V-JEPA 的时空管 masking
- ❌ LeCun 2022 六模块架构论文（我们已经有总结）
- ❌ 什么是对比学习、什么是非对比学习

---

## 进度追踪

| Level | 学了什么 | 实验 | 状态 |
|-------|---------|------|------|
| 1 | DINOv2 + JEPA 预测 | 冻结 DINOv2 → 预测下一帧 | ⬜ |
| 2 | World Model + 防坍缩 + 拉直 | 训一个稳定的迷你世界模型 | ⬜ |
| 3 | Cost + CEM 规划 | 在 World Model 中规划 | ⬜ |
| 4 | CarRacing 集成 | 跑通完整流程 | ⬜ |
