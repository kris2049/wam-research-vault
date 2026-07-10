# Level 6: Research Frontier

> **Duration**: Ongoing | **Compute**: Varies | **Papers**: Read as published

---

## 🎯 Learning Objectives

1. Identify which open problems you could contribute to with limited compute
2. Understand the research frontier: what's being worked on RIGHT NOW
3. Choose a sub-direction for your own research or deep exploration

---

## 🔴 Open Problems (Mapped to Compute Requirements)

### 🟢 Feasible on 8-12G VRAM

| Problem | Why Important | Starting Point |
|---------|--------------|----------------|
| **Modality-agnostic JEPA** | Prove JEPA works on YOUR data type (medical, robotics, audio) | A-JEPA (2311.15830) — same arch, new data |
| **Efficient JEPA architectures** | Make JEPA trainable on consumer hardware | CNN-JEPA (2408.07514), Rethinking JEPA (2509.24317) |
| **Theoretical understanding** | Why does JEPA work? When does it fail? | When Does LeJEPA Learn? (2605.26379) |
| **Benchmark-driven improvement** | Standardized comparison of world models | stable-worldmodel (2605.21800) |
| **Interpretability of latent spaces** | What do JEPA latents actually encode? | Probing Latent World (2603.20327) |
| **Combining JEPA with your domain** | Apply JEPA to YOUR problem (e.g., robot navigation) | Mini I-JEPA (Level 2) + Mini Dreamer (Level 4) |

### 🟡 Feasible on 24G VRAM

| Problem | Why Important | Starting Point |
|---------|--------------|----------------|
| **Action-conditioned JEPA** | Bridge JEPA prediction with action → world model | SkyJEPA (2606.23444), LeWorldModel (2603.19312) |
| **Hierarchical JEPA** | Multi-level abstraction for long-horizon tasks | Hierarchical Planning (2604.03208) |
| **Disentangled action spaces** | Compositional control | DiLA (2605.15725) |
| **Video JEPA for embodied AI** | Robot learning with video JEPA | JEPA-VLA (2602.11832) |

### 🔴 Requires 40G+ / Multi-GPU

| Problem | Status |
|---------|--------|
| Full end-to-end JEPA world model at scale | LeWorldModel (2603.19312) |
| Video JEPA at scale | V-JEPA 2 (2506.09985) |
| Autonomous driving world models | Drive-JEPA (2601.22032), GAIA-1 (2309.17080) |

---

## 🗺 Frontier Map

```
                    LeCun's Complete Autonomous Agent
                              │
                    ┌─────────┴─────────┐
                    │                   │
              CONVERGING            MISSING
                    │                   │
        ┌───────────┴──────┐      ┌────┴────┐
        │                  │      │         │
   JEPA Lineage      Dreamer Line  Cost    Configurator
        │                  │     Module    (attention-
   I-JEPA               DayDreamer           based
   MC-JEPA              TransDreamer        routing)
   V-JEPA 2             Dreamer-CDP
   LeWorldModel ←──── convergence
        │
   ┌────┴────┬─────────┬──────────┐
   │         │         │          │
 Theory   Efficient  Modality   Planning
 (SiamJ)  (CNN-J)   (A-J, S-J)  (HierPlan)
 (Gauss)  (Rethink)  (Point-J)  (DiLA)
 (LeJEPA?)                     (UWM-J)
```

---

## 🎓 Suggested Research Directions

### Direction 1: "Tiny JEPA" (🟢 8G VRAM)

**Goal**: Build the smallest possible JEPA that still learns useful representations.

**Approach**:
1. Start from Mini I-JEPA (Level 2)
2. Apply architectural optimizations (CNN-JEPA ideas, frozen teacher)
3. Benchmark: how small can you go while maintaining >60% linear probe on CIFAR-10?
4. Publish: a recipe for JEPA on consumer hardware

**Papers to reference**: CNN-JEPA (2408.07514), Rethinking JEPA (2509.24317)

---

### Direction 2: "JEPA for YOUR Domain" (🟢 8G VRAM)

**Goal**: Prove JEPA works on a non-standard data type.

**Approach**:
1. Pick a domain: medical images, robot sensor data, audio, financial time series
2. Adapt the masking strategy to your data's structure
3. Train Mini JEPA and evaluate representations via downstream tasks
4. Publish: JEPA is general — here's proof on [your domain]

**Papers to reference**: A-JEPA (2311.15830), Point-JEPA (2404.16432) — modality extension case studies

---

### Direction 3: "World Model for Simple Robot" (🟢-🟡 8-12G VRAM)

**Goal**: Build an end-to-end world model + controller for a simple simulated robot.

**Approach**:
1. Combine Mini I-JEPA (Level 2) + Mini Dreamer (Level 4)
2. Environment: DMControl walker or MetaWorld reaching task
3. Learn a JEPA world model from pixels, then train a policy inside it
4. Compare: JEPA-based controller vs pure Dreamer — which is more sample-efficient?

**Papers to reference**: LeWorldModel (2603.19312), Dreamer-CDP (2603.07083), DayDreamer (2206.14176)

---

### Direction 4: "Why Does JEPA Work?" (🟢 4-8G VRAM)

**Goal**: Theoretical or empirical investigation of JEPA's learning dynamics.

**Approach**:
1. Design controlled experiments to answer: What is the MINIMAL sufficient condition for JEPA to learn useful representations?
2. Vary: masking ratio, architecture depth, data diversity, EMA decay
3. Produce a "phase diagram" of JEPA behavior
4. Publish: a practitioner's guide to JEPA hyperparameters

**Papers to reference**: When Does LeJEPA Learn? (2605.26379), Gaussian Embeddings (2510.05949), Connecting JEPA↔Contrastive (2410.19560)

---

## 📡 Staying Current

1. **Daily**: Check `WAM Research Log.md` (auto-updated at 08:00 UTC)
2. **Weekly**: Read arXiv cs.LG/cs.AI listings for "world model" or "JEPA"
3. **Monthly**: Review [Knowledge Graph](../Knowledge%20Graph.md) — are new papers filling gaps?
4. **Quarterly**: Re-evaluate open problems — has anything changed?

---

## ✅ Level 6 Checklist

- [ ] Identified 2+ open problems feasible on your hardware
- [ ] Selected a research direction for deeper exploration
- [ ] Read the 3 most recent papers in the WAM Research Log
- [ ] (Optional) Drafted a 1-page research proposal for your chosen direction

---

*This curriculum is designed to be iterated. As new papers appear in the daily scan, they fill gaps in the architecture. Revisit this page quarterly.*
