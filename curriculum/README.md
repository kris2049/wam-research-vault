# WAM/JEPA Learning Curriculum

> **Goal**: Master Yann LeCun's World Models research — from vision paper to frontier.
> **Constraint**: Limited compute (8-12G VRAM, single GPU). All experiments verified for this range.
> **Prerequisites**: Python, PyTorch, basic RL, basic CV.

---

## Progress Tracker

| Level | Topic | Papers | Experiment | Status |
|-------|-------|--------|------------|--------|
| 1 | Foundations | 2 close-read | Conceptual exercises | ⬜ |
| 2 | JEPA Core | 2 close-read + 1 skim | Mini I-JEPA on CIFAR-10 | ⬜ |
| 3 | Video JEPA | 1 close-read + 2 skim | Moving MNIST JEPA | ⬜ |
| 4 | World Models/Control | 1 close-read + 1 skim | Mini Dreamer on CartPole | ⬜ |
| 5 | Advanced | 3 skim | Architecture analysis | ⬜ |
| 6 | Research Frontier | Knowledge Graph | Open problem mapping | ⬜ |

---

## Paper Legend

- 📖 **Close-read**: Read every section, understand every equation. Take notes. ~2-3 hours each.
- 👀 **Skim**: Read abstract, intro, method overview, results. Understand the contribution. ~30 min each.
- 🔬 **Experiment**: Hands-on implementation. Code from scratch or adapt open-source.

## Hardware Legend

- 🟢 **Light**: 4-6G VRAM, runs on laptop GPU (RTX 2060, GTX 1060)
- 🟡 **Moderate**: 8-12G VRAM, needs RTX 3060/4060 or better
- 🔴 **Heavy**: 24G+, multi-GPU. **Read paper only** — do not attempt to train.

---

## Repository Structure

```
curriculum/
  level-01-foundations/     # Vision paper + basics
  level-02-jepa-core/       # I-JEPA architecture
  level-03-video-jepa/      # Multimodal JEPA
  level-04-world-models-control/  # Dreamer + MBRL
  level-05-advanced/        # Planning, hierarchy
  level-06-frontier/        # Open problems
```

Each level: `README.md` + `exercises/` + `experiments/` + `tests/`

---
*Curriculum aligned with [WAM Research Log](../WAM%20Research%20Log.md) and [Knowledge Graph](../Knowledge%20Graph.md)*
