# Level 5: Advanced — Planning, Hierarchy, Convergence

> **Duration**: 1 week | **Compute**: None (read-only) | **Papers**: 3 skim + architecture analysis

---

## 🎯 Learning Objectives

1. Understand hierarchical planning in latent world models
2. Grasp the convergence of JEPA + Dreamer → LeWorldModel
3. Map the research frontier: what's solved, what's open?

---

## 👀 Skim Papers (30 min each)

### LeWorldModel (2026)
- **arXiv**: [2603.19312](https://arxiv.org/abs/2603.19312)
- **Focus**: End-to-end JEPA world model from pixels. The convergence point.
- **Key questions**:
  1. How does LeWorldModel achieve stability without reconstruction?
  2. What does it inherit from I-JEPA? What from Dreamer?
  3. Is it truly "end-to-end" or does it still have separate training phases?

### Hierarchical Planning with Latent World Models (2026)
- **arXiv**: [2604.03208](https://arxiv.org/abs/2604.03208)
- **Focus**: Two-level planning: high-level subgoal setting + low-level execution
- **Key questions**:
  1. How are subgoals represented? In latent space or observation space?
  2. What makes hierarchical planning more efficient than flat planning?
  3. How do the two levels communicate?

### DiLA — Disentangled Latent Action World Models (2026)
- **arXiv**: [2605.15725](https://arxiv.org/abs/2605.15725)
- **Focus**: Factorizing action spaces for compositional control
- **Key questions**:
  1. How do you disentangle action dimensions without labeled data?
  2. What's the benefit of compositional actions (e.g., navigate independently of manipulate)?

---

## 🔬 Architecture Analysis Exercise

**Hardware**: None — pen & paper + code reading | **Time**: 3 hours

### Task: Draw the FULL LeCun Architecture with Implemented Papers

Take LeCun's 6-module diagram from the vision paper and annotate it with which papers implement which modules:

```
LeCun's Architecture          Papers That Implement It
─────────────────────         ─────────────────────────
  ┌──────────────┐
  │ Configurator  │            Hierarchical Planning (2604.03208) — subgoal setting
  └──────┬───────┘            DiLA (2605.15725) — action factorization
         │
  ┌──────▼───────┐
  │  World Model  │            I-JEPA (2301.08243) — latent prediction
  │  (JEPA)       │            V-JEPA 2 (2506.09985) — video prediction
  └──────┬───────┘            LeWorldModel (2603.19312) — full end-to-end
         │
  ┌──────▼───────┐
  │  Cost Module  │            Probabilistic Dreaming (2603.04715) — uncertainty
  └──────┬───────┘            UWM-JEPA (2605.25313) — belief space
         │
  ┌──────▼───────┐
  │   Actor       │            Dreamer's actor-critic (2206.14176)
  └──────┬───────┘            JEPA-VLA (2602.11832) — VLA for robots
         │
  ┌──────▼───────┐
  │   Perception  │            I-JEPA encoder (2301.08243)
  └──────────────┘            CNN-JEPA (2408.07514) — efficient encoder
                              Point-JEPA (2404.16432) — 3D encoder
  ┌──────────────┐
  │Short-Term Mem │            RSSM's GRU (DayDreamer)
  └──────────────┘
```

### Gap Analysis — What's NOT yet implemented?

| LeCun Module | Status | Missing |
|-------------|--------|---------|
| World Model (JEPA) | ✅ Mostly there | Action-conditioned JEPA still emerging (SkyJEPA, 2606.23444) |
| Configurator | 🟡 Partial | Only subgoal setting; full attention-based configurator missing |
| Cost Module | 🔴 Minimal | Some uncertainty work; full intrinsic cost (curiosity, affordance) missing |
| Actor | ✅ Functional | Works in simulation; real-world generalization still limited |
| Perception | ✅ Solid | Vision (I-JEPA), 3D (Point-JEPA), Audio (A-JEPA), Speech (S-JEPA) |
| Short-Term Memory | ✅ Simple | RSSM/GRU works; transformer memory emerging |

---

## 🔬 Research Line Mapping

**Hardware**: None | **Time**: 1 hour

For each of these papers, identify which "gap" it fills:

| Paper | Gap It Fills |
|-------|-------------|
| Sub-JEPA (2605.09241) | Stabilizes JEPA training (infrastructure) |
| UWM-JEPA (2605.25313) | Belief space — partial observability (cost module precursor) |
| SkyJEPA (2606.23444) | Action-conditioned JEPA + sim-to-real (actor + world model bridge) |
| AdaJEPA (2606.32026) | Adaptive computation (configurator-like resource allocation) |
| When Does LeJEPA Learn? (2605.26379) | Theoretical validation of world model emergence |
| DSeq-JEPA (2511.17354) | Energy-based alternative to masking (cost module connection) |

---

## ✅ Level 5 Checklist

- [ ] Skimmed LeWorldModel — understand the JEPA+MBRL convergence
- [ ] Skimmed Hierarchical Planning — understand subgoal-based planning
- [ ] Skimmed DiLA — understand action factorization
- [ ] Completed Architecture-to-Papers mapping exercise
- [ ] Identified 3+ open research gaps in the LeCun architecture

---

## 📚 Supplementary

| Resource | Type |
|----------|------|
| [Knowledge Graph](../Knowledge%20Graph.md) | Map of all 37 papers and their relationships |
| LeCun @ NeurIPS 2025 (speculative) | Check for updated vision talks |
| TD-MPC2 paper | Alternative model-based approach to compare |
