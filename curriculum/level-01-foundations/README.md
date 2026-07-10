# Level 1: Foundations

> **Duration**: 1 week | **Compute**: None required | **Papers**: 2 close-read

---

## 🎯 Learning Objectives

1. Understand WHY LeCun argues generative models are the wrong path to AGI
2. Internalize the JEPA architecture: Encoder → Predictor → Target
3. Trace the historical lineage: World Models (2018) → LeCun Vision (2022) → I-JEPA (2023)
4. Grasp the Energy-Based Model (EBM) connection

---

## 📖 Close-Read Papers

### Paper 1: "A Path Towards Autonomous Machine Intelligence" (LeCun, 2022)

- **Link**: https://openreview.net/forum?id=BZ5a1r-kVsf
- **Time**: 3 hours
- **Hardware**: None — pure theory

**Reading Guide:**

| Section | Focus | Key Questions |
|---------|-------|---------------|
| §1-2 | The argument against generation | Why is predicting pixels "wasteful"? |
| §3 | World Model architecture | What are the 6 modules? How do they connect? |
| §4 | JEPA concept | What is the difference between JEPA and autoencoders? |
| §5 | Energy-Based Models | How does EBM relate to JEPA? Why is an energy function needed? |
| §6 | Hierarchical planning | Why multiple levels of abstraction? |
| §7 | The Configurator | What does the configurator do? Is it attention? |

**After reading, answer:**
1. Why does LeCun believe pixel-level generation is a dead end for world models?
2. Draw the 6-module architecture from memory. Label every arrow.
3. What is the "cost" module and why is it essential?
4. How does H-JEPA (Hierarchical JEPA) differ from a flat world model?

---

### Paper 2: "World Models" (Ha & Schmidhuber, 2018)

- **Link**: https://arxiv.org/abs/1803.10122
- **Time**: 2 hours
- **Hardware**: None
- **Why this paper**: This is the paper LeCun's vision REACTS TO. Understanding it shows what JEPA is trying to solve.

**Reading Guide:**

| Section | Focus | Key Questions |
|---------|-------|---------------|
| §1-2 | The VAE world model | How does the VAE compress observations? |
| §3 | The MDN-RNN | What does the RNN predict? Why a mixture density network? |
| §4 | The Controller | How does the controller use the world model? |
| §5 | Dreaming | What does "dreaming" mean in this context? |

**After reading, answer:**
1. Where does Ha & Schmidhuber's architecture predict PIXELS vs. LATENTS?
2. What aspect of this paper would LeCun criticize as "wasteful"?
3. What aspect did LeCun KEEP in his own vision?

---

## 🔬 Exercises

### Exercise 1.1: Architecture Mapping (pen & paper)

Draw two diagrams side by side:
- Left: Ha & Schmidhuber's World Models architecture (VAE → MDN-RNN → Controller)
- Right: LeCun's 6-module architecture

Annotate every component with: "predicts pixels" vs "predicts latents".

### Exercise 1.2: Energy Function Intuition

```python
# Run in your head — no computer needed
# An energy function E(x,y) should be LOW when (x,y) is a valid pair
# and HIGH when it's invalid.

# Example: E(x, y) = ||f(x) - g(y)||^2
# Where f = context encoder, g = target encoder

# Question: If E(x,y) = 0, what does that tell us about x and y?
# Question: What happens if we ONLY minimize E(x,y) without any regularization?
# Answer: Collapse — the encoders can output 0 for everything.
# This is the central problem JEPA must solve.
```

### Exercise 1.3: Modality Independence

JEPA claims to be modality-agnostic. For each of the following, sketch what the Context and Target would be:
- **Vision**: Context = ? (masked regions), Target = ? (unmasked regions)
- **Audio**: Context = ? (past spectrogram), Target = ? (future spectrogram)
- **Video**: Context = ? (past frames), Target = ? (future frames)
- **Robotics**: Context = ? (current state + action), Target = ? (next state)

---

## ✅ Level 1 Checklist

- [ ] Read LeCun 2022 — can draw the architecture from memory
- [ ] Read Ha & Schmidhuber 2018 — understand what LeCun is reacting to
- [ ] Understand the EBMs-JEPA connection
- [ ] Completed all 3 exercises

---

## 📚 Supplementary

| Resource | Type | Why |
|----------|------|-----|
| LeCun @ ICML 2022 keynote | Video | Watch him explain the vision in his own words |
| "What are Energy-Based Models?" | Blog (Lilian Weng) | Concrete introduction to EBMs |
| World Models interactive demo | https://worldmodels.github.io/ | See Dreamer in action |
