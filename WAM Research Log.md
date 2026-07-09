# WAM Research Log — Deep Analysis

> Curated papers from Yann LeCun's World Models/JEPA ecosystem, with detailed architectural analysis, research lineage, and LeCun alignment assessment.

> **37 papers** (2022—2026) | Daily monitoring at 08:00 UTC

---

## 📊 Paper Index

| # | Date | Paper | Alignment | Compute |
|---|------|-------|-----------|--------|
| 1 | 2026-07-04 | [SiamJEPA: On the Role of Siamese Student Encoders in JEPA](https://arxiv.org/abs/2607.04044) | HIGH — Theoretical validation of JEPA architecture. | Mid (24G): Ablation studies on standard benchmarks. |
| 2 | 2026-06-30 | [AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026) | HIGH — Adaptive computation key to efficient autonomous systems. | Mid (24G): Focus on efficiency. |
| 3 | 2026-06-22 | [SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-](https://arxiv.org/abs/2606.23444) | HIGH — Direct JEPA application to physical robot control. | Large (40G+): Training + real-time drone inference. |
| 4 | 2026-06-17 | [S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Repre](https://arxiv.org/abs/2606.19398) | MEDIUM — Expands JEPA generality. | Mid (24G): LibriSpeech-scale. |
| 5 | 2026-06-14 | [You Don't Need Strong Assumptions: Visual Representation Learning](https://arxiv.org/abs/2606.15956) | HIGH — Explores a potentially simpler path to the same world model goal. | Mid (24G) |
| 6 | 2026-05-25 | [When Does LeJEPA Learn a World Model?](https://arxiv.org/abs/2605.26379) | HIGH — Directly investigates whether JEPA fulfills LeCun's world model vision. | Mid (24G): Controlled analytical experiments. |
| 7 | 2026-05-25 | [UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/abs/2605.25313) | HIGH — Addresses key practical limitation for real-world autonomous systems. | Mid (24G): Belief-state inference adds moderate overhead. |
| 8 | 2026-05-20 | [stable-worldmodel: A Platform for Reproducible World Modeling Res](https://arxiv.org/abs/2605.21800) | MEDIUM — Enables the broader world model ecosystem that JEPA is part of. | Small (8-12G): Designed to be accessible for researchers. |
| 9 | 2026-05-15 | [DiLA: Disentangled Latent Action World Models](https://arxiv.org/abs/2605.15725) | HIGH — Factorized control aligns with LeCun's modular agent architecture. | Mid (24G): Standard world model + disentanglement objectives. |
| 10 | 2026-05-10 | [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End ](https://arxiv.org/abs/2605.09241) | HIGH — Makes JEPA more practical and reliable. | Mid (24G): Adds regularization to existing JEPA. |
| 11 | 2026-05-05 | [Text-Conditional JEPA for Learning Semantically Rich Visual Repre](https://arxiv.org/abs/2605.03245) | MEDIUM — Extends JEPA but adds language which LeCun's vision treats as a separate module. | Large (40G+): Requires paired image-text data at scale. |
| 12 | 2026-04-03 | [Hierarchical Planning with Latent World Models](https://arxiv.org/abs/2604.03208) | HIGH — Directly implements LeCun's hierarchical planning vision. | Mid (24G): Two-level planning more efficient than flat. |
| 13 | 2026-03-20 | [Probing the Latent World: Emergent Discrete Symbols and Physical ](https://arxiv.org/abs/2603.20327) | MEDIUM — Tests a core assumption of LeCun's vision empirically. | Mid (24G): Probing experiments on pre-trained models. |
| 14 | 2026-03-15 | [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Lea](https://arxiv.org/abs/2603.14482) | HIGH — Meta FAIR. Addresses key limitation on path to full world models. | Large (40G+): Extended V-JEPA with dense heads. |
| 15 | 2026-03-13 | [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Archit](https://arxiv.org/abs/2603.19312) | HIGH — Likely LeCun's group. Name signals direct alignment. | Large (40G+): End-to-end pixel-to-latent training. |
| 16 | 2026-03-07 | [Dreamer-CDP: Improving Reconstruction-free World Models Via Conti](https://arxiv.org/abs/2603.07083) | MEDIUM — Moves Dreamer closer to LeCun's vision by eliminating reconstruction. | Mid (24G): More efficient than standard Dreamer. |
| 17 | 2026-03-05 | [Probabilistic Dreaming for World Models](https://arxiv.org/abs/2603.04715) | MEDIUM — Essential for safe deployment, though not directly addressed in LeCun's architecture. | Mid (24G): Adds probabilistic outputs to standard world model. |
| 18 | 2026-02-12 | [JEPA-VLA: Video Predictive Embedding is Needed for VLA Models](https://arxiv.org/abs/2602.11832) | HIGH — Demonstrates practical necessity of JEPA for embodied AI. | Large (40G+): Video JEPA + VLA fine-tuning. |
| 19 | 2026-01-29 | [Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation f](https://arxiv.org/abs/2601.22032) | HIGH — Validates JEPA in high-stakes real-world application. | Large (40G+): Driving video + trajectory model. |
| 20 | 2025-11-21 | [DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive A](https://arxiv.org/abs/2511.17354) | HIGH — Combines JEPA with energy-based learning, two pillars of LeCun's vision. | Mid (24G) |
| 21 | 2025-10-07 | [Gaussian Embeddings: How JEPAs Secretly Learn Your Data Density](https://arxiv.org/abs/2510.05949) | HIGH — Provides theoretical validation of JEPA's connection to energy-based models. | Small (8-12G): Theoretical analysis with small-scale experiments. |
| 22 | 2025-09-29 | [Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers](https://arxiv.org/abs/2509.24317) | MEDIUM — Makes JEPA more practical but doesn't advance the theoretical vision. | Mid (24G): Focus on reducing training cost. |
| 23 | 2025-06-11 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Pred](https://arxiv.org/abs/2506.09985) | HIGH — Meta FAIR flagship. Shows JEPA scales to full vision triad. | Large (40G+/Multi-card): Massive video transformer, Meta-scale compute. |
| 24 | 2024-10-25 | [Connecting Joint-Embedding Predictive Architecture with Contrasti](https://arxiv.org/abs/2410.19560) | HIGH — Theoretical work that strengthens the foundations of JEPA. | Small (8-12G): Theoretical paper with illustrative experiments. |
| 25 | 2024-08-14 | [CNN-JEPA: Self-Supervised Pretraining Convolutional Neural Networ](https://arxiv.org/abs/2408.07514) | MEDIUM — Extends JEPA to practical architectures for real-world deployment. | Mid (24G): CNN-based, more efficient than ViT JEPA. |
| 26 | 2024-05-06 | [Sora and V-JEPA Have Not Learned The Complete Real World Model --](https://arxiv.org/abs/2407.10311) | HIGH — Directly engages with LeCun's criteria for world models and finds current systems lacking. | N/A (philosophical analysis) |
| 27 | 2024-05-06 | [Is Sora a World Simulator? A Comprehensive Survey on General Worl](https://arxiv.org/abs/2405.03520) | HIGH — Provides the conceptual framework for evaluating progress toward LeCun's vision. | N/A (survey) |
| 28 | 2024-04-25 | [Point-JEPA: A Joint Embedding Predictive Architecture for Self-Su](https://arxiv.org/abs/2404.16432) | MEDIUM — Extends JEPA to 3D, a necessary modality for embodied world models. | Mid (24G): Point cloud processing on standard GPUs. |
| 29 | 2024-03-16 | [Dreaming of Many Worlds: Learning Contextual World Models Aids Ze](https://arxiv.org/abs/2403.10967) | MEDIUM — Addresses a key requirement for autonomous intelligence but uses Dreamer rather than JEPA. | Mid (24G) |
| 30 | 2024-03-08 | [Sora as a World Model? A Complete Survey on Text-to-Video Generat](https://arxiv.org/abs/2403.05131) | MEDIUM — Supports LeCun's argument that generative models != world models. | N/A (survey) |
| 31 | 2023-11-27 | [A-JEPA: Joint-Embedding Predictive Architecture Can Listen](https://arxiv.org/abs/2311.15830) | HIGH — Validates JEPA's generality, a key claim in LeCun's vision. | Mid (24G): Audio SSL on standard datasets. |
| 32 | 2023-09-29 | [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | MEDIUM — Powerful world model but uses generative approach LeCun considers inefficient. Important counterpoint. | Large (40G+/Multi-card): 4.6B parameter video diffusion. |
| 33 | 2023-07-24 | [MC-JEPA: A Joint-Embedding Predictive Architecture for Self-Super](https://arxiv.org/abs/2307.12698) | HIGH — Core JEPA extension to video, embodying modular world model concept. | Large (40G+): Video transformer on Something-Something-v2, Kinetics-400. |
| 34 | 2023-07-14 | [SafeDreamer: Safe Reinforcement Learning with World Models](https://arxiv.org/abs/2307.07176) | MEDIUM — Addresses a practical requirement for deployment. | Mid (24G): Adds safety constraints to standard Dreamer. |
| 35 | 2023-01-19 | [Self-Supervised Learning from Images with a Joint-Embedding Predi](https://arxiv.org/abs/2301.08243) | HIGH — Direct implementation of LeCun's core vision. | Large (40G+): ViT-H/14 on ImageNet-1K. |
| 36 | 2022-06-28 | [DayDreamer: World Models for Physical Robot Learning](https://arxiv.org/abs/2206.14176) | HIGH — Landmark empirical validation of learned world models on real robots. | Mid (24G): Training from real robot data on single GPU. |
| 37 | 2022-02-19 | [TransDreamer: Reinforcement Learning with Transformer World Model](https://arxiv.org/abs/2202.09481) | MEDIUM — Advances the transformer-based approach that JEPA later adopts. | Mid (24G) |

---

## 1. [2026-07-04] SiamJEPA: On the Role of Siamese Student Encoders in JEPA

- **arXiv**: [2607.04044](https://arxiv.org/abs/2607.04044)
- **Authors**: Makoto Yamada
- **Abstract**: Recently, Joint Embedding Predictive Architectures (JEPAs) have attracted significant attention in the computer vision and machine learning communities as a promising framework for self-supervised representation learning. Unlike masked autoencoders that reconstruct pixels, JEPA models learn representations by predicting latent embeddings of masked regions. Existing JEPA-based methods, such as I-JEPA and V-JEPA, typically employ a single encoder in the student network. In contrast, using Siamese encoders for student network is more naturally aligned with brain-inspired representation learning f
- **Compute Scale**: Mid (24G): Ablation studies on standard benchmarks.
- **LeCun Alignment**: HIGH — Theoretical validation of JEPA architecture.

### What / Why / Solve

- **Proposal**: SiamJEPA — Analyzes role of Siamese (weight-shared) student encoders in JEPA.
- **Motivation**: JEPA uses separate context/target encoders — is this necessary? Siamese simpler. Understanding this is crucial.
- **Problem Solved**: Theoretical analysis of encoder architecture choices in JEPA.

### Academic Context

- **Inheritance / Response**: Extends I-JEPA (2301.08243). Connects to BYOL/SimSiam SSL literature.
- **Implicit Connection**: Theoretical validation of ALL JEPA variants' core architectural choices.
- **Research Line**: JEPA Theory — architectural analysis and inductive biases.

- **Future Directions**: Apply findings to video/multimodal JEPA.
- **GitHub**: To be checked

---

## 2. [2026-06-30] AdaJEPA: An Adaptive Latent World Model

- **arXiv**: [2606.32026](https://arxiv.org/abs/2606.32026)
- **Authors**: Ying Wang, Oumayma Bounou, Yann LeCun, Mengye Ren
- **Abstract**: Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation sign
- **Compute Scale**: Mid (24G): Focus on efficiency.
- **LeCun Alignment**: HIGH — Adaptive computation key to efficient autonomous systems.

### What / Why / Solve

- **Proposal**: AdaJEPA — Adaptive latent world model with dynamic latent resolution based on task complexity.
- **Motivation**: Fixed-size latent spaces waste compute or lose information. Autonomous systems need adaptive representations.
- **Problem Solved**: Adaptive latent dimensionality — model learns WHEN to use more capacity.

### Academic Context

- **Inheritance / Response**: JEPA framework + efficient world model literature.
- **Implicit Connection**: Adaptive capacity aligns with LeCun's hierarchical planning — different abstraction levels need different capacities.
- **Research Line**: Efficient JEPA — reducing world model compute through adaptivity.

- **Future Directions**: Multi-level adaptive hierarchies; action-conditioned prediction.
- **GitHub**: To be checked

---

## 3. [2026-06-22] SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors

- **arXiv**: [2606.23444](https://arxiv.org/abs/2606.23444)
- **Authors**: Pratyaksh Rao, Wancong Zhang, Randall Balestriero, Yann LeCun, Giuseppe Loianno
- **Abstract**: Accurate dynamics models are critical for informed decision-making in robotic systems, particularly for agile aerial vehicles operating under uncertainty. Neural network dynamics models are attractive for capturing complex nonlinear effects, but existing predictive approaches struggle with long-horizon forecasting because their autoregressive rollout mechanism amplifies errors over time. Joint Embedding Predictive Architectures (JEPAs) offer a compelling alternative by modeling dynamics in latent space, yet prior JEPA-style methods for robot navigation have been studied primarily for kinematic
- **Compute Scale**: Large (40G+): Training + real-time drone inference.
- **LeCun Alignment**: HIGH — Direct JEPA application to physical robot control.

### What / Why / Solve

- **Proposal**: SkyJEPA — Long-horizon world model for zero-shot sim-to-real quadrotor control.
- **Motivation**: Sim-to-real transfer fundamental challenge. JEPA's latent-space prediction should be more transferable than pixel-space.
- **Problem Solved**: Zero-shot sim-to-real drone control using JEPA world model. Validates latent-space robustness.

### Academic Context

- **Inheritance / Response**: JEPA + Dreamer-style MBRL. Applies JEPA to sim-to-real robotics.
- **Implicit Connection**: First JEPA for real-world robotics control. Validates LeCun's argument about latent-space vs pixel-space prediction.
- **Research Line**: JEPA for Robotics — sim-to-real transfer via latent world models.

- **Future Directions**: Other robot platforms; multi-agent; longer horizons.
- **GitHub**: To be checked

---

## 4. [2026-06-17] S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Representation Learning

- **arXiv**: [2606.19398](https://arxiv.org/abs/2606.19398)
- **Authors**: Georgios Ioannides, Adrian Kieback, Judah Goldfeder, Linsey Pang, Aman Chadha, Aaron Elkins, Yann LeCun, Ravid Shwartz-Ziv
- **Abstract**: Self-supervised speech encoders are predominantly trained by predicting discrete hard cluster IDs at masked positions, a recipe that collapses acoustic ambiguity at category boundaries and requires interrupting training to re-cluster the entire corpus between iterations. We introduce S-JEPA, a JEPA-style encoder-predictor pair trained to match the soft posteriors of a Gaussian Mixture Model at masked positions via KL divergence. Training runs as one continuous optimization trajectory in two phases: a fixed GMM over MFCC features, then an online GMM over encoder features, with the input layer s
- **Compute Scale**: Mid (24G): LibriSpeech-scale.
- **LeCun Alignment**: MEDIUM — Expands JEPA generality.

### What / Why / Solve

- **Proposal**: S-JEPA — Soft Clustering Anchors for self-supervised speech representation learning.
- **Motivation**: JEPA unexplored in speech. Speech has unique temporal structure requiring modality-specific adaptation.
- **Problem Solved**: First thorough JEPA for speech SSL with soft clustering as target representations.

### Academic Context

- **Inheritance / Response**: I-JEPA + A-JEPA. Extends JEPA to speech.
- **Implicit Connection**: With A-JEPA, establishes JEPA as general-purpose SSL beyond vision.
- **Research Line**: Multimodal JEPA — extending to speech/audio.

- **Future Directions**: Joint audio-visual JEPA; dialogue systems.
- **GitHub**: To be checked

---

## 5. [2026-06-14] You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences

- **arXiv**: [2606.15956](https://arxiv.org/abs/2606.15956)
- **Authors**: Ninad Daithankar, Alexi Gladstone, Yann LeCun, Heng Ji
- **Abstract**: Progress in AI has largely been driven by methods that assume less. As compute and data increase, approaches with weaker inductive biases generally outperform those with stronger assumptions. This is particularly characteristic of the field of Visual Representation Learning, where approaches have gone from being dominated by Supervised Learning, to Weakly Supervised Learning, to the now widespread success of Self-Supervised Learning without human labels. Yet, even modern Self-Supervised Learning approaches still depend on strong inductive biases such as augmentations, masking, or cropping. If 
- **Compute Scale**: Mid (24G)
- **LeCun Alignment**: HIGH — Explores a potentially simpler path to the same world model goal.

### What / Why / Solve

- **Proposal**: Visual representation learning via temporal differences — uses the difference between consecutive frames as a self-supervised signal, without explicit JEPA-style masking.
- **Motivation**: JEPA and masked prediction require complex masking strategies. Temporal differences provide a simpler, naturally-occurring supervisory signal that captures motion and change.
- **Problem Solved**: Simplifies self-supervised visual learning by using temporal differences instead of spatial masking. Maintains JEPA-like efficiency without architectural complexity.

### Academic Context

- **Inheritance / Response**: Connects to JEPA through the predictive objective in latent space, but replaces masking with temporal difference. Related to temporal SSL methods.
- **Implicit Connection**: This paper explores whether the masking mechanism is essential to JEPA or whether ANY predictive objective works. If temporal differences suffice, it simplifies world model training significantly.
- **Research Line**: Alternative JEPA Objectives — exploring different predictive signals beyond masking.

- **Future Directions**: Combine temporal differences with masking; apply to action-conditioned prediction.
- **GitHub**: To be checked

---

## 6. [2026-05-25] When Does LeJEPA Learn a World Model?

- **arXiv**: [2605.26379](https://arxiv.org/abs/2605.26379)
- **Authors**: David Klindt, Yann LeCun, Randall Balestriero
- **Abstract**: A representation that scrambles the true degrees of freedom of the world cannot support reliable planning or compositional generalization. We prove that LeJEPA (alignment plus Gaussian regularization) linearly recovers the world's latent variables from nonlinear observations, a property known as linear identifiability, in a broad class of worlds where latents evolve under stationary, additive-noise transitions. Our main result is that among all such worlds, the Gaussian is the unique latent distribution for which this guarantee holds. The forward direction rests on a spectral decomposition in 
- **Compute Scale**: Mid (24G): Controlled analytical experiments.
- **LeCun Alignment**: HIGH — Directly investigates whether JEPA fulfills LeCun's world model vision.

### What / Why / Solve

- **Proposal**: When Does LeJEPA Learn a World Model? — Theoretical/empirical analysis of conditions for JEPA to encode world model capabilities.
- **Motivation**: JEPA predicts latent representations — but does that mean it learns a world model? Gap between objective and capability.
- **Problem Solved**: Identifies necessary conditions for JEPA to function as actual world model vs. feature extractor.

### Academic Context

- **Inheritance / Response**: Analyzes I-JEPA/LeWorldModel. Connects to SSL theory.
- **Implicit Connection**: CRITICAL paper for entire JEPA program. Asks THE fundamental question: when does JEPA become a world model?
- **Research Line**: JEPA Theory — conditions for emergent world model capabilities.

- **Future Directions**: Architectural inductive biases for world model emergence; convergence guarantees.
- **GitHub**: To be checked

---

## 7. [2026-05-25] UWM-JEPA: Predictive World Models That Imagine in Belief Space

- **arXiv**: [2605.25313](https://arxiv.org/abs/2605.25313)
- **Authors**: Santosh Kumar Radha, Oktay Goktas
- **Abstract**: World models for partially observed environments must imagine multiple compatible hidden futures and steer between them under counterfactual actions. Joint Embedding Predictive Architectures (JEPAs) do this in latent space, but a vector-valued latent has no internal structure for carrying the belief over hidden continuations through blind rollout. We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. The construction preserves the joint-state spectrum exactly during rollout, so 
- **Compute Scale**: Mid (24G): Belief-state inference adds moderate overhead.
- **LeCun Alignment**: HIGH — Addresses key practical limitation for real-world autonomous systems.

### What / Why / Solve

- **Proposal**: UWM-JEPA — Predictive world models in belief space for partially observable environments.
- **Motivation**: Real environments partially observable. JEPA must handle uncertainty. Belief-space prediction enables robust POMDP planning.
- **Problem Solved**: Extends JEPA world models to partially observable settings via belief-state representations.

### Academic Context

- **Inheritance / Response**: I-JEPA + Dreamer + POMDP/belief-state RL.
- **Implicit Connection**: Belief-space prediction essential for real-world robotics with noisy/occluded sensors. Connects JEPA to embodied AI challenges.
- **Research Line**: Robust JEPA — partial observability in world models.

- **Future Directions**: Active information gathering; multi-agent belief-space planning.
- **GitHub**: To be checked

---

## 8. [2026-05-20] stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation

- **arXiv**: [2605.21800](https://arxiv.org/abs/2605.21800)
- **Authors**: Lucas Maes, Quentin Le Lidec, Luiz Facury, Nassim Massaudi, Ayush Chaurasia, Francesco Capuano, Richard Gao, Taj Gillin et al.
- **Abstract**: World models are central to building agents that can reason, plan, and generalize beyond their training data. However, research on world models is currently fragmented, with disparate codebases, data pipelines, and evaluation protocols hindering reproducibility and fair comparison. Current practice is further limited by three key bottlenecks: fragile one-off codebases, slow video data loading, and the lack of standardized generalization benchmarks. We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation. It delivers (
- **Compute Scale**: Small (8-12G): Designed to be accessible for researchers.
- **LeCun Alignment**: MEDIUM — Enables the broader world model ecosystem that JEPA is part of.

### What / Why / Solve

- **Proposal**: Stable-worldmodel — A standardized platform for reproducible world modeling research. Provides benchmarks, metrics, and implementations of major world model architectures (Dreamer, TD-MPC, etc.).
- **Motivation**: World model research suffers from reproducibility issues — different papers use different environments, metrics, and baselines. A standardized benchmark is essential for the field to make progress.
- **Problem Solved**: Creates a common evaluation framework for world models. Enables fair comparison across architectures and accelerates research iteration.

### Academic Context

- **Inheritance / Response**: Builds on the world model literature (Dreamer, TD-MPC, MuZero). Similar in spirit to other ML benchmarks like Gymnasium, DMControl.
- **Implicit Connection**: As a benchmark, this paper affects ALL world model research. It could become the standard for measuring progress toward LeCun's vision, including JEPA-based approaches.
- **Research Line**: Infrastructure/Benchmark — enabling reproducible world model research.

- **Future Directions**: Include JEPA-based models; add real-world robotics benchmarks; community-driven evaluation.
- **GitHub**: To be checked

---

## 9. [2026-05-15] DiLA: Disentangled Latent Action World Models

- **arXiv**: [2605.15725](https://arxiv.org/abs/2605.15725)
- **Authors**: Tianqiu Zhang, Muyang Lyu, Yufan Zhang, Fang Fang, Si Wu
- **Abstract**: Latent Action Models (LAMs) enable the learning of world models from unlabeled video by inferring abstract actions between consecutive frames. However, LAMs face a fundamental trade-off between action abstraction and generation fidelity. Existing methods typically circumvent this issue by using two-stage training with pre-trained world models or by limiting predictions to optical flow. In this paper, we introduce DiLA, a novel Disentangled Latent Action world model that aims to resolve this trade-off via content-structure disentanglement. Our key insight is that disentanglement and latent acti
- **Compute Scale**: Mid (24G): Standard world model + disentanglement objectives.
- **LeCun Alignment**: HIGH — Factorized control aligns with LeCun's modular agent architecture.

### What / Why / Solve

- **Proposal**: DiLA — Disentangled Latent Action world models. Factorizes action space into independent control components.
- **Motivation**: Monolithic action spaces conflate different behaviors. LeCun's hierarchy needs factorized control.
- **Problem Solved**: Interpretable, factorized action representations enabling compositional control.

### Academic Context

- **Inheritance / Response**: Dreamer + disentanglement literature.
- **Implicit Connection**: Disentangled actions complement JEPA's factorized representations — together enable modular world models.
- **Research Line**: Latent Action — factorizing action representations in world models.

- **Future Directions**: Compositional task learning; zero-shot action transfer.
- **GitHub**: To be checked

---

## 10. [2026-05-10] Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models

- **arXiv**: [2605.09241](https://arxiv.org/abs/2605.09241)
- **Authors**: Kai Zhao, Dongliang Nie, Yuchen Lin, Zhehan Luo, Yixiao Gu, Deng-Ping Fan, Dan Zeng
- **Abstract**: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be alleviated bysimply constraining latent embeddings with an isotropic Gaussian prior.However, latent representations inherently lie on low-dimensional manifoldswithin a high-dimensional ambient space, and e
- **Compute Scale**: Mid (24G): Adds regularization to existing JEPA.
- **LeCun Alignment**: HIGH — Makes JEPA more practical and reliable.

### What / Why / Solve

- **Proposal**: Sub-JEPA — Subspace Gaussian Regularization for stable end-to-end world models.
- **Motivation**: JEPA training unstable — predictor can collapse. Stop-gradient/EMA are heuristics. Need principled solution.
- **Problem Solved**: Principled, theoretically-grounded solution to representation collapse. Eliminates stop-gradient hacks.

### Academic Context

- **Inheritance / Response**: I-JEPA + SSL collapse prevention literature.
- **Implicit Connection**: If adopted, simplifies ALL JEPA training. Infrastructure-level improvement for entire research line.
- **Research Line**: Stable JEPA — reliable JEPA convergence techniques.

- **Future Directions**: Video/multimodal JEPA application; theoretical analysis.
- **GitHub**: To be checked

---

## 11. [2026-05-05] Text-Conditional JEPA for Learning Semantically Rich Visual Representations

- **arXiv**: [2605.03245](https://arxiv.org/abs/2605.03245)
- **Authors**: Chen Huang, Xianhang Li, Vimal Thilak, Etai Littwin, Josh Susskind
- **Abstract**: Image-based Joint-Embedding Predictive Architecture (I-JEPA) offers a promising approach to visual self-supervised learning through masked feature prediction. However with the inherent visual uncertainty at masked positions, feature prediction remains challenging and may fail to learn semantic representations. In this work, we propose Text-Conditional JEPA (TC-JEPA) that uses image captions to reduce the prediction uncertainty. Specifically, we modulate the predicted patch features using a fine-grained text conditioner that computes sparse cross-attention over input text tokens. With such cond
- **Compute Scale**: Large (40G+): Requires paired image-text data at scale.
- **LeCun Alignment**: MEDIUM — Extends JEPA but adds language which LeCun's vision treats as a separate module.

### What / Why / Solve

- **Proposal**: Text-Conditional JEPA — Extends JEPA to learn semantically rich visual representations conditioned on text descriptions. The predictor network takes both visual context AND text as input.
- **Motivation**: Pure visual JEPA learns representations based on visual similarity, not semantic meaning. Text conditioning grounds visual representations in language, making them more useful for downstream tasks.
- **Problem Solved**: Enables JEPA-style self-supervised learning with semantic grounding. The learned representations capture both visual and linguistic structure.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and multimodal learning (CLIP, etc.). Adds language conditioning to the JEPA predictor.
- **Implicit Connection**: This connects JEPA to the multimodal foundation model paradigm. It shows that JEPA can incorporate language without losing its predictive advantages. Related to JEPA-VLA which also bridges vision and language for action.
- **Research Line**: Multimodal JEPA — grounding visual JEPA with language.

- **Future Directions**: Joint video-text JEPA; language-guided planning in world models.
- **GitHub**: To be checked

---

## 12. [2026-04-03] Hierarchical Planning with Latent World Models

- **arXiv**: [2604.03208](https://arxiv.org/abs/2604.03208)
- **Authors**: Wancong Zhang, Basile Terver, Artem Zholus, Soham Chitnis, Harsh Sutaria, Mido Assran, Randall Balestriero, Amir Bar et al.
- **Abstract**: World models are a promising path to zero-shot embodied control through planning. However, existing world model planners struggle on long-horizon, multi-stage tasks: prediction errors compound and naive search is exponential in the planning horizon. Hierarchy mitigates both by decomposing tasks into shorter, tractable subproblems; yet prior hierarchical approaches either amortize control into task-specific policies (hierarchical RL) or assume low-dimensional states and known dynamics (classical hierarchical MPC). We present Hierarchical Planning with Latent World Models (HWM), an architecture 
- **Compute Scale**: Mid (24G): Two-level planning more efficient than flat.
- **LeCun Alignment**: HIGH — Directly implements LeCun's hierarchical planning vision.

### What / Why / Solve

- **Proposal**: Hierarchical planning with latent world models — High-level subgoal setting + low-level execution in latent space.
- **Motivation**: Long-horizon tasks require hierarchical decomposition — exactly LeCun's architecture calls for this.
- **Problem Solved**: Long-horizon planning via hierarchical decomposition in latent space.

### Academic Context

- **Inheritance / Response**: JEPA + hierarchical RL. Direct implementation of LeCun's hierarchical planner.
- **Implicit Connection**: Closest implementation of LeCun's full architecture. Subgoal setting in latent space = LeCun's 'configurator' module.
- **Research Line**: Hierarchical WAM — multi-level planning in latent world models.

- **Future Directions**: More levels; learned subgoals; real robot integration.
- **GitHub**: To be checked

---

## 13. [2026-03-20] Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations

- **arXiv**: [2603.20327](https://arxiv.org/abs/2603.20327)
- **Authors**: Liu hung ming
- **Abstract**: Video world models trained with Joint Embedding Predictive Architectures (JEPA) acquire rich spatiotemporal representations by predicting masked regions in latent space rather than reconstructing pixels. This removes the visual verification pathway of generative models, creating a structural interpretability gap: the encoder has learned physical structure inaccessible in any inspectable form. Existing probing methods either operate in continuous space without a structured intermediate layer, or attach generative components whose parameters confound attribution of behavior to the encoder.
  We 
- **Compute Scale**: Mid (24G): Probing experiments on pre-trained models.
- **LeCun Alignment**: MEDIUM — Tests a core assumption of LeCun's vision empirically.

### What / Why / Solve

- **Proposal**: Probing the Latent World — Investigates whether latent representations in video models (including JEPA) spontaneously develop discrete symbolic structure and physical understanding.
- **Motivation**: LeCun's vision requires that world models develop abstract, symbolic-like representations. But does this actually happen in practice? This paper probes whether latent spaces contain interpretable structure.
- **Problem Solved**: Provides empirical evidence about the emergence of symbolic structure in latent world models. Validates (or challenges) a core assumption of the JEPA research program.

### Academic Context

- **Inheritance / Response**: Builds on probing methodology from NLP and the video SSL literature. Directly tests claims made in LeCun's vision paper.
- **Implicit Connection**: This paper is a REALITY CHECK on the entire JEPA research program. If latent spaces DON'T develop symbolic structure, the path to autonomous intelligence needs rethinking. If they DO, it validates the approach.
- **Research Line**: JEPA Interpretability — understanding what latent world models actually learn.

- **Future Directions**: Inducing symbolic structure through architectural priors; causal probing.
- **GitHub**: To be checked

---

## 14. [2026-03-15] V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning

- **arXiv**: [2603.14482](https://arxiv.org/abs/2603.14482)
- **Authors**: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas et al.
- **Abstract**: We present V-JEPA 2.1, a family of self-supervised models that learn dense, high-quality visual representations for both images and videos while retaining strong global scene understanding. The approach combines four key components. First, a dense predictive loss uses a masking-based objective in which both visible and masked tokens contribute to the training signal, encouraging explicit spatial and temporal grounding. Second, deep self-supervision applies the self-supervised objective hierarchically across multiple intermediate encoder layers to improve representation quality. Third, multi-mo
- **Compute Scale**: Large (40G+): Extended V-JEPA with dense heads.
- **LeCun Alignment**: HIGH — Meta FAIR. Addresses key limitation on path to full world models.

### What / Why / Solve

- **Proposal**: V-JEPA 2.1 — Unlocks dense features in video SSL for fine-grained understanding.
- **Motivation**: V-JEPA sparse features insufficient for segmentation/tracking/depth. World model needs DENSE spatial understanding.
- **Problem Solved**: Extends JEPA from sparse to dense spatial representations.

### Academic Context

- **Inheritance / Response**: Iterative improvement of V-JEPA 2 (2506.09985).
- **Implicit Connection**: Dense features connect JEPA to object detection/tracking — essential for robotic world models.
- **Research Line**: Video JEPA — dense feature iteration for practical vision tasks.

- **Future Directions**: Dense JEPA for robotics; real-time dense prediction; 3D integration.
- **GitHub**: Meta FAIR

---

## 15. [2026-03-13] LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

- **arXiv**: [2603.19312](https://arxiv.org/abs/2603.19312)
- **Authors**: Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
- **Abstract**: Joint Embedding Predictive Architectures (JEPAs) offer a compelling framework for learning world models in compact latent spaces, yet existing methods remain fragile, relying on complex multi-term losses, exponential moving averages, pre-trained encoders, or auxiliary supervision to avoid representation collapse. In this work, we introduce LeWorldModel (LeWM), the first JEPA that trains stably end-to-end from raw pixels using only two loss terms: a next-embedding prediction loss and a regularizer enforcing Gaussian-distributed latent embeddings. This reduces tunable loss hyperparameters from s
- **Compute Scale**: Large (40G+): End-to-end pixel-to-latent training.
- **LeCun Alignment**: HIGH — Likely LeCun's group. Name signals direct alignment.

### What / Why / Solve

- **Proposal**: LeWorldModel — Stable end-to-end JEPA from pixels. Complete world model mapping raw pixels→latent→future prediction.
- **Motivation**: Existing world models use reconstruction objectives. JEPA alternative unstable end-to-end. Need stable JEPA world model.
- **Problem Solved**: First stable end-to-end JEPA world model from raw pixels, no reconstruction.

### Academic Context

- **Inheritance / Response**: I-JEPA (2301.08243) + Dreamer. Name directly references LeCun.
- **Implicit Connection**: Most direct implementation of LeCun's complete architecture. Bridges JEPA (SSL) with model-based RL (Dreamer).
- **Research Line**: End-to-end JEPA World Model — realizes full JEPA-based world model vision.

- **Future Directions**: Complex environments; action-conditioned prediction; real-world robotics.
- **GitHub**: Meta FAIR (likely)

---

## 16. [2026-03-07] Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction

- **arXiv**: [2603.07083](https://arxiv.org/abs/2603.07083)
- **Authors**: Michael Hauri, Friedemann Zenke
- **Abstract**: Model-based reinforcement learning (MBRL) agents operating in high-dimensional observation spaces, such as Dreamer, rely on learning abstract representations for effective planning and control. Existing approaches typically employ reconstruction-based objectives in the observation space, which can render representations sensitive to task-irrelevant details. Recent alternatives trade reconstruction for auxiliary action prediction heads or view augmentation strategies, but perform worse in the Crafter environment than reconstruction-based methods. We close this gap between Dreamer and reconstruc
- **Compute Scale**: Mid (24G): More efficient than standard Dreamer.
- **LeCun Alignment**: MEDIUM — Moves Dreamer closer to LeCun's vision by eliminating reconstruction.

### What / Why / Solve

- **Proposal**: Dreamer-CDP — Continuous Deterministic Representation Prediction. Improves Dreamer-style world models by replacing stochastic latent states with continuous deterministic representations, eliminating the need for reconstruction losses.
- **Motivation**: Dreamer uses stochastic latent states and reconstruction-based objectives. Reconstruction wastes capacity on irrelevant pixels. Continuous deterministic representations are more efficient and align with JEPA's philosophy.
- **Problem Solved**: Improves Dreamer's sample efficiency by removing reconstruction losses. Moves Dreamer closer to JEPA's non-generative philosophy.

### Academic Context

- **Inheritance / Response**: Builds on Dreamer (Hafner et al.) and JEPA principles. Bridges the gap between Dreamer and JEPA.
- **Implicit Connection**: Dreamer-CDP represents a CONVERGENCE between the Dreamer and JEPA research lines. Both are moving toward reconstruction-free, latent-space prediction. This is a key trend in the field.
- **Research Line**: Convergent World Models — merging Dreamer and JEPA approaches.

- **Future Directions**: Full integration with JEPA-style architectures; application to real robots.
- **GitHub**: To be checked

---

## 17. [2026-03-05] Probabilistic Dreaming for World Models

- **arXiv**: [2603.04715](https://arxiv.org/abs/2603.04715)
- **Authors**: Gavin Wong
- **Abstract**: "Dreaming" enables agents to learn from imagined experiences, enabling more robust and sample-efficient learning of world models. In this work, we consider innovations to the state-of-the-art Dreamer model using probabilistic methods that enable: (1) the parallel exploration of many latent states; and (2) maintaining distinct hypotheses for mutually exclusive futures while retaining the desirable gradient properties of continuous latents. Evaluating on the MPE SimpleTag domain, our method outperforms standard Dreamer with a 4.5% score improvement and 28% lower variance in episode returns. We a
- **Compute Scale**: Mid (24G): Adds probabilistic outputs to standard world model.
- **LeCun Alignment**: MEDIUM — Essential for safe deployment, though not directly addressed in LeCun's architecture.

### What / Why / Solve

- **Proposal**: Probabilistic Dreaming — Adds uncertainty quantification to world model predictions. The model outputs distributions over future states rather than point estimates.
- **Motivation**: World models make mistakes, especially on out-of-distribution inputs. An autonomous agent needs to KNOW when its predictions are uncertain to avoid dangerous actions.
- **Problem Solved**: Enables calibrated uncertainty in world model predictions. The agent can use prediction confidence to decide when to trust the model vs. gather more data.

### Academic Context

- **Inheritance / Response**: Builds on Dreamer and uncertainty quantification literature. Addresses a known limitation of deterministic world models.
- **Implicit Connection**: Uncertainty-aware world models are essential for SAFE autonomous systems. This connects to LeCun's 'cost' module which must evaluate the reliability of predictions before acting on them.
- **Research Line**: Robust World Models — uncertainty and safety in model-based RL.

- **Future Directions**: Active learning with uncertainty; risk-aware planning.
- **GitHub**: To be checked

---

## 18. [2026-02-12] JEPA-VLA: Video Predictive Embedding is Needed for VLA Models

- **arXiv**: [2602.11832](https://arxiv.org/abs/2602.11832)
- **Authors**: Shangchen Miao, Ningya Feng, Jialong Wu, Ye Lin, Xu He, Dong Li, Mingsheng Long
- **Abstract**: Recent vision-language-action (VLA) models built upon pretrained vision-language models (VLMs) have achieved significant improvements in robotic manipulation. However, current VLAs still suffer from low sample efficiency and limited generalization. This paper argues that these limitations are closely tied to an overlooked component, pretrained visual representation, which offers insufficient knowledge on both aspects of environment understanding and policy prior. Through an in-depth analysis, we find that commonly used visual representations in VLAs, whether pretrained via language-image contr
- **Compute Scale**: Large (40G+): Video JEPA + VLA fine-tuning.
- **LeCun Alignment**: HIGH — Demonstrates practical necessity of JEPA for embodied AI.

### What / Why / Solve

- **Proposal**: JEPA-VLA — Video predictive embedding is necessary for Vision-Language-Action models in robotics.
- **Motivation**: Current VLA models use static image features, losing temporal dynamics. Video JEPA provides temporally-aware representations.
- **Problem Solved**: Demonstrates video JEPA features significantly improve VLA performance on real robot tasks.

### Academic Context

- **Inheritance / Response**: V-JEPA + VLA models (RT-2, Octo). Bridges video SSL and robot learning.
- **Implicit Connection**: Directly connects JEPA to robot foundation models. Makes case that LeCun's vision is practically NECESSARY for robotics.
- **Research Line**: Embodied JEPA — JEPA representations for robot learning and control.

- **Future Directions**: Streaming video JEPA for real-time VLA; multi-embodiment transfer.
- **GitHub**: To be checked

---

## 19. [2026-01-29] Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving

- **arXiv**: [2601.22032](https://arxiv.org/abs/2601.22032)
- **Authors**: Linhan Wang, Zichong Yang, Chen Bai, Guoxiang Zhang, Xiaotong Liu, Xiaoyin Zheng, Xiao-Xiao Long, Chang-Tien Lu et al.
- **Abstract**: End-to-end autonomous driving increasingly leverages self-supervised video pretraining to learn transferable planning representations. However, pretraining video world models for scene understanding has so far brought only limited improvements. This limitation is compounded by the inherent ambiguity of driving: each scene typically provides only a single human trajectory, making it difficult to learn multimodal behaviors. In this work, we propose Drive-JEPA, a framework that integrates Video Joint-Embedding Predictive Architecture (V-JEPA) with multimodal trajectory distillation for end-to-end
- **Compute Scale**: Large (40G+): Driving video + trajectory model.
- **LeCun Alignment**: HIGH — Validates JEPA in high-stakes real-world application.

### What / Why / Solve

- **Proposal**: Drive-JEPA — Video JEPA meets multimodal trajectory distillation for end-to-end autonomous driving.
- **Motivation**: Autonomous driving requires structured world understanding. Video JEPA provides temporal representations for trajectory prediction.
- **Problem Solved**: Improves driving trajectory prediction by incorporating video JEPA features.

### Academic Context

- **Inheritance / Response**: V-JEPA + trajectory prediction. Applies JEPA to autonomous driving.
- **Implicit Connection**: With GAIA-1, establishes world models for driving. JEPA-based alternative to generative approaches.
- **Research Line**: JEPA for Autonomous Driving — world models for vehicle behavior prediction.

- **Future Directions**: Interactive prediction; multi-agent driving JEPA.
- **GitHub**: To be checked

---

## 20. [2025-11-21] DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture

- **arXiv**: [2511.17354](https://arxiv.org/abs/2511.17354)
- **Authors**: Xiangteng He, Shunsuke Sakai, Shivam Chandhok, Sara Beery, Kun Yuan, Nicolas Padoy, Tatsuhito Hasegawa, Leonid Sigal
- **Abstract**: Recent advances in self-supervised visual representation learning have demonstrated the effectiveness of predictive latent-space objectives for learning transferable features. In particular, Image-based Joint-Embedding Predictive Architecture (I-JEPA) learns representations by predicting latent embeddings of masked target regions from visible context. However, it predicts target regions in parallel and all at once, lacking ability to order predictions meaningfully. Inspired by human visual perception, which attends selectively and progressively from primary to secondary cues, we propose DSeq-J
- **Compute Scale**: Mid (24G)
- **LeCun Alignment**: HIGH — Combines JEPA with energy-based learning, two pillars of LeCun's vision.

### What / Why / Solve

- **Proposal**: DSeq-JEPA — Discriminative Sequential JEPA. Extends JEPA to sequential data by making it discriminative (distinguishing real from fake sequences) rather than purely predictive.
- **Motivation**: Standard JEPA predicts one future state. Sequential prediction requires modeling multiple timesteps. A discriminative approach (real vs. fake sequences) is more stable than multi-step prediction.
- **Problem Solved**: Enables JEPA to handle sequential/temporal data with a more stable training objective. Bridges JEPA and contrastive/energy-based approaches.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and energy-based models. The discriminative aspect connects to LeCun's earlier work on energy-based learning.
- **Implicit Connection**: DSeq-JEPA represents a synthesis of JEPA and energy-based models — two of LeCun's key ideas. This convergence suggests a unified framework may be emerging.
- **Research Line**: Sequential JEPA — handling temporal data with discriminative objectives.

- **Future Directions**: Long-sequence modeling; integration with action-conditioned prediction.
- **GitHub**: To be checked

---

## 21. [2025-10-07] Gaussian Embeddings: How JEPAs Secretly Learn Your Data Density

- **arXiv**: [2510.05949](https://arxiv.org/abs/2510.05949)
- **Authors**: Randall Balestriero, Nicolas Ballas, Mike Rabbat, Yann LeCun
- **Abstract**: Joint Embedding Predictive Architectures (JEPAs) learn representations able to solve numerous downstream tasks out-of-the-box. JEPAs combine two objectives: (i) a latent-space prediction term, i.e., the representation of a slightly perturbed sample must be predictable from the original sample's representation, and (ii) an anti-collapse term, i.e., not all samples should have the same representation. While (ii) is often considered as an obvious remedy to representation collapse, we uncover that JEPAs' anti-collapse term does much more--it provably estimates the data density. In short, any succe
- **Compute Scale**: Small (8-12G): Theoretical analysis with small-scale experiments.
- **LeCun Alignment**: HIGH — Provides theoretical validation of JEPA's connection to energy-based models.

### What / Why / Solve

- **Proposal**: Gaussian Embeddings — Reveals that JEPA representations implicitly learn the data density. The latent space organizes as a Gaussian mixture where each component corresponds to a semantic cluster.
- **Motivation**: Understanding WHAT JEPA learns is crucial. If JEPA just learns data density, it's essentially doing density estimation, not world modeling. This paper investigates this question theoretically.
- **Problem Solved**: Provides theoretical insight into JEPA's learning dynamics. Shows that JEPA representations capture both semantic structure AND data density.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and representation learning theory.
- **Implicit Connection**: This paper connects JEPA to energy-based models: if representations follow a Gaussian mixture, the predictor is implicitly estimating an energy function. This validates LeCun's intuition about the connection between JEPA and EBMs.
- **Research Line**: JEPA Theory — understanding what JEPA representations encode.

- **Future Directions**: Leverage density estimates for uncertainty quantification; density-aware planning.
- **GitHub**: To be checked

---

## 22. [2025-09-29] Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers

- **arXiv**: [2509.24317](https://arxiv.org/abs/2509.24317)
- **Authors**: Xianhang Li, Chen Huang, Chun-Liang Li, Eran Malach, Josh Susskind, Vimal Thilak, Etai Littwin
- **Abstract**: Video Joint Embedding Predictive Architectures (V-JEPA) learn generalizable off-the-shelf video representation by predicting masked regions in latent space with an exponential moving average (EMA)-updated teacher. While EMA prevents representation collapse, it complicates scalable model selection and couples teacher and student architectures. We revisit masked-latent prediction and show that a frozen teacher suffices. Concretely, we (i) train a target encoder with a simple pixel-reconstruction o
- **Compute Scale**: Mid (24G): Focus on reducing training cost.
- **LeCun Alignment**: MEDIUM — Makes JEPA more practical but doesn't advance the theoretical vision.

### What / Why / Solve

- **Proposal**: Rethinking JEPA — Proposes compute-efficient video SSL by freezing the teacher (target) encoder after initial training, dramatically reducing the computational cost of JEPA training.
- **Motivation**: JEPA's dual-encoder architecture doubles the computational cost compared to single-encoder methods. For video, this cost is prohibitive. Freezing the teacher reduces cost without significant performance loss.
- **Problem Solved**: Reduces JEPA training cost for video by ~40% while maintaining representation quality. Makes video JEPA practical for researchers with limited compute.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and V-JEPA. The frozen teacher idea comes from self-distillation methods.
- **Implicit Connection**: If frozen teachers work well, it simplifies JEPA deployment significantly. This could make JEPA-based world models accessible to smaller labs, accelerating the entire field.
- **Research Line**: Efficient JEPA — reducing compute requirements for practical adoption.

- **Future Directions**: Adaptive teacher updating; apply frozen teacher to other JEPA variants.
- **GitHub**: To be checked

---

## 23. [2025-06-11] V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- **arXiv**: [2506.09985](https://arxiv.org/abs/2506.09985)
- **Authors**: Mido Assran, Adrien Bardes, David Fan, Quentin Garrido, Russell Howes,  Mojtaba,  Komeili, Matthew Muckley et al.
- **Abstract**: A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on 
- **Compute Scale**: Large (40G+/Multi-card): Massive video transformer, Meta-scale compute.
- **LeCun Alignment**: HIGH — Meta FAIR flagship. Shows JEPA scales to full vision triad.

### What / Why / Solve

- **Proposal**: V-JEPA 2 — Self-supervised video models enabling understanding, prediction, and planning at scale.
- **Motivation**: Previous V-JEPA limited in scale. Full vision requires understanding + prediction + planning from same representation.
- **Problem Solved**: Demonstrates single video JEPA supports all three pillars simultaneously.

### Academic Context

- **Inheritance / Response**: Scales V-JEPA (2024). Lineage from I-JEPA, MC-JEPA, LeCun vision paper.
- **Implicit Connection**: Prediction and planning capabilities bridge to WAM — V-JEPA 2 is essentially a queryable world model.
- **Research Line**: Video JEPA — the scaling story. Establishes video JEPA as backbone for autonomous systems.

- **Future Directions**: Real-time planning; action model integration; open-world video understanding.
- **GitHub**: Meta FAIR

---

## 24. [2024-10-25] Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning

- **arXiv**: [2410.19560](https://arxiv.org/abs/2410.19560)
- **Authors**: Shentong Mo, Shengbang Tong
- **Abstract**: In recent advancements in unsupervised visual representation learning, the Joint-Embedding Predictive Architecture (JEPA) has emerged as a significant method for extracting visual features from unlabeled imagery through an innovative masking strategy. Despite its success, two primary limitations have been identified: the inefficacy of Exponential Moving Average (EMA) from I-JEPA in preventing entire collapse and the inadequacy of I-JEPA prediction in accurately learning the mean of patch represe
- **Compute Scale**: Small (8-12G): Theoretical paper with illustrative experiments.
- **LeCun Alignment**: HIGH — Theoretical work that strengthens the foundations of JEPA.

### What / Why / Solve

- **Proposal**: Connecting JEPA with Contrastive SSL — Provides a theoretical bridge showing that JEPA and contrastive learning are two ends of a spectrum, with JEPA corresponding to a specific form of contrastive learning in latent space.
- **Motivation**: JEPA and contrastive learning are often presented as competing paradigms. Understanding their relationship helps unify the self-supervised learning field and reveals design choices.
- **Problem Solved**: Establishes a theoretical connection between JEPA and contrastive learning. Shows that JEPA can be understood as a form of contrastive learning where the negative samples are implicit.

### Academic Context

- **Inheritance / Response**: Builds on the contrastive learning literature (SimCLR, MoCo) and JEPA (2301.08243).
- **Implicit Connection**: If JEPA IS contrastive learning in latent space, it suggests that future improvements to either paradigm could benefit the other. This unification is important for the theoretical foundations of the field.
- **Research Line**: SSL Theory — understanding the relationships between self-supervised learning paradigms.

- **Future Directions**: Unified SSL framework; optimal transport perspective on JEPA.
- **GitHub**: To be checked

---

## 25. [2024-08-14] CNN-JEPA: Self-Supervised Pretraining Convolutional Neural Networks Using Joint Embedding Predictive Architecture

- **arXiv**: [2408.07514](https://arxiv.org/abs/2408.07514)
- **Authors**: András Kalapos, Bálint Gyires-Tóth
- **Abstract**: Self-supervised learning (SSL) has become an important approach in pretraining large neural networks, enabling unprecedented scaling of model and dataset sizes. While recent advances like I-JEPA have shown promising results for Vision Transformers, adapting such methods to Convolutional Neural Networks (CNNs) presents unique challenges. In this paper, we introduce CNN-JEPA, a novel SSL method that successfully applies the joint embedding predictive architecture approach to CNNs. Our method incor
- **Compute Scale**: Mid (24G): CNN-based, more efficient than ViT JEPA.
- **LeCun Alignment**: MEDIUM — Extends JEPA to practical architectures for real-world deployment.

### What / Why / Solve

- **Proposal**: CNN-JEPA — Self-supervised pretraining of convolutional neural networks using JEPA. Adapts the JEPA framework from Vision Transformers to CNNs, addressing the architectural differences.
- **Motivation**: JEPA was designed for Vision Transformers which have natural patch-based representations. CNNs have different inductive biases (translation equivariance, local receptive fields) that require adapting the masking and prediction strategy.
- **Problem Solved**: Extends JEPA to CNN backbones, making JEPA-style pretraining available for architectures that are more efficient for edge deployment and real-time applications.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and CNN architectures. Addresses the ViT-centric nature of JEPA.
- **Implicit Connection**: CNN-JEPA enables JEPA-based world models on resource-constrained devices (robots, phones). This is crucial for deploying LeCun's vision in the real world where ViT-scale compute isn't available.
- **Research Line**: Efficient JEPA — adapting JEPA to lightweight architectures.

- **Future Directions**: CNN-JEPA for video; mobile deployment of JEPA world models.
- **GitHub**: To be checked

---

## 26. [2024-05-06] Sora and V-JEPA Have Not Learned The Complete Real World Model -- A Philosophical Analysis of Video AIs Through the Theory of Productive Imagination

- **arXiv**: [2407.10311](https://arxiv.org/abs/2407.10311)
- **Authors**: Jianqiu Zhang
- **Abstract**: Sora from Open AI has shown exceptional performance, yet it faces scrutiny over whether its technological prowess equates to an authentic comprehension of reality. Critics contend that it lacks a foundational grasp of the world, a deficiency V-JEPA from Meta aims to amend with its joint embedding approach. This debate is vital for steering the future direction of Artificial General Intelligence(AGI). We enrich this debate by developing a theory of productive imagination that generates a coherent
- **Compute Scale**: N/A (philosophical analysis)
- **LeCun Alignment**: HIGH — Directly engages with LeCun's criteria for world models and finds current systems lacking.

### What / Why / Solve

- **Proposal**: Philosophical analysis arguing that Sora and V-JEPA have NOT learned complete real world models, despite their impressive generation capabilities. They lack causal understanding, counterfactual reasoning, and physical consistency.
- **Motivation**: The hype around Sora and V-JEPA claims they are 'world simulators'. This paper provides a critical reality check: what does it actually MEAN to be a world model, and do current systems qualify?
- **Problem Solved**: Clarifies the philosophical criteria for being a 'world model' vs. a pattern matcher. Helps the field avoid overclaiming and directs attention to genuine gaps.

### Academic Context

- **Inheritance / Response**: Engages directly with Sora, V-JEPA, and LeCun's vision paper. Provides philosophical scrutiny of empirical claims.
- **Implicit Connection**: This paper is essential reading alongside ALL JEPA papers. It defines the bar that future world models must clear. If the critiques are valid, they redirect the JEPA research program toward causal reasoning and physics.
- **Research Line**: Critical Analysis — philosophical and methodological scrutiny of world model claims.

- **Future Directions**: Developing benchmarks for causal understanding in world models.
- **GitHub**: N/A

---

## 27. [2024-05-06] Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond

- **arXiv**: [2405.03520](https://arxiv.org/abs/2405.03520)
- **Authors**: Zheng Zhu, Xiaofeng Wang, Wangbo Zhao, Chen Min, Bohan Li, Nianchen Deng, Min Dou, Yuqi Wang et al.
- **Abstract**: General world models represent a crucial pathway toward achieving Artificial General Intelligence (AGI), serving as the cornerstone for various applications ranging from virtual environments to decision-making systems. Recently, the emergence of the Sora model has attained significant attention due to its remarkable simulation capabilities, which exhibits an incipient comprehension of physical laws. In this survey, we embark on a comprehensive exploration of the latest advancements in world mode
- **Compute Scale**: N/A (survey)
- **LeCun Alignment**: HIGH — Provides the conceptual framework for evaluating progress toward LeCun's vision.

### What / Why / Solve

- **Proposal**: Comprehensive survey examining whether video generation models like Sora can be considered world simulators. Categorizes different types of world models and evaluates current systems against each definition.
- **Motivation**: The term 'world model' is used inconsistently across the literature. This survey provides a taxonomy of world model types and evaluates where current systems fit.
- **Problem Solved**: Provides a clear taxonomy of world model definitions. Helps researchers position their work within the broader landscape of world model research.

### Academic Context

- **Inheritance / Response**: Builds on the world model survey literature. Engages with Sora, Dreamer, JEPA, and related work.
- **Implicit Connection**: This survey provides the TAXONOMIC FRAMEWORK for the entire field. Its categorization of world models (generative vs. predictive, pixel-space vs. latent-space) directly maps to the JEPA vs. generative debate.
- **Research Line**: Survey/Taxonomy — organizing the world model research landscape.

- **Future Directions**: Updating the taxonomy as new world model types emerge.
- **GitHub**: N/A

---

## 28. [2024-04-25] Point-JEPA: A Joint Embedding Predictive Architecture for Self-Supervised Learning on Point Cloud

- **arXiv**: [2404.16432](https://arxiv.org/abs/2404.16432)
- **Authors**: Ayumu Saito, Prachi Kudeshia, Jiju Poovvancheri
- **Abstract**: Recent advancements in self-supervised learning in the point cloud domain have demonstrated significant potential. However, these methods often suffer from drawbacks, including lengthy pre-training time, the necessity of reconstruction in the input space, or the necessity of additional modalities. In order to address these issues, we introduce Point-JEPA, a joint embedding predictive architecture designed specifically for point cloud data. To this end, we introduce a sequencer that orders point 
- **Compute Scale**: Mid (24G): Point cloud processing on standard GPUs.
- **LeCun Alignment**: MEDIUM — Extends JEPA to 3D, a necessary modality for embodied world models.

### What / Why / Solve

- **Proposal**: Point-JEPA — JEPA for 3D point cloud self-supervised learning. Adapts the masking and prediction strategy from 2D images to 3D point clouds, which have irregular spatial structure.
- **Motivation**: Point clouds are the native representation for 3D perception (LiDAR, depth sensors). A world model for robotics needs to understand 3D space. Extending JEPA to point clouds is a necessary step toward 3D world models.
- **Problem Solved**: First JEPA implementation for 3D point clouds. Demonstrates that JEPA's principles generalize beyond 2D images to irregular 3D data.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and point cloud deep learning (PointNet++, etc.).
- **Implicit Connection**: Point-JEPA enables 3D world models — essential for robotics and autonomous driving. Together with SkyJEPA and Drive-JEPA, this extends JEPA into the 3D physical world.
- **Research Line**: 3D JEPA — extending JEPA to spatial 3D representations.

- **Future Directions**: Temporal Point-JEPA for 4D (3D+time); integration with V-JEPA for joint 2D-3D understanding.
- **GitHub**: To be checked

---

## 29. [2024-03-16] Dreaming of Many Worlds: Learning Contextual World Models Aids Zero-Shot Generalization

- **arXiv**: [2403.10967](https://arxiv.org/abs/2403.10967)
- **Authors**: Sai Prasanna, Karim Farid, Raghu Rajan, André Biedenkapp
- **Abstract**: Zero-shot generalization (ZSG) to unseen dynamics is a major challenge for creating generally capable embodied agents. To address the broader challenge, we start with the simpler setting of contextual reinforcement learning (cRL), assuming observability of the context values that parameterize the variation in the system's dynamics, such as the mass or dimensions of a robot, without making further simplifying assumptions about the observability of the Markovian state. Toward the goal of ZSG to un
- **Compute Scale**: Mid (24G)
- **LeCun Alignment**: MEDIUM — Addresses a key requirement for autonomous intelligence but uses Dreamer rather than JEPA.

### What / Why / Solve

- **Proposal**: Dreaming of Many Worlds — Learns contextual world models that can generalize to new environments zero-shot by conditioning on context observations from the target environment.
- **Motivation**: Standard world models overfit to their training environment. A truly autonomous agent must adapt to new environments without retraining. Contextual world models address this by conditioning on environment identity.
- **Problem Solved**: Enables zero-shot generalization of world models to new environments by learning environment-conditional dynamics. The model learns 'how the world works in general' rather than 'how this specific environment works'.

### Academic Context

- **Inheritance / Response**: Builds on Dreamer and meta-learning. Addresses the environment-specificity limitation of world models.
- **Implicit Connection**: Zero-shot generalization is a key capability for LeCun's vision of autonomous agents that operate in the open world. This paper shows one path toward environment-agnostic world models.
- **Research Line**: Generalizable World Models — learning dynamics that transfer across environments.

- **Future Directions**: Open-world generalization; combining with JEPA architectures.
- **GitHub**: To be checked

---

## 30. [2024-03-08] Sora as a World Model? A Complete Survey on Text-to-Video Generation

- **arXiv**: [2403.05131](https://arxiv.org/abs/2403.05131)
- **Authors**: Fachrina Dewi Puspitasari, Chaoning Zhang, Joseph Cho, Adnan Haider, Noor Ul Eman, Omer Amin, Alexis Mankowski, Muhammad Umair et al.
- **Abstract**: The evolution of video generation from text, from animating MNIST to simulating the world with Sora, has progressed at a breakneck speed. Here, we systematically discuss how far text-to-video generation technology supports essential requirements in world modeling. We curate 250+ studies on text-based video synthesis and world modeling. We then observe that recent models increasingly support spatial, action, and strategic intelligences in world modeling through adherence to completeness, consiste
- **Compute Scale**: N/A (survey)
- **LeCun Alignment**: MEDIUM — Supports LeCun's argument that generative models != world models.

### What / Why / Solve

- **Proposal**: Complete survey on text-to-video generation models as world models. Evaluates whether video diffusion models (Sora, etc.) qualify as world models under various definitions.
- **Motivation**: Sora sparked claims that video generation IS world modeling. This survey examines the evidence for and against this claim across multiple dimensions.
- **Problem Solved**: Provides the most comprehensive survey of the 'video generator as world model' question. Concludes that current systems fall short of being true world models.

### Academic Context

- **Inheritance / Response**: Engages with Sora, video diffusion, and world model literature.
- **Implicit Connection**: Together with 2405.03520 and 2407.10311, this forms a trilogy of critical analysis papers that define what a world model SHOULD be. These papers implicitly argue that JEPA-style architectures are more aligned with true world modeling than generative approaches.
- **Research Line**: Survey/Critical Analysis.

- **Future Directions**: Benchmarks for video-model-as-world-simulator evaluation.
- **GitHub**: N/A

---

## 31. [2023-11-27] A-JEPA: Joint-Embedding Predictive Architecture Can Listen

- **arXiv**: [2311.15830](https://arxiv.org/abs/2311.15830)
- **Authors**: Zhengcong Fei, Mingyuan Fan, Junshi Huang
- **Abstract**: This paper presents that the masked-modeling principle driving the success of large foundational vision models can be effectively applied to audio by making predictions in a latent space. We introduce Audio-based Joint-Embedding Predictive Architecture (A-JEPA), a simple extension method for self-supervised learning from the audio spectrum. Following the design of I-JEPA, our A-JEPA encodes visible audio spectrogram patches with a curriculum masking strategy via context encoder, and predicts the
- **Compute Scale**: Mid (24G): Audio SSL on standard datasets.
- **LeCun Alignment**: HIGH — Validates JEPA's generality, a key claim in LeCun's vision.

### What / Why / Solve

- **Proposal**: A-JEPA — Joint-Embedding Predictive Architecture for audio. The first extension of JEPA beyond vision, applying the context/target/predictor framework to audio spectrograms.
- **Motivation**: JEPA's principles should be modality-agnostic. Audio is a natural next modality after vision and has unique temporal structure that tests JEPA's generality.
- **Problem Solved**: First demonstration that JEPA works beyond vision. Validates JEPA as a general-purpose SSL framework rather than a vision-specific trick.

### Academic Context

- **Inheritance / Response**: Builds directly on I-JEPA (2301.08243). Adapts the masking strategy for audio spectrograms.
- **Implicit Connection**: A-JEPA opens the door to multimodal JEPA — if JEPA works for both vision and audio, it can work for video (vision + audio). This is the first step toward a unified multimodal world model.
- **Research Line**: Multimodal JEPA — extending JEPA beyond vision.

- **Future Directions**: Joint audio-visual JEPA; speech JEPA for dialogue; audio-based world models.
- **GitHub**: To be checked

---

## 32. [2023-09-29] GAIA-1: A Generative World Model for Autonomous Driving

- **arXiv**: [2309.17080](https://arxiv.org/abs/2309.17080)
- **Authors**: Anthony Hu, Lloyd Russell, Hudson Yeo, Zak Murez, George Fedoseev, Alex Kendall, Jamie Shotton, Gianluca Corrado
- **Abstract**: Autonomous driving promises transformative improvements to transportation, but building systems capable of safely navigating the unstructured complexity of real-world scenarios remains challenging. A critical problem lies in effectively predicting the various potential outcomes that may emerge in response to the vehicle's actions as the world evolves.
  To address this challenge, we introduce GAIA-1 ('Generative AI for Autonomy'), a generative world model that leverages video, text, and action i
- **Compute Scale**: Large (40G+/Multi-card): 4.6B parameter video diffusion.
- **LeCun Alignment**: MEDIUM — Powerful world model but uses generative approach LeCun considers inefficient. Important counterpoint.

### What / Why / Solve

- **Proposal**: GAIA-1 — Generative World Model for Autonomous Driving. Wayve's large-scale video diffusion world model.
- **Motivation**: Autonomous driving needs future prediction. Learned world models could capture complex real-world dynamics.
- **Problem Solved**: Learns driving world model generating realistic future frames conditioned on ego-vehicle actions.

### Academic Context

- **Inheritance / Response**: Video diffusion + world model literature. Generative approach (predicts pixels).
- **Implicit Connection**: Generative counterpart to JEPA. Embodies approach LeCun argues against but achieves impressive results. Key tension in field.
- **Research Line**: Generative World Models — pixel-space prediction for driving.

- **Future Directions**: More diverse scenarios; planning integration; real-time inference.
- **GitHub**: Wayve (proprietary)

---

## 33. [2023-07-24] MC-JEPA: A Joint-Embedding Predictive Architecture for Self-Supervised Learning of Motion and Content Features

- **arXiv**: [2307.12698](https://arxiv.org/abs/2307.12698)
- **Authors**: Adrien Bardes, Jean Ponce, Yann LeCun
- **Abstract**: Self-supervised learning of visual representations has been focusing on learning content features, which do not capture object motion or location, and focus on identifying and differentiating objects in images and videos. On the other hand, optical flow estimation is a task that does not involve understanding the content of the images on which it is estimated. We unify the two approaches and introduce MC-JEPA, a joint-embedding predictive architecture and self-supervised learning approach to joi
- **Compute Scale**: Large (40G+): Video transformer on Something-Something-v2, Kinetics-400.
- **LeCun Alignment**: HIGH — Core JEPA extension to video, embodying modular world model concept.

### What / Why / Solve

- **Proposal**: MC-JEPA — Motion and Content JEPA. Learns separate motion and content representations via joint embedding with optical flow as weak motion signal.
- **Motivation**: Video understanding requires distinguishing object motion from scene content. JEPA's two-stream factorization enables this disentanglement.
- **Problem Solved**: Disentangled motion-content representation learning without labels.

### Academic Context

- **Inheritance / Response**: Direct successor to I-JEPA (2301.08243).
- **Implicit Connection**: Motion-content factorization foreshadows action-conditioned world models. Two-stream encoder blueprint for future multimodal JEPA.
- **Research Line**: Multimodal JEPA — first JEPA for video with explicit factorization.

- **Future Directions**: Action models; longer videos; 3D scene understanding.
- **GitHub**: Meta FAIR

---

## 34. [2023-07-14] SafeDreamer: Safe Reinforcement Learning with World Models

- **arXiv**: [2307.07176](https://arxiv.org/abs/2307.07176)
- **Authors**: Weidong Huang, Jiaming Ji, Chunhe Xia, Borong Zhang, Yaodong Yang
- **Abstract**: The deployment of Reinforcement Learning (RL) in real-world applications is constrained by its failure to satisfy safety criteria. Existing Safe Reinforcement Learning (SafeRL) methods, which rely on cost functions to enforce safety, often fail to achieve zero-cost performance in complex scenarios, especially vision-only tasks. These limitations are primarily due to model inaccuracies and inadequate sample efficiency. The integration of the world model has proven effective in mitigating these sh
- **Compute Scale**: Mid (24G): Adds safety constraints to standard Dreamer.
- **LeCun Alignment**: MEDIUM — Addresses a practical requirement for deployment.

### What / Why / Solve

- **Proposal**: SafeDreamer — Safe reinforcement learning with world models. Adds safety constraints to Dreamer's planning, ensuring the agent avoids dangerous states during both exploration and exploitation.
- **Motivation**: Dreamer explores freely without safety considerations. For real-world deployment (robots, autonomous vehicles), safety constraints are non-negotiable. SafeDreamer bridges model-based RL and safe RL.
- **Problem Solved**: First integration of safety constraints into Dreamer-style world model planning. The agent learns to achieve goals while satisfying safety constraints.

### Academic Context

- **Inheritance / Response**: Builds on Dreamer and safe RL (constrained MDPs).
- **Implicit Connection**: Safety is an implicit requirement in LeCun's vision — the cost module must include safety considerations. SafeDreamer implements this practically for Dreamer, and the approach could extend to JEPA-based world models.
- **Research Line**: Safe World Models — constrained planning in model-based RL.

- **Future Directions**: Learned safety constraints from demonstrations; safe JEPA-based planning.
- **GitHub**: To be checked

---

## 35. [2023-01-19] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

- **arXiv**: [2301.08243](https://arxiv.org/abs/2301.08243)
- **Authors**: Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael Rabbat, Yann LeCun, Nicolas Ballas
- **Abstract**: This paper demonstrates an approach for learning highly semantic image representations without relying on hand-crafted data-augmentations. We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image. A core design choice to guide I-JEPA towards producing semantic representations is the masking strategy; specifically, it is crucial to (a) sample target blocks with sufficiently 
- **Compute Scale**: Large (40G+): ViT-H/14 on ImageNet-1K.
- **LeCun Alignment**: HIGH — Direct implementation of LeCun's core vision.

### What / Why / Solve

- **Proposal**: JEPA (Joint Embedding Predictive Architecture) — predicts representations of masked target blocks in latent space rather than pixel-level reconstruction. Uses context encoder + target encoder + predictor network.
- **Motivation**: Generative architectures waste capacity modeling pixel-level details irrelevant to semantics. The world is not predictable at the pixel level but is predictable at the representation level.
- **Problem Solved**: Eliminates pixel-level generation in SSL. Enables semantic-level predictive learning without generative burden.

### Academic Context

- **Inheritance / Response**: Builds on LeCun's 'A Path Towards Autonomous Machine Intelligence' (2022). Extends BYOL/SimSiam-style non-contrastive SSL with latent-space prediction.
- **Implicit Connection**: Multi-block masking strategy (target blocks predicted from context) — the core JEPA pattern reused in V-JEPA, MC-JEPA, and all derivatives.
- **Research Line**: JEPA Core — the canonical implementation of LeCun's predictive world model architecture.

- **Future Directions**: Scaling; extension to video/multimodal; action-conditioned prediction for world models.
- **GitHub**: Meta FAIR

---

## 36. [2022-06-28] DayDreamer: World Models for Physical Robot Learning

- **arXiv**: [2206.14176](https://arxiv.org/abs/2206.14176)
- **Authors**: Philipp Wu, Alejandro Escontrela, Danijar Hafner, Ken Goldberg, Pieter Abbeel
- **Abstract**: To solve tasks in complex environments, robots need to learn from experience. Deep reinforcement learning is a common approach to robot learning but requires a large amount of trial and error to learn, limiting its deployment in the physical world. As a consequence, many advances in robot learning rely on simulators. On the other hand, learning inside of simulators fails to capture the complexity of the real world, is prone to simulator inaccuracies, and the resulting behaviors do not adapt to c
- **Compute Scale**: Mid (24G): Training from real robot data on single GPU.
- **LeCun Alignment**: HIGH — Landmark empirical validation of learned world models on real robots.

### What / Why / Solve

- **Proposal**: DayDreamer — World Models for physical robot learning. First Dreamer deployment on real robots.
- **Motivation**: World models previously simulation-only. Need real-world validation for LeCun's vision.
- **Problem Solved**: First demonstration of model-based RL world models training on physical robots in hours.

### Academic Context

- **Inheritance / Response**: Dreamer (Hafner et al.). Applies MBRL to real-world robotics.
- **Implicit Connection**: Validates core premise: latent-space learning more efficient than pixel-space. Predates JEPA but demonstrates same principle.
- **Research Line**: Real-World World Models — deploying MBRL on physical robots.

- **Future Directions**: JEPA integration; lifelong learning; multi-task.
- **GitHub**: https://github.com/danijar/daydreamer

---

## 37. [2022-02-19] TransDreamer: Reinforcement Learning with Transformer World Models

- **arXiv**: [2202.09481](https://arxiv.org/abs/2202.09481)
- **Authors**: Chang Chen, Yi-Fu Wu, Jaesik Yoon, Sungjin Ahn
- **Abstract**: The Dreamer agent provides various benefits of Model-Based Reinforcement Learning (MBRL) such as sample efficiency, reusable knowledge, and safe planning. However, its world model and policy networks inherit the limitations of recurrent neural networks and thus an important question is how an MBRL framework can benefit from the recent advances of transformers and what the challenges are in doing so. In this paper, we propose a transformer-based MBRL agent, called TransDreamer. We first introduce
- **Compute Scale**: Mid (24G)
- **LeCun Alignment**: MEDIUM — Advances the transformer-based approach that JEPA later adopts.

### What / Why / Solve

- **Proposal**: TransDreamer — Reinforcement learning with transformer world models. Replaces Dreamer's RNN-based dynamics with a transformer, enabling better long-range credit assignment and parallel computation.
- **Motivation**: Dreamer uses RNNs which struggle with long-term dependencies and are slow to train (sequential computation). Transformers offer parallel computation and better long-range modeling through attention.
- **Problem Solved**: Extends Dreamer with transformer dynamics for improved long-horizon credit assignment and faster training.

### Academic Context

- **Inheritance / Response**: Builds on Dreamer and Decision Transformer. Applies the transformer architecture to world model dynamics.
- **Implicit Connection**: TransDreamer represents the convergence of transformers and world models — the same architectural trend that later produced JEPA (which is transformer-based). This paper foreshadows the dominance of attention-based world models.
- **Research Line**: Transformer World Models — applying attention mechanisms to model-based RL.

- **Future Directions**: Integration with JEPA-style latent prediction; sparse attention for efficiency.
- **GitHub**: To be checked

---


*Generated: 2026-07-09 | Papers: 37 | All 37 papers with deep analysis*
