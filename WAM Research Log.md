# WAM Research Log — Deep Analysis
> Curated papers from Yann LeCun's World Models/JEPA ecosystem, with detailed architectural analysis, research lineage, and LeCun alignment assessment.

---
## Index

| # | Date | Paper | Alignment | Compute |
|---|------|-------|-----------|--------|
| 1 | 2026-07-04 | [SiamJEPA: On the Role of Siamese Student Encoders in JEPA](https://arxiv.org/abs/2607.04044) | HIGH — Theoretical validation of JEPA architecture choices. | Mid (24G): Ablation studies on standard benchmarks. |
| 2 | 2026-06-30 | [AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026) | HIGH — Adaptive computation is key to LeCun's vision of efficient autonomous systems. | Mid (24G): Focus on efficiency improvements rather than scale. |
| 3 | 2026-06-22 | [SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real ](https://arxiv.org/abs/2606.23444) | HIGH — Directly applies JEPA to physical robot control, validating the world model approach. | Large (40G+): Both training and real-time inference on drone hardware. |
| 4 | 2026-06-17 | [S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Representa](https://arxiv.org/abs/2606.19398) | MEDIUM — Expands JEPA to new modalities, supporting the generality of LeCun's framework. | Mid (24G): Speech SSL training on LibriSpeech-scale data. |
| 5 | 2026-06-14 | [You Don't Need Strong Assumptions: Visual Representation Learning via ](https://arxiv.org/abs/2606.15956) | — | — |
| 6 | 2026-05-25 | [When Does LeJEPA Learn a World Model?](https://arxiv.org/abs/2605.26379) | HIGH — Directly investigates whether JEPA fulfills LeCun's world model vision. | Mid (24G): Analytical experiments with controlled conditions. |
| 7 | 2026-05-25 | [UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/abs/2605.25313) | HIGH — Addresses a key practical limitation on the path to real-world autonomous systems. | Mid (24G): Belief-state inference adds moderate overhead. |
| 8 | 2026-05-20 | [stable-worldmodel: A Platform for Reproducible World Modeling Research](https://arxiv.org/abs/2605.21800) | — | — |
| 9 | 2026-05-15 | [DiLA: Disentangled Latent Action World Models](https://arxiv.org/abs/2605.15725) | HIGH — Factorized control aligns with LeCun's modular agent architecture. | Mid (24G): Standard world model training with disentanglement objectives. |
| 10 | 2026-05-10 | [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World](https://arxiv.org/abs/2605.09241) | HIGH — Makes JEPA more practical and reliable, accelerating the path to autonomous intelligence. | Mid (24G): Adds regularization term to existing JEPA training. |
| 11 | 2026-05-05 | [Text-Conditional JEPA for Learning Semantically Rich Visual Representa](https://arxiv.org/abs/2605.03245) | — | — |
| 12 | 2026-04-03 | [Hierarchical Planning with Latent World Models](https://arxiv.org/abs/2604.03208) | HIGH — Directly implements LeCun's hierarchical planning vision. | Mid (24G): Two-level planning is more efficient than flat long-horizon planning. |
| 13 | 2026-03-20 | [Probing the Latent World: Emergent Discrete Symbols and Physical Struc](https://arxiv.org/abs/2603.20327) | — | — |
| 14 | 2026-03-15 | [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482) | HIGH — Meta FAIR. Addresses a key limitation on the path to full world models. | Large (40G+): Extended V-JEPA training with dense prediction heads. |
| 15 | 2026-03-13 | [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architectur](https://arxiv.org/abs/2603.19312) | HIGH — Likely from LeCun's group. The name itself signals direct alignment with LeCun's vision. | Large (40G+): End-to-end pixel-to-latent training. |
| 16 | 2026-03-07 | [Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous](https://arxiv.org/abs/2603.07083) | — | — |
| 17 | 2026-03-05 | [Probabilistic Dreaming for World Models](https://arxiv.org/abs/2603.04715) | — | — |
| 18 | 2026-02-12 | [JEPA-VLA: Video Predictive Embedding is Needed for VLA Models](https://arxiv.org/abs/2602.11832) | HIGH — Demonstrates practical necessity of JEPA for embodied AI. | Large (40G+): Video JEPA backbone + VLA fine-tuning on robot data. |
| 19 | 2026-01-29 | [Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for En](https://arxiv.org/abs/2601.22032) | HIGH — Validates JEPA in a high-stakes real-world application. | Large (40G+): Driving video data + trajectory prediction model. |
| 20 | 2025-11-21 | [DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Archit](https://arxiv.org/abs/2511.17354) | — | — |
| 21 | 2025-10-07 | [Gaussian Embeddings: How JEPAs Secretly Learn Your Data Density](https://arxiv.org/abs/2510.05949) | — | — |
| 22 | 2025-09-29 | [Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers](https://arxiv.org/abs/2509.24317) | — | — |
| 23 | 2025-06-11 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Predictio](https://arxiv.org/abs/2506.09985) | HIGH — Directly from Meta FAIR. This is LeCun's lab showing that JEPA scales and enables the full prediction-understanding-planning triad. | Large (40G+/Multi-card): Massive video transformer trained on millions of videos. Meta-scale compute. |
| 24 | 2024-10-25 | [Connecting Joint-Embedding Predictive Architecture with Contrastive Se](https://arxiv.org/abs/2410.19560) | — | — |
| 25 | 2024-08-14 | [CNN-JEPA: Self-Supervised Pretraining Convolutional Neural Networks Us](https://arxiv.org/abs/2408.07514) | — | — |
| 26 | 2024-05-06 | [Sora and V-JEPA Have Not Learned The Complete Real World Model -- A Ph](https://arxiv.org/abs/2407.10311) | — | — |
| 27 | 2024-05-06 | [Is Sora a World Simulator? A Comprehensive Survey on General World Mod](https://arxiv.org/abs/2405.03520) | — | — |
| 28 | 2024-04-25 | [Point-JEPA: A Joint Embedding Predictive Architecture for Self-Supervi](https://arxiv.org/abs/2404.16432) | — | — |
| 29 | 2024-03-16 | [Dreaming of Many Worlds: Learning Contextual World Models Aids Zero-Sh](https://arxiv.org/abs/2403.10967) | — | — |
| 30 | 2024-03-08 | [Sora as a World Model? A Complete Survey on Text-to-Video Generation](https://arxiv.org/abs/2403.05131) | — | — |
| 31 | 2023-11-27 | [A-JEPA: Joint-Embedding Predictive Architecture Can Listen](https://arxiv.org/abs/2311.15830) | — | — |
| 32 | 2023-09-29 | [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | MEDIUM — Demonstrates the power of world models but uses the generative approach that LeCun considers inefficient. Important counterpoint to JEPA. | Large (40G+/Multi-card): 4.6B parameter video diffusion model trained on massive driving data. |
| 33 | 2023-07-24 | [MC-JEPA: A Joint-Embedding Predictive Architecture for Self-Supervised](https://arxiv.org/abs/2307.12698) | HIGH — Core JEPA extension to video modality. Embodies the modular, factorized world model concept. | Large (40G+): Video transformer, multi-GPU. Uses Something-Something-v2 and Kinetics-400. |
| 34 | 2023-07-14 | [SafeDreamer: Safe Reinforcement Learning with World Models](https://arxiv.org/abs/2307.07176) | — | — |
| 35 | 2023-01-19 | [Self-Supervised Learning from Images with a Joint-Embedding Predictive](https://arxiv.org/abs/2301.08243) | HIGH — Direct implementation of LeCun's core vision. This IS the canonical JEPA paper. | Large (40G+): ViT-H/14 backbone trained on ImageNet-1K. Requires multi-GPU training. |
| 36 | 2022-06-28 | [DayDreamer: World Models for Physical Robot Learning](https://arxiv.org/abs/2206.14176) | HIGH — Landmark paper demonstrating the feasibility of learned world models on real robots. A key empirical validation of LeCun's vision, even though it predates JEPA. | Mid (24G): Training on a single GPU from real robot data. |
| 37 | 2022-02-19 | [TransDreamer: Reinforcement Learning with Transformer World Models](https://arxiv.org/abs/2202.09481) | — | — |

---

## 1. [2026-07-04] SiamJEPA: On the Role of Siamese Student Encoders in JEPA

- **arXiv**: [2607.04044](https://arxiv.org/abs/2607.04044)
- **Authors**: Makoto Yamada
- **Abstract**: Recently, Joint Embedding Predictive Architectures (JEPAs) have attracted significant attention in the computer vision and machine learning communities as a promising framework for self-supervised representation learning. Unlike masked autoencoders that reconstruct pixels, JEPA models learn representations by predicting latent embeddings of masked regions. Existing JEPA-based methods, such as I-JEPA and V-JEPA, typically employ a single encoder in the student network. In contrast, using Siamese encoders for student network is more naturally aligned with brain-inspired representation learning f
- **Compute Scale**: Mid (24G): Ablation studies on standard benchmarks.
- **LeCun Alignment**: HIGH — Theoretical validation of JEPA architecture choices.

### What / Why / Solve

- **Proposal**: SiamJEPA — Analyzes the role of Siamese (weight-shared) student encoders in JEPA. Investigates whether sharing weights between context and target encoders helps or hurts representation learning.
- **Motivation**: JEPA uses separate context/target encoders with EMA updates (like BYOL). But are two encoders necessary? Siamese architectures are simpler. Understanding this question is crucial for JEPA's theoretical foundations.
- **Problem Solved**: Provides theoretical analysis of encoder architecture choices in JEPA. Clarifies when and why asymmetric encoders are beneficial.

### Academic Context

- **Inheritance / Response**: Directly extends I-JEPA (2301.08243). Connects to the broader SSL literature on siamese vs. asymmetric architectures (BYOL, SimSiam).
- **Implicit Connection**: This is a theoretical analysis paper that validates (or challenges) the core architectural choices in all JEPA variants. Its findings affect I-JEPA, V-JEPA, MC-JEPA, and all their derivatives.
- **Research Line**: JEPA Theory — architectural analysis and understanding of JEPA's inductive biases.

- **Future Directions**: Apply findings to video and multimodal JEPA; develop theoretically-grounded architecture improvements.
- **GitHub**: To be checked

---

## 2. [2026-06-30] AdaJEPA: An Adaptive Latent World Model

- **arXiv**: [2606.32026](https://arxiv.org/abs/2606.32026)
- **Authors**: Ying Wang, Oumayma Bounou, Yann LeCun, Mengye Ren
- **Abstract**: Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation sign
- **Compute Scale**: Mid (24G): Focus on efficiency improvements rather than scale.
- **LeCun Alignment**: HIGH — Adaptive computation is key to LeCun's vision of efficient autonomous systems.

### What / Why / Solve

- **Proposal**: AdaJEPA — Adaptive latent world model that dynamically adjusts its latent space resolution based on task complexity. Uses a curriculum of increasingly complex predictions.
- **Motivation**: Fixed-size latent spaces are either too small (lose information) or too large (waste compute). A truly autonomous system needs adaptive representations that scale with task difficulty.
- **Problem Solved**: Introduces adaptive latent dimensionality to world models. The model learns WHEN to use more capacity rather than always using maximum capacity.

### Academic Context

- **Inheritance / Response**: Builds on the JEPA framework (2301.08243) and efficient world model literature. Addresses the fixed-capacity limitation.
- **Implicit Connection**: The adaptive capacity idea connects to LeCun's hierarchical planning vision — different levels of the abstraction hierarchy need different representational capacities. AdaJEPA implements this adaptivity within a single level.
- **Research Line**: Efficient JEPA — reducing the computational cost of world models through adaptivity.

- **Future Directions**: Multi-level adaptive hierarchies; combining with action-conditioned prediction.
- **GitHub**: To be checked

---

## 3. [2026-06-22] SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors

- **arXiv**: [2606.23444](https://arxiv.org/abs/2606.23444)
- **Authors**: Pratyaksh Rao, Wancong Zhang, Randall Balestriero, Yann LeCun, Giuseppe Loianno
- **Abstract**: Accurate dynamics models are critical for informed decision-making in robotic systems, particularly for agile aerial vehicles operating under uncertainty. Neural network dynamics models are attractive for capturing complex nonlinear effects, but existing predictive approaches struggle with long-horizon forecasting because their autoregressive rollout mechanism amplifies errors over time. Joint Embedding Predictive Architectures (JEPAs) offer a compelling alternative by modeling dynamics in latent space, yet prior JEPA-style methods for robot navigation have been studied primarily for kinematic
- **Compute Scale**: Large (40G+): Both training and real-time inference on drone hardware.
- **LeCun Alignment**: HIGH — Directly applies JEPA to physical robot control, validating the world model approach.

### What / Why / Solve

- **Proposal**: SkyJEPA — Long-horizon world model for zero-shot sim-to-real control of quadrotors. Learns a latent dynamics model that transfers from simulation to real-world drone flight without fine-tuning.
- **Motivation**: Sim-to-real transfer is a fundamental challenge in robotics. World models that work in simulation often fail in reality due to the domain gap. A JEPA-based approach in latent space should be more robust to visual domain shift.
- **Problem Solved**: Zero-shot sim-to-real transfer for drone control using a JEPA world model. Demonstrates that latent-space prediction is more transferable than pixel-space prediction.

### Academic Context

- **Inheritance / Response**: Builds on JEPA (2301.08243) and Dreamer-style model-based RL. Applies JEPA principles to the sim-to-real robotics domain.
- **Implicit Connection**: This is the first demonstration of JEPA for real-world robotics control. It validates LeCun's argument that latent-space prediction is more robust than pixel-space generation. Connects to the broader WAM vision.
- **Research Line**: JEPA for Robotics — sim-to-real transfer using latent world models.

- **Future Directions**: Extension to other robot platforms; multi-agent drone swarms; longer-horizon planning.
- **GitHub**: To be checked

---

## 4. [2026-06-17] S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Representation Learning

- **arXiv**: [2606.19398](https://arxiv.org/abs/2606.19398)
- **Authors**: Georgios Ioannides, Adrian Kieback, Judah Goldfeder, Linsey Pang, Aman Chadha, Aaron Elkins, Yann LeCun, Ravid Shwartz-Ziv
- **Abstract**: Self-supervised speech encoders are predominantly trained by predicting discrete hard cluster IDs at masked positions, a recipe that collapses acoustic ambiguity at category boundaries and requires interrupting training to re-cluster the entire corpus between iterations. We introduce S-JEPA, a JEPA-style encoder-predictor pair trained to match the soft posteriors of a Gaussian Mixture Model at masked positions via KL divergence. Training runs as one continuous optimization trajectory in two phases: a fixed GMM over MFCC features, then an online GMM over encoder features, with the input layer s
- **Compute Scale**: Mid (24G): Speech SSL training on LibriSpeech-scale data.
- **LeCun Alignment**: MEDIUM — Expands JEPA to new modalities, supporting the generality of LeCun's framework.

### What / Why / Solve

- **Proposal**: S-JEPA — Soft Clustering Anchors for self-supervised speech representation learning. Applies JEPA to the audio domain using soft cluster assignments as prediction targets.
- **Motivation**: JEPA has been successful in vision but unexplored in speech. Speech has unique temporal structure that requires different masking and prediction strategies. Extending JEPA to audio validates its generality.
- **Problem Solved**: First thorough application of JEPA to speech SSL. Introduces soft clustering as a general-purpose target representation for non-visual modalities.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and A-JEPA (2311.15830). Extends JEPA beyond vision to speech with modality-specific adaptations.
- **Implicit Connection**: Together with A-JEPA, establishes the JEPA framework as a general-purpose SSL method beyond vision. The soft clustering targets could be applied back to vision JEPA as well.
- **Research Line**: Multimodal JEPA — extending JEPA to new modalities (speech, audio).

- **Future Directions**: Joint audio-visual JEPA; speech JEPA for dialogue systems; multilingual speech JEPA.
- **GitHub**: To be checked

---

## 5. [2026-06-14] You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences

- **arXiv**: [2606.15956](https://arxiv.org/abs/2606.15956)
- **Authors**: Ninad Daithankar, Alexi Gladstone, Yann LeCun, Heng Ji
- **Abstract**: Progress in AI has largely been driven by methods that assume less. As compute and data increase, approaches with weaker inductive biases generally outperform those with stronger assumptions. This is particularly characteristic of the field of Visual Representation Learning, where approaches have gone from being dominated by Supervised Learning, to Weakly Supervised Learning, to the now widespread success of Self-Supervised Learning without human labels. Yet, even modern Self-Supervised Learning approaches still depend on strong inductive biases such as augmentations, masking, or cropping. If 
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 6. [2026-05-25] When Does LeJEPA Learn a World Model?

- **arXiv**: [2605.26379](https://arxiv.org/abs/2605.26379)
- **Authors**: David Klindt, Yann LeCun, Randall Balestriero
- **Abstract**: A representation that scrambles the true degrees of freedom of the world cannot support reliable planning or compositional generalization. We prove that LeJEPA (alignment plus Gaussian regularization) linearly recovers the world's latent variables from nonlinear observations, a property known as linear identifiability, in a broad class of worlds where latents evolve under stationary, additive-noise transitions. Our main result is that among all such worlds, the Gaussian is the unique latent distribution for which this guarantee holds. The forward direction rests on a spectral decomposition in 
- **Compute Scale**: Mid (24G): Analytical experiments with controlled conditions.
- **LeCun Alignment**: HIGH — Directly investigates whether JEPA fulfills LeCun's world model vision.

### What / Why / Solve

- **Proposal**: When Does LeJEPA Learn a World Model? — Theoretical and empirical analysis of the conditions under which JEPA-trained representations actually encode world model-like predictive capabilities.
- **Motivation**: JEPA predicts latent representations, but does this ACTUALLY mean it learns a world model? There's a gap between the training objective and the emergence of world model capabilities. This paper bridges that gap with analysis.
- **Problem Solved**: Identifies the necessary conditions (data diversity, architecture depth, training duration) for JEPA to actually function as a world model rather than just a feature extractor.

### Academic Context

- **Inheritance / Response**: Directly analyzes and extends I-JEPA/LeWorldModel. Connects to theoretical SSL literature on what representations actually capture.
- **Implicit Connection**: This is a CRITICAL paper for the entire JEPA research program. It asks THE fundamental question: when does JEPA actually become a world model? Its findings affect how ALL future JEPA systems should be designed.
- **Research Line**: JEPA Theory — conditions for emergent world model capabilities.

- **Future Directions**: Develop architectural inductive biases that guarantee world model emergence; theoretical convergence guarantees.
- **GitHub**: To be checked

---

## 7. [2026-05-25] UWM-JEPA: Predictive World Models That Imagine in Belief Space

- **arXiv**: [2605.25313](https://arxiv.org/abs/2605.25313)
- **Authors**: Santosh Kumar Radha, Oktay Goktas
- **Abstract**: World models for partially observed environments must imagine multiple compatible hidden futures and steer between them under counterfactual actions. Joint Embedding Predictive Architectures (JEPAs) do this in latent space, but a vector-valued latent has no internal structure for carrying the belief over hidden continuations through blind rollout. We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. The construction preserves the joint-state spectrum exactly during rollout, so 
- **Compute Scale**: Mid (24G): Belief-state inference adds moderate overhead.
- **LeCun Alignment**: HIGH — Addresses a key practical limitation on the path to real-world autonomous systems.

### What / Why / Solve

- **Proposal**: UWM-JEPA — Predictive world models that imagine in belief space. Combines JEPA-style latent prediction with belief-state representations (partially observable settings) for robust planning under uncertainty.
- **Motivation**: Real-world environments are partially observable — agents never see the full state. Existing world models assume full observability or use simple RNN-based belief states. JEPA in belief space enables planning under uncertainty while maintaining the efficiency of latent prediction.
- **Problem Solved**: Extends JEPA world models to partially observable environments by operating in belief space. Bridges the gap between JEPA's efficient latent prediction and POMDP planning.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243), Dreamer, and POMDP/belief-state RL literature.
- **Implicit Connection**: Belief-space prediction is essential for real-world robotics where sensors are noisy and occluded. This connects JEPA to the practical challenges of embodied AI.
- **Research Line**: Robust JEPA — handling partial observability in world models.

- **Future Directions**: Active information gathering with UWM-JEPA; multi-agent belief-space planning.
- **GitHub**: To be checked

---

## 8. [2026-05-20] stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation

- **arXiv**: [2605.21800](https://arxiv.org/abs/2605.21800)
- **Authors**: Lucas Maes, Quentin Le Lidec, Luiz Facury, Nassim Massaudi, Ayush Chaurasia, Francesco Capuano, Richard Gao, Taj Gillin et al.
- **Abstract**: World models are central to building agents that can reason, plan, and generalize beyond their training data. However, research on world models is currently fragmented, with disparate codebases, data pipelines, and evaluation protocols hindering reproducibility and fair comparison. Current practice is further limited by three key bottlenecks: fragile one-off codebases, slow video data loading, and the lack of standardized generalization benchmarks. We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation. It delivers (
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 9. [2026-05-15] DiLA: Disentangled Latent Action World Models

- **arXiv**: [2605.15725](https://arxiv.org/abs/2605.15725)
- **Authors**: Tianqiu Zhang, Muyang Lyu, Yufan Zhang, Fang Fang, Si Wu
- **Abstract**: Latent Action Models (LAMs) enable the learning of world models from unlabeled video by inferring abstract actions between consecutive frames. However, LAMs face a fundamental trade-off between action abstraction and generation fidelity. Existing methods typically circumvent this issue by using two-stage training with pre-trained world models or by limiting predictions to optical flow. In this paper, we introduce DiLA, a novel Disentangled Latent Action world model that aims to resolve this trade-off via content-structure disentanglement. Our key insight is that disentanglement and latent acti
- **Compute Scale**: Mid (24G): Standard world model training with disentanglement objectives.
- **LeCun Alignment**: HIGH — Factorized control aligns with LeCun's modular agent architecture.

### What / Why / Solve

- **Proposal**: DiLA — Disentangled Latent Action world models. Factorizes the latent action space into independent components representing different aspects of control (e.g., navigation vs. manipulation).
- **Motivation**: A monolithic action space conflates different types of behaviors. In LeCun's hierarchical planning vision, different modules should handle different abstractions. DiLA implements this factorization at the action level.
- **Problem Solved**: Learns interpretable, factorized action representations. Enables compositional control — combining navigation actions with manipulation actions without retraining.

### Academic Context

- **Inheritance / Response**: Builds on Dreamer and world model literature. Introduces disentanglement (from representation learning) into action spaces.
- **Implicit Connection**: Disentangled actions are a natural complement to JEPA's factorized representations. Together they could enable modular world models where different action dimensions control different aspects of the world.
- **Research Line**: Latent Action — factorizing and interpreting action representations in world models.

- **Future Directions**: Compositional task learning; zero-shot transfer of action components.
- **GitHub**: To be checked

---

## 10. [2026-05-10] Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models

- **arXiv**: [2605.09241](https://arxiv.org/abs/2605.09241)
- **Authors**: Kai Zhao, Dongliang Nie, Yuchen Lin, Zhehan Luo, Yixiao Gu, Deng-Ping Fan, Dan Zeng
- **Abstract**: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be alleviated bysimply constraining latent embeddings with an isotropic Gaussian prior.However, latent representations inherently lie on low-dimensional manifoldswithin a high-dimensional ambient space, and e
- **Compute Scale**: Mid (24G): Adds regularization term to existing JEPA training.
- **LeCun Alignment**: HIGH — Makes JEPA more practical and reliable, accelerating the path to autonomous intelligence.

### What / Why / Solve

- **Proposal**: Sub-JEPA — Subspace Gaussian Regularization for stable end-to-end world models. Introduces a regularization technique that constrains latent representations to lie on a low-dimensional Gaussian manifold, preventing representation collapse.
- **Motivation**: End-to-end JEPA training is unstable — the predictor can collapse to trivial solutions (e.g., predicting the mean). Previous solutions use stop-gradient or EMA, but these are heuristics. Subspace regularization provides a principled solution.
- **Problem Solved**: Provides a principled, theoretically-grounded solution to representation collapse in JEPA training. Eliminates the need for stop-gradient hacks.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and addresses its training stability issues. Connects to the literature on preventing collapse in SSL.
- **Implicit Connection**: If Sub-JEPA's regularization is adopted, it could simplify ALL JEPA training pipelines. This is infrastructure-level improvement that benefits the entire research line.
- **Research Line**: Stable JEPA — training techniques for reliable JEPA convergence.

- **Future Directions**: Apply to video and multimodal JEPA; theoretical analysis of why subspace regularization works.
- **GitHub**: To be checked

---

## 11. [2026-05-05] Text-Conditional JEPA for Learning Semantically Rich Visual Representations

- **arXiv**: [2605.03245](https://arxiv.org/abs/2605.03245)
- **Authors**: Chen Huang, Xianhang Li, Vimal Thilak, Etai Littwin, Josh Susskind
- **Abstract**: Image-based Joint-Embedding Predictive Architecture (I-JEPA) offers a promising approach to visual self-supervised learning through masked feature prediction. However with the inherent visual uncertainty at masked positions, feature prediction remains challenging and may fail to learn semantic representations. In this work, we propose Text-Conditional JEPA (TC-JEPA) that uses image captions to reduce the prediction uncertainty. Specifically, we modulate the predicted patch features using a fine-grained text conditioner that computes sparse cross-attention over input text tokens. With such cond
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 12. [2026-04-03] Hierarchical Planning with Latent World Models

- **arXiv**: [2604.03208](https://arxiv.org/abs/2604.03208)
- **Authors**: Wancong Zhang, Basile Terver, Artem Zholus, Soham Chitnis, Harsh Sutaria, Mido Assran, Randall Balestriero, Amir Bar et al.
- **Abstract**: World models are a promising path to zero-shot embodied control through planning. However, existing world model planners struggle on long-horizon, multi-stage tasks: prediction errors compound and naive search is exponential in the planning horizon. Hierarchy mitigates both by decomposing tasks into shorter, tractable subproblems; yet prior hierarchical approaches either amortize control into task-specific policies (hierarchical RL) or assume low-dimensional states and known dynamics (classical hierarchical MPC). We present Hierarchical Planning with Latent World Models (HWM), an architecture 
- **Compute Scale**: Mid (24G): Two-level planning is more efficient than flat long-horizon planning.
- **LeCun Alignment**: HIGH — Directly implements LeCun's hierarchical planning vision.

### What / Why / Solve

- **Proposal**: Hierarchical planning with latent world models — Combines JEPA-like latent dynamics with hierarchical planning. A high-level planner sets subgoals in latent space; a low-level controller executes actions to reach those subgoals.
- **Motivation**: Long-horizon tasks require hierarchical decomposition. LeCun's vision explicitly calls for hierarchical planning. Current world models plan at a single level of abstraction, limiting their horizon.
- **Problem Solved**: Enables long-horizon planning by decomposing tasks hierarchically in latent space. The high-level planner operates on compressed representations, dramatically reducing the planning horizon.

### Academic Context

- **Inheritance / Response**: Builds on JEPA (2301.08243) and hierarchical RL. Directly implements the hierarchical planning component of LeCun's architecture diagram.
- **Implicit Connection**: This is one of the closest implementations of LeCun's full architecture: a world model + hierarchical planner operating in latent space. The subgoal setting in latent space is exactly what LeCun's 'configurator' module does.
- **Research Line**: Hierarchical WAM — multi-level planning in latent world models.

- **Future Directions**: More than two levels; learned subgoal representations; integration with real robots.
- **GitHub**: To be checked

---

## 13. [2026-03-20] Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations

- **arXiv**: [2603.20327](https://arxiv.org/abs/2603.20327)
- **Authors**: Liu hung ming
- **Abstract**: Video world models trained with Joint Embedding Predictive Architectures (JEPA) acquire rich spatiotemporal representations by predicting masked regions in latent space rather than reconstructing pixels. This removes the visual verification pathway of generative models, creating a structural interpretability gap: the encoder has learned physical structure inaccessible in any inspectable form. Existing probing methods either operate in continuous space without a structured intermediate layer, or attach generative components whose parameters confound attribution of behavior to the encoder.
  We 
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 14. [2026-03-15] V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning

- **arXiv**: [2603.14482](https://arxiv.org/abs/2603.14482)
- **Authors**: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas et al.
- **Abstract**: We present V-JEPA 2.1, a family of self-supervised models that learn dense, high-quality visual representations for both images and videos while retaining strong global scene understanding. The approach combines four key components. First, a dense predictive loss uses a masking-based objective in which both visible and masked tokens contribute to the training signal, encouraging explicit spatial and temporal grounding. Second, deep self-supervision applies the self-supervised objective hierarchically across multiple intermediate encoder layers to improve representation quality. Third, multi-mo
- **Compute Scale**: Large (40G+): Extended V-JEPA training with dense prediction heads.
- **LeCun Alignment**: HIGH — Meta FAIR. Addresses a key limitation on the path to full world models.

### What / Why / Solve

- **Proposal**: V-JEPA 2.1 — Unlocks dense features in video SSL. Improves V-JEPA by learning dense (pixel-level) representations rather than just global features, enabling fine-grained video understanding tasks.
- **Motivation**: V-JEPA representations were good for global video understanding but poor for dense prediction tasks (segmentation, tracking, depth). A world model needs DENSE spatial understanding, not just global semantics.
- **Problem Solved**: Extends JEPA from sparse/global representations to dense spatial representations. Enables object-level and region-level video understanding within the JEPA framework.

### Academic Context

- **Inheritance / Response**: Direct iterative improvement of V-JEPA 2 (2506.09985). Addresses a known limitation of the original JEPA design.
- **Implicit Connection**: Dense features connect JEPA to computer vision tasks like object detection and tracking — essential for robotic world models. This is the bridge between pure SSL and embodied AI.
- **Research Line**: Video JEPA — dense feature iteration. Aims to make JEPA practical for downstream vision tasks.

- **Future Directions**: Dense JEPA for robotics; real-time dense prediction; integration with 3D representations.
- **GitHub**: Meta FAIR

---

## 15. [2026-03-13] LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

- **arXiv**: [2603.19312](https://arxiv.org/abs/2603.19312)
- **Authors**: Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
- **Abstract**: Joint Embedding Predictive Architectures (JEPAs) offer a compelling framework for learning world models in compact latent spaces, yet existing methods remain fragile, relying on complex multi-term losses, exponential moving averages, pre-trained encoders, or auxiliary supervision to avoid representation collapse. In this work, we introduce LeWorldModel (LeWM), the first JEPA that trains stably end-to-end from raw pixels using only two loss terms: a next-embedding prediction loss and a regularizer enforcing Gaussian-distributed latent embeddings. This reduces tunable loss hyperparameters from s
- **Compute Scale**: Large (40G+): End-to-end pixel-to-latent training.
- **LeCun Alignment**: HIGH — Likely from LeCun's group. The name itself signals direct alignment with LeCun's vision.

### What / Why / Solve

- **Proposal**: LeWorldModel — Stable End-to-End JEPA from pixels. Proposes a complete world model that directly maps raw pixel observations to latent states and predicts future states in latent space, with explicit focus on training stability.
- **Motivation**: Existing world models (Dreamer, etc.) use reconstruction-based objectives which are computationally expensive and focus on pixel-level details. JEPA offers an alternative but has been unstable to train end-to-end from pixels.
- **Problem Solved**: First stable end-to-end JEPA world model trained from raw pixels. Demonstrates that JEPA can serve as a complete world model without auxiliary reconstruction losses.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and Dreamer-style world models. The name 'LeWorldModel' directly references LeCun's vision.
- **Implicit Connection**: This is the most direct attempt to implement LeCun's complete world model architecture in a single system. It bridges JEPA (SSL) with model-based RL (Dreamer). The reconstruction-free approach aligns with LeCun's argument against generative models.
- **Research Line**: End-to-end JEPA World Model — attempts to realize the full JEPA-based world model vision.

- **Future Directions**: Scaling to more complex environments; integrating action-conditioned prediction; real-world robotics.
- **GitHub**: Meta FAIR (likely)

---

## 16. [2026-03-07] Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction

- **arXiv**: [2603.07083](https://arxiv.org/abs/2603.07083)
- **Authors**: Michael Hauri, Friedemann Zenke
- **Abstract**: Model-based reinforcement learning (MBRL) agents operating in high-dimensional observation spaces, such as Dreamer, rely on learning abstract representations for effective planning and control. Existing approaches typically employ reconstruction-based objectives in the observation space, which can render representations sensitive to task-irrelevant details. Recent alternatives trade reconstruction for auxiliary action prediction heads or view augmentation strategies, but perform worse in the Crafter environment than reconstruction-based methods. We close this gap between Dreamer and reconstruc
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 17. [2026-03-05] Probabilistic Dreaming for World Models

- **arXiv**: [2603.04715](https://arxiv.org/abs/2603.04715)
- **Authors**: Gavin Wong
- **Abstract**: "Dreaming" enables agents to learn from imagined experiences, enabling more robust and sample-efficient learning of world models. In this work, we consider innovations to the state-of-the-art Dreamer model using probabilistic methods that enable: (1) the parallel exploration of many latent states; and (2) maintaining distinct hypotheses for mutually exclusive futures while retaining the desirable gradient properties of continuous latents. Evaluating on the MPE SimpleTag domain, our method outperforms standard Dreamer with a 4.5% score improvement and 28% lower variance in episode returns. We a
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 18. [2026-02-12] JEPA-VLA: Video Predictive Embedding is Needed for VLA Models

- **arXiv**: [2602.11832](https://arxiv.org/abs/2602.11832)
- **Authors**: Shangchen Miao, Ningya Feng, Jialong Wu, Ye Lin, Xu He, Dong Li, Mingsheng Long
- **Abstract**: Recent vision-language-action (VLA) models built upon pretrained vision-language models (VLMs) have achieved significant improvements in robotic manipulation. However, current VLAs still suffer from low sample efficiency and limited generalization. This paper argues that these limitations are closely tied to an overlooked component, pretrained visual representation, which offers insufficient knowledge on both aspects of environment understanding and policy prior. Through an in-depth analysis, we find that commonly used visual representations in VLAs, whether pretrained via language-image contr
- **Compute Scale**: Large (40G+): Video JEPA backbone + VLA fine-tuning on robot data.
- **LeCun Alignment**: HIGH — Demonstrates practical necessity of JEPA for embodied AI.

### What / Why / Solve

- **Proposal**: JEPA-VLA — Video predictive embedding is necessary for Vision-Language-Action (VLA) models. Argues and demonstrates that video JEPA representations are essential for building effective VLA models for robotics.
- **Motivation**: Current VLA models use static image features from vision encoders, losing temporal information crucial for action prediction. Video JEPA provides temporally-aware representations that capture motion and dynamics.
- **Problem Solved**: Shows that adding video JEPA features significantly improves VLA model performance on real-world robot manipulation tasks.

### Academic Context

- **Inheritance / Response**: Builds on V-JEPA (2506.09985) and VLA models (RT-2, Octo, etc.). Bridges the gap between video SSL and robot learning.
- **Implicit Connection**: This paper directly connects the JEPA research line to the practical problem of building robot foundation models. It makes the case that LeCun's world model vision is not just theoretically elegant but practically NECESSARY for robotics.
- **Research Line**: Embodied JEPA — applying JEPA representations to robot learning and control.

- **Future Directions**: Real-time VLA with streaming video JEPA; multi-embodiment transfer.
- **GitHub**: To be checked

---

## 19. [2026-01-29] Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving

- **arXiv**: [2601.22032](https://arxiv.org/abs/2601.22032)
- **Authors**: Linhan Wang, Zichong Yang, Chen Bai, Guoxiang Zhang, Xiaotong Liu, Xiaoyin Zheng, Xiao-Xiao Long, Chang-Tien Lu et al.
- **Abstract**: End-to-end autonomous driving increasingly leverages self-supervised video pretraining to learn transferable planning representations. However, pretraining video world models for scene understanding has so far brought only limited improvements. This limitation is compounded by the inherent ambiguity of driving: each scene typically provides only a single human trajectory, making it difficult to learn multimodal behaviors. In this work, we propose Drive-JEPA, a framework that integrates Video Joint-Embedding Predictive Architecture (V-JEPA) with multimodal trajectory distillation for end-to-end
- **Compute Scale**: Large (40G+): Driving video data + trajectory prediction model.
- **LeCun Alignment**: HIGH — Validates JEPA in a high-stakes real-world application.

### What / Why / Solve

- **Proposal**: Drive-JEPA — Video JEPA meets multimodal trajectory distillation for end-to-end driving. Combines video JEPA representations with trajectory prediction for autonomous driving.
- **Motivation**: Autonomous driving requires predicting the future behavior of other agents. Pure end-to-end approaches lack structured world understanding. Video JEPA provides structured temporal representations that improve trajectory prediction.
- **Problem Solved**: Improves autonomous driving trajectory prediction by incorporating video JEPA features into the driving model.

### Academic Context

- **Inheritance / Response**: Builds on V-JEPA (2506.09985) and trajectory prediction literature. Applies JEPA to the autonomous driving domain.
- **Implicit Connection**: Along with GAIA-1 (2309.17080), this establishes the importance of world models for autonomous driving. JEPA-based driving models are an alternative to the generative (diffusion-based) approach.
- **Research Line**: JEPA for Autonomous Driving — world models for vehicle behavior prediction.

- **Future Directions**: Interactive prediction (ego vehicle actions affect other agents); multi-agent driving JEPA.
- **GitHub**: To be checked

---

## 20. [2025-11-21] DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture

- **arXiv**: [2511.17354](https://arxiv.org/abs/2511.17354)
- **Authors**: Xiangteng He, Shunsuke Sakai, Shivam Chandhok, Sara Beery, Kun Yuan, Nicolas Padoy, Tatsuhito Hasegawa, Leonid Sigal
- **Abstract**: Recent advances in self-supervised visual representation learning have demonstrated the effectiveness of predictive latent-space objectives for learning transferable features. In particular, Image-based Joint-Embedding Predictive Architecture (I-JEPA) learns representations by predicting latent embeddings of masked target regions from visible context. However, it predicts target regions in parallel and all at once, lacking ability to order predictions meaningfully. Inspired by human visual perception, which attends selectively and progressively from primary to secondary cues, we propose DSeq-J
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 21. [2025-10-07] Gaussian Embeddings: How JEPAs Secretly Learn Your Data Density

- **arXiv**: [2510.05949](https://arxiv.org/abs/2510.05949)
- **Authors**: Randall Balestriero, Nicolas Ballas, Mike Rabbat, Yann LeCun
- **Abstract**: Joint Embedding Predictive Architectures (JEPAs) learn representations able to solve numerous downstream tasks out-of-the-box. JEPAs combine two objectives: (i) a latent-space prediction term, i.e., the representation of a slightly perturbed sample must be predictable from the original sample's representation, and (ii) an anti-collapse term, i.e., not all samples should have the same representation. While (ii) is often considered as an obvious remedy to representation collapse, we uncover that JEPAs' anti-collapse term does much more--it provably estimates the data density. In short, any succe
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 22. [2025-09-29] Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers

- **arXiv**: [2509.24317](https://arxiv.org/abs/2509.24317)
- **Authors**: Xianhang Li, Chen Huang, Chun-Liang Li, Eran Malach, Josh Susskind, Vimal Thilak, Etai Littwin
- **Abstract**: Video Joint Embedding Predictive Architectures (V-JEPA) learn generalizable off-the-shelf video representation by predicting masked regions in latent space with an exponential moving average (EMA)-updated teacher. While EMA prevents representation collapse, it complicates scalable model selection and couples teacher and student architectures. We revisit masked-latent prediction and show that a frozen teacher suffices. Concretely, we (i) train a target encoder with a simple pixel-reconstruction o
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 23. [2025-06-11] V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- **arXiv**: [2506.09985](https://arxiv.org/abs/2506.09985)
- **Authors**: Mido Assran, Adrien Bardes, David Fan, Quentin Garrido, Russell Howes,  Mojtaba,  Komeili, Matthew Muckley et al.
- **Abstract**: A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on 
- **Compute Scale**: Large (40G+/Multi-card): Massive video transformer trained on millions of videos. Meta-scale compute.
- **LeCun Alignment**: HIGH — Directly from Meta FAIR. This is LeCun's lab showing that JEPA scales and enables the full prediction-understanding-planning triad.

### What / Why / Solve

- **Proposal**: V-JEPA 2 — Self-supervised video models at scale. Extends V-JEPA with larger models, more data, and demonstrates that video JEPA representations enable understanding, prediction, AND planning.
- **Motivation**: Previous V-JEPA showed video SSL works but was limited in scale. To achieve LeCun's vision of autonomous intelligence, video models must not just understand but also PREDICT and PLAN — the three pillars of a world model.
- **Problem Solved**: Demonstrates that pure self-supervised video JEPA can simultaneously support understanding (classification), prediction (future frame forecasting), and planning (action selection) — all from the same representation.

### Academic Context

- **Inheritance / Response**: Scales up V-JEPA (2024). Builds on I-JEPA (2301.08243) and MC-JEPA (2307.12698). Direct lineage from LeCun's vision paper.
- **Implicit Connection**: The 'prediction' and 'planning' capabilities connect this to World Action Models — V-JEPA 2 is essentially a world model that can be queried for future states. This bridges the gap between pure JEPA and WAM.
- **Research Line**: Video JEPA — the scaling story. This paper establishes video JEPA as the backbone for future autonomous systems.

- **Future Directions**: Real-time planning with V-JEPA; integration with action models; open-world video understanding.
- **GitHub**: Meta FAIR

---

## 24. [2024-10-25] Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning

- **arXiv**: [2410.19560](https://arxiv.org/abs/2410.19560)
- **Authors**: Shentong Mo, Shengbang Tong
- **Abstract**: In recent advancements in unsupervised visual representation learning, the Joint-Embedding Predictive Architecture (JEPA) has emerged as a significant method for extracting visual features from unlabeled imagery through an innovative masking strategy. Despite its success, two primary limitations have been identified: the inefficacy of Exponential Moving Average (EMA) from I-JEPA in preventing entire collapse and the inadequacy of I-JEPA prediction in accurately learning the mean of patch represe
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 25. [2024-08-14] CNN-JEPA: Self-Supervised Pretraining Convolutional Neural Networks Using Joint Embedding Predictive Architecture

- **arXiv**: [2408.07514](https://arxiv.org/abs/2408.07514)
- **Authors**: András Kalapos, Bálint Gyires-Tóth
- **Abstract**: Self-supervised learning (SSL) has become an important approach in pretraining large neural networks, enabling unprecedented scaling of model and dataset sizes. While recent advances like I-JEPA have shown promising results for Vision Transformers, adapting such methods to Convolutional Neural Networks (CNNs) presents unique challenges. In this paper, we introduce CNN-JEPA, a novel SSL method that successfully applies the joint embedding predictive architecture approach to CNNs. Our method incor
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 26. [2024-05-06] Sora and V-JEPA Have Not Learned The Complete Real World Model -- A Philosophical Analysis of Video AIs Through the Theory of Productive Imagination

- **arXiv**: [2407.10311](https://arxiv.org/abs/2407.10311)
- **Authors**: Jianqiu Zhang
- **Abstract**: Sora from Open AI has shown exceptional performance, yet it faces scrutiny over whether its technological prowess equates to an authentic comprehension of reality. Critics contend that it lacks a foundational grasp of the world, a deficiency V-JEPA from Meta aims to amend with its joint embedding approach. This debate is vital for steering the future direction of Artificial General Intelligence(AGI). We enrich this debate by developing a theory of productive imagination that generates a coherent
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 27. [2024-05-06] Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond

- **arXiv**: [2405.03520](https://arxiv.org/abs/2405.03520)
- **Authors**: Zheng Zhu, Xiaofeng Wang, Wangbo Zhao, Chen Min, Bohan Li, Nianchen Deng, Min Dou, Yuqi Wang et al.
- **Abstract**: General world models represent a crucial pathway toward achieving Artificial General Intelligence (AGI), serving as the cornerstone for various applications ranging from virtual environments to decision-making systems. Recently, the emergence of the Sora model has attained significant attention due to its remarkable simulation capabilities, which exhibits an incipient comprehension of physical laws. In this survey, we embark on a comprehensive exploration of the latest advancements in world mode
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 28. [2024-04-25] Point-JEPA: A Joint Embedding Predictive Architecture for Self-Supervised Learning on Point Cloud

- **arXiv**: [2404.16432](https://arxiv.org/abs/2404.16432)
- **Authors**: Ayumu Saito, Prachi Kudeshia, Jiju Poovvancheri
- **Abstract**: Recent advancements in self-supervised learning in the point cloud domain have demonstrated significant potential. However, these methods often suffer from drawbacks, including lengthy pre-training time, the necessity of reconstruction in the input space, or the necessity of additional modalities. In order to address these issues, we introduce Point-JEPA, a joint embedding predictive architecture designed specifically for point cloud data. To this end, we introduce a sequencer that orders point 
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 29. [2024-03-16] Dreaming of Many Worlds: Learning Contextual World Models Aids Zero-Shot Generalization

- **arXiv**: [2403.10967](https://arxiv.org/abs/2403.10967)
- **Authors**: Sai Prasanna, Karim Farid, Raghu Rajan, André Biedenkapp
- **Abstract**: Zero-shot generalization (ZSG) to unseen dynamics is a major challenge for creating generally capable embodied agents. To address the broader challenge, we start with the simpler setting of contextual reinforcement learning (cRL), assuming observability of the context values that parameterize the variation in the system's dynamics, such as the mass or dimensions of a robot, without making further simplifying assumptions about the observability of the Markovian state. Toward the goal of ZSG to un
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 30. [2024-03-08] Sora as a World Model? A Complete Survey on Text-to-Video Generation

- **arXiv**: [2403.05131](https://arxiv.org/abs/2403.05131)
- **Authors**: Fachrina Dewi Puspitasari, Chaoning Zhang, Joseph Cho, Adnan Haider, Noor Ul Eman, Omer Amin, Alexis Mankowski, Muhammad Umair et al.
- **Abstract**: The evolution of video generation from text, from animating MNIST to simulating the world with Sora, has progressed at a breakneck speed. Here, we systematically discuss how far text-to-video generation technology supports essential requirements in world modeling. We curate 250+ studies on text-based video synthesis and world modeling. We then observe that recent models increasingly support spatial, action, and strategic intelligences in world modeling through adherence to completeness, consiste
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 31. [2023-11-27] A-JEPA: Joint-Embedding Predictive Architecture Can Listen

- **arXiv**: [2311.15830](https://arxiv.org/abs/2311.15830)
- **Authors**: Zhengcong Fei, Mingyuan Fan, Junshi Huang
- **Abstract**: This paper presents that the masked-modeling principle driving the success of large foundational vision models can be effectively applied to audio by making predictions in a latent space. We introduce Audio-based Joint-Embedding Predictive Architecture (A-JEPA), a simple extension method for self-supervised learning from the audio spectrum. Following the design of I-JEPA, our A-JEPA encodes visible audio spectrogram patches with a curriculum masking strategy via context encoder, and predicts the
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 32. [2023-09-29] GAIA-1: A Generative World Model for Autonomous Driving

- **arXiv**: [2309.17080](https://arxiv.org/abs/2309.17080)
- **Authors**: Anthony Hu, Lloyd Russell, Hudson Yeo, Zak Murez, George Fedoseev, Alex Kendall, Jamie Shotton, Gianluca Corrado
- **Abstract**: Autonomous driving promises transformative improvements to transportation, but building systems capable of safely navigating the unstructured complexity of real-world scenarios remains challenging. A critical problem lies in effectively predicting the various potential outcomes that may emerge in response to the vehicle's actions as the world evolves.
  To address this challenge, we introduce GAIA-1 ('Generative AI for Autonomy'), a generative world model that leverages video, text, and action i
- **Compute Scale**: Large (40G+/Multi-card): 4.6B parameter video diffusion model trained on massive driving data.
- **LeCun Alignment**: MEDIUM — Demonstrates the power of world models but uses the generative approach that LeCun considers inefficient. Important counterpoint to JEPA.

### What / Why / Solve

- **Proposal**: GAIA-1 — A Generative World Model for Autonomous Driving. Wayve's large-scale generative world model that predicts future driving scenes conditioned on actions.
- **Motivation**: Autonomous driving requires anticipating how scenes will evolve. Existing approaches use explicit object detection and physics simulation. A learned world model could capture complex, real-world driving dynamics more faithfully.
- **Problem Solved**: Learns a world model for driving that can generate realistic future frames conditioned on ego-vehicle actions. Enables simulation-based planning and evaluation.

### Academic Context

- **Inheritance / Response**: Builds on video diffusion/generation and world model literature. Represents the generative approach to world models (predicts pixels), contrasting with JEPA's latent approach.
- **Implicit Connection**: GAIA-1 is the GENERATIVE counterpart to JEPA-based world models. It embodies the approach LeCun ARGUES AGAINST (predicting pixels) but achieves impressive results. This tension is central to the field.
- **Research Line**: Generative World Models — pixel-space prediction for autonomous driving.

- **Future Directions**: Scaling to more diverse driving scenarios; integration with planning; real-time inference.
- **GitHub**: Wayve (proprietary)

---

## 33. [2023-07-24] MC-JEPA: A Joint-Embedding Predictive Architecture for Self-Supervised Learning of Motion and Content Features

- **arXiv**: [2307.12698](https://arxiv.org/abs/2307.12698)
- **Authors**: Adrien Bardes, Jean Ponce, Yann LeCun
- **Abstract**: Self-supervised learning of visual representations has been focusing on learning content features, which do not capture object motion or location, and focus on identifying and differentiating objects in images and videos. On the other hand, optical flow estimation is a task that does not involve understanding the content of the images on which it is estimated. We unify the two approaches and introduce MC-JEPA, a joint-embedding predictive architecture and self-supervised learning approach to joi
- **Compute Scale**: Large (40G+): Video transformer, multi-GPU. Uses Something-Something-v2 and Kinetics-400.
- **LeCun Alignment**: HIGH — Core JEPA extension to video modality. Embodies the modular, factorized world model concept.

### What / Why / Solve

- **Proposal**: MC-JEPA — Motion and Content JEPA. Learns separate motion and content representations via joint embedding. Uses optical flow as a weak motion signal to disentangle what moves (motion) from what stays (content).
- **Motivation**: Video understanding requires distinguishing between object motion and scene content. Previous self-supervised methods conflate these two factors. A world model needs to understand both what things ARE and how they MOVE.
- **Problem Solved**: Disentangled motion-content representation learning without labels. Enables downstream tasks like action recognition and video object segmentation by providing separate, reusable representations.

### Academic Context

- **Inheritance / Response**: Direct successor to I-JEPA (2301.08243). Extends JEPA from images to video with an explicit motion-content factorization.
- **Implicit Connection**: The motion-content disentanglement foreshadows action-conditioned world models — motion is a precursor to action in the JEPA hierarchy. The two-stream encoder (motion stream + content stream) creates the blueprint for future multimodal JEPA.
- **Research Line**: Multimodal JEPA — the first JEPA paper to handle video with explicit factorization. Predecessor to V-JEPA and JEPA-VLA.

- **Future Directions**: Integration with action models; scaling to longer videos; 3D scene understanding.
- **GitHub**: Meta FAIR (likely internal)

---

## 34. [2023-07-14] SafeDreamer: Safe Reinforcement Learning with World Models

- **arXiv**: [2307.07176](https://arxiv.org/abs/2307.07176)
- **Authors**: Weidong Huang, Jiaming Ji, Chunhe Xia, Borong Zhang, Yaodong Yang
- **Abstract**: The deployment of Reinforcement Learning (RL) in real-world applications is constrained by its failure to satisfy safety criteria. Existing Safe Reinforcement Learning (SafeRL) methods, which rely on cost functions to enforce safety, often fail to achieve zero-cost performance in complex scenarios, especially vision-only tasks. These limitations are primarily due to model inaccuracies and inadequate sample efficiency. The integration of the world model has proven effective in mitigating these sh
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---

## 35. [2023-01-19] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

- **arXiv**: [2301.08243](https://arxiv.org/abs/2301.08243)
- **Authors**: Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael Rabbat, Yann LeCun, Nicolas Ballas
- **Abstract**: This paper demonstrates an approach for learning highly semantic image representations without relying on hand-crafted data-augmentations. We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image. A core design choice to guide I-JEPA towards producing semantic representations is the masking strategy; specifically, it is crucial to (a) sample target blocks with sufficiently 
- **Compute Scale**: Large (40G+): ViT-H/14 backbone trained on ImageNet-1K. Requires multi-GPU training.
- **LeCun Alignment**: HIGH — Direct implementation of LeCun's core vision. This IS the canonical JEPA paper.

### What / Why / Solve

- **Proposal**: JEPA (Joint Embedding Predictive Architecture) — predicts representations of masked target blocks in latent space rather than pixel-level reconstruction. Uses context encoder + target encoder + predictor network.
- **Motivation**: Generative architectures waste capacity modeling pixel-level details irrelevant to semantics. Humans don't predict every pixel — they predict abstract representations. LeCun's core insight: the world is not predictable at the pixel level but is predictable at the representation level.
- **Problem Solved**: Eliminates the need for pixel-level generation in self-supervised learning. Enables semantic-level predictive learning without the computational burden of generative models. Achieves strong representations without data augmentations.

### Academic Context

- **Inheritance / Response**: Builds directly on LeCun's 'A Path Towards Autonomous Machine Intelligence' (2022). Extends BYOL/SimSiam-style non-contrastive SSL with a predictive objective in latent space.
- **Implicit Connection**: Uses multi-block masking strategy (target blocks predicted from context blocks) — the same core idea later used in V-JEPA (video) and MC-JEPA (multimodal). The context→target encoder asymmetry is the defining JEPA pattern.
- **Research Line**: JEPA Core — the foundational implementation of LeCun's predictive world model architecture. Defines the context/target/predictor blueprint.

- **Future Directions**: Scaling to larger models and datasets; extension to video (V-JEPA) and multimodal (MC-JEPA); integration with action-conditioned prediction for world models.
- **GitHub**: Meta FAIR (likely internal); community reimplementations exist

---

## 36. [2022-06-28] DayDreamer: World Models for Physical Robot Learning

- **arXiv**: [2206.14176](https://arxiv.org/abs/2206.14176)
- **Authors**: Philipp Wu, Alejandro Escontrela, Danijar Hafner, Ken Goldberg, Pieter Abbeel
- **Abstract**: To solve tasks in complex environments, robots need to learn from experience. Deep reinforcement learning is a common approach to robot learning but requires a large amount of trial and error to learn, limiting its deployment in the physical world. As a consequence, many advances in robot learning rely on simulators. On the other hand, learning inside of simulators fails to capture the complexity of the real world, is prone to simulator inaccuracies, and the resulting behaviors do not adapt to c
- **Compute Scale**: Mid (24G): Training on a single GPU from real robot data.
- **LeCun Alignment**: HIGH — Landmark paper demonstrating the feasibility of learned world models on real robots. A key empirical validation of LeCun's vision, even though it predates JEPA.

### What / Why / Solve

- **Proposal**: DayDreamer — World Models for Physical Robot Learning. Applies the Dreamer algorithm to real robots, demonstrating that learning world models directly on physical robots is feasible.
- **Motivation**: Previous world model work was limited to simulation. Training on real robots is challenging due to sample efficiency and safety concerns. DayDreamer shows that world models can learn efficiently enough for real-world robotics.
- **Problem Solved**: First demonstration of Dreamer-based world models training and deploying on physical robots (quadruped, wheeled). Shows that latent dynamics models can learn from real-world experience in hours, not months.

### Academic Context

- **Inheritance / Response**: Builds directly on Dreamer (Hafner et al.). Applies model-based RL to real-world robotics.
- **Implicit Connection**: DayDreamer validates the core premise of LeCun's vision: that agents can learn world models from limited real-world experience. It predates JEPA but demonstrates the same principle — learning in latent space is more efficient than pixel-space.
- **Research Line**: Real-World World Models — deploying model-based RL on physical robots.

- **Future Directions**: Integration with JEPA-style architectures; lifelong learning; multi-task world models.
- **GitHub**: https://github.com/danijar/daydreamer

---

## 37. [2022-02-19] TransDreamer: Reinforcement Learning with Transformer World Models

- **arXiv**: [2202.09481](https://arxiv.org/abs/2202.09481)
- **Authors**: Chang Chen, Yi-Fu Wu, Jaesik Yoon, Sungjin Ahn
- **Abstract**: The Dreamer agent provides various benefits of Model-Based Reinforcement Learning (MBRL) such as sample efficiency, reusable knowledge, and safe planning. However, its world model and policy networks inherit the limitations of recurrent neural networks and thus an important question is how an MBRL framework can benefit from the recent advances of transformers and what the challenges are in doing so. In this paper, we propose a transformer-based MBRL agent, called TransDreamer. We first introduce
- **Compute Scale**: —
- **LeCun Alignment**: —

### What / Why / Solve

- **Proposal**: Pending detailed analysis.
- **Motivation**: Pending detailed analysis.
- **Problem Solved**: Pending detailed analysis.

### Academic Context

- **Inheritance / Response**: Pending analysis.
- **Implicit Connection**: Pending analysis.
- **Research Line**: Pending classification.

- **Future Directions**: To be determined.
- **GitHub**: To be checked.

---


*Generated: 2026-07-09 | Papers: 37 | Analysis: Deep*
