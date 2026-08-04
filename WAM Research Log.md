# WAM Research Log — Deep Analysis

> Curated papers from Yann LeCun's World Models/JEPA ecosystem, with detailed architectural analysis, research lineage, and LeCun alignment assessment.

> **86 papers** (2022—2026) | Daily monitoring at 08:00 UTC | Last scan: 2026-08-04 (2 new papers — July 31 backlog)

---

## 📊 Paper Index

| # | Date | Paper | Alignment | Compute |
||---|------|-------|-----------|--------|
||| 1 | 2026-07-31 | [WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2607.29613) | HIGH — LeJEPA-based world critic for VLA RL; joint latent prediction + value estimation; 149 tasks + 7 real-world. | Mid (24G): Lightweight LeJEPA + Pi0/Pi0.5/OpenVLA-OFT backbones. |
||| 2 | 2026-07-31 | [AquaJEPA: Action-Conditioned Multimodal Predictive Representations for Underwater Robot Dynamics](https://arxiv.org/abs/2607.29393) | HIGH — JEPA for underwater robots; RGB+sonar+proprioception fusion; preregistered 120-env replication. | Small-Mid (8-24G): Stonefish simulator, 120 environments. |
||| 1 | 2026-07-30 | [CS-JEPA: One Future, Every Robot — Label-Efficient Collective-State Prediction with Decentralized JEPA](https://arxiv.org/abs/2607.28443) | HIGH — Recurrent decentralized JEPA for multi-robot swarms; 45.5% MSE reduction, label-efficient. | Small (8-12G): 16-frame history, 64-float msg per robot. |
||| 2 | 2026-07-30 | [PhiZero: A World Model Built Around Physical Language](https://arxiv.org/abs/2607.28624) | MEDIUM — Discrete physical language + VLM reasoning + diffusion rendering; critiques pixel prediction. | Large (40G+): VLM reasoner + diffusion decoder. |
||| 1 | 2026-07-30 | [QQWorld: Quantile-Quantile Matching for World Model Regularization](https://arxiv.org/abs/2607.28415) | HIGH — Replaces LeWM's Epps-Pulley with quantile-quantile matching; fixes vanishing tail gradients. | Small-Mid (8-24G): Four LeWM control environments. |
||| 2 | 2026-07-30 | [QuantWAMs: Calibrating at the Right Granularity for World Action Models](https://arxiv.org/abs/2607.28405) | MEDIUM — PTQ for WAM deployment; 29% memory, 0.2–0.7pp accuracy loss. | Large (40G+): Fast-WAM, LingBot-VA on RoboTwin 2.0/LIBERO. |
|||| 3 | 2026-07-30 | [ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations](https://arxiv.org/abs/2607.28362) | MEDIUM — Cross-shadow prediction for appearance-invariant action control; 86% blinded win rate. | Mid-Large (24-40G+): Block-causal video world model. |
|||| 4 | 2026-07-29 | [JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation](https://arxiv.org/abs/2607.26600) | MEDIUM — I-JEPA auxiliary objective improves monocular depth estimation; zero-shot transfer, no inference overhead. | Mid (24G): DINOv3 ViT + photometric pipeline on KITTI. |
|||| 1 | 2026-07-28 | [INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models](https://arxiv.org/abs/2607.26056) | HIGH — JEPA-based search-free world model on LeWM; 2.9–5.5ms inference. | Mid (24G): LeWM push/pick/place/navigation benchmarks. |
|| 2 | 2026-07-28 | [TD-JEPA: Plan-Aware Representation Learning for Latent World Model MPC](https://arxiv.org/abs/2607.25337) | HIGH — Temporal-distance JEPA closes train-plan gap; 100% Two-Room, +14.2 OGB-Cube. | Mid (24G): LeWM encoder-predictor backbone. |
|| 3 | 2026-07-28 | [Rad-JEPA 3D: Radiology Joint-Embedding Predictive Model for 3D Computed Tomography](https://arxiv.org/abs/2607.26196) | MEDIUM — JEPA for volumetric CT with H-Mamba encoder + HSOR; 4B params, SOTA spatial reasoning. | Large (40G+): 4B params on 120K CT scans. |
|| 4 | 2026-07-27 | [τ: Touch-Augmented VLA Models from Future Visual Supervision](https://arxiv.org/abs/2607.24485) | MEDIUM-HIGH — JEPA-inspired tactile representation for VLA models; no deployment overhead. | Mid (24G): VLA + tactile encoder finetuning. |
|| 4 | 2026-07-24 | [IQ-JEPA: JEPA with Hermitian ViT for Ultrasound Sound Speed Estimation](https://arxiv.org/abs/2607.22351) | MEDIUM — Cross-domain validation: complex-valued JEPA for medical imaging. | Mid (24G): Fullwave 79K simulations; 3–4× label efficiency gain. |
|| 5 | 2026-07-20 | [AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Learning](https://arxiv.org/abs/2607.15295) | HIGH — Multimodal JEPA, LeJEPA-based, no decoder/EMA. | Mid (24G): Audio-visual ViT on VGGSound/AudioSet. |
| 2 | 2026-07-15 | [The SIGReg Objective as Variational Free Energy: A Theoretical Active-Inference Account of JEPA World Models](https://arxiv.org/abs/2607.13612) | HIGH — Foundational theory connecting JEPA to Active Inference. | Small (8-12G): Theoretical with Lean 4 verification. |
| 3 | 2026-07-14 | [Mind the Gap: Promises and Pitfalls of Hierarchical Planning in LeWorldModel](https://arxiv.org/abs/2607.12547) | HIGH — Direct LeWorldModel investigation with Hi-LeWM. | Mid (24G): Two-level planning over frozen LeWM. |
| 4 | 2026-07-13 | [From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence](https://arxiv.org/abs/2607.11689) | HIGH — Explicit WAM roadmap; coins "embodied brain" concept. | N/A (roadmap/position paper) |
| 5 | 2026-07-11 | [A Control Theory of Predictability in Latent World Models](https://arxiv.org/abs/2607.10362) | HIGH — Proves prediction error ≠ control success; structural decoupling. | Mid (24G): Synthetic + MPC experiments. |
| 6 | 2026-07-17 | [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898) | MEDIUM — Hierarchical driving world model; generative approach as counterpoint. | Large (40G+): Two-level video prediction. |
| 7 | 2026-07-04 | [SiamJEPA: On the Role of Siamese Student Encoders in JEPA](https://arxiv.org/abs/2607.04044) | HIGH — Theoretical validation of JEPA architecture. | Mid (24G): Ablation studies on standard benchmarks. |
| 8 | 2026-06-30 | [AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026) | HIGH — Adaptive computation key to efficient autonomous systems. | Mid (24G): Focus on efficiency. |
| 9 | 2026-06-22 | [SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-](https://arxiv.org/abs/2606.23444) | HIGH — Direct JEPA application to physical robot control. | Large (40G+): Training + real-time drone inference. |
| 10 | 2026-06-17 | [S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Repre](https://arxiv.org/abs/2606.19398) | MEDIUM — Expands JEPA generality. | Mid (24G): LibriSpeech-scale. |
| 11 | 2026-06-14 | [You Don't Need Strong Assumptions: Visual Representation Learning](https://arxiv.org/abs/2606.15956) | HIGH — Explores a potentially simpler path to the same world model goal. | Mid (24G) |
| 12 | 2026-05-25 | [When Does LeJEPA Learn a World Model?](https://arxiv.org/abs/2605.26379) | HIGH — Directly investigates whether JEPA fulfills LeCun's world model vision. | Mid (24G): Controlled analytical experiments. |
| 13 | 2026-05-25 | [UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/abs/2605.25313) | HIGH — Addresses key practical limitation for real-world autonomous systems. | Mid (24G): Belief-state inference adds moderate overhead. |
| 14 | 2026-05-20 | [stable-worldmodel: A Platform for Reproducible World Modeling Res](https://arxiv.org/abs/2605.21800) | MEDIUM — Enables the broader world model ecosystem that JEPA is part of. | Small (8-12G): Designed to be accessible for researchers. |
| 15 | 2026-05-15 | [DiLA: Disentangled Latent Action World Models](https://arxiv.org/abs/2605.15725) | HIGH — Factorized control aligns with LeCun's modular agent architecture. | Mid (24G): Standard world model + disentanglement objectives. |
| 16 | 2026-05-10 | [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End ](https://arxiv.org/abs/2605.09241) | HIGH — Makes JEPA more practical and reliable. | Mid (24G): Adds regularization to existing JEPA. |
| 17 | 2026-05-05 | [Text-Conditional JEPA for Learning Semantically Rich Visual Repre](https://arxiv.org/abs/2605.03245) | MEDIUM — Extends JEPA but adds language which LeCun's vision treats as a separate module. | Large (40G+): Requires paired image-text data at scale. |
| 18 | 2026-04-03 | [Hierarchical Planning with Latent World Models](https://arxiv.org/abs/2604.03208) | HIGH — Directly implements LeCun's hierarchical planning vision. | Mid (24G): Two-level planning more efficient than flat. |
| 19 | 2026-03-20 | [Probing the Latent World: Emergent Discrete Symbols and Physical ](https://arxiv.org/abs/2603.20327) | MEDIUM — Tests a core assumption of LeCun's vision empirically. | Mid (24G): Probing experiments on pre-trained models. |
| 20 | 2026-03-15 | [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Lea](https://arxiv.org/abs/2603.14482) | HIGH — Meta FAIR. Addresses key limitation on path to full world models. | Large (40G+): Extended V-JEPA with dense heads. |
| 21 | 2026-03-13 | [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Archit](https://arxiv.org/abs/2603.19312) | HIGH — Likely LeCun's group. Name signals direct alignment. | Large (40G+): End-to-end pixel-to-latent training. |
| 22 | 2026-03-07 | [Dreamer-CDP: Improving Reconstruction-free World Models Via Conti](https://arxiv.org/abs/2603.07083) | MEDIUM — Moves Dreamer closer to LeCun's vision by eliminating reconstruction. | Mid (24G): More efficient than standard Dreamer. |
| 23 | 2026-03-05 | [Probabilistic Dreaming for World Models](https://arxiv.org/abs/2603.04715) | MEDIUM — Essential for safe deployment, though not directly addressed in LeCun's architecture. | Mid (24G): Adds probabilistic outputs to standard world model. |
| 24 | 2026-02-12 | [JEPA-VLA: Video Predictive Embedding is Needed for VLA Models](https://arxiv.org/abs/2602.11832) | HIGH — Demonstrates practical necessity of JEPA for embodied AI. | Large (40G+): Video JEPA + VLA fine-tuning. |
| 25 | 2026-01-29 | [Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation f](https://arxiv.org/abs/2601.22032) | HIGH — Validates JEPA in high-stakes real-world application. | Large (40G+): Driving video + trajectory model. |
| 26 | 2025-11-21 | [DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive A](https://arxiv.org/abs/2511.17354) | HIGH — Combines JEPA with energy-based learning, two pillars of LeCun's vision. | Mid (24G) |
| 27 | 2025-10-07 | [Gaussian Embeddings: How JEPAs Secretly Learn Your Data Density](https://arxiv.org/abs/2510.05949) | HIGH — Provides theoretical validation of JEPA's connection to energy-based models. | Small (8-12G): Theoretical analysis with small-scale experiments. |
| 28 | 2025-09-29 | [Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers](https://arxiv.org/abs/2509.24317) | MEDIUM — Makes JEPA more practical but doesn't advance the theoretical vision. | Mid (24G): Focus on reducing training cost. |
| 29 | 2025-06-11 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Pred](https://arxiv.org/abs/2506.09985) | HIGH — Meta FAIR flagship. Shows JEPA scales to full vision triad. | Large (40G+/Multi-card): Massive video transformer, Meta-scale compute. |
| 30 | 2024-10-25 | [Connecting Joint-Embedding Predictive Architecture with Contrasti](https://arxiv.org/abs/2410.19560) | HIGH — Theoretical work that strengthens the foundations of JEPA. | Small (8-12G): Theoretical paper with illustrative experiments. |
| 31 | 2024-08-14 | [CNN-JEPA: Self-Supervised Pretraining Convolutional Neural Networ](https://arxiv.org/abs/2408.07514) | MEDIUM — Extends JEPA to practical architectures for real-world deployment. | Mid (24G): CNN-based, more efficient than ViT JEPA. |
| 32 | 2024-05-06 | [Sora and V-JEPA Have Not Learned The Complete Real World Model --](https://arxiv.org/abs/2407.10311) | HIGH — Directly engages with LeCun's criteria for world models and finds current systems lacking. | N/A (philosophical analysis) |
| 33 | 2024-05-06 | [Is Sora a World Simulator? A Comprehensive Survey on General Worl](https://arxiv.org/abs/2405.03520) | HIGH — Provides the conceptual framework for evaluating progress toward LeCun's vision. | N/A (survey) |
| 34 | 2024-04-25 | [Point-JEPA: A Joint Embedding Predictive Architecture for Self-Su](https://arxiv.org/abs/2404.16432) | MEDIUM — Extends JEPA to 3D, a necessary modality for embodied world models. | Mid (24G): Point cloud processing on standard GPUs. |
| 35 | 2024-03-16 | [Dreaming of Many Worlds: Learning Contextual World Models Aids Ze](https://arxiv.org/abs/2403.10967) | MEDIUM — Addresses a key requirement for autonomous intelligence but uses Dreamer rather than JEPA. | Mid (24G) |
| 36 | 2024-03-08 | [Sora as a World Model? A Complete Survey on Text-to-Video Generat](https://arxiv.org/abs/2403.05131) | MEDIUM — Supports LeCun's argument that generative models != world models. | N/A (survey) |
| 37 | 2023-11-27 | [A-JEPA: Joint-Embedding Predictive Architecture Can Listen](https://arxiv.org/abs/2311.15830) | HIGH — Validates JEPA's generality, a key claim in LeCun's vision. | Mid (24G): Audio SSL on standard datasets. |
| 38 | 2023-09-29 | [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | MEDIUM — Powerful world model but uses generative approach LeCun considers inefficient. Important counterpoint. | Large (40G+/Multi-card): 4.6B parameter video diffusion. |
| 39 | 2023-07-24 | [MC-JEPA: A Joint-Embedding Predictive Architecture for Self-Super](https://arxiv.org/abs/2307.12698) | HIGH — Core JEPA extension to video, embodying modular world model concept. | Large (40G+): Video transformer on Something-Something-v2, Kinetics-400. |
| 40 | 2023-07-14 | [SafeDreamer: Safe Reinforcement Learning with World Models](https://arxiv.org/abs/2307.07176) | MEDIUM — Addresses a practical requirement for deployment. | Mid (24G): Adds safety constraints to standard Dreamer. |
| 41 | 2023-01-19 | [Self-Supervised Learning from Images with a Joint-Embedding Predi](https://arxiv.org/abs/2301.08243) | HIGH — Direct implementation of LeCun's core vision. | Large (40G+): ViT-H/14 on ImageNet-1K. |
| 42 | 2022-06-28 | [DayDreamer: World Models for Physical Robot Learning](https://arxiv.org/abs/2206.14176) | HIGH — Landmark empirical validation of learned world models on real robots. | Mid (24G): Training from real robot data on single GPU. |
| 43 | 2022-02-19 | [TransDreamer: Reinforcement Learning with Transformer World Model](https://arxiv.org/abs/2202.09481) | MEDIUM — Advances the transformer-based approach that JEPA later adopts. | Mid (24G) |
| 44 | 2026-07-20 | [SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning](https://arxiv.org/abs/2607.17973) | HIGH — Prior-conditioned planner for latent world models; 5x long-horizon improvement. | Mid (24G): PushT and OGBench Cube benchmarks. |
| 45 | 2026-07-20 | [Thinking in Video: Can Video Generators Really Reason About the Real World?](https://arxiv.org/abs/2607.17523) | MEDIUM-HIGH — Empirically validates LeCun's claim that generative video ≠ world understanding. | N/A (evaluation/benchmark framework) |
| 46 | 2026-07-20 | [Patch Policy: Efficient Embodied Control via Dense Visual Representations](https://arxiv.org/abs/2607.18236) | MEDIUM — LeCun co-author; dense ViT features for robot control, 0.7% of VLA parameters. | Small-Mid (8-24G): Efficient block-causal attention. |
| 47 | 2026-07-18 | [Learning from World Feedback: Why Model Uncertainty Fails as a Risk Signal in Model-Based RL](https://arxiv.org/abs/2607.16591) | HIGH — RLxF: model uncertainty anti-correlated with safety; world-feedback signals essential. | Small-Mid (8-24G): Standard MBRL benchmarks. |
| 48 | 2026-07-04 | [Separating Representation from Reconstruction Enables Scalable Text Encoders](https://arxiv.org/abs/2607.04011) | MEDIUM — LeCun co-author; CrossBERT separates representation from reconstruction (JEPA-aligned philosophy). | Mid (24G): MTEB/GLUE benchmarks. |
| 49 | 2026-06-07 | [Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks](https://arxiv.org/abs/2606.08775) | MEDIUM-HIGH — LeCun co-author; WorldDP: hierarchical world model + diffusion policy for multi-stage manipulation. | Mid (24G): Standard robotic manipulation benchmarks. |
| 50 | 2026-07-21 | [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) | MEDIUM — Video world models for robotics; pixel-space action interface; generative video counterpoint. | Large (40G+): Video generation + robotics fine-tuning. |
| 51 | 2026-07-15 | [When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models](https://arxiv.org/abs/2607.14169) | MEDIUM — Proves prediction accuracy ≠ planning adequacy; critical for world model evaluation. | Small (8-12G): LLM-synthesized code world models on board games. |
| 52 | 2026-05-14 | [Crys-JEPA: Accelerating Crystal Discovery via Embedding Screening and Generative Refinement](https://arxiv.org/abs/2605.14759) | MEDIUM — LeCun co-author; extends JEPA architecture to materials science for energy-aware crystal discovery. | Mid (24G): Crystal structure prediction benchmarks. |
|| 53 | 2026-07-23 | [Self-Supervised Learning of Structured Dynamics from Videos](https://arxiv.org/abs/2607.21576) | MEDIUM-HIGH — JEPA-aligned future-feature prediction; structured dynamics decomposition (camera vs object). | Small-Mid (8-24G): Frozen ViT + prediction heads. |
|| 54 | 2026-07-15 | [Depth-Regularized JEPA World Models Learn More Transferable Representations from Real Outdoor Robot Data](https://arxiv.org/abs/2607.16314) | HIGH — JEPA world model with geometric depth prior; 33% lower VO error on real agricultural robot data. | Small (8-12G): 18M-param model on single GPU. |
|| 55 | 2026-07-08 | [The JEPA Predictor: A Transferable Operator for Occluded Feature Completion](https://arxiv.org/abs/2607.16274) | HIGH — Proves JEPA predictors are portable across encoder families; closes gap against discriminative baselines. | Small-Mid (8-24G): Frozen encoder + linear projection on 500 images. |
||| 56 | 2026-07-22 | [JEPA-CFM: A JEPA-based Channel Foundation Model for Robust Fluid Antenna Systems](https://arxiv.org/abs/2607.20202) | MEDIUM — Cross-domain validation: JEPA + SIGReg for 6G wireless channel modeling. | Mid (24G): DeepMIMO urban scenario simulations. |
|| 57 | 2026-07-24 | [Music-JEPA: Learning a World Model of Sound from Action](https://arxiv.org/abs/2607.22000) | HIGH — LeCun co-author; action-conditioned JEPA world model for music; piano transcription via planning. | Mid (24G): Audio-pianoroll paired data. |
|| 58 | 2026-07-24 | [On the Identifiability of Controlled World Models](https://arxiv.org/abs/2607.22430) | HIGH — JEPA identifiability theory; proves conditions for latent state/transition recovery under Gaussian policies. | Small (8-12G): Theoretical with synthetic experiments. |
|| 59 | 2026-07-24 | [Robot-Factored World Models via Robot Rendering](https://arxiv.org/abs/2607.22535) | MEDIUM-HIGH — Factorizes robot kinematics/geometry out of world model; cross-embodiment generalization. | Mid (24G): Robot manipulation video prediction. |
|| 60 | 2026-07-24 | [ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2607.22530) | MEDIUM-HIGH — First visuo-tactile world model; policy evaluation + data augmentation via rollout. | Large (40G+): Multi-modal visuo-tactile pretraining + finetuning. |
||| 61 | 2026-07-24 | [Unbiased Open World Regularization for Fair Self-Supervised Learning](https://arxiv.org/abs/2607.22149) | MEDIUM — JEPA bias regularization; conditional distribution matching for debiased SSL. | Small-Mid (8-24G): Encoder-only framework on CelebA. |
|| 62 | 2026-07-27 | [LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments](https://arxiv.org/abs/2607.23969) | HIGH — JEPA-as-World-Anchor WAM paradigm; Predictive-Latent replaces pixel generation. | Large (40G+): Asymmetric MoT + Anchor/Action Diffusion Transformers. |
|| 63 | 2026-07-26 | [The JEPA Paradox in Language: The Geometry of Linguistic Alternatives](https://arxiv.org/abs/2607.23531) | MEDIUM-HIGH — Explains why JEPA fails for text; conditional concentration mismatch formalized. | Small (8-12G): I-JEPA/T-JEPA experiments; theoretical analysis. |
|| 64 | 2026-07-21 | [Toward Goal-Agnostic Joint-Embedding Predictive Control of Partial Differential Equations](https://arxiv.org/abs/2607.21644) | HIGH — JEPA + MPPI for PDE control; goal-agnostic latent dynamics with physical observables. | Small-Mid (8-24G): Small 2D ViT encoder; Navier-Stokes benchmark. |
|| 65 | 2026-07-16 | [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065) | MEDIUM — Drifting generative world model; 17× faster than diffusion; strong counterpoint to generative critics. | Mid (24G): Single forward pass at 30+ fps. |
|| 66 | 2026-07-10 | [Causally Debiased Latent Action Model for Embodied Action Conditioned World Models](https://arxiv.org/abs/2607.09185) | MEDIUM-HIGH — Causal debiasing for LAM-based world models; disentangles action from visual confounders. | Large (40G+): 2B/14B ACWM backbones. |
|| 67 | 2026-06-29 | [Latent Actions from Factorized Transition Effects under Agent Ambiguity](https://arxiv.org/abs/2606.30544) | MEDIUM-HIGH — Balestriero co-author; OTF-LAM with decoder-free DINOv2 variant; sparse transition primitives. | Small-Mid (8-24G): DINOv2-based; ICML 2026 Workshop. |
|| 68 | 2026-07-13 | [WALA: Learning Executable Latent Actions from Action-Labeled Demonstrations and Action-Free Videos](https://arxiv.org/abs/2607.11397) | MEDIUM — Latent actions from videos without reconstruction; DINOv3 + depth prediction space. | Mid (24G): SOTA on RoboCasa (75.2%). |
||| 69 | 2026-07-29 | [What Can Latent World Models Know? Physical Parameter Identifiability in Multimodal Predictive Representations](https://arxiv.org/abs/2607.27017) | HIGH — POKEWORLD identifiability study: objective structure determines which physics enters the latent; data scale only amplifies what's already acquired. | Small-Mid (8-24G): Controlled interventions + RH20T scaling curves. |
||| 70 | 2026-07-29 | [DLAM: Distributional Latent Actions with Temporal Constraints](https://arxiv.org/abs/2607.27138) | MEDIUM-HIGH — Distributional latent actions with temporal variance constraints; reconstruction-free flow-matching policy; improved MetaWorld MT50 and real-world manipulation. | Mid (24G): Encoder + flow-matching policy. |
||| 71 | 2026-07-26 | [Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models](https://arxiv.org/abs/2607.23602) | HIGH — Proves latent-cost selection systematically fails; ASAR adjacency-based reconstruction; +18.7–28.0pp improvement. | Small-Mid (8-24G): Cube + Carry-and-Release benchmarks. |
||| 72 | 2026-07-25 | [WCM: World-Cognition Model for Generalizable Human-Robot Interaction](https://arxiv.org/abs/2607.22999) | MEDIUM — SLAK modular architecture for HRI; human-in-the-loop teaching mode; 73.8% across 9 real-world HRI tasks. | Mid (24G): Modular perception/reasoning/control/memory. |
||| 73 | 2026-07-29 | [Mental World Modeling](https://arxiv.org/abs/2607.27201) | MEDIUM — Extends world models to hidden mental states (beliefs, intentions); MENTIS baseline; LLM-based, not JEPA-aligned architecturally. | Small (8-12G): LLM-based world model; situated decision scenarios. |

---


---

## [2026-07-31] WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

- **arXiv**: [2607.29613](https://arxiv.org/abs/2607.29613)
- **Authors**: Senyu Fei, Xiaopeng Yu, Siyin Wang, Xianzhong Zhao, Jingjing Gong, Xipeng Qiu
- **TL;DR**: Equips VLA RL critics with a lightweight LeJEPA world model that jointly predicts future latent states and estimates values — explicitly training the critic's representation to capture temporal dynamics rather than merely regressing scalar returns.
- **Problem**: RL post-training of VLA models relies on critics that operate on single-frame observations or single-frame VLM latents — a fundamental mismatch with the partially observable nature of robot control. Incorporating observation history naively incurs exponential complexity, and pure scalar-return regression provides insufficient supervision for learning cross-temporal dynamics.
- **Architecture**: WCM (World Critic Model) — A lightweight LeJEPA architecture integrated into the critic. The context encoder processes observation history; the target encoder produces latent targets for future states; the predictor jointly estimates values AND predicts future latent states from the context. This dual objective explicitly trains the critic's representation to capture temporal structure. WCM integrates seamlessly into both on-policy and off-policy training pipelines and is compatible with SOTA VLA backbones (Pi0, Pi0.5, OpenVLA-OFT). Evaluated on 149 tasks across 4 benchmarks + 7 real-world manipulation tasks.
- **Compute Scale**: Mid (24G): Lightweight LeJEPA architecture. Training on standard VLA benchmarks + real-world robot fine-tuning. Compatible with existing VLA pipelines without major overhead.
- **LeCun Alignment**: HIGH — Directly implements LeCun's JEPA vision for embodied RL. STRENGTHS: (1) Uses LeJEPA as the core architecture — predicting in latent space with a lightweight predictor, not pixel generation. (2) Addresses a key limitation identified in LeCun's roadmap: the need for world models that support planning/control, not just perception. (3) The joint prediction + value estimation objective demonstrates how JEPA representations can serve dual purposes (world understanding + decision-making). (4) Seamless integration with existing VLA pipelines shows practical viability. (5) Explicitly frames the problem as "state approximation" requiring world modeling — aligning with LeCun's argument that pure pattern matching is insufficient. WEAKNESSES: (1) The JEPA component is auxiliary to the VLA — not a standalone world model for open-ended planning. (2) Limited to critic enhancement within RL framework, not a full hierarchical planning architecture. Overall, WCM is a strong practical demonstration of LeJEPA's value for embodied AI, showing that even a lightweight JEPA can significantly improve temporal reasoning in RL critics.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: WCM — Augment VLA RL critics with a LeJEPA world model that jointly predicts future latents and estimates values. The dual objective forces the critic to learn temporal dynamics, addressing the fundamental mismatch between single-frame critics and partially observable robot control.
- **Motivation**: Current VLA RL critics operate on single frames, missing the temporal structure essential for accurate value estimation in partially observable environments. Naively adding history is exponentially expensive. A world-modeling objective provides the necessary inductive bias for learning temporal dynamics.
- **Problem Solved**: State-of-the-art performance across 149 tasks (4 benchmarks) and 7 real-world tasks. Particularly strong out-of-distribution generalization. Demonstrates that LeJEPA-based world modeling directly improves RL critic quality.

### Academic Context

- **Inheritance / Response**: Builds on LeJEPA (LeCun's joint-embedding predictive architecture) and applies it to the RL critic setting. Extends prior work on VLA post-training (RT-2, OpenVLA, Pi0) and model-based RL. The key insight is that world modeling and value estimation are complementary objectives that can share a representation.
- **Implicit Connection**: Validates LeCun's claim that world models are necessary for decision-making, not just perception. Shows that even a lightweight JEPA can capture the temporal structure that pure value regression misses. The architecture follows LeCun's modular design principle: separate world model from policy, but share representations.
- **Research Line**: JEPA for Embodied RL — applying joint-embedding predictive architectures to improve decision-making in physical agents.
- **Future Directions**: Standalone JEPA world model for model-based RL; hierarchical planning with JEPA-predicted latents; integration with the full LeCun autonomous agent architecture (World Model → Cost → Actor → Configurator).
- **GitHub**: Not found

---

## [2026-07-31] AquaJEPA: Action-Conditioned Multimodal Predictive Representations for Underwater Robot Dynamics

- **arXiv**: [2607.29393](https://arxiv.org/abs/2607.29393)
- **Authors**: Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov
- **TL;DR**: An action-conditioned JEPA that fuses RGB camera, forward-looking sonar, and proprioception with explicit sensor validity for underwater robot dynamics — preregistered 120-environment replication shows significant improvement over recurrent and supervised baselines.
- **Problem**: Underwater robots combine complementary sensors whose reliability changes abruptly with water visibility, viewpoint, and vehicle motion. Existing predictive models struggle when sensors become unreliable, and standard fusion approaches don't account for dynamic sensor validity.
- **Architecture**: AquaJEPA — An action-conditioned joint-embedding predictive model with explicit sensor validity handling. Fuses three modalities: (1) RGB camera, (2) forward-looking sonar, (3) proprioception (with DVL velocity). Each modality has its own encoder; an explicit validity mechanism weights modalities based on reliability. Conditioned on eight-thruster commands, the predictor infers future latent targets in a shared embedding space. The predicted latents supply velocity and sonar-profile predictions to a shared receding-horizon planner. Key design: EMA target encoder, action margin masking, and modality dropout during training to handle sensor degradation. Evaluated in Stonefish simulator with preregistered 120-environment replication (5 independent replicates × grid crossing, 3 unseen obstacle maps, 4 water-visibility coefficients, nominal vs. shifted dynamics, intermittent DVL loss).
- **Compute Scale**: Small-Mid (8-24G): Three modality encoders + lightweight predictor. Stonefish simulator (not real hardware). 120 environments × 5 replicates = 600 total runs, but each run is simulated (moderate compute).
- **LeCun Alignment**: HIGH — Direct JEPA variant for physical robot dynamics. STRENGTHS: (1) Pure JEPA architecture — predicts in latent space from action-conditioned context, no pixel reconstruction. (2) Multimodal sensor fusion with explicit validity aligns with LeCun's vision of world models that handle diverse, unreliable sensory inputs. (3) Action-conditioned prediction is the core mechanism in LeCun's world model module. (4) Preregistered replication with rigorous statistics (95% CIs, paired tests) demonstrates scientific rigor. (5) Modality dropout during training mirrors JEPA's robustness to partial observability. WEAKNESSES: (1) Underwater domain is niche — doesn't directly validate JEPA for general manipulation or navigation. (2) Stonefish simulator, not real robots (though designed for eventual transfer). (3) The planner is a separate receding-horizon controller, not an end-to-end learned policy — the JEPA provides predictions to an external planner rather than being the complete world model for planning. Overall, AquaJEPA is excellent cross-domain validation of JEPA for physical dynamics with rigorous experimental methodology, demonstrating that JEPA's multimodal prediction approach handles sensor degradation better than alternatives.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: AquaJEPA — Apply action-conditioned JEPA to underwater robot dynamics with multimodal sensor fusion and explicit sensor validity. The model predicts future latent states conditioned on thruster commands, fusing RGB, sonar, and proprioception.
- **Motivation**: Underwater environments create extreme sensor degradation (turbidity, viewpoint changes, DVL dropout). Standard predictive models fail when key sensors become unreliable. JEPA's latent-space prediction with modality dropout provides inherent robustness.
- **Problem Solved**: AquaJEPA achieves 74 goals (vs. 68 for state-only and recurrent baselines) in 120 paired environments with scheduled DVL loss. Lowest mean final error (0.906 m). Significant paired final-error reductions vs. ordinary multimodal prediction (−0.273 m, 95% CI: 0.190–0.356), supervised dynamics (−0.364 m, 0.260–0.468), and recurrent world model (−0.106 m, 0.025–0.187). Advantage over state-only remains statistically unresolved but directionally positive.

### Academic Context

- **Inheritance / Response**: Extends the JEPA family (I-JEPA, V-JEPA, MC-JEPA) to the underwater domain with multimodal sensor fusion. Builds on prior work in underwater robot dynamics modeling and sensor fusion. The preregistered methodology follows best practices in experimental robotics and psychology.
- **Implicit Connection**: Demonstrates JEPA's core strength — robust latent-space prediction under sensor degradation. The action-conditioned design directly mirrors LeCun's world model module. The finding that JEPA outperforms recurrent world models and supervised dynamics baselines supports the argument that predictive architectures in latent space are more robust than reconstructive approaches.
- **Research Line**: JEPA for Extreme Domains — applying joint-embedding predictive architectures to challenging physical environments where sensor reliability is inherently variable.
- **Future Directions**: Real underwater robot deployment; integration with end-to-end learned planners; extension to multi-robot underwater operations; cross-domain transfer (underwater → terrestrial/aerial).
- **GitHub**: Not found

---

## [2026-07-29] JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation

- **arXiv**: [2607.26600](https://arxiv.org/abs/2607.26600)
- **Authors**: Ionuţ Grigore, Călin-Adrian Popa
- **TL;DR**: Augments standard photometric monocular depth estimation with an I-JEPA-style masked predictive objective in DINOv3 representation space — consistent improvement with zero inference cost.
- **Problem**: Self-supervised monocular depth estimation relies on photometric reconstruction losses that couple depth, pose, and appearance assumptions — a fragile, multi-variable optimization. The challenge is to incorporate a complementary training signal that captures geometric structure without adding inference overhead.
- **Architecture**: JEPADepth — A standard photometric depth pipeline (target image + source image → pose network + depth network → warped reconstruction → photometric loss) augmented with an I-JEPA side objective. A frozen pretrained DINOv3 ViT serves as the target encoder (produces embeddings for masked target regions) and a lightweight predictor (a small transformer) infers these target-region embeddings from visible context-region embeddings under structured block masking. The JEPA loss is computed in DINOv3 representation space. At inference time, both the target encoder branch and the predictor are discarded — only the depth network runs, adding zero deployment cost. Key JEPA characteristics: (1) Predicts in latent representation space, not pixels. (2) Target encoder is frozen (EMA-like behavior). (3) Predictor is lightweight and discarded after training. (4) Structured masking forces the model to learn non-local geometric relationships. On KITTI, the JEPA objective consistently improves over the DINOv3-based photometric baseline. Zero-shot transfer to Make3D and Cityscapes achieves best or near-best performance.
- **Compute Scale**: Mid (24G): DINOv3 ViT backbone. Training on KITTI (standard benchmark). Inference uses only the depth network (no predictor/target encoder), so deployable on smaller hardware.
- **LeCun Alignment**: MEDIUM — Cross-domain JEPA application. STRENGTHS: (1) Directly uses I-JEPA's core mechanism (masked prediction in latent space with discarded predictor) as an auxiliary objective. (2) Proves JEPA representations encode useful geometric information — the masked prediction objective captures spatial relationships beneficial for depth estimation. (3) Zero inference overhead — the JEPA components are discarded, aligning with JEPA's philosophy of learning transferable representations rather than generative decoders. (4) Consistent improvement across benchmarks and zero-shot transfer demonstrates the representation's quality. WEAKNESSES: (1) Not a world model — applies JEPA to a perception task rather than predictive dynamics for planning/control. (2) The primary pipeline is still photometric reconstruction-based; JEPA is auxiliary, not the core learning objective. (3) No action conditioning — purely a static perception task. Overall, JEPADepth is valuable cross-domain validation of JEPA's representational power but does not advance the world model/autonomous intelligence agenda directly.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: JEPADepth — Incorporate an I-JEPA masked predictive objective as a complementary training signal for monocular depth estimation. The JEPA loss operates in DINOv3 representation space, encouraging the depth network to learn features that support geometric prediction.
- **Motivation**: Photometric losses alone couple too many variables (depth, pose, appearance, lighting). A representation-space predictive objective provides a complementary signal focused on structural understanding, disentangled from pixel-level appearance matching.
- **Problem Solved**: Consistent depth estimation improvement on KITTI over photometric-only baselines. Competitive with SOTA transformer-based methods. Strong zero-shot transfer to Make3D and Cityscapes, suggesting the learned representations generalize beyond training distribution.

### Academic Context

- **Inheritance / Response**: Extends I-JEPA (Assran et al., 2023) from pure self-supervised representation learning to task-specific depth estimation. Uses DINOv3 as the representation backbone (following the trend of using DINO-family features for dense prediction tasks). The photometric pipeline follows standard monocular depth estimation work (Monodepth2, etc.).
- **Implicit Connection**: Demonstrates that JEPA-pretrained or JEPA-style objectives capture spatial-geometric structure — a property that would be essential for world models that need to understand 3D scene geometry. The finding that JEPA representations transfer well to depth estimation supports the broader claim that predictive architectures learn structurally meaningful representations. Also validates the "discard the predictor" design pattern — the JEPA component improves training but costs nothing at inference, a key efficiency argument for JEPA over generative approaches.
- **Research Line**: JEPA for Dense Prediction — applying joint-embedding predictive objectives to pixel-level tasks beyond self-supervised pretraining.
- **Future Directions**: Full JEPA-based depth estimation (replace photometric loss entirely); extension to video depth estimation with temporal JEPA objectives; integration with 3D world models for embodied agents.
- **GitHub**: To be checked

---

## [2026-07-28] Rad-JEPA 3D: Radiology Joint-Embedding Predictive Model for 3D Computed Tomography

- **arXiv**: [2607.26196](https://arxiv.org/abs/2607.26196)
- **Authors**: Quoc-Huy Trinh, Minh-Van Nguyen, Ulas Bagci
- **TL;DR**: A JEPA framework for 3D CT volumes using a hybrid H-Mamba encoder (Mamba + grouped-query attention) with Hidden States Orthogonal Regularization (HSOR); 4B params pretrained on 120K scans, achieving SOTA spatial reasoning on Spatial-Med benchmark.
- **Problem**: Existing volumetric medical image encoders (CNNs, ViTs, SSMs) fail to preserve the coarse spatial and geometric structure that downstream reasoning tasks (organ disentanglement, abnormality detection, spatial understanding) depend on. Standard SSL objectives like MAE or contrastive learning don't explicitly enforce spatial-geometric consistency in the learned representations.
- **Architecture**: Rad-JEPA 3D — A joint-embedding predictive framework for 3D CT volumes. The context encoder processes a masked view of a CT volume; the target encoder processes the full volume (or differently masked view). The predictor infers target-region latent features from context-region features. Core architectural innovations: (1) **H-Mamba Encoder**: A hybrid block that fuses a Mamba state-space branch (modeling inter-slice continuity through sequential scanning) with a grouped-query attention (GQA) branch (capturing cross-plane spatial context), combined via a lightweight per-token router. This design captures both the sequential nature of CT slices and the 3D spatial relationships. (2) **Hidden States Orthogonal Regularization (HSOR)**: Aligns student-teacher hidden states throughout the encoder layers, reducing feature redundancy and promoting orthogonal (non-redundant) intermediate representations. This produces more consistent and discriminative volumetric features. Pretrained on ~120,000 CT scans (self-supervised, no labels). At 4.0B total parameters, achieves competitive VQA results and best average spatial-reasoning score on Spatial-Med. Ablations show H-Mamba + HSOR contribute complementary gains; the induced spatial structure can substitute for raw LM scale on volumetric reasoning.
- **Compute Scale**: Large (40G+): 4.0B total parameters. Pretraining on ~120,000 CT scans requires substantial compute. Inference is more efficient due to the Mamba component's linear complexity.
- **LeCun Alignment**: MEDIUM — Cross-domain JEPA for medical imaging. STRENGTHS: (1) Pure JEPA architecture — predicts in latent space from masked context, no pixel reconstruction. (2) The H-Mamba encoder design is an architectural contribution to the JEPA family — exploring state-space models as alternatives to pure transformer encoders for JEPA. (3) HSOR regularization aligns with JEPA's emphasis on preventing representation collapse (like SIGReg, variance regularization) — it's a new regularization technique for the JEPA training dynamics. (4) Demonstrates JEPA scale to 3D volumetric data. WEAKNESSES: (1) Not a world model for planning/control — medical imaging application, not embodied AI. (2) No action conditioning — static volume understanding, not dynamics prediction. (3) The spatial reasoning evaluation is about answering questions about anatomy, not about predicting future states or planning interventions. (4) The 4B parameter scale is large but for a domain-specific application, not a general-purpose world model. Overall, Rad-JEPA 3D is valuable cross-domain validation of JEPA's scalability to 3D data and introduces architectural innovations (H-Mamba, HSOR) that could inform future JEPA designs for embodied world models, but the application domain (diagnostic radiology) is peripheral to the autonomous intelligence agenda.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Rad-JEPA 3D — A JEPA framework for learning volumetric CT representations that preserve spatial-geometric structure. Key contributions: H-Mamba hybrid encoder (Mamba for slice continuity + GQA for cross-plane context) and HSOR (Hidden States Orthogonal Regularization) for reducing feature redundancy.
- **Motivation**: Medical image analysis needs representations that understand 3D spatial relationships (organ positions, abnormalities). Existing encoders lose this structure. JEPA's predictive-in-latent-space approach forces the encoder to capture structural information that supports predicting the full volume from partial views — a natural fit for volumetric understanding.
- **Problem Solved**: Achieves SOTA spatial reasoning on Spatial-Med benchmark despite "compact" 4B parameter size. Demonstrates that JEPA-induced spatial structure can substitute for raw LM scale on volumetric reasoning tasks. H-Mamba + HSOR provide complementary improvements validated through ablation studies.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA and V-JEPA (masked prediction in latent space) and adapts to 3D CT volumes. The Mamba component draws from the state-space model literature (Mamba, Mamba-2) as efficient alternatives to attention for long sequences. HSOR is a novel regularization technique for JEPA training. Evaluated against medical VLM benchmarks (Spatial-Med, closed-ended VQA).
- **Implicit Connection**: The H-Mamba architecture is interesting for embodied world models — Mamba's linear complexity could enable efficient processing of long video sequences, and the hybrid attention+Mamba design could balance local continuity (Mamba on temporal dimension) with global spatial context (attention on spatial dimensions). HSOR (layer-wise orthogonal regularization) addresses a key JEPA training challenge — preventing feature collapse and ensuring the encoder learns diverse, non-redundant representations. This connects to broader JEPA research on regularization (SIGReg, variance regularization, Gaussian embeddings). The finding that JEPA representations can substitute for LLM scale on spatial reasoning suggests JEPA captures structure that LLMs miss — relevant to the debate about LLMs as world models.
- **Research Line**: 3D JEPA — extending joint-embedding predictive architectures from 2D images and videos to volumetric data with specialized encoder architectures for spatial-geometric reasoning.
- **Future Directions**: Temporal extension for 4D CT (3D + time); application to surgical planning (action-conditioned prediction); integration with robotic surgery world models; HSOR adapted for video JEPA training.
- **GitHub**: To be checked

---

## [2026-07-30] CS-JEPA: One Future, Every Robot — Label-Efficient Collective-State Prediction with Decentralized JEPA

- **arXiv**: [2607.28443](https://arxiv.org/abs/2607.28443)
- **Authors**: Alan-Barsag Gazzaev, Alexey Garvilov, Sergey Muravyov
- **TL;DR**: Introduces Collective-State JEPA (CS-JEPA), a recurrent decentralized JEPA where every robot in a swarm predicts the same future collective state from only local observations and bandwidth-limited messages — no global pooling, no target encoder, no episode clock.
- **Problem**: Multi-robot swarms need to predict future collective states for planning, but existing approaches either require centralized coordination (bottleneck), full future-action knowledge (unrealistic), or global pooling (bandwidth-expensive). Decentralized prediction from local observations alone is an open challenge, especially under topology and swarm-size shifts.
- **Architecture**: CS-JEPA — A recurrent joint-embedding predictive architecture distributed across robots. Each robot uses a 16-frame local history and exchanges one 64-float recurrent message per directed edge. The predictor at each robot outputs a common future token field representing the collective state. Key JEPA characteristics: (1) No target encoder — the target is the shared future representation itself. (2) No decoder/reconstruction — operates purely in latent space. (3) Pretrained without downstream collective labels; evaluated via ridge probes on as few as 6 globally labeled episodes. (4) Action-conditioned variant receives candidate plans and produces receiver-local predictive representations for planning. Against raw-future reconstruction baselines with matched capacity, CS-JEPA reduces branch-value MSE by 45.5% and improves candidate-score correlation by 0.1291 — all effects favorable in 8/8 outer seeds including unseen N=32.
- **Compute Scale**: Small (8-12G): Decentralized per-robot deployment. Each robot runs a lightweight recurrent predictor; 16-frame history + 64-float messages. Designed for bandwidth-limited swarm deployment, not datacenter training.
- **LeCun Alignment**: HIGH — Direct JEPA implementation for embodied multi-agent systems. Three core LeCun-aligned properties: (1) Operates purely in latent predictive space (no pixel reconstruction). (2) Label-efficient via self-supervised pretraining — learns useful representations from unlabeled interaction data and requires only handful of labeled episodes for task transfer. (3) Planning-relevant — the action-conditioned variant produces representations that improve candidate-score correlation, directly supporting model-predictive control in the latent space. The decentralized architecture with no target encoder is a novel twist on JEPA that demonstrates its applicability beyond single-agent settings. The finding that JEPA targets serve as "label-efficient primitives" validates LeCun's claim that predictive architectures extract more useful representations per data point than reconstructive alternatives.
- **GitHub**: Not found (submitted to IEEE ICRA 2027)

### What / Why / Solve

- **Proposal**: CS-JEPA — Decentralized JEPA where every robot outputs the same future collective representation using only local observations and lightweight edge messages. The common-future target serves as a self-supervised signal that produces representations useful for both state prediction and planning.
- **Motivation**: Swarm robotics needs decentralized prediction. Centralized approaches don't scale; reconstruction-based approaches waste capacity on irrelevant details; and label-dependent approaches require impossible amounts of human annotation. JEPA's predictive-in-latent-space approach solves all three: decentralized by design, efficient by avoiding reconstruction, and label-efficient through self-supervised pretraining.
- **Problem Solved**: 45.5% MSE reduction in branch-value estimation. Outperforms reconstruction baselines in prediction error and inter-robot agreement across in-distribution, ring, mutual-kNN, and unseen-size topologies up to 108 robots. All effects favorable across independent seed groups (5/5 outer seeds for prediction, 8/8 for planning).

### Academic Context

- **Inheritance / Response**: Extends JEPA from single-agent (I-JEPA, V-JEPA, MC-JEPA) to multi-agent decentralized settings. The recurrent architecture with edge-based messaging draws from graph neural network literature but adapts it to the JEPA predictive framework. The "common future token field" concept is a novel contribution — it's the JEPA equivalent of a shared world state in multi-agent systems.
- **Implicit Connection**: The decentralized JEPA architecture mirrors LeCun's configurator module concept at the swarm level — each robot maintains a local predictive model that converges to a shared representation of the collective future. The elimination of the target encoder (a key JEPA design choice) is maintained in the decentralized setting through the common-future target. This paper also connects to the growing literature on JEPA for physical systems (SkyJEPA, Depth-Regularized JEPA) by demonstrating JEPA's value for real-world robotic deployment under communication constraints.
- **Research Line**: Multi-Agent JEPA — extending predictive architectures from single-agent to distributed, decentralized settings.
- **Future Directions**: Integration with hierarchical planning (Hi-LeWM style) for swarm-level objectives; heterogeneous robot teams with different sensor modalities; real-world deployment on physical robot swarms; combining with belief-state JEPA (UWM-JEPA) for partial observability in adversarial environments.
- **GitHub**: To be checked (ICRA 2027 submission)

---

## [2026-07-30] PhiZero: A World Model Built Around Physical Language

- **arXiv**: [2607.28624](https://arxiv.org/abs/2607.28624)
- **Authors**: Shuyao Shang, Yuqi Wang, Ruopeng Gao, Xu Chen, Tieniu Tan, Lue Fan, Zhaoxiang Zhang
- **TL;DR**: Proposes PhiZero, a physical world model using "physical language" — compact discrete tokens representing world-state transitions — with a reason-then-render paradigm: first infer future evolution as a physical-language sequence via a VLM, then render into videos via diffusion.
- **Problem**: Existing physical world models predict future videos directly in pixel space, leaving underlying dynamics implicit within high-dimensional visual representations. This incurs prohibitive generative costs and prioritizes pixel-level realism over physical plausibility. The challenge is to learn explicit, abstract representations of world dynamics that can support reasoning without being entangled with appearance.
- **Architecture**: PhiZero — Two-stage architecture: (1) **Physical Language Tokenizer**: Encodes video transitions into compact discrete tokens using a transition-level Q-Former encoder. A diffusion-prior decoder reconstructs videos from tokens + first frame (flow-matching objective). Trained self-supervised on 10K hours of in-the-wild videos with curriculum learning. (2) **Physical Language Reasoner**: A pretrained VLM fine-tuned to reason about future world evolution in the physical language token space. Given past physical-language context and first frame, it autoregressively predicts future physical-language sequences. The reason-then-render paradigm separates dynamics reasoning (in discrete token space) from appearance rendering (in pixel space via diffusion). Applications demonstrated: physically realistic video world modeling, fine-grained action-conditioned simulation, zero-shot cross-embodiment motion transfer.
- **Compute Scale**: Large (40G+): VLM reasoner + diffusion decoder. Training: 10K hours video pretraining + VLM fine-tuning. Inference: autoregressive token generation + diffusion-based rendering.
- **LeCun Alignment**: MEDIUM — Mixed alignment. STRENGTHS: (1) Explicitly critiques pixel-space prediction as the wrong objective for world models — directly echoes LeCun's core argument. (2) Separates dynamics reasoning from appearance rendering — the physical language is an abstract representation of transitions, conceptually similar to JEPA's latent space. (3) Self-supervised learning from in-the-wild video — no action labels needed. WEAKNESSES: (1) Still renders pixels via diffusion decoder — LeCun argues this is wasteful and the wrong target. (2) Uses a pretrained VLM/LLM for the reasoning component — LeCun's vision treats language as a separate module, not the core reasoning engine. (3) The discrete token representation with autoregressive prediction is closer to LLM-style next-token prediction than JEPA's continuous latent prediction. (4) The physical language is discovered through reconstruction pressure (tokenizer must reconstruct videos), not purely through predictive objectives. Overall, PhiZero shares the critique but takes a different solution path — discrete symbolic reasoning + generative rendering rather than continuous predictive architectures.
- **GitHub**: Project page: [phi-zero.github.io](https://phi-zero.github.io)

### What / Why / Solve

- **Proposal**: PhiZero — Learn a compact discrete "physical language" from unlabeled videos that captures world-state transitions. Use a VLM to reason about future evolution in this language space, then render the predicted transitions into videos. The key insight: separate the "what happens" (physical language reasoning) from the "what it looks like" (appearance rendering).
- **Motivation**: Humans don't memorize pixel-level visual outcomes — they abstract patterns into generalizable knowledge and reason symbolically. Current video world models do the opposite: they memorize pixels and hope dynamics emerge implicitly. Physical language provides an explicit symbolic space for dynamics reasoning while the rendering module handles appearance.
- **Problem Solved**: Demonstrates physically coherent world evolution across generation and understanding benchmarks. Shows applications in realistic world modeling, action-conditioned simulation, and zero-shot motion transfer. The discrete bottleneck forces the tokenizer to capture transition-relevant information while the first-frame conditioning provides static appearance, achieving a form of dynamics-appearance disentanglement.

### Academic Context

- **Inheritance / Response**: Builds on video tokenization (VQ-VAE, MAGVIT), video generation (Sora, diffusion models), and latent-action world models. The physical language concept can be seen as a learned action representation — the tokens describe "what changed" between frames, similar to how latent action models (LAMs) learn action representations. The VLM-as-reasoner approach connects to the growing trend of using LLMs as world models, but PhiZero constrains the LLM to operate in a learned physical token space rather than natural language.
- **Implicit Connection**: PhiZero is an interesting counterpoint to JEPA. Both critique pixel-space prediction and advocate for abstract representations of dynamics. But they diverge on the representation: JEPA uses continuous latent vectors with energy-based regularization; PhiZero uses discrete tokens with autoregressive prediction. This tension — discrete vs. continuous, symbolic vs. subsymbolic — is central to the world model debate. PhiZero's approach is more compatible with the current LLM ecosystem (VLM fine-tuning, token-based interfaces) but may inherit the limitations of autoregressive discrete prediction that LeCun has criticized (error accumulation, lack of continuous planning gradients). The rendering decoder (diffusion) is also fundamentally at odds with JEPA's reconstruction-free philosophy.
- **Research Line**: Symbolic World Models — representing world dynamics through learned discrete tokens, bridging the gap between neural world models and classical symbolic AI approaches to planning and reasoning.
- **Future Directions**: Replacing the diffusion decoder with a JEPA-style latent predictor (no rendering); using the physical language tokens directly for planning in token space without rendering; combining with action-conditioned JEPA for a fully latent pipeline; scaling physical language to real robot data.
- **GitHub**: Project page: [phi-zero.github.io](https://phi-zero.github.io)

---

## [2026-07-30] QQWorld: Quantile-Quantile Matching for World Model Regularization

- **arXiv**: [2607.28415](https://arxiv.org/abs/2607.28415)
- **Authors**: Zhoushun Yu, Xiaoyu Hu, Xiangyu Xu
- **TL;DR**: Replaces LeWM's Epps-Pulley regularization with quantile-quantile matching — EP's corrective gradients vanish for tail samples, while QQ matching maintains effective tail control, directly improving planning success rates across four control environments.
- **Problem**: LeWorldModel (LeWM) regularizes latent distributions toward isotropic Gaussian using the Epps-Pulley (EP) objective. However, EP's corrective gradients rapidly vanish for isolated tail samples, leaving heavy-tailed latent deviations insufficiently controlled. These fat tails degrade planning because extreme latent values produce unpredictable dynamics rollouts.
- **Architecture**: QQWorld — Replaces EP with a quantile-quantile (QQ) matching objective: projected latent samples are directly aligned with rank-matched Gaussian quantiles, maintaining effective corrective gradients even in the tails. Cross-batch QQ enlarges the effective ranking pool using detached samples from previous batches, with a characterized bias-variance trade-off. The encoder-predictor backbone is unchanged from LeWM; only the regularization term is replaced.
- **Compute Scale**: Small-Mid (8-24G): Four LeWM control environments. Cross-batch QQ adds negligible memory overhead.
- **LeCun Alignment**: HIGH — Directly improves a core architectural component of the JEPA/LeWM stack. The finding that EP's tail-control failure is structural (not a hyperparameter issue) suggests LeWM's current regularization may be fundamentally limited. QQ matching provides a principled fix that preserves the isotropic-Gaussian prior while ensuring all samples — including outliers — receive effective regularization gradients. This is a classic example of the kind of architectural refinement the JEPA program needs: identify where the inductive bias fails and replace it with a better one, without changing the overall predictive-architecture philosophy.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: QQWorld — Replace Epps-Pulley regularization in LeWM with quantile-quantile matching. QQ aligns projected latents with Gaussian quantiles directly, maintaining non-vanishing corrective gradients for all samples including tail outliers.
- **Motivation**: The Epps-Pulley test statistic used in LeWM measures distributional discrepancy but provides weak correction signals for samples far from the distribution center. In practice, latent world models develop heavy tails that EP cannot control, and these tails cause planning failures because extreme latent values cascade through multi-step rollouts.
- **Problem Solved**: QQWorld improves average planning success rate over LeWM across four control environments, while consistently yielding better Gaussian alignment and thinner latent tails. Cross-batch QQ further stabilizes training by enlarging the ranking pool.

### Academic Context

- **Inheritance / Response**: Builds directly on LeWorldModel (2603.19312). The EP→QQ replacement is a drop-in improvement — same encoder-predictor backbone, different regularization term. This makes adoption straightforward.
- **Implicit Connection**: The regularization quality of JEPA world models has been an under-explored dimension. Most work focuses on architectures (LeWM, INTACT, TD-JEPA) but assumes the SIGReg/EP regularization is sufficient. QQWorld shows it isn't — and provides a principled alternative. The QQ approach is conceptually related to the distribution-matching philosophy behind SIGReg but operates in quantile space rather than moment space, giving it better tail sensitivity.
- **Research Line**: JEPA Regularization — improving the anti-collapse and distribution-shaping mechanisms in predictive architectures.
- **Future Directions**: Integration with other JEPA variants (V-JEPA, action-conditioned JEPA); theoretical analysis of optimal latent distribution shape for planning; adaptive QQ targets that evolve during training.
- **GitHub**: To be checked

---

## [2026-07-30] QuantWAMs: Calibrating at the Right Granularity for World Action Models

- **arXiv**: [2607.28405](https://arxiv.org/abs/2607.28405)
- **Authors**: Jiacheng Zhou, Jinfan Lv, Ruixuan Li, Longtai Zhang, Yan Wang, Wenqiang Zhang, Lizhe Qi
- **TL;DR**: A post-training quantization (PTQ) framework specifically designed for World Action Models — aligning quantization decisions with WAM-specific structure (denoising, rollout distribution, task objective) to preserve deployment accuracy within 0.2–0.7pp of FP16 while reducing memory to 29%.
- **Problem**: WAMs jointly predict future observations and actions via iterative denoising and closed-loop execution, making efficient deployment costly. Existing PTQ methods fail for WAMs because they: (1) use open-loop objectives that ignore the closed-loop rollout distribution, (2) treat all modules homogeneously despite heterogeneous sensitivity, (3) use calibration distributions that don't match deployment conditions.
- **Architecture**: QuantWAMs — Three WAM-specific strategies: (1) **Shared-basis outlier calibration**: pools activation evidence only across coordinate-compatible modules to catch deployment-specific outliers. (2) **Co-training-objective saliency**: computes empirical-Fisher scores from the joint video-action gradient, assigning weight precision at calibration-stable layer granularity. (3) **Fixed-intervention rollout auditing**: revises denoising-step protection schedules using reachable closed-loop states without changing the precision budget. Evaluated on Fast-WAM and LingBot-VA across RoboTwin 2.0, LIBERO, and real-robot AgiBot G2 manipulation.
- **Compute Scale**: Large (40G+): WAM backbones. Quantization reduces peak weight-and-activation memory to ~29% of FP16, providing 1.4–1.6× block-level speedups.
- **LeCun Alignment**: MEDIUM — Deployment engineering for WAMs. While not advancing core world model theory, efficient deployment is critical for the embodied AI vision LeCun advocates. WAMs that can't run on embedded hardware are irrelevant for real-world autonomous systems. QuantWAMs demonstrates that WAMs can be compressed to practical levels with minimal accuracy loss — a necessary condition for the vision of always-on, real-time world models in robots.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: QuantWAMs — A WAM-specific PTQ framework that aligns quantization decisions with three deployment realities: model structure (which modules are coordinate-compatible), rollout distribution (what states the model actually encounters in closed loop), and task objective (what matters for the joint video-action prediction).
- **Motivation**: WAMs are computationally heavy at deployment. Without efficient quantization, they can't run on robot-embeddable hardware. But naive quantization destroys WAM performance because their iterative denoising amplifies quantization errors across steps, and their closed-loop execution means calibration distributions must match deployment, not training.
- **Problem Solved**: Under W4A4-dominant quantization, simulation means differ from FP16 by only 0.2–0.7pp. Real-robot trials confirm deployment feasibility on three manipulation tasks with an AgiBot G2. Memory reduced to ~29% of FP16.

### Academic Context

- **Inheritance / Response**: Extends PTQ methodology to the WAM domain. Builds on Fast-WAM, LingBot-VA, and the broader WAM deployment literature. The WAM-specific calibration strategies (rollout auditing, co-training saliency) are novel contributions.
- **Implicit Connection**: Efficiency is a prerequisite for LeCun's vision of autonomous intelligence. A world model that requires a datacenter GPU defeats the purpose of embodied deployment. QuantWAMs addresses this practical bottleneck. The rollout auditing strategy (using closed-loop states for calibration) echoes the closed-loop nature of LeCun's agent architecture where perception → world model → actor form a tight loop.
- **Research Line**: Efficient WAM Deployment — making world action models practical for real-world embodied systems.
- **Future Directions**: Integration with JEPA-based WAMs (currently evaluated on diffusion-based WAMs); hardware-aware quantization for specific robot platforms; quantization-aware training for WAMs.
- **GitHub**: To be checked

---

## [2026-07-30] ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations

- **arXiv**: [2607.28362](https://arxiv.org/abs/2607.28362)
- **Authors**: Jin Cao, Zian Meng, Kaipeng Zhang
- **TL;DR**: Creates "shadow pairs" — video pairs replaying the same dynamics under independently resampled appearance — and learns a unified dynamics representation via cross-shadow prediction, enabling any-action control of video world models without action labels, motion estimators, or fine-tuning (86% blinded win rate).
- **Problem**: Interactive video world models need precise action control, but existing interfaces either: (1) encode actions loosely (text descriptions), leaving the model to improvise how the action unfolds, or (2) encode actions through structured signals (joint angles, optical flow) that serve only one dynamics family and are hard to acquire. Demonstration videos specify any dynamics frame-by-frame, but the dynamics are entangled with appearance — actions learned from one scene don't transfer to another.
- **Architecture**: ShadowDancer — Two key innovations: (1) **Shadow pairs**: video pairs that replay the same underlying dynamics under independently resampled appearance, constructed at scale via a Shadow Library. A dynamics family becomes controllable exactly when such pairs can be constructed. (2) **Cross-shadow prediction**: learns actions by predicting one shadow video from the other — whatever the pairing resamples (appearance) is discarded by construction, and whatever it preserves (dynamics) becomes the action. This yields a unified dynamics representation that drives a block-causal world model. Any demonstrated clip becomes a reusable action asset, replayable in new environments without labels or fine-tuning.
- **Compute Scale**: Mid-Large (24-40G+): Video world model with cross-shadow prediction. Shadow pair construction is a data preprocessing cost, not an inference cost.
- **LeCun Alignment**: MEDIUM — Uses generative video world models (pixel prediction) rather than JEPA-style latent prediction, which places it in the counterpoint category. However, the core insight — learning dynamics representations that are invariant to appearance — aligns deeply with LeCun's emphasis on abstract, reusable world knowledge. The cross-shadow prediction objective is conceptually similar to JEPA: predict one representation (shadow B's video) from another (shadow A's video + context), discarding nuisance factors (appearance). The unified dynamics representation could potentially be learned in latent space (JEPA-style) rather than pixel space. The block-causal architecture also echoes temporal-JEPA designs.
- **GitHub**: [ShadowDancer-1.github.io](https://ShadowDancer-1.github.io)

### What / Why / Solve

- **Proposal**: ShadowDancer — Build "shadow pairs" (same dynamics, different appearance) and learn actions via cross-shadow prediction that is invariant to appearance by construction. Any demonstration video becomes a reusable action asset for controlling the world model in new environments.
- **Motivation**: The fundamental challenge in interactive world models is the action interface. Text is too loose, structured signals are too narrow, and demonstrations are too appearance-bound. Shadow pairs solve this by providing a data construction principle that makes dynamics separable from appearance without requiring action labels or motion capture.
- **Problem Solved**: Improved action transfer and long action rollout over latent-action and interactive world model baselines across diverse dynamics families. Average blinded win rate of 86% in rollout comparisons.

### Academic Context

- **Inheritance / Response**: Builds on interactive video world models (Genie, etc.), latent action models, and video-to-video translation. The shadow-pair construction is a novel data-centric approach to the appearance-dynamics disentanglement problem.
- **Implicit Connection**: The cross-shadow prediction objective has a JEPA-like structure: predict target (shadow B) from context (shadow A), with the prediction target being another representation of the same underlying dynamics. If implemented in latent space rather than pixel space, this would be a JEPA variant. The unified dynamics representation that emerges is exactly the kind of abstract, reusable action representation that LeCun's modular agent architecture needs for the actor module.
- **Research Line**: Appearance-Invariant World Models — learning dynamics representations that transfer across visual domains.
- **Future Directions**: JEPA-style latent cross-shadow prediction (replacing pixel-space prediction); integration with real-robot world models; scaling the Shadow Library to internet-scale video.
- **GitHub**: [ShadowDancer-1.github.io](https://ShadowDancer-1.github.io)

---

## [2026-07-29] What Can Latent World Models Know? Physical Parameter Identifiability in Multimodal Predictive Representations

- **arXiv**: [2607.27017](https://arxiv.org/abs/2607.27017)
- **Authors**: Kaizhen Tan, Xin Xu, Siru Tao, Hanzhe Hong, Yang Feng, Heqing Du
- **TL;DR**: Demonstrates via controlled POKEWORLD interventions that a latent world model's prediction TARGETS (not data scale) determine which physical parameters enter the representation — and single-step vision-only prediction discards even perfectly visible object state.
- **Problem**: The central premise of latent world models is that predicting the future forces the representation to internalize physics. But which physical quantities actually enter the latent, and what determines this? Without answering this, we don't know what world models actually know.
- **Architecture**: POKEWORLD — an interactive environment with visually identical objects that hide mass, drag, and contact stiffness. Uses a certificate-gated protocol: first certify each parameter is recoverable from raw observations, then measure whether it enters the latent. Key findings: (1) Inputs limit what can be known, but prediction targets decide what is retained. (2) Stiffness enters the latent only when touch is forecast (R²=0.50 vs -0.02 when merely fused into input). (3) Single-step vision-only prediction discards even perfectly visible object state. (4) Drag carries 0.89 recoverability certificate yet plateaus near 0.13 under every deterministic prediction objective. (5) On RH20T (4,258 episodes, 2 robots), only the full multimodal objective forecasts force beyond persistence baseline — and these gains grow with scale. The fundamental finding: objective structure determines WHICH physical parameters a latent acquires; additional data only improves parameters it ALREADY acquires.
- **Compute Scale**: Small-Mid (8-24G): Controlled POKEWORLD interventions + RH20T scaling curves across two robots and 4,258 episodes.
- **LeCun Alignment**: HIGH — Foundational paper for the JEPA/world model research program. Proves that prediction targets (not data volume) govern what physics world models learn. Directly validates LeCun's emphasis on multimodal prediction (vision + touch + force) as essential for acquiring complete physical understanding. The finding that vision-only prediction discards object state is a powerful argument against purely visual world models and for the multimodal sensor fusion LeCun advocates. Critical empirical grounding for the "what does a world model know?" question.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Use controlled interventions in POKEWORLD + RH20T scaling curves to create an "identifiability map" — showing exactly which physical parameters enter a world model's latent representation under different prediction objectives and data scales.
- **Motivation**: The world model community assumes more data = better physics. This paper shows that assumption is wrong: a latent world model will NEVER acquire certain physical parameters regardless of data scale if the prediction objective doesn't demand them. This is the "frontier" problem — some physics is fundamentally inaccessible to certain objectives.
- **Problem Solved**: Provides the first systematic empirical map of physical parameter identifiability in latent world models. Establishes that prediction targets (not data scale) are the binding constraint. Shows that multimodal prediction (vision + proprioception + force) is necessary for acquiring complete physics. Identifies "drag" as a parameter class that fundamentally challenges deterministic prediction objectives.

### Academic Context

- **Inheritance / Response**: Builds on JEPA/world model literature, identifiability theory (2607.22430), and multimodal world models. The certificate-gated protocol is a methodological contribution for future identifiability studies.
- **Implicit Connection**: This paper provides the empirical complement to the theoretical identifiability work (2607.22430) and the evaluation critique (2607.10362). Together they form a trilogy: identifiability tells us what CAN be learned, this paper tells us what ACTUALLY gets learned under different objectives, and the control theory paper tells us whether what's learned supports planning.
- **Research Line**: World Model Identifiability — empirical investigation of what physics predictive objectives actually extract.
- **Future Directions**: Extend to more complex physics (friction models, deformables); test with JEPA-style objectives rather than reconstruction-based ones; develop objectives that explicitly target currently-unacquired physics (like drag).
- **GitHub**: To be checked

---

## [2026-07-29] DLAM: Distributional Latent Actions with Temporal Constraints

- **arXiv**: [2607.27138](https://arxiv.org/abs/2607.27138)
- **Authors**: Zuojin Tang, Feifan Luo, Haoyun Liu, Botai Yuan, Dekang Qi, Ronghan Chen, Yandan Yang, Tong Lin, Xinyuan Chang, Mu Xu, Bin Liu, De Ma, Zhiheng Ma
- **TL;DR**: Replaces deterministic latent action codes with diagonal Gaussian distributions, adding normalized temporal constraints (composition + reversal over equal-gap triplets) — the learned variance and correlation-aware composition improve downstream control while the flow-matching policy operates reconstruction-free on frozen encoders.
- **Problem**: Latent action models (LAMs) extract action priors from action-free videos, but reconstruction-trained codes may lack the temporal structure required for joint generation with robot actions. Existing structured methods add temporal constraints but retain deterministic transition points, so residual errors propagate and compound under recursive composition.
- **Architecture**: DLAM — Three innovations: (1) **Distributional representation**: each transition is a diagonal Gaussian — the mean grounds in observed visual change (via reconstruction conditioned on reference frame), and the variance captures transition uncertainty. (2) **Temporal constraints**: normalized composition (how two consecutive latents compose) and reversal (negating the mean while preserving variance) over equal-gap triplets constrain both the mean and dimension-wise variance. Variance composition uses a lightweight shared-correlation coefficient to account for dependence between adjacent transitions sharing an intermediate frame. (3) **Reconstruction-free policy**: For downstream learning, the encoder is frozen and a flow-matching policy jointly generates mean transition sequences and robot actions — no reconstruction needed at deployment. Evaluated on MetaWorld MT50, LIBERO, and real-world manipulation.
- **Compute Scale**: Mid (24G): Encoder training + flow-matching policy. Reconstruction-free at deployment.
- **LeCun Alignment**: MEDIUM-HIGH — The reconstruction-free downstream policy (operating purely in latent space) aligns with JEPA's philosophy. The distributional approach addresses the "multiple valid futures" problem that JEPA faces (cf. 2607.23531 on JEPA Paradox in language). However, the encoder is still trained with reconstruction, making this a hybrid rather than pure-JEPA approach. The temporal constraint design (composition + reversal) is a principled way to inject physical structure into learned dynamics.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: DLAM — Move from deterministic latent actions to distributional ones (Gaussian mean + variance), constrain the distributions with physically-motivated temporal rules (composition, reversal), and deploy with a reconstruction-free flow-matching policy.
- **Motivation**: Deterministic LAMs can't express uncertainty about transitions — when a latent action is ambiguous (common in real videos), forcing a single point estimate injects error that compounds across multi-step rollouts. Distributional codes with learned variance let the model express uncertainty, and temporal constraints regularize how uncertainties compose.
- **Problem Solved**: DLAM learns more temporally consistent latent dynamics than existing LAM baselines. Under controlled π₀ transfer protocol, improves policy performance on MetaWorld MT50, LIBERO, and real-world manipulation. Ablations show normalized mean constraints account for most reconstruction gain, while learned variance and correlation-aware composition provide complementary improvements in downstream control.

### Academic Context

- **Inheritance / Response**: Builds on LAM literature (including WALA 2607.11397, CD-LAM 2607.09185, OTF-LAM 2606.30544). The distributional approach addresses the same fundamental issue as the JEPA Paradox paper (2607.23531): when multiple futures are valid, a deterministic point prediction is wrong.
- **Implicit Connection**: DLAM represents a convergence point between LAM research and JEPA philosophy. The reconstruction-free downstream policy mirrors JEPA's latent-space operation, while the distributional transition model addresses a limitation of deterministic JEPA predictors.
- **Research Line**: Distributional World Models — moving from deterministic to probabilistic latent dynamics.
- **Future Directions**: Pure JEPA-style training (no reconstruction objective); learned correlation structures beyond diagonal Gaussians; integration with planning algorithms that exploit transition variance for risk-aware control.
- **GitHub**: To be checked

---

## [2026-07-26] Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models

- **arXiv**: [2607.23602](https://arxiv.org/abs/2607.23602)
- **Authors**: Liangyu Li, Qingwen Liu, Mingqing Liu
- **TL;DR**: Proves that standard latent-cost-based action selection in world model MPC systematically fails — residual prediction error gives infeasible sequences anomalously low costs, and larger proposal pools make this WORSE. Introduces ASAR (Adjacent Set Action Reconstruction) which recovers feasible actions from the density of adjacent proposals, improving success by 18.7–28.0pp.
- **Problem**: World model MPC selects actions by: (1) sample many action sequences, (2) predict their terminal cost via the world model, (3) pick the cheapest. This rule can fail even when the terminal cost PERFECTLY reflects the true task objective — residual prediction error gives infeasible sequences anomalously low costs, and more proposals give more chances for such errors to outrank feasible alternatives ("proposal overgeneration").
- **Architecture**: ASAR — Adjacent Set Action Reconstruction. Instead of blindly trusting the minimum-cost proposal, ASAR (1) measures density from standardized early action prefixes among low-cost proposals, (2) reconstructs a full sequence from an adjacent set with a light anchor from the minimum-cost sequence. This exploits the insight that feasible actions tend to cluster in action space even when their predicted costs are unreliable. Three variants: Kernel ASAR (best), Distance ASAR, and Prefix ASAR. Evaluated on Cube and Carry-and-Release benchmarks.
- **Compute Scale**: Small-Mid (8-24G): Cube + Carry-and-Release benchmarks. Modest computational overhead (density estimation on proposal pool).
- **LeCun Alignment**: HIGH — This paper provides the strongest empirical demonstration yet that the standard "predict → rank → select" pipeline in world model planning is fundamentally broken. The finding that larger proposal pools can REDUCE selection reliability directly challenges current MPC practices. Supports the search-free planning direction pursued by INTACT (2607.26056) and TD-JEPA (2607.25337). The ASAR approach — using structure in the action space rather than trusting predicted costs — suggests a principled alternative.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: ASAR — Replace minimum-cost selection with adjacency-based reconstruction. Identify clusters of similar action proposals, and reconstruct the final action from adjacent proposals rather than trusting the single lowest-cost one.
- **Motivation**: In Cube candidate execution audits, increasing the proposal budget from 72 to 288 reduces the feasibility of minimum-cost selection from 0.375 to 0.062 for position targets — even though EVERY larger pool contains a feasible sequence. More computation makes the planner WORSE. This is a structural failure.
- **Problem Solved**: Kernel ASAR improves event completion success by 18.7–28.0pp over standard minimum-cost selection across proposal budgets (72/144/288). Even trajectory reachability cost (a better cost function) still benefits from ASAR (+17.3–20.0pp). Analysis characterizes selection risk, separation by radius support statistic, and sequence containment under local feasibility.

### Academic Context

- **Inheritance / Response**: Directly challenges the core planning loop used by Dreamer, TD-MPC, LeWM, and all MPC-based world model planners. Connects to the growing critique of prediction-based evaluation (2607.10362, 2607.16591, 2607.14169).
- **Implicit Connection**: Together with INTACT (search-free planning) and TD-JEPA (plan-aware representations), this paper contributes to a growing consensus that the standard MPC-over-latent-world-model pipeline needs fundamental redesign.
- **Research Line**: World Model Planning Critique — identifying and fixing structural failures in sampling-based planning.
- **Future Directions**: Integration with search-free planners (INTACT-style); learned adjacency metrics; extension to continuous action spaces.
- **GitHub**: To be checked

---

## [2026-07-25] WCM: World-Cognition Model for Generalizable Human-Robot Interaction

- **arXiv**: [2607.22999](https://arxiv.org/abs/2607.22999)
- **Authors**: Yuzhen Chen, KC Zhou
- **TL;DR**: A human-centered embodied agent built on the modular SLAK architecture (Sensing, Logic, Action, Knowledge) with asynchronous runtime and human-in-the-loop teaching mode — achieving 73.8% across 9 real-world HRI tasks including long-horizon tasks learned through interactive teaching.
- **Problem**: Current robot-control paradigms (VLA policies, world-model-based planners) are optimized for instruction execution, leaving users with little visibility into WHY an action is chosen and few mechanisms to redirect, correct, or teach the robot through interaction.
- **Architecture**: WCM (World-Cognition Model) — Built on SLAK: four separated modules (Sensing, Logic, Action, Knowledge) communicating through an asynchronous runtime that allows reasoning, dialogue, and execution to proceed concurrently. Key innovation: human-in-the-loop teaching mode where teaching episodes and autonomous task rollouts are refined into chain-of-thought supervision for continual improvement. The SLAK architecture's modular decomposition echoes LeCun's modular agent design (perception → world model → cost → actor).
- **Compute Scale**: Mid (24G): Modular architecture — perception/reasoning/control/memory run concurrently on GPU.
- **LeCun Alignment**: MEDIUM — The SLAK architecture's modular decomposition aligns with LeCun's modular agent architecture. The human-in-the-loop teaching mode connects to how world models acquire knowledge. However, WCM is not a latent predictive world model — it's an HRI architecture that uses world models as a component.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: WCM — A modular embodied agent architecture (SLAK) that separates perception, reasoning, control, and memory, connected through an asynchronous runtime. Adds human-in-the-loop teaching mode for continual improvement from interaction.
- **Motivation**: Robots deployed in human environments need to be teachable, interpretable, and responsive to real-time human feedback. Current systems are black boxes optimized for autonomous execution.
- **Problem Solved**: 73.8% average success across 9 real-world HRI tasks, including tasks held out from CoT fine-tuning and a long-horizon task learned entirely through interactive teaching.

### Academic Context

- **Inheritance / Response**: Builds on VLA models, world model planners, and HRI literature. The SLAK architecture is a practical instantiation of modular agent design principles.
- **Implicit Connection**: The SLAK decomposition mirrors LeCun's modular agent architecture. The asynchronous runtime addresses a practical concern: how modules coordinate in real time. The human teaching mode raises the question of whether world models should learn from human feedback.
- **Research Line**: Interactive World Models — making world models teachable and interpretable for human interaction.
- **Future Directions**: Integration with JEPA-based predictive world models; multi-modal teaching signals.
- **GitHub**: To be checked

---

## [2026-07-29] Mental World Modeling

- **arXiv**: [2607.27201](https://arxiv.org/abs/2607.27201)
- **Authors**: Hao Fei, Yiran Zhao
- **TL;DR**: Extends world models beyond physical prediction to include hidden mental states (beliefs, intentions, desires) as first-class components — a coupled physical-mental world state — necessary for predicting human behavior in social scenarios. Introduces MENTIS baseline evaluated on text, image, and video decision scenarios.
- **Problem**: Existing world models answer only physical questions (what/where/how will it evolve). But human behavior is driven by hidden mental states — beliefs, wants, intentions, social norms. A model tracking only the physical scene predicts the wrong action for the right-looking scene.
- **Architecture**: MWM (Mental World Modeling) — Generic theoretical framework with coupled physical-mental world state. Maintains physical + mental state (beliefs, desires, intentions for each agent), renders target-specific partial observations, and simulates how candidate actions jointly update both components. MENTIS is a training-free, LLM-based baseline that decomposes the process into state parsing, target-observation generation, action decomposition, coupled physical+mental transition, and branch-level value evaluation. Tested on 8 modern LLM-based world models across text, image, and video story scenarios.
- **Compute Scale**: Small (8-12G): LLM-based world model inference; manually constructed dataset of situated decision scenarios.
- **LeCun Alignment**: MEDIUM — The idea of extending world models to mental states is conceptually aligned with LeCun's vision of agents that understand other agents (theory of mind). However, the implementation is LLM-based (not JEPA/latent-predictive) and focused on language/social reasoning rather than physical control. The paper argues mental world modeling is the "next stage" beyond physical world modeling — interesting but not on LeCun's current research trajectory.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: MWM — Formalize "mental world modeling" as extending world models from physical prediction to coupled physical-mental state prediction. A world model that doesn't track what agents believe and want will predict wrong actions.
- **Motivation**: Human interaction requires theory of mind. An autonomous agent navigating social environments must predict how others will act based on mental states, not just physical positions. Current world models are "mind-blind."
- **Problem Solved**: Demonstrates that explicitly modeling mental states is essential for predicting human decisions in social scenarios. MENTIS baseline provides proof-of-concept across text, image, and video modalities.

### Academic Context

- **Inheritance / Response**: Extends the world model concept from physical dynamics to social/mental dynamics. Builds on cognitive science (theory of mind) and LLM-based reasoning.
- **Implicit Connection**: Raises the question: can JEPA-style architectures learn mental world models from observation alone? Mental states are linguistic/conceptual rather than visual/physical — testing whether JEPA objectives can discover mental state latents from multi-agent video would be fascinating.
- **Research Line**: Social World Models — extending predictive architectures to multi-agent, mental-state-aware domains.
- **Future Directions**: Learning mental state representations from interaction data; integrating mental + physical world models for embodied social agents; testing JEPA-style objectives on multi-agent video.
- **GitHub**: To be checked

---

## [2026-07-28] INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models

- **arXiv**: [2607.26056](https://arxiv.org/abs/2607.26056)
- **Authors**: Junhan Sun, Hao Zhao, Guofeng Zhang
- **TL;DR**: An end-to-end JEPA that maps latent "intent" (desired state change) directly to actions without test-time search, achieving 85.78%–100% on LeWM benchmarks with inference in 2.9–5.5ms — 23.44× fewer samples than pure CEM.
- **Problem**: Forward latent world models (JEPA-based) can predict how actions change a scene, but recovering which actions produce a desired change requires expensive test-time search (CEM/MPPI sampling). This search bottleneck limits real-time deployment.
- **Architecture**: INTACT — Isomorphic architecture where local motion intent (zₜ₊₁−zₜ from transitions) and goal motion intent (sg(z_g)−zₜ from future targets) share identical four-slot input graphs and parameters. Key innovations: (1) **Isomorphic backbones**: the same predictor induces action-law semantics for both local and goal intents, eliminating pointwise latent matching. (2) **Asymmetric endpoint gradients**: physical successors are grounded via gradient, while future goals are fixed as anchors via stop-gradient — joining representation learning and control without globally linear dynamics. (3) **Distributional action law**: conditional mean of the predicted action distribution serves as a search-free direct policy; sampling remains available for diversity/verification. Evaluated on four LeWM tasks with one-epoch, zero-search models. Optional local CEM centered on the Direct plan reduces sampling 23.44× while improving CEM by 16 points.
- **Compute Scale**: Mid (24G): LeWM push/pick/place/navigation benchmarks. Direct inference 2.9–5.5ms. Shared four-task encoder.
- **LeCun Alignment**: HIGH — Directly addresses the search-to-plan bottleneck in JEPA world models. INTACT shows that JEPA training can produce action-effective latent coordinates that support search-free planning, fundamentally changing the relationship between world models and control. The isomorphic design (same architecture for local and goal intents) mirrors LeCun's vision of unified predictive architectures. The search-free direct policy closes the loop between JEPA representation learning and actionable control — a key gap in LeCun's modular agent design.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: INTACT — Learn an intent-to-action interface directly from JEPA training, eliminating test-time search. The model learns to map latent state changes (intents) to actions during training, so at deployment, a desired goal produces an intent that maps directly to an action.
- **Motivation**: JEPA-based world models excel at predicting future states, but planning still requires sampling thousands of action sequences (CEM/MPPI). This search is the computational bottleneck for real-time control. If JEPA can learn to invert its own prediction — mapping desired outcomes back to actions — planning becomes search-free.
- **Problem Solved**: Zero-search models reach 85.78–100% on LeWM tasks after one epoch. Direct inference takes 2.9–5.5ms compared to CEM's ~9,000 candidate evaluations. When search IS used (local CEM centered on Direct plan), only 384 samples are needed vs 9,000 — a 23.44× reduction. Shared encoder across all four tasks improves over per-task LeWM.

### Academic Context

- **Inheritance / Response**: Builds directly on LeWorldModel (2603.19312) and JEPA-based latent world models. Addresses the planner bottleneck identified by SAGE (2607.17973) and the search limitation of prior JEPA planners.
- **Implicit Connection**: This paper represents a critical architectural innovation for JEPA world models. LeCun's vision separates the world model (predicts consequences) from the actor (chooses actions). INTACT shows these can be learned jointly with an isomorphic architecture — the same predictor that models forward dynamics also provides the inverse mapping. This could simplify LeCun's modular agent design by collapsing the world model + actor interface.
- **Research Line**: Search-Free WAM — eliminating planning search in JEPA-based world models through learned intent-action mappings.
- **Future Directions**: Extension to visual observation spaces (currently uses LeWM latent states); multi-task continual learning; integration with hierarchical planning.
- **GitHub**: To be checked

---

## [2026-07-28] TD-JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control

- **arXiv**: [2607.25337](https://arxiv.org/abs/2607.25337)
- **Authors**: Jiaxin Bai, Jiaxuan Xiong
- **TL;DR**: Mines temporal-distance supervision from offline trajectory logs to train JEPA world models whose latent geometry is plan-aware — achieving 100% Two-Room and +14.2 points on OGB-Cube over LeWM under shared evaluation, with released code.
- **Problem**: JEPA-style training optimizes short-horizon latent prediction, whereas planning requires multi-step ranking of imagined futures by goal progress. Prior JEPA planners inherit their ranking metric from embedding geometry (typically Euclidean distance), which arises as a byproduct of representation learning rather than being explicitly optimized for planning. There's a fundamental train-plan gap.
- **Architecture**: TD-JEPA — Retains the LeWorldModel (LeWM) encoder-predictor backbone and adds a directed temporal cost mined from reward-free trajectories: (1) **Same-trajectory step order** supplies positive targets (later timesteps should have lower temporal distance to goal), (2) **Cross-trajectory pairs** serve as heuristic negatives, (3) **Rollout-consistency term** matches the planner's multi-step horizon. The mined supervision serves dual purpose: as the deployed planning cost when progress is topological (Two-Room: 100% vs LeWM's 97.4%), and as a representation signal that improves Euclidean planning when contact geometry dominates (OGB-Cube: +14.2 points over LeWM).
- **Compute Scale**: Mid (24G): LeWM encoder-predictor backbone on PushT, OGB-Cube, Two-Room. Locked evaluation protocol.
- **LeCun Alignment**: HIGH — Addresses a fundamental gap in JEPA-based planning: the cost function used for planning is not optimized during world model training. TD-JEPA shows that mining temporal structure from offline logs and co-designing the cost with planning deployment substantially improves JEPA planners. This aligns with LeCun's vision of world models that are trained not just to predict, but to support downstream reasoning. The train-plan gap has been a criticism of JEPA — TD-JEPA directly responds.
- **GitHub**: [github.com/HKBU-KnowComp/TD-JEPA](https://github.com/HKBU-KnowComp/TD-JEPA)

### What / Why / Solve

- **Proposal**: TD-JEPA — Augment JEPA world model training with temporal-distance supervision mined from offline trajectories. The model learns a latent geometry where temporal distance to goal is explicitly represented, enabling effective planning without post-hoc cost design.
- **Motivation**: JEPA world models predict well but plan poorly because their latent space isn't optimized for ranking futures by goal progress. Euclidean distance in latent space is a weak proxy for temporal distance to goal. Mining temporal structure from the same offline logs used for training solves this without additional data.
- **Problem Solved**: Under locked evaluation (frozen encoder + predictor, only changing planning cost), TD-JEPA's temporally-aware cost achieves 100% on Two-Room (vs LeWM's 97.4%) and +14.2 points on OGB-Cube. Even when using shared Euclidean planning, the temporally-trained checkpoint improves over LeWM — showing the temporal supervision also improves the latent geometry itself.

### Academic Context

- **Inheritance / Response**: Builds on LeWorldModel (2603.19312), I-JEPA (2301.08243), and the growing literature on JEPA-based planning. Directly addresses the train-plan gap critique raised by works like 2607.10362 (prediction error ≠ control success) and SAGE (2607.17973).
- **Implicit Connection**: TD-JEPA operationalizes a key insight: world models for planning need plan-aware representations. The temporal-distance cost is not just a better planner — it's a training signal that reshapes the latent space to be more useful for planning. This blurs the line between representation learning and planning that LeCun's architecture keeps separate, suggesting a more integrated approach may be beneficial.
- **Research Line**: Plan-Aware JEPA — training world model representations explicitly for planning utility.
- **Future Directions**: Extension to longer horizons; integration with hierarchical planning; learned temporal distances for multi-goal settings.
- **GitHub**: [github.com/HKBU-KnowComp/TD-JEPA](https://github.com/HKBU-KnowComp/TD-JEPA)

---

## [2026-07-27] τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision

- **arXiv**: [2607.24485](https://arxiv.org/abs/2607.24485)
- **Authors**: Ning Cheng, Jinan Xu, Wanlin Li, Yangzhi Chen, Jing Gao, Yiqun Wang, Kelan Peng, Wenjuan Han
- **TL;DR**: Learns action-conditioned spatiotemporal tactile representations via JEPA-inspired future visual latent prediction (training-only, no inference overhead), fusing with pretrained VLA models for contact-rich manipulation with improved generalization.
- **Problem**: Incorporating tactile sensing into Vision-Language-Action (VLA) models is challenging: (1) task-specific tactile data is scarce, (2) large-scale tactile pretraining is expensive, (3) existing methods either focus on instantaneous contact or use low-dimensional wrench sequences that don't exploit rich high-dimensional tactile signals.
- **Architecture**: τ (tau) — Two key innovations: (1) **JEPA-inspired tactile encoder**: an action-conditioned spatiotemporal tactile encoder is trained to predict future visual features (from the VLA's vision encoder) in latent space — supervision that operates only during training and adds zero deployment overhead. (2) **Tactile fusion**: the trained tactile representations are fused with VLA vision-language features for action generation. Introduces TacAura dataset with synchronized vision, proprioception, and vision-based tactile signals across four contact-rich tasks. Training supervision follows JEPA principles: predict in latent space (future visual features), not reconstruct tactile signals.
- **Compute Scale**: Mid (24G): VLA backbone + tactile encoder finetuning. No inference overhead from tactile training.
- **LeCun Alignment**: MEDIUM-HIGH — The JEPA-inspired training objective (predict future visual latents from tactile+action context) directly applies LeCun's core insight to a novel modality. The "training-only supervision, zero deployment overhead" pattern mirrors how JEPA world models use prediction during training but only the encoder during inference. However, the primary architecture is a VLA policy, not a world model — making this JEPA-inspired rather than JEPA-based. The TacAura dataset contribution enables future JEPA-based visuo-tactile world models.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: τ — A touch-augmented VLA framework that learns tactile representations by predicting future visual features (JEPA-style latent prediction) during training, with zero inference overhead. The tactile encoder captures spatiotemporal contact dynamics, fused with vision-language for improved action prediction.
- **Motivation**: Contact-rich tasks (insertion, grasping delicate objects) require tactile feedback that vision alone can't provide. But collecting large-scale tactile data is expensive, and integrating touch into billion-parameter VLAs is architecturally challenging. JEPA-style latent prediction offers a way to learn from limited tactile data by predicting in the already-rich visual feature space.
- **Problem Solved**: τ outperforms existing VLA models on contact-rich manipulation tasks and generalizes to unseen objects and scenes. The JEPA-inspired tactile pretraining improves manipulation performance and robustness without adding inference cost.

### Academic Context

- **Inheritance / Response**: Builds on VLA models (OpenVLA, π₀) and JEPA (I-JEPA, V-JEPA). The tactile-predicts-visual-future design echoes the JEPA predictor's role: learn by predicting in representation space. Complements ViTacWorld (2607.22530) which builds full visuo-tactile world models — τ shows a lighter-weight approach focused on policy learning.
- **Implicit Connection**: τ demonstrates a practical, lightweight way to bring JEPA principles into robot learning without building a full world model. The "predict future visual features" objective is a minimal JEPA — context encoder (tactile+action) → predictor → target (future visual features). This suggests a spectrum of JEPA adoption: from full world models (SkyJEPA, LeWM) to JEPA-inspired auxiliary objectives (τ). Also complements Patch Policy (2607.18236) from LeCun's group — together they suggest a research direction of lightweight JEPA-inspired modules for robot learning.
- **Research Line**: JEPA-Inspired Robotics — auxiliary JEPA objectives for policy learning without full world model deployment.
- **Future Directions**: Multi-modal JEPA pretraining for visuo-tactile-action spaces; real-time tactile JEPA for reactive control.
- **GitHub**: To be checked

---

## [2026-07-24] IQ-JEPA: A JEPA with Hermitian ViT for Ultrasound Sound Speed Estimation

- **arXiv**: [2607.22351](https://arxiv.org/abs/2607.22351)
- **Authors**: Masashi Sode, Gianmarco Pinton
- **TL;DR**: Adapts JEPA to complex-valued medical ultrasound data via a Hermitian Vision Transformer that is equivariant to phase offset — achieving 3–4× label efficiency gains for sound speed estimation, a step toward foundation models for quantitative ultrasound.
- **Problem**: Ultrasound sound speed estimation from raw IQ (in-phase/quadrature) channel data is a nonlinear inverse problem. Learned solvers are fast but require large labeled datasets, while abundant real channel data is unlabeled. How to leverage JEPA pretraining for complex-valued medical signals?
- **Architecture**: IQ-JEPA — (1) JEPA pretraining: context encoder + predictor trained to predict masked IQ region latents from visible context, without labels. (2) **Hermitian Vision Transformer**: operates directly on complex IQ data. Its attention is equivariant to constant phase offset (a nuisance parameter in ultrasound), and its conjugate-product feed-forward is invariant to it — the encoder reads a quantity analogous to classical coherence methods. (3) Fine-tuning on simulated sound speed maps. Trained on 79,293 Fullwave 2.5 MHz simulations (63,435 unlabeled for pretraining). The equivariance/invariance properties make the architecture physically principled for the domain.
- **Compute Scale**: Mid (24G): Fullwave 79K simulation dataset; JEPA pretraining + supervised fine-tuning.
- **LeCun Alignment**: MEDIUM — Cross-domain validation of JEPA in medical imaging with complex-valued signals. Demonstrates JEPA's generality to modalities beyond RGB images and to signals with domain-specific physical invariances. The Hermitian ViT's treatment of phase equivariance is a nice example of building physical structure into JEPA encoders. However, this is primarily a domain application rather than advancing world model theory. The 3–4× label efficiency gain validates JEPA's practical value for label-scarce scientific domains.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: IQ-JEPA — Apply JEPA pretraining to complex-valued ultrasound data using a physically-principled encoder (Hermitian ViT). Pretrain on unlabeled IQ data to predict masked region latents, then fine-tune on simulated sound speed maps with dramatically improved label efficiency.
- **Motivation**: Medical imaging has abundant unlabeled data and scarce labeled data. JEPA's self-supervised pretraining is ideal for this regime, but ultrasound IQ data is complex-valued with domain-specific structure (phase offset nuisance, coherence-like features). A vanilla ViT would waste capacity learning phase invariance from data; a Hermitian ViT bakes it in architecturally.
- **Problem Solved**: JEPA pretraining achieves 15.60 m/s RMSE at 10,000 labels — roughly 3× label efficiency over supervised training (4× at 1,000 labels). The pretrained encoder's frozen features expose both sound speed and attenuation, suggesting transfer to multiple downstream tasks. Cross-distribution pretraining (layered→abdominal phantoms) costs little accuracy.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA (2301.08243) and quantitative ultrasound literature. Adapts JEPA to complex-valued signals with domain-specific neural architecture (Hermitian ViT).
- **Implicit Connection**: This paper extends the JEPA application portfolio to medical/scientific domains, following Crys-JEPA (2605.14759, materials science) and JEPA-CFM (2607.20202, wireless communications). Together these papers demonstrate that JEPA is a general-purpose SSL paradigm for structured physical signals, not just natural images. The Hermitian ViT's treatment of physical invariances echoes LeCun's call for architectures that incorporate known physical structure rather than learning everything from data.
- **Research Line**: Scientific JEPA — adapting JEPA to domain-specific physical signals.
- **Future Directions**: Extension to other medical imaging modalities (MRI, CT); foundation model for quantitative ultrasound; real-time clinical deployment.
- **GitHub**: To be checked

---

## [2026-07-27] LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments

- **arXiv**: [2607.23969](https://arxiv.org/abs/2607.23969)
- **Authors**: Pei Liu, Nan Zheng, Lang Zhang, Daojie Peng, Yanan Zhang, Feilong Kong, Mingyue Feng, Jiachao Liu, Yaonong Wang, Qifeng Chen, Jun Ma
- **TL;DR**: Proposes a Predictive-Latent paradigm for World Action Models (WAMs) that replaces pixel-level video generation with JEPA-based latent semantic alignment — the "World-Anchor" — achieving state-of-the-art performance without large-scale trajectory pretraining.
- **Problem**: Existing WAMs rely on pixel-level video generation, wasting capacity on task-irrelevant visual details and making policies vulnerable to visual distractors. Diffusion-based generation is computationally expensive for planning.
- **Architecture**: LeapBot-WA — Three key innovations: (1) **Predictive Semantic Alignment** via JEPA as World-Anchor: extracts abstract physical dynamics in latent foundation space rather than generating pixels. (2) **Isotropic Semantic Autoencoder (ISAE)**: reshapes the anchor's non-Gaussian latent space into a diffusion-friendly manifold to prevent off-manifold drift. (3) **Asymmetric Mixture-of-Transformers (MoT)**: Anchor Diffusion Transformer acts as privileged dynamics expert during training, guiding the Action Diffusion Transformer; at inference, the heavy dynamics branch is pruned for zero-overhead execution.
- **Compute Scale**: Large (40G+): Asymmetric MoT architecture with Anchor and Action Diffusion Transformers.
- **LeCun Alignment**: HIGH — Directly instantiates LeCun's vision: JEPA as the core world model, latent-space prediction replacing pixel generation, modular architecture with separate dynamics and action components. The paper explicitly positions itself against pixel-generation WAMs and adopts JEPA as the predictive core. The "Predictive-Latent" paradigm is precisely the direction LeCun advocates.
- **GitHub**: [github.com/LeapWM/leapbot-wa](https://github.com/LeapWM/leapbot-wa)

### What / Why / Solve

- **Proposal**: LeapBot-WA — Replace pixel-generation in WAMs with JEPA-based Predictive Semantic Alignment. The World-Anchor predicts future latent states, and actions are generated by aligning with these predictions rather than reconstructing pixels.
- **Motivation**: Pixel-level video generation in WAMs is a bottleneck — it wastes capacity on irrelevant details, is vulnerable to distractors, and is computationally expensive. JEPA offers a more efficient alternative: predict in latent space, not pixel space.
- **Problem Solved**: Achieves SOTA among predictive models on LIBERO, matches top-tier generative WAMs on RoboTwin 2.0 without large-scale pretraining, and demonstrates superior zero-shot robustness to unseen environments with real-world transfer.

### Academic Context

- **Inheritance / Response**: Builds directly on LeCun's JEPA framework and the WAM paradigm. Responds to the limitation of pixel-generative WAMs (like GAIA-1, UniSim) by proposing a purely latent predictive approach.
- **Implicit Connection**: This is the closest paper yet to LeCun's full "Path Towards Autonomous Machine Intelligence" vision applied to robotics: a JEPA-based world model that predicts in latent space, with a separate action module, deployed in an MPC-like planning loop.
- **Research Line**: Predictive-Latent WAMs — a new subcategory of World Action Models that abandon pixel generation entirely.
- **Future Directions**: Scaling to longer horizons; integration with hierarchical planning; multi-embodiment transfer via the World-Anchor abstraction.
- **GitHub**: [github.com/LeapWM/leapbot-wa](https://github.com/LeapWM/leapbot-wa)

---

## [2026-07-26] The JEPA Paradox in Language: The Geometry of Linguistic Alternatives

- **arXiv**: [2607.23531](https://arxiv.org/abs/2607.23531)
- **Authors**: Anh Trac Duc Dinh, Khang Nhat Hoang Vo
- **TL;DR**: Formalizes why deterministic JEPA fails for text — language has multiple valid completions that don't share a coherent latent center, violating the conditional concentration assumption that makes JEPA work for images/video/audio.
- **Problem**: JEPA is highly effective for images, video, and audio, but has not become standard for text encoders. Why? The paper identifies a fundamental geometric mismatch between squared-error latent prediction and the multi-modal conditional structure of language.
- **Architecture**: Theoretical analysis using three conditions: (1) **Predictability** — context must carry information about the target, (2) **Non-collapse** — representations must not collapse to a trivial constant, (3) **Low conditional variance** — given context, the target representation must lie near a single meaningful point. The paper proves that text violates condition 3 because masked positions admit multiple valid completions (e.g., "the cat sat on the ___" could be "mat", "chair", "floor", etc. whose representations don't cluster). Validated with matched I-JEPA and T-JEPA experiments showing mutual-information saturation, effective-rank degeneration, cosine collapse, and poor downstream transfer.
- **Compute Scale**: Small (8-12G): Controlled experiments with I-JEPA/T-JEPA on text; theoretical analysis.
- **LeCun Alignment**: MEDIUM-HIGH — Directly addresses a critical question in the JEPA research program: why hasn't JEPA succeeded for language? The answer (conditional multimodality) has implications for how to design text-compatible JEPA objectives. LeCun's architecture envisions language as a separate module — this paper provides theoretical justification for that separation.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Formal analysis of why JEPA fails for text — the "JEPA Paradox" — and identification of conditional concentration as the key requirement that language violates.
- **Motivation**: Understanding JEPA's domain boundaries is crucial for the research program. If JEPA is truly general, it should work for text. If it fundamentally can't, we need to understand why.
- **Problem Solved**: Provides rigorous geometric explanation for JEPA's failure in NLP: text's multi-modal conditional distribution means no single latent point can represent all valid completions, causing centroid degeneracy and representation collapse.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA, V-JEPA, and the broader JEPA literature. Responds to the puzzle: why has deterministic JEPA not displaced BERT-style masked token prediction?
- **Implicit Connection**: Validates LeCun's architectural choice to treat language as a separate module rather than fitting it into the same JEPA framework. The paper's finding that "text-compatible JEPA objectives must preserve multiple plausible completions" suggests future JEPA variants for language need stochastic or multi-modal prediction heads.
- **Research Line**: JEPA theory — understanding the fundamental constraints and domain boundaries of predictive architectures.
- **Future Directions**: Stochastic JEPA for language (multi-modal prediction heads); energy-based JEPA for text; connection to LeCun's proposed "world model + configurator" architecture.
- **GitHub**: To be checked

---

## [2026-07-21] Toward Goal-Agnostic Joint-Embedding Predictive Control of Partial Differential Equations

- **arXiv**: [2607.21644](https://arxiv.org/abs/2607.21644)
- **Authors**: Jonathan Gallagher, Roberto Guglielmi
- **TL;DR**: Applies JEPA to PDE control: a goal-agnostic framework where a small ViT encoder + action-conditioned latent dynamics are trained offline without any reward, frozen, and reused by an MPPI controller — demonstrating that physical observables (not raw latent distance) are better control objectives.
- **Problem**: Can JEPA-learned latent dynamics support goal-agnostic control of complex physical systems (PDEs) without task-specific training? And what objective should the controller optimize — latent distance or a physical observable?
- **Architecture**: JEPA-based control framework: (1) Small 2D ViT encoder maps PDE states to latent embeddings. (2) Action-conditioned latent dynamics predictor trained offline with no reward or downstream goal. (3) Frozen model reused by Model-Predictive Path Integral (MPPI) controller. Key finding: controlling via a learned linear probe on physical observables (kinetic energy) outperforms raw latent L² distance, because the latent space isn't necessarily Euclidean-meaningful for control.
- **Compute Scale**: Small-Mid (8-24G): Small 2D ViT encoder; Navier-Stokes benchmark on PDE Control Gym.
- **LeCun Alignment**: HIGH — Directly instantiates LeCun's vision of goal-agnostic world models: learn the dynamics once, freeze, reuse for many tasks. The finding that "physical observables beat latent distance" aligns with LeCun's emphasis on the world model learning abstract, controllable representations rather than pixel-perfect reconstructions.
- **GitHub**: Code to be open-sourced with V2 submission

### What / Why / Solve

- **Proposal**: A JEPA-based goal-agnostic control framework for PDEs. Train the world model once without any task-specific objective, freeze it, and use MPPI to solve diverse control tasks by optimizing physical observables rather than latent distance.
- **Motivation**: Traditional PDE control methods are task-specific (trained per objective). A goal-agnostic world model that learns general dynamics could be reused across many control tasks, dramatically improving sample efficiency.
- **Problem Solved**: Demonstrates that JEPA-learned latent dynamics on Navier-Stokes equations support diverse control tasks (trajectory following, stabilization) with a single frozen model. The KE-probe approach improves control quality by 53% over latent-L² planning on held-out targets.

### Academic Context

- **Inheritance / Response**: Builds on JEPA for representation learning and extends it to PDE control. Bridges the gap between self-supervised world models and scientific computing/control theory.
- **Implicit Connection**: This paper validates LeCun's claim that world models should be goal-agnostic — learned once and reused. The MPPI controller on frozen dynamics is essentially the "actor" in LeCun's modular agent architecture.
- **Research Line**: Scientific JEPA — applying predictive world models to physical systems beyond robotics (fluids, climate, materials).
- **Future Directions**: Extension to 3D PDEs; integration with real-world sensor data; hierarchical JEPA for multi-scale physical systems.
- **GitHub**: To be released

---

## [2026-07-16] DriftWorld: Fast World Modeling through Drifting

- **arXiv**: [2607.15065](https://arxiv.org/abs/2607.15065)
- **Authors**: Susie Lu, Haonan Chen, Weirui Ye, Yilun Du
- **TL;DR**: Replaces iterative diffusion denoising in world models with a learned "drift" that generates future frames in a single forward pass at 30+ fps — 17× faster than diffusion — while matching or exceeding planning performance.
- **Problem**: Diffusion-based world models are too slow for real-time planning because each rollout requires multi-step iterative denoising. This limits the number of action sequences that can be evaluated at inference time.
- **Architecture**: DriftWorld — An action-conditioned world model based on drifting generative models. During training, it learns an action-conditioned drift function that maps current observation + action sequence → future frames directly, without iterative denoising. At inference: single forward pass at 30+ fps. Evaluated on Bridge-V2, RT-1, Language Table, Push-T, and Robomimic.
- **Compute Scale**: Mid (24G): Single forward pass generation; standard manipulation benchmarks.
- **LeCun Alignment**: MEDIUM — Still uses generative (frame prediction) approach rather than latent prediction, BUT directly addresses LeCun's key criticism of generative world models: they're too slow. DriftWorld shows that fast generation is possible, which partially mitigates the efficiency argument against generative approaches. However, it still wastes capacity on pixel-level details that JEPA avoids entirely.
- **GitHub**: [susie-lu.github.io/driftworld](https://susie-lu.github.io/driftworld/)

### What / Why / Solve

- **Proposal**: DriftWorld — Replace iterative denoising with a learned deterministic drift for fast world model rollouts.
- **Motivation**: World models need many rollouts for planning. Diffusion models are accurate but slow (multi-step). Drift models are fast (single-step) and can match diffusion quality when properly trained.
- **Problem Solved**: Achieves 17× faster inference than diffusion-based world models while maintaining competitive planning performance. Also serves as an offline policy evaluator with rollout scores correlating up to 0.99 with ground truth.

### Academic Context

- **Inheritance / Response**: Responds to the speed limitation of diffusion-based world models (UniSim, GAIA-1, etc.). Builds on the drifting generative model framework.
- **Implicit Connection**: This paper is the best counterargument to LeCun's "generative models are wasteful" critique — it shows that generation CAN be fast. However, it doesn't address the deeper critique about wasting capacity on irrelevant details. A hybrid DriftWorld + JEPA (drifting in latent space) could be a promising direction.
- **Research Line**: Efficient Generative World Models — making pixel-level world models fast enough for real-time control.
- **Future Directions**: Drifting in JEPA latent space; combining drift efficiency with latent prediction; scaling to longer horizons.
- **GitHub**: [susie-lu.github.io/driftworld](https://susie-lu.github.io/driftworld/)

---

## [2026-07-10] Causally Debiased Latent Action Model for Embodied Action Conditioned World Models

- **arXiv**: [2607.09185](https://arxiv.org/abs/2607.09185)
- **Authors**: Yufan Wei, Kun Zhou, Lingjun Mao, Zijun Zhang, Ziming Xu, Ziqiao Xi, Shuang Liang, Ruobing Han, Yuchen Yan, Xinyue Wang, Fan Feng, Biwei Huang
- **TL;DR**: Identifies and fixes action-irrelevant bias in latent action models for world models using causal debiasing: embodiment-centric reconstruction + action-centric contrastive learning + latent calibration, requiring only 6K fine-tuning steps.
- **Problem**: Latent action models (LAMs) infer actions from unlabeled videos, but existing methods entangle action-relevant dynamics with irrelevant visual factors (backgrounds, untouched objects). This "action-irrelevant bias" prevents controllable world models.
- **Architecture**: CD-LAM (Causally Debiased LAM) — Three fine-tuning objectives: (1) Embodiment-centric reconstruction: focus on the robot/agent, not background. (2) Action-centric contrastive learning: push apart latents for different actions, pull together for same actions. (3) Latent space calibration: prevent representation collapse. Applied to 2B and 14B ACWM backbones with 12× fewer adaptation updates.
- **Compute Scale**: Large (40G+): Built on 2B and 14B ACWM backbones.
- **LeCun Alignment**: MEDIUM-HIGH — Directly addresses a core challenge in LeCun's vision: learning controllable latent representations that isolate action effects from irrelevant factors. The causal debiasing approach aligns with LeCun's emphasis on learning "abstract representations" that capture only what matters for planning and control.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: CD-LAM — Identify and remove action-irrelevant bias from LAM-based world models using causal debiasing objectives.
- **Motivation**: For world models to be controllable, latent actions must capture only action-relevant dynamics. Existing LAMs mix in irrelevant visual factors, making downstream control unreliable.
- **Problem Solved**: Substantially improves latent-action controllability, robot-action following, visual fidelity, and adaptation efficiency — requiring only 6K fine-tuning steps and 12× fewer robot-action adaptation updates than baselines.

### Academic Context

- **Inheritance / Response**: Builds on the LAM literature (learning actions from videos) and ACWM literature (action-conditioned world models). Brings causal inference tools to bear on the entanglement problem.
- **Implicit Connection**: This is the kind of representation-quality work that LeCun's vision demands. The emphasis on disentangling action-relevant from action-irrelevant factors is exactly what the JEPA objective implicitly achieves through its design. CD-LAM makes this disentanglement explicit and causally grounded.
- **Research Line**: Causal World Models — applying causal discovery and debiasing to learned dynamics models.
- **Future Directions**: Integration with JEPA-style objectives; causal discovery of action effects in multi-agent settings; real-robot deployment.
- **GitHub**: To be checked

---

## [2026-06-29] Latent Actions from Factorized Transition Effects under Agent Ambiguity

- **arXiv**: [2606.30544](https://arxiv.org/abs/2606.30544)
- **Authors**: Heejeong Nam, Chandradithya S Jonnalagadda, Harshit Aggarwal, Eric Xu, Randall Balestriero
- **TL;DR**: Factorizes video transitions into sparse reusable primitives (OTF) to learn robust latent actions even when the agent is ambiguous — with a decoder-free DINOv2 variant that predicts future states in frozen representation space.
- **Problem**: In multi-object or distractor-rich scenes, latent action models confuse agent motion with distractors, camera moves, and background changes. Which visual change is the "action"?
- **Architecture**: OTF-LAM — (1) Observed Transition Factorization (OTF): decomposes each transition into sparse observed transition primitives. (2) OTF-LAM: uses these primitives in a standard inverse-forward dynamics framework. (3) OTF-LAM-Dino: decoder-free variant that predicts future states in frozen DINOv2 representation space — aligning with JEPA's "predict in representation space" philosophy. Accepted at ICML 2026 Workshop on Compositional Learning.
- **Compute Scale**: Small-Mid (8-24G): DINOv2-based; standard manipulation benchmarks.
- **LeCun Alignment**: MEDIUM-HIGH — Randall Balestriero is a LeCun collaborator. The decoder-free DINOv2 variant (predicting in representation space) is conceptually JEPA-aligned. The factorization approach addresses the compositionality that LeCun sees as essential for world models.
- **GitHub**: [hazel-heejeong-nam.github.io/LAM](https://hazel-heejeong-nam.github.io/LAM/)

### What / Why / Solve

- **Proposal**: OTF-LAM — Factorize transitions into reusable primitives to disambiguate which visual effects are the agent's actions, enabling robust latent action inference.
- **Motivation**: In real-world scenes, many things move simultaneously. Without factorization, LAMs can't tell which motion belongs to the agent. This is the "agent ambiguity" problem.
- **Problem Solved**: OTF primitives transfer zero-shot across carrier and morphology shifts. The decoder-free variant (OTF-LAM-Dino) matches or outperforms baselines under complex transition ambiguity, demonstrating that pixel reconstruction isn't necessary.

### Academic Context

- **Inheritance / Response**: Builds on LAM and inverse-forward dynamics literature. The decoder-free variant is a direct step toward JEPA-style world models.
- **Implicit Connection**: Balestriero's involvement connects this to the Meta/LeCun research ecosystem. The decoder-free approach (predicting in DINOv2 space) is essentially JEPA with a frozen target encoder — the same architecture as I-JEPA. This paper provides an alternative path to the same goal: learn actionable representations without pixel reconstruction.
- **Research Line**: Factorized World Models — learning compositional, reusable dynamics primitives.
- **Future Directions**: Scaling to more complex multi-agent scenes; integration with JEPA training objectives; hierarchical factorization.
- **GitHub**: [Project page](https://hazel-heejeong-nam.github.io/LAM/)

---

## [2026-07-13] WALA: Learning Executable Latent Actions from Action-Labeled Demonstrations and Action-Free Videos

- **arXiv**: [2607.11397](https://arxiv.org/abs/2607.11397)
- **Authors**: Jiahao Liu, Zhongpu Xia, Shuai Tian, Huangrui Li, Yuhang Zheng, Ning Ma, Xin Fu, Xiaotian Liu, Jing Li, Yixian Li, ShangQing Zhou, Zebin Xing, Linbo Wang, Chaoyue Li, Haoran Li, Dongbin Zhao
- **TL;DR**: Learns executable latent actions from both labeled demos and unlabeled videos by predicting future deltas in DINOv3 + depth space (not pixels), achieving SOTA 75.2% on RoboCasa with strong real-world transfer.
- **Problem**: Robot policies need action-labeled data (expensive), but massive video data exists without action labels. How to leverage both?
- **Architecture**: WALA — (1) Pretrain a semantic-geometric latent action model from videos by predicting future deltas in DINOv3 feature space + dense depth space (not raw pixels), preserving task-relevant structure while ignoring appearance. (2) During policy training: pretrained encoder provides stable latent action targets, decoder serves as trainable latent world model. (3) Joint supervision: robot action prediction + latent action target matching + future dynamics prediction.
- **Compute Scale**: Mid (24G): DINOv3 + depth prediction; RoboTwin, RoboCasa, real-world manipulation.
- **LeCun Alignment**: MEDIUM — Predicts in representation space (DINOv3 + depth) rather than pixel space, which aligns with JEPA's philosophy. However, the focus is on policy learning rather than building a general-purpose world model. The "latent world model" component connects to the broader world model ecosystem.
- **GitHub**: [liujiahao2077.github.io/WALA](https://liujiahao2077.github.io/WALA)

### What / Why / Solve

- **Proposal**: WALA — Bridge action-labeled demos and action-free videos by predicting future representations (not pixels) in a shared semantic-geometric latent space.
- **Motivation**: Action-labeled robot data is scarce and expensive; video data is abundant but lacks action labels. WALA leverages both by learning what changes between frames in representation space.
- **Problem Solved**: SOTA 75.2% average success on RoboCasa, strong performance on RoboTwin, and improved real-world manipulation generalization — all while leveraging unlabeled video data.

### Academic Context

- **Inheritance / Response**: Builds on LAM literature and DINOv3. The key innovation is predicting in DINOv3 + depth space rather than pixels — a step toward JEPA-style representation prediction.
- **Implicit Connection**: WALA doesn't use JEPA explicitly, but its core design choice — predict future representation deltas rather than reconstruct pixels — is the same insight that motivates JEPA. This convergence from the robot learning community validates LeCun's architectural argument.
- **Research Line**: Representation-Space Dynamics — learning world dynamics in pretrained feature spaces as an alternative to both pixel generation and end-to-end latent world models.
- **Future Directions**: Integration with JEPA training for the latent world model; scaling to more diverse video sources; multi-embodiment transfer.
- **GitHub**: [Project page](https://liujiahao2077.github.io/WALA)

---

## [2026-07-24] Music-JEPA: Learning a World Model of Sound from Action

- **arXiv**: [2607.22000](https://arxiv.org/abs/2607.22000)
- **Authors**: Ziyu Wang, Kun Fang, Yann LeCun
- **TL;DR**: Frames music as an action-conditioned system for JEPA world model learning — piano audio as state, pianoroll as action — enabling piano transcription via planning by searching for actions that best explain target sound.
- **Problem**: JEPA has been applied to music before but without the world model framing. Can JEPA learn a genuine world model of musical sound by treating it as an action-conditioned dynamical system?
- **Architecture**: Music-JEPA — Action-conditioned JEPA world model. Takes current audio state + pianoroll action → predicts future audio state in latent space. Trained fully offline on paired audio-pianoroll data. Evaluated on beat tracking, composer identification, key estimation, and piano transcription via planning (searching actions that minimize prediction error against target audio).
- **Compute Scale**: Mid (24G): Audio-pianoroll paired data; standard GPU training.
- **LeCun Alignment**: HIGH — **LeCun is co-author.** Directly instantiates the core JEPA world model concept in the audio/music domain. Action-conditioned latent prediction mirrors LeCun's vision of world models that predict consequences of interventions. The planning loop (search actions → predict outcome → compare to target) is a miniature version of MPC in latent space. Demonstrates JEPA's generality beyond vision/robotics into creative domains.
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: Music-JEPA — Learn a world model of piano sound by framing music as an action-conditioned dynamical system: audio = state, pianoroll = action. Given current audio and an action (notes to play), predict the resulting future audio in latent space.
- **Motivation**: Music is inherently action-conditioned — a pianist's actions produce sound. This makes it a natural domain for JEPA-style world models. Previous music JEPA attempts didn't exploit this action-state structure for full world model learning.
- **Problem Solved**: Demonstrates that JEPA world models can capture musical causality: the relationship between instrumental actions and resulting sound. The learned representations transfer to multiple downstream tasks (beat tracking, composer ID, key estimation). Most innovatively, enables piano transcription via planning — searching for the action sequence that best predicts a target audio, essentially "explaining" the audio as the result of imagined actions.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA, V-JEPA, and action-conditioned JEPA extensions. Extends the world model paradigm to the music/audio domain with explicit action conditioning.
- **Implicit Connection**: This paper closes an important gap: JEPA world models have been demonstrated for visual/physical domains (robotics, driving) but not for creative/artistic domains where actions are discrete symbolic events (musical notes). It validates LeCun's claim that JEPA is a general-purpose world model architecture, not tied to any specific sensory modality or action space.
- **Research Line**: Multimodal JEPA — extending action-conditioned world models beyond physical control to creative/symbolic action spaces.
- **Future Directions**: Extension to multi-instrument music; improvisation via planning; integration with music generation; joint audio-visual-motor world models for music performance.
- **GitHub**: To be checked

---

## [2026-07-24] On the Identifiability of Controlled World Models

- **arXiv**: [2607.22430](https://arxiv.org/abs/2607.22430)
- **Authors**: Xiangteng Zhang, Yang Guan, Bo Zhang, Ya-Qin Zhang, Shengbo Eben Li
- **TL;DR**: Establishes the first joint identifiability theory for JEPA-based controlled world models — proving that under Gaussian latent dynamics and sufficient action variation, JEPA recovers true latent states and transitions up to orthogonal transformation.
- **Problem**: Action-conditioned JEPA world models work well empirically, but there's no theoretical guarantee that they actually identify the true underlying state and dynamics. Under nonlinear observations and limited action variation, state evolution and action effects can be statistically confounded — the model might learn a scrambled representation.
- **Architecture**: Theoretical analysis of controlled JEPA — Gaussian latent states with state-dependent Gaussian behavior policies. Two conditions identified: (1) spectral separation of predictable signal governs representation identifiability; (2) non-degenerate conditional action variation governs transition identifiability. Proves that when both hold, every global minimizer identifies latent state and controlled transition up to orthogonal transformation. Also constructs a counterfactual diagnostic: predictor perturbations along weakly excited action directions whose error ratio reveals transition-identifiability margins.
- **Compute Scale**: Small (8-12G): Primarily theoretical with synthetic experiments across nonlinear observation maps and behavior policies.
- **LeCun Alignment**: HIGH — Provides the theoretical foundation that the JEPA world model program has been missing. Answers the fundamental question: *when does training a JEPA world model actually recover the true world state?* The identifiability conditions (spectral separation, action variation) give practical guidance for designing training environments and data collection. The counterfactual diagnostic directly addresses the evaluation problem raised by 2607.10362 (prediction error ≠ control success).
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: Joint identifiability theory for controlled world models — proves that under Gaussian latent dynamics and sufficient policy variation, JEPA training recovers the true latent state and controlled transition up to an orthogonal transformation. Derives quantitative bounds under approximate optimization.
- **Motivation**: The JEPA community has been building increasingly sophisticated world models without answering the foundational question: does the training objective actually identify the true dynamics? Without identifiability, a world model could achieve low prediction error on training data while learning a scrambled representation that fails under distribution shift.
- **Problem Solved**: Provides necessary and sufficient conditions for JEPA identifiability. Shows that two factors matter: (1) how predictable the latent signal is (spectral separation), and (2) how much the behavior policy varies actions conditional on state. When action variation is limited, the model can't disentangle state evolution from action effects — a practical warning for data collection in robotics.

### Academic Context

- **Inheritance / Response**: Builds on nonlinear ICA identifiability theory and JEPA literature (I-JEPA, LeWM, action-conditioned JEPA). Extends identifiability analysis from static representation learning to controlled dynamical systems.
- **Implicit Connection**: This paper is a crucial piece of the JEPA research programme's theoretical foundation. Together with 2607.13612 (SIGReg as Variational Free Energy) and 2605.26379 (When Does LeJEPA Learn a World Model?), it forms a trilogy of theoretical papers that establish JEPA as a principled rather than heuristic architecture. The identifiability results also connect to the evaluation critique in 2607.10362 — if the model isn't identifiable, prediction error on training data tells you nothing about control.
- **Research Line**: JEPA Theory — identifiability and recovery guarantees for world model learning.
- **Future Directions**: Extension to non-Gaussian latent dynamics; identifiability under partial observability; practical identifiability diagnostics for deployed world models.
- **GitHub**: To be checked

---

## [2026-07-24] Robot-Factored World Models via Robot Rendering

- **arXiv**: [2607.22535](https://arxiv.org/abs/2607.22535)
- **Authors**: Byungjun Kim, Taeksoo Kim, Hyunsoo Cha, Hanbyul Joo
- **TL;DR**: Factorizes robot kinematics and geometry OUT of the world model by pre-rendering actions as robot geometry via URDF — the world model only sees visible robot geometry and learns object response, enabling cross-embodiment generalization.
- **Problem**: Standard action-conditioned video world models must learn BOTH how actions translate to robot motion AND how objects respond to that motion. This entangles robot-specific factors (kinematics, appearance) with general physical dynamics, preventing transfer across embodiments.
- **Architecture**: Robot-Factored World Model — Two robot-specific factors moved outside the world model: (1) Action Realization: commands go through robot controller/kinematics to produce a nominal trajectory. (2) Robot Rendering: this trajectory is rendered through URDF as visible robot geometry, paired with scene depth for occlusion/contact reasoning. The world model receives camera-aware static RGB/depth context + rendered robot geometry as input, and predicts how objects respond. No robot-specific learning inside the model.
- **Compute Scale**: Mid (24G): Video prediction with pre-rendered robot geometry; generalizes to unseen embodiments at inference.
- **LeCun Alignment**: MEDIUM-HIGH — The factorization philosophy strongly aligns with LeCun's modular agent architecture: the world model should learn about the WORLD, not about the agent's specific embodiment. By factoring out robot kinematics/geometry (which are known/controllable), the model focuses on learning general physical dynamics — exactly the kind of reusable world knowledge LeCun envisions. However, uses pixel-space video prediction (generative) rather than JEPA-style latent prediction. The robot-rendering interface could be paired with a JEPA backbone.
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: Robot-Factored World Models — Instead of conditioning directly on action commands or future states, pre-render actions as robot geometry using known URDF/kinematics. The world model sees a visual interface (rendered robot + scene) and learns how objects respond. This factorization means the model never needs to learn robot-specific realization.
- **Motivation**: Current approaches either condition on raw actions (forcing the model to learn robot kinematics) or condition on future states (leaking the outcome). Neither is right: the model should focus on general physical dynamics, not robot-specific implementation details.
- **Problem Solved**: Demonstrates that robot-factored interface (1) outperforms vector-conditioned baselines, (2) generalizes to unseen robot embodiments at inference, and (3) enables robot manipulation video generation from human demonstrations by retargeting hand motion as robot geometry. The depth-aware rendering resolves contact/occlusion ambiguity.

### Academic Context

- **Inheritance / Response**: Builds on video world model literature (Dreamer, video prediction) and robot learning. The factorization insight echoes modular robotics and sim-to-real approaches.
- **Implicit Connection**: This paper represents an important architectural principle: not everything should be learned. Known physical properties (robot kinematics, geometry) should be factored out so the learned model can focus on unknown physical dynamics (object response, contact). This aligns with LeCun's argument that world models should leverage structured knowledge rather than learning everything from scratch. The visual interface (rendered geometry) is compatible with JEPA encoders — future work could combine robot-factored input with JEPA-style latent prediction.
- **Research Line**: Structured World Models — factoring known physics out of learned models.
- **Future Directions**: Integration with JEPA latent prediction; extension to multi-object scenes; real-robot deployment with imperfect URDF/kinematics.
- **GitHub**: To be checked

---

## [2026-07-24] ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation

- **arXiv**: [2607.22530](https://arxiv.org/abs/2607.22530)
- **Authors**: Yunao Huang, Shiyu Sang, Haotao Lu, Suting Ni, Shijie Wu, Ziyang Guo, Ye Shi, Jingya Wang
- **TL;DR**: First visuo-tactile world model — pretrains on large-scale real + simulated visuo-tactile trajectories, then finetunes on real policy rollouts, enabling rollout generation for data augmentation and action-conditioned policy evaluation.
- **Problem**: Contact-rich manipulation requires tactile sensing (forces, contacts invisible to cameras), but real tactile data is expensive to collect and hardware-specific. How can we scale visuo-tactile world model training when real data is scarce?
- **Architecture**: ViTacWorld — Action-conditioned world model that predicts both visual observations AND tactile feedback from robot actions. Two-stage training: (1) large-scale pretraining on public real tactile datasets + simulated visuo-tactile trajectories (exploiting that tactile signals have smaller sim-to-real gap than vision), (2) finetuning on real-world policy rollouts. Serves dual purpose: synthesizing rollouts to augment downstream policy training, and evaluating policies by predicting action-conditioned outcomes.
- **Compute Scale**: Large (40G+): Multi-modal pretraining on visuo-tactile data + finetuning on real robot rollouts.
- **LeCun Alignment**: MEDIUM-HIGH — Addresses a critical gap for embodied world models: tactile sensing. LeCun's vision emphasizes multi-modal world models that integrate all sensory streams. ViTacWorld demonstrates that world models can bridge vision and touch, predicting both from actions. However, uses pixel-level video prediction (generative) rather than JEPA-style latent prediction. The sim-to-real insight (tactile has smaller gap) is practically valuable.
- **GitHub**: Project page: https://vitacworld.github.io/

### What / Why / Solve

- **Proposal**: ViTacWorld — Scale visuo-tactile world model training by leveraging public real datasets + simulation, exploiting the fact that tactile signals are more transferable across sim-to-real than visual observations. The model predicts aligned visual and tactile futures from actions.
- **Motivation**: Contact-rich tasks (peg insertion, assembly, button pressing) require tactile feedback that cameras can't provide. But collecting real tactile data at scale is prohibitively expensive. A world model that can simulate both vision and touch would enable scalable policy learning.
- **Problem Solved**: First framework to use a world model for visuo-tactile trajectory generation. Demonstrates two practical applications: (1) synthesizing additional rollouts to improve downstream policy performance (data augmentation), (2) evaluating policies by predicting their visuo-tactile outcomes without real execution (policy evaluation). Generates physically meaningful rollouts on contact-rich tasks.

### Academic Context

- **Inheritance / Response**: Builds on video world models (Dreamer, video prediction) and tactile sensing literature. Extends world models to the visuo-tactile modality for the first time.
- **Implicit Connection**: Multi-modal world models are essential for LeCun's vision of autonomous intelligence — agents need to predict across ALL sensory modalities, not just vision. ViTacWorld takes a step toward this by incorporating touch. However, the generative (pixel-prediction) approach is less aligned with JEPA than a latent-prediction approach would be. Future work could combine ViTacWorld's multi-modal pretraining strategy with JEPA's latent-space prediction.
- **Research Line**: Multi-Modal World Models — incorporating tactile, force, and proprioceptive sensing.
- **Future Directions**: JEPA-style latent visuo-tactile prediction; real-time model-predictive control with tactile feedback; integration with force/torque sensing.
- **GitHub**: https://vitacworld.github.io/

---

## [2026-07-24] Unbiased Open World Regularization for Fair Self-Supervised Learning

- **arXiv**: [2607.22149](https://arxiv.org/abs/2607.22149)
- **Authors**: Léo Nicollier, Marc Pic, Pablo Musé, Enric Meinhardt-Llopis, Gabriele Facciolo
- **TL;DR**: Shows JEPA/SSL global regularization (Gaussian/uniform priors) is insufficient to prevent bias entanglement; proposes conditional distribution matching (UOWReg) that provably guarantees statistical independence between representations and protected attributes.
- **Problem**: JEPA and SSL methods enforce global target distributions (Gaussian, uniform on sphere) to prevent collapse, but these global constraints don't prevent the latent space from segregating along spurious bias dimensions (race, gender, etc.). Task-irrelevant features can still dominate the representation.
- **Architecture**: UOWReg (Unbiased Open World Regularization) — Replaces global distribution matching with conditional distribution matching. For each protected attribute value, enforce the target distribution independently. This shift from global to conditional objective provably guarantees statistical independence between learned representations and protected attributes. Works with both Gaussian and spherical target distributions. Encoder-only framework — no auxiliary networks needed.
- **Compute Scale**: Small-Mid (8-24G): Encoder-only; evaluated on CelebA and a novel Synthetic Engraving Task.
- **LeCun Alignment**: MEDIUM — Addresses a practical concern for JEPA deployment (bias/fairness) but doesn't advance the core world model theory. The finding that global regularization is insufficient for debiasing is relevant to JEPA practitioners, as all JEPA variants (I-JEPA, V-JEPA, LeWM) use global regularization (SIGReg, VICReg, etc.) that could encode spurious biases. The conditional matching approach could be integrated into JEPA training.
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: UOWReg — Shift JEPA/SSL regularization from global distribution matching to conditional distribution matching. For each value of a protected attribute, enforce the target distribution independently. This guarantees statistical independence between representations and attributes.
- **Motivation**: Standard JEPA regularization (SIGReg enforces isotropic Gaussian) prevents collapse but doesn't prevent bias — the latent space can still segregate by spurious attributes. This is a practical concern for deploying JEPA-based systems in high-stakes applications where fairness matters.
- **Problem Solved**: Provides theoretical guarantee (statistical independence) for debiased SSL/JEPA representations. Empirically reduces Equalized Odds violations on CelebA while maintaining accuracy. On a novel Synthetic Engraving Task (macro-structure masks micro-signature), UOWReg successfully isolates micro-signatures that standard SSL collapses into the dominant macro-structure.

### Academic Context

- **Inheritance / Response**: Builds on JEPA/SSL regularization literature (VICReg, SIGReg) and fairness in representation learning (EnD, FSCL). Shows that existing debiasing methods are partial approximations of conditional distribution matching.
- **Implicit Connection**: This paper flags a blind spot in the JEPA research programme: the same global regularization that prevents collapse can also encode dataset biases. For JEPA world models deployed in social contexts (e.g., autonomous driving where pedestrian detection must be fair across demographics), this is a practical concern. The conditional matching approach is compatible with SIGReg and could be incorporated into LeWM training.
- **Research Line**: Fair JEPA — debiasing joint embedding representations for equitable deployment.
- **Future Directions**: Integration with SIGReg-regularized JEPA training; multi-attribute debiasing; fairness-aware world model planning.
- **GitHub**: To be checked

---

## [2026-07-15] Depth-Regularized JEPA World Models Learn More Transferable Representations from Real Outdoor Robot Data

- **arXiv**: [2607.16314](https://arxiv.org/abs/2607.16314)
- **Authors**: Usman M. Khan
- **TL;DR**: Adds depth as a geometric prior during JEPA world model training on real outdoor robot video, achieving 33% lower visual odometry error and improved surprise detection — all without inference overhead.
- **Problem**: JEPA world models struggle with visually complex real-world outdoor data. Standard approaches don't leverage geometric structure that could help learn more robust latent dynamics from noisy, unstructured robot video.
- **Architecture**: Depth-regularized JEPA world model — Combines depth supervision with SIGReg (isotropy-inducing latent regularizer) during training. Adds training-only overparameterization for handling greater complexity without increasing inference cost. 18M parameters. Evaluated via frozen-representation visual odometry probes, predictor-based surprise detection, and multi-step latent rollout fidelity on real agricultural robot data.
- **Compute Scale**: Small (8-12G): 18M-parameter model trained on single GPU.
- **LeCun Alignment**: HIGH — Directly extends JEPA world models for real embodied deployment. Depth as a physically-grounded prior aligns with LeCun's vision of world models that learn from structured sensory input. Uses SIGReg (the same anti-collapse regularizer from LeJEPA). Evaluates on surprise detection and multi-step rollout — core world model capabilities. Shows that lightweight geometric priors make JEPA world models more transferable without adding inference overhead, critical for deployment on real robots.
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: Depth-Regularized JEPA — A JEPA world model that uses monocular depth as a training-time geometric prior (combined with SIGReg regularization) to learn more robust latent dynamics from real outdoor robot video. The depth supervision acts as a physically grounded inductive bias that helps the world model disentangle scene geometry from appearance.
- **Motivation**: Existing JEPA world models are mostly evaluated in simulation or controlled indoor settings. Real outdoor environments (agricultural robots, autonomous vehicles) introduce visual complexity — varying lighting, shadows, terrain textures — that challenge purely appearance-based latent dynamics learning. Depth provides a complementary geometric signal that is invariant to many appearance variations.
- **Problem Solved**: Demonstrates that adding depth as a training-only prior (no inference cost) significantly improves JEPA world model quality on real outdoor data: 33% lower visual odometry error, substantially better surprise-score separation (both in-domain and on out-of-domain TartanGround benchmark), and improved multi-step rollout fidelity under domain shift. Gains grow with rollout horizon, suggesting the geometric prior helps learn more stable long-term dynamics.

### Academic Context

- **Inheritance / Response**: Builds directly on LeWM (LeWorldModel) and SIGReg-regularized JEPA. Extends the JEPA world model paradigm from controlled settings to real outdoor robot data. The use of SIGReg connects to the broader LeCun research programme on anti-collapse regularization for JEPA.
- **Implicit Connection**: This work demonstrates a key principle in LeCun's vision: world models should learn from multiple complementary sensory modalities (here, RGB + depth). The finding that a geometric prior improves representations even for non-geometric tasks (lighting, shadows) suggests that structured inductive biases help JEPA learn more factorized, generalizable world representations.
- **Research Line**: Real-World JEPA — scaling JEPA world models from simulation to real outdoor deployment, with emphasis on training efficiency (training-only priors, no inference overhead).
- **Future Directions**: Extension to multi-modal priors (semantic segmentation, surface normals); application to planning and control on real agricultural robots; scaling to larger models and more diverse outdoor environments.
- **GitHub**: To be checked

---

## [2026-07-08] The JEPA Predictor: A Transferable Operator for Occluded Feature Completion

- **arXiv**: [2607.16274](https://arxiv.org/abs/2607.16274)
- **Authors**: William Nguyen, Christopher Nguyen
- **TL;DR**: Shows that the trained predictor from JEPA models (I-JEPA, V-JEPA 2) is a portable operator that can be bolted onto non-JEPA encoders (CLIP, DINOv3, DINOv2, MAE) via a simple linear projection, recovering accuracy under heavy occlusion — the JEPA predictor generalizes across encoder families.
- **Problem**: JEPA predictors are typically discarded after training — only the encoder is used downstream. But the predictor is a learned operator from visible-context features to features at masked positions. Can this capability be transferred to other encoders that weren't trained with JEPA?
- **Architecture**: Portable JEPA Predictor — Take a frozen JEPA predictor (from I-JEPA or V-JEPA 2) and bolt it onto a frozen non-JEPA host encoder (CLIP, DINOv3, DINOv2, MAE) via a single linear projection between feature spaces, fit in closed form on just 500 ImageNet-1k images. The projection pays a fixed cost on visible patches; the predictor provides growing benefit on masked patches. At heavy occlusion (high K), the benefit dominates. Evaluated on ImageNet-9 and Stanford Dogs across three mask fractions.
- **Compute Scale**: Small-Mid (8-24G): Frozen encoders + linear projection on 500 images. No retraining required.
- **LeCun Alignment**: HIGH — This work validates a core architectural insight of JEPA: the predictor learns a general-purpose operator for completing latent features from partial observations, not just a task-specific byproduct of training. The portability finding suggests that JEPA-style training produces representations and operators that capture fundamental structure, aligning with LeCun's vision of architectures that learn the underlying structure of the world rather than surface-level pixel correlations. The occluded feature completion task is directly relevant to world models operating under partial observability.
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: The Frozen JEPA Predictor — Demonstrate that JEPA-trained predictors function as portable, transferable operators for occluded feature completion. A single linear projection (fit on 500 images) is sufficient to bridge the feature spaces between the JEPA encoder and any host encoder, enabling the host to benefit from the JEPA predictor's learned completion capability.
- **Motivation**: The standard JEPA pipeline discards the predictor after training. But the predictor has been trained on a difficult task — predicting features at masked locations from visible context — and may have learned generalizable completion strategies. If portable, JEPA predictors could be a drop-in module to improve any vision encoder's robustness to occlusion.
- **Problem Solved**: Empirically demonstrates that frozen JEPA predictors substantially close the accuracy gap between masked and unmasked encoders across diverse host architectures. CLIP paired with I-JEPA predictor recovers most accuracy on ImageNet-9 at heavy occlusion. On fine-grained Stanford Dogs, lifts accuracy from 15.9% to 52.1% (+36pp). The mechanism is identifiable: the projection has a fixed cost on visible patches, the predictor provides growing benefit on masked patches, and the benefit dominates in heavy-occlusion regimes.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA, V-JEPA 2, and the broader JEPA literature. The key insight — that the JEPA predictor is a generalizable operator, not just an auxiliary training component — reframes how we think about JEPA architectures.
- **Implicit Connection**: This finding supports a core tenet of LeCun's vision: learning to predict in latent space (rather than pixel space) produces more transferable, generalizable representations and operators. The predictor's portability suggests it has learned something fundamental about feature completion that transcends the specific encoder it was trained with — a form of structural knowledge that aligns with the world model agenda.
- **Research Line**: JEPA Architecture Analysis — understanding the components of JEPA and their generalization properties.
- **Future Directions**: Extension to video predictors (V-JEPA → CLIP for temporal completion); application to robotic perception under occlusion; theoretical analysis of why the linear bridge works; scaling to larger predictors and more diverse hosts.
- **GitHub**: To be checked

---

## [2026-07-22] JEPA-CFM: A JEPA-based Channel Foundation Model for Robust Fluid Antenna Systems

- **arXiv**: [2607.20202](https://arxiv.org/abs/2607.20202)
- **Authors**: Yuan Gao, Yiming Liu, Jun Jiang, Jianbo Du, Shunqing Zhang, Xiaoli Chu, Kai-Kit Wong
- **TL;DR**: Applies JEPA with SIGReg regularization to 6G wireless channel modeling, outperforming standard masked autoencoders on channel extrapolation and positioning tasks for fluid antenna systems.
- **Problem**: Fluid antenna systems (FAS) for 6G need real-time channel state information (CSI) extrapolation to unmeasured antenna ports and accurate user positioning, but strong spatial correlations and sparse observations make this challenging for conventional approaches.
- **Architecture**: JEPA-CFM — JEPA-based channel foundation model. Pre-training combines three loss terms: standard MAE reconstruction loss + JEPA latent prediction loss + SIGReg regularization. After pre-training, the encoder is frozen and lightweight task heads are attached for channel extrapolation (decoder) and wireless positioning (MLP regression). Evaluated on DeepMIMO urban scenario simulations.
- **Compute Scale**: Mid (24G): Pre-training on simulated wireless channel data + lightweight task heads.
- **LeCun Alignment**: MEDIUM — Cross-domain validation of the JEPA + SIGReg recipe in a completely different modality (wireless channel state information). Demonstrates that JEPA's latent prediction approach generalizes beyond vision/audio to structured physical signals. However, this is primarily a domain application rather than advancing world model theory or architecture. The use of MAE reconstruction loss alongside JEPA is a hybrid approach that partially contradicts JEPA's pure latent-prediction philosophy.
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: JEPA-CFM — Adapt the JEPA pre-training paradigm (latent prediction + SIGReg regularization) to wireless channel modeling for fluid antenna systems. The model learns versatile representations of channel state information that transfer to downstream tasks (channel extrapolation, positioning) with lightweight task-specific heads.
- **Motivation**: 6G fluid antenna systems promise rich spatial diversity but require accurate CSI estimation at unmeasured antenna ports — a prediction task that JEPA's masked latent prediction is naturally suited for. Conventional MAE approaches that reconstruct raw CSI coefficients are inefficient and don't capture the abstract structure of wireless channels.
- **Problem Solved**: JEPA-CFM substantially outperforms conventional MAE baselines on both channel extrapolation and wireless positioning in realistic DeepMIMO urban scenarios. The SIGReg regularizer prevents representation collapse under severe spatial correlation and sparse observations — a practical validation of SIGReg's effectiveness in a new domain.

### Academic Context

- **Inheritance / Response**: Combines JEPA (I-JEPA/V-JEPA style latent prediction) with SIGReg regularization and MAE reconstruction in a hybrid objective. The application to wireless communications demonstrates the generality of the JEPA paradigm.
- **Implicit Connection**: Interesting as a cross-domain stress test of JEPA + SIGReg. The fact that this recipe works for wireless signals (fundamentally different from images/video) supports the claim that JEPA captures a general principle of representation learning rather than a vision-specific trick. However, the hybrid MAE+JEPA approach is less aligned with LeCun's pure latent-prediction philosophy.
- **Research Line**: JEPA Domain Transfer — validating the JEPA paradigm across diverse modalities beyond vision/audio.
- **Future Directions**: Extension to other wireless scenarios (massive MIMO, mmWave); integration with real-time adaptive systems; removing the MAE reconstruction component for a pure JEPA approach.
- **GitHub**: To be checked

---

## 1. [2026-07-23] Self-Supervised Learning of Structured Dynamics from Videos

- **arXiv**: [2607.21576](https://arxiv.org/abs/2607.21576)
- **Authors**: Lukas Knobel, Andrew Zisserman, Yuki M. Asano
- **TL;DR**: Learns to decompose video dynamics into camera vs. object motion via future-feature prediction from frozen ViT features — JEPA-aligned structured representation learning without pixel reconstruction.
- **Problem**: Video frame changes entangle camera and object motion, making it hard to learn robust dynamics representations. Current SSL methods treat all temporal change as a single entangled latent or use unstructured dense transition tokens.
- **Architecture**: Structured Dynamics Model (SDM) — Uses frozen pretrained ViT features as prediction targets; explicitly separates the dominant source of temporal change (camera motion) from residual dynamics (object motion) through future-feature prediction. No pixel decoder — all prediction in latent feature space. Trained with self-supervised learning on real video + weak supervision on synthetic Kubric data.
- **Compute Scale**: Small-Mid (8-24G): Frozen ViT backbone, lightweight prediction heads. Trained on real video + synthetic Kubric data.
- **LeCun Alignment**: MEDIUM-HIGH — Future-feature prediction paradigm matches JEPA's core design: predict in latent space, not pixel space. Structured dynamics decomposition (camera vs. object) aligns with LeCun's call for world models that learn factorized, interpretable representations of physical dynamics. Introduces ProbeMotion benchmark for structured dynamics evaluation. Not explicitly JEPA-branded and focused on representation learning rather than planning/control, but architectural philosophy is strongly aligned with the JEPA research programme.
- **GitHub**: To be checked

### What / Why / Solve

- **Proposal**: SDM — A structured dynamics model that decomposes video motion into camera-induced and object-induced components via future-feature prediction from frozen ViT features. Introduces ProbeMotion evaluation suite.
- **Motivation**: Current video SSL methods don't disentangle camera motion from object motion, limiting their ability to learn robust, interpretable dynamics representations. This decomposition is crucial for downstream tasks that need to reason about physical object behavior independent of viewpoint changes.
- **Problem Solved**: Demonstrates that frozen pretrained image ViT features contain sufficient information to recover structured dynamics when combined with appropriate architectural inductive biases. SDM outperforms global-pooled baselines and compares favorably to strongly supervised VGGT on motion probing tasks.

### Academic Context

- **Inheritance / Response**: Builds on frozen-feature evaluation (probing paradigm), ViT pretraining literature (DINO, etc.), and video self-supervised learning. The future-feature prediction objective echoes JEPA's latent-space prediction philosophy.
- **Implicit Connection**: This is the representation-learning counterpart to JEPA-style world models. While JEPA predicts future latent states for planning, SDM learns to decompose those latent dynamics into interpretable components (camera vs. object). Together, they suggest a pipeline: SDM for structured dynamics representation → JEPA for predictive world modeling → hierarchical planning.
- **Research Line**: Structured Video Dynamics — learning factorized motion representations as building blocks for world models.
- **Future Directions**: Integration with action-conditioned prediction (world model extension); scaling to longer horizons; application to embodied agent perception.
- **GitHub**: To be checked

---

## 2. [2026-07-21] Masked Visual Actions for Unified World Modeling

- **arXiv**: [2607.19343](https://arxiv.org/abs/2607.19343)
- **Authors**: Hadi Alzayer, Wenlong Huang, Haonan Chen, Christopher Luey, Lvmin Zhang, Maneesh Agrawala, Gordon Wetzstein, Li Fei-Fei, Yilun Du, Jiajun Wu, Jia-Bin Huang
- **Abstract**: Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling. The central challenge is how to communicate action to such models in a form aligned with the visual space in which they learned these interaction priors, yet still grounded in physical manipulation. We introduce Masked Visual Actions, a pixel-space control interface that expresses action as a partially revealed trajectory of an arbitrary entity in a video. Revealing robot motion makes the model act as a forward dynamics model that predicts the scene's response to low-level robot actions, while revealing desired object motion makes the same model recover robot behavior consistent with that outcome. Finetuned with only 15 hours of masked examples from real videos and simulation, a single checkpoint achieves strong visual fidelity and controllability across diverse scenes and multiple embodiments. In downstream manipulation settings, the model produces imagined rollouts whose outcomes correlate with real-world execution for policy evaluation, improves decision making by ranking candidate futures in model-based planning, and supports inverse modeling by synthesizing robot motion from desired object motion.
- **Compute Scale**: Large (40G+): Video generation + robotics fine-tuning on multiple embodiments.
- **LeCun Alignment**: MEDIUM — Uses generative video models as world model substrates (counterpoint to JEPA). Pixel-space action conditioning provides practical robotics utility, but LeCun would argue latent-space prediction is more efficient. Relevant as a strong generative-video world modeling baseline for robotics.

### What / Why / Solve

- **Proposal**: Masked Visual Actions — a pixel-space control interface for video models that expresses action as partially revealed trajectories in video frames. Enables a single checkpoint to serve as forward dynamics model (robot→scene), inverse model (object→robot), and planner.
- **Motivation**: Video models have learned rich visual-physics priors, but communicating physical actions to them is hard. Most approaches use text or numeric tokens that don't align with the visual space.
- **Problem Solved**: Demonstrates that video models fine-tuned with masked visual actions can serve as world models for robotics — generating rollouts correlated with real execution, improving model-based planning, and supporting inverse modeling. Only 15 hours of fine-tuning data needed.

### Academic Context

- **Inheritance / Response**: Builds on video generation models (Sora, etc.) and extends them for robotic world modeling. The pixel-space action interface is novel — different from text-conditioning or latent actions.
- **Implicit Connection**: Represents the generative video approach to world modeling that LeCun critiques. Strong results with minimal data suggest video models capture useful physical priors, even if the generative approach is computationally expensive.
- **Research Line**: Video World Models — using pre-trained video generators as world simulators for robotics.
- **Future Directions**: Integration with JEPA-style latent prediction for efficiency; multi-task generalization beyond the trained embodiments.
- **GitHub**: To be checked

---

## 3. [2026-07-15] When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models

- **arXiv**: [2607.14169](https://arxiv.org/abs/2607.14169)
- **Authors**: Javier Aguilar Martín
- **Abstract**: Large language models can synthesize a game's rules as executable code — a Code World Model (CWM) — which a classical planner then searches over. Such models are typically accepted when they reach high transition accuracy on sampled trajectories. We argue this is the wrong notion of adequacy for planning. We show four things: (1) An LLM-synthesized CWM can pass a sampling gate at 100% transition accuracy and be ≥98% state-accurate on the planner's own search distribution, yet lose systematically at play, because the <1% it gets wrong is exactly the pivotal dynamics. (2) The harm follows a quantitative law: danger = play_cost × (1−rarity)^N. (3) The failure is not repaired by more data — LLM synthesis behaves as rule translation, not rule inference. (4) The same mechanism recurs on the belief-inference function of imperfect-information CWMs. These results suggest adequacy for planning-oriented world models should be measured on the search distribution or by play directly, not by prediction accuracy on sampled transitions.
- **Compute Scale**: Small (8-12G): LLM-synthesized code world models on board games; primarily conceptual/theoretical.
- **LeCun Alignment**: MEDIUM — The core insight that prediction accuracy ≠ planning utility directly supports LeCun's argument that world models should be evaluated by their usefulness for downstream tasks, not raw reconstruction/prediction fidelity. However, the paper uses LLM-synthesized symbolic world models rather than learned latent world models.

### What / Why / Solve

- **Proposal**: Code World Models (CWMs) synthesized by LLMs can have near-perfect transition accuracy yet fail catastrophically at planning because the tiny fraction of errors hits exactly the pivotal dynamics. Introduces a quantitative danger law and argues for play-based evaluation.
- **Motivation**: Current world model evaluation uses prediction accuracy on sampled transitions, which systematically misses rare-but-critical dynamics. This "verified-vs-correct gap" means models that pass all tests can still lose every game.
- **Problem Solved**: Provides formal analysis of why prediction accuracy is insufficient for world model evaluation. Proposes that adequacy should be measured on the planner's search distribution or by actual play outcomes.

### Academic Context

- **Inheritance / Response**: Builds on the literature of LLM-synthesized world models and model-based planning. Responds to the assumption that high transition accuracy implies good planning performance.
- **Implicit Connection**: The danger law (danger = play_cost × (1−rarity)^N) parallels concerns in LeCun's vision: a world model that is 99% accurate but misses rare critical events (collisions, physical violations) fails as a planning substrate. This validates the need for architectures like JEPA that learn causally relevant representations rather than pixel-perfect predictions.
- **Research Line**: World Model Evaluation — establishing proper adequacy criteria for planning-oriented world models.
- **Future Directions**: Extending the analysis to continuous-state learned world models; integration with JEPA-style evaluation protocols.
- **GitHub**: To be checked

---

## 4. [2026-05-14] Crys-JEPA: Accelerating Crystal Discovery via Embedding Screening and Generative Refinement

- **arXiv**: [2605.14759](https://arxiv.org/abs/2605.14759)
- **Authors**: Nian Liu, Nikita Kazeev, Stephen Gregory Dale, Artem Maevskiy, Yuwei Zeng, Ryoji Kubo, Pengru Huang, Thomas Laurent, Yann LeCun, Kostya S. Novoselov, Xavier Bresson
- **Abstract**: De novo crystal generation seeks to discover materials that are not merely realistic, but also stable and novel. However, most existing generative models are trained to maximize the likelihood of observed crystals, which encourages samples to stay close to known materials yet not necessarily align with the criteria that matter in discovery. Our empirical analysis shows that current crystal generative models exhibit a clear conflict between stability and novelty. To move beyond this limitation, we introduce Crys-JEPA, a joint embedding predictive architecture for crystals that learns an energy-aware latent space preserving formation-energy differences. In this space, stability assessment can be reformulated as an embedding-based screening, enabling efficient filtering of candidate structures. Combined with a generative refinement stage, Crys-JEPA achieves state-of-the-art performance in discovering stable and novel crystals, outperforming purely generative approaches.
- **Compute Scale**: Mid (24G): Crystal structure prediction benchmarks; JEPA training + generative refinement.
- **LeCun Alignment**: MEDIUM — **LeCun is a co-author.** Extends JEPA architecture to scientific discovery (materials science). Demonstrates JEPA's generality beyond vision/robotics. The energy-aware latent space aligns with LeCun's energy-based model philosophy. However, the paper is about crystal discovery, not autonomous intelligence/world models for planning.

### What / Why / Solve

- **Proposal**: Crys-JEPA — a JEPA for crystals that learns an energy-aware latent space preserving formation-energy differences. Stability assessment becomes embedding-based screening (fast), combined with generative refinement (accurate). Outperforms purely generative crystal discovery methods.
- **Motivation**: Existing generative models for crystal discovery optimize for likelihood of known crystals, creating a stability-novelty trade-off. Samples near the training distribution are stable but not novel; samples far from it lose stability.
- **Problem Solved**: Crys-JEPA's energy-aware latent space enables efficient screening for both stability and novelty. The JEPA architecture avoids the stability-novelty conflict that plagues likelihood-based generative models.

### Academic Context

- **Inheritance / Response**: Builds on the I-JEPA and V-JEPA architectures, adapting joint embedding prediction to crystal structures. Responds to limitations of FlowMM, DiffCSP, and other generative crystal models.
- **Implicit Connection**: Demonstrates the generality of JEPA — the same architectural principles (joint embedding, latent prediction, no reconstruction) that work for vision also work for materials science. Validates LeCun's claim that JEPA is a broadly applicable self-supervised learning paradigm.
- **Research Line**: JEPA Applications — extending joint embedding predictive architectures to scientific domains.
- **Future Directions**: Multi-property JEPA for simultaneous optimization of stability, band gap, and synthesizability; integration with active learning for closed-loop materials discovery.
- **GitHub**: To be checked

---

## 5. [2026-07-20] SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning

- **arXiv**: [2607.17973](https://arxiv.org/abs/2607.17973)
- **Authors**: Letian Cheng, Qi Zhang, Yisen Wang
- **Abstract**: Latent world models have emerged as a powerful planning paradigm by learning action-conditioned predictive dynamics and using them as internal simulators to imagine and evaluate candidate action sequences. However, as the planning horizon grows, performance becomes increasingly constrained by proposal quality: a fixed candidate budget must search an exponentially larger action space, making it difficult to expose the world model to high-quality candidate futures for evaluation. In this paper, we introduce a prior-conditioned planner that replaces random proposal initialization with structured guidance. At each planning stage, a goal-conditioned generator predicts the next reachable latent subgoal for a specified duration, which is then used to condition the generation of candidate action sequences. To capture semantic information across temporal scales, we use subgoals of varying durations as priors, balancing fine-grained local control with higher-level long-horizon progress. Then the frozen world model evaluates and refines these subgoal-conditioned proposals before execution. Experiments on PushT and OGBench Cube show that coupling latent subgoal decomposition with prior-conditioned action generation substantially improves long-horizon planning while preserving strong short-horizon performance. To be specific, when the target offset is 150, it raises PushT success from 12.7% to 64.7% and OGBench Cube success from 26.7% to 67.3%.
- **Compute Scale**: Mid (24G): PushT and OGBench Cube benchmarks with frozen world model.
- **LeCun Alignment**: HIGH — Directly addresses the planning bottleneck in latent world models. Uses frozen world model as simulator (not generative). Subgoal decomposition aligns with LeCun's hierarchical planning vision.

### What / Why / Solve

- **Proposal**: SAGE — Prior-conditioned planner that replaces random action proposals with goal-conditioned subgoal generation. A subgoal generator predicts reachable latent subgoals at multiple temporal scales, then the frozen world model evaluates and refines them.
- **Motivation**: Random action proposals can't efficiently explore the exponentially growing action space at long horizons. The world model never sees good candidate futures, so planning fails even if the model is accurate.
- **Problem Solved**: 5x improvement on long-horizon PushT (12.7% → 64.7%). Shows that planning quality, not model accuracy, is the bottleneck for long-horizon world model control.

### Academic Context

- **Inheritance / Response**: Builds on latent world model planners (TD-MPC, Dreamer). Addresses the proposal bottleneck that limits all sampling-based planning approaches.
- **Implicit Connection**: Validates LeCun's hierarchical planning vision: subgoal decomposition at multiple temporal scales is essential for long-horizon reasoning. The frozen world model + separate planner mirrors LeCun's modular architecture.
- **Research Line**: Latent World Model Planning — improving proposal quality for model-based control.

- **Future Directions**: Learned subgoal durations; integration with action-chunked JEPA; multi-task generalization.
- **GitHub**: To be checked (possible: github.com/BerkinChen/AlphaSAGE)

---

## 6. [2026-07-20] Thinking in Video: Can Video Generators Really Reason About the Real World?

- **arXiv**: [2607.17523](https://arxiv.org/abs/2607.17523)
- **Authors**: Yongheng Zhang, Guang Yang, Ruihan Hou, Qiguang Chen, Ziang Liu, Xiaolong Liu, Manman Zhang, Yanchao Hao, Zheng Wei, Hao Wu, Libo Qin, Peishan Dai, Yinghui Li, Di Yin, Xing Sun
- **Abstract**: Recent advances in world models and video generation have given rise to an emerging reasoning paradigm that leverages video generative models to simulate, predict, and reason about real-world dynamics. We redefine this paradigm as Thinking in Video, where video is not merely an output artifact but a medium for constructing, extending, and verifying causal thought. However, this promise remains unverified: convincing rollouts may reflect memorized appearances rather than causal understanding, while existing metrics separate perceptual fidelity from semantic logic. To evaluate whether video generators support such reasoning, we introduce the Causal-Generative Dual-Judge (CGDJ), auditing World Model Consistency from two perspectives. Explicit Causal Perception tests whether a generator reads a video scenario as a reasoning problem through spatio-temporal flattened visual question answering, while Implicit Generative Perception-Prediction Gap evaluates whether it renders the causal consequence as a consistent future video. Applying CGDJ to representative open- and closed-source generators reveals a clear Perception-Prediction Gap: open-source models produce plausible dynamics despite near-zero explicit causal perception, whereas advanced closed-source systems show stronger but still limited alignment between reasoning and generation. Further analysis exposes audio-visual misalignment, where models verbalize correct causal logic more reliably than they render it, challenging the "world simulator" narrative.
- **Compute Scale**: N/A (evaluation/benchmark framework).
- **LeCun Alignment**: MEDIUM-HIGH — Provides empirical evidence that generative video models ≠ world understanding. The "Perception-Prediction Gap" finding directly supports LeCun's argument that pixel-space generation is insufficient for causal reasoning.

### What / Why / Solve

- **Proposal**: CGDJ (Causal-Generative Dual-Judge) — A dual-perspective evaluation framework that tests both explicit causal perception (can the model answer causal questions?) and implicit generative prediction (can it render consistent futures?).
- **Motivation**: Current video world model evaluations only measure perceptual quality, not whether the model actually understands causality. "Thinking in Video" requires causal understanding, not just plausible pixels.
- **Problem Solved**: Demonstrates a clear Perception-Prediction Gap: open-source models produce plausible dynamics with near-zero explicit causal perception. Audio-visual misalignment: models verbalize correct logic but can't render it. This directly challenges the "world simulator" narrative for generative video models.

### Academic Context

- **Inheritance / Response**: Responds to the "Sora/V-JEPA as world simulators" debate (2407.10311, 2405.03520). Provides the evaluation methodology that debate was missing.
- **Implicit Connection**: This is the EMPIRICAL counterpart to LeCun's philosophical argument. It provides the audit framework to show that generative video models DON'T learn causal world models — they learn to produce plausible continuations without understanding.
- **Research Line**: World Model Evaluation — distinguishing real understanding from memorized appearance.

- **Future Directions**: Extend CGDJ to action-conditioned generation; test JEPA-based models against generative ones.
- **GitHub**: To be checked

---

## 7. [2026-07-20] Patch Policy: Efficient Embodied Control via Dense Visual Representations

- **arXiv**: [2607.18236](https://arxiv.org/abs/2607.18236)
- **Authors**: Gaoyue Zhou, Zichen Jeff Cui, Ada Langford, Bowen Tan, Yann LeCun, Lerrel Pinto
- **Abstract**: Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have been underutilized in robot learning. Modern robot policies either compress each observation into a single global token, or rely on visual backbones trained from scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale visual pre-training. While there exist policies that do operate on dense patch features like large vision-language-action models (VLAs), they tend to be heavy and slow, inheriting the full cost of a billion-parameter vision-language model (VLM) backbone. We close this gap with Patch Policy, a minimal architectural extension that enables transformer-based policies to consume dense pre-trained patch tokens directly without the computational overhead of a full VLM. At its core is a block-causal attention mask that preserves the temporal causality of standard policies while letting the model attend over many patch tokens per observation, alongside other state information. Patch Policy is lightweight, fast, and highly effective. Across four simulated and three real-world environment suites, our method achieves a 40% relative improvement over policies using state-of-the-art global-pooled representations. Furthermore, it surpasses fine-tuned OpenVLA-OFT by 18% while using roughly 0.7% of the parameters.
- **Compute Scale**: Small-Mid (8-24G): Minimal architectural extension — 0.7% of OpenVLA parameters. Efficient block-causal attention.
- **LeCun Alignment**: MEDIUM — LeCun co-author. Uses dense pretrained visual features (JEPA-like philosophy of leveraging SSL representations) for embodied control. Not a world model, but advances the embodied AI component of LeCun's architecture.

### What / Why / Solve

- **Proposal**: Patch Policy — A minimal architectural extension using block-causal attention masks to let transformer policies consume dense ViT patch tokens directly, without full VLM overhead.
- **Motivation**: Robot policies either lose spatial detail (global pooling) or are too heavy (billion-parameter VLAs). Dense patch-level features are powerful but underutilized.
- **Problem Solved**: 40% improvement over global-pooled methods; beats OpenVLA-OFT by 18% with 0.7% of the parameters. Enables efficient, reactive control with rich visual features.

### Academic Context

- **Inheritance / Response**: Builds on ViT pretraining (DINO, JEPA-family features). Addresses the efficiency gap between VLAs and lightweight policies.
- **Implicit Connection**: From LeCun's group at NYU/Meta. While not a world model paper, it advances the perceptual front-end that world models and policies need. The dense patch representation philosophy echoes JEPA's emphasis on preserving spatial structure.
- **Research Line**: Embodied AI — efficient visual representations for robot control.

- **Future Directions**: Integration with JEPA-pretrained features; action-conditioned patch attention.
- **GitHub**: Project page: https://patch-policy.github.io

---

## 8. [2026-07-18] Learning from World Feedback: Why Model Uncertainty Fails as a Risk Signal in Model-Based RL

- **arXiv**: [2607.16591](https://arxiv.org/abs/2607.16591)
- **Authors**: Zhaohui Wang
- **Abstract**: The RLxF programme argues that learning signals should come from world feedback rather than from internal model proxies. We instantiate this position in safe model-based control and distil it into three concrete design principles. Empirically, across four world-model architectures spanning a 2x MSE range, MPC planning is statistically equivalent (TOST, n=200), and dynamics-based uncertainty penalties increase collision rates from 26% to 34%: the standard MBRL safety proxy is anti-correlated with safety in this regime. Replacing the model-internal proxy with three world-feedback signals (a sensor-derived margin via minimum lidar, a temporal signal via time-to-collision, and an outcome-supervised feedback model g_psi trained on prior collision labels, structurally analogous to outcome-trained reward models in RLHF) reduces collisions to 1-14% without retraining the world model or the planner. The mechanism is structural: model uncertainty has support over state-prediction space, whereas task risk has support over constraint boundaries, with empirical correlation r < 0.15. From this we extract three RLxF principles (ground risk in world outcomes, validate proxies before deployment, and substitute outcome-trained feedback models when direct world signals are unavailable) and argue they apply equally to model-based control and to verifier-based or RLHF approaches in LLM alignment.
- **Compute Scale**: Small-Mid (8-24G): Standard MBRL benchmarks. Four world-model architectures tested.
- **LeCun Alignment**: HIGH — Foundational critique of model-based RL that reinforces JEPA philosophy. Shows model-internal metrics (uncertainty) are anti-correlated with real-world outcomes. Argues for "world feedback" over "model proxy" signals — directly aligned with LeCun's emphasis on grounding in real-world consequences.

### What / Why / Solve

- **Proposal**: RLxF (Reinforcement Learning from X Feedback) programme applied to model-based control. Shows model uncertainty is anti-correlated with safety (r < 0.15). Proposes three world-feedback signals that reduce collisions from 26-34% to 1-14%.
- **Motivation**: Standard MBRL uses model uncertainty as a safety signal — but this assumes uncertainty in prediction space correlates with real-world risk. It doesn't.
- **Problem Solved**: Empirically proves that model uncertainty is WORSE than useless for safety (increases collisions). Provides three practical world-feedback alternatives. Extracts three design principles applicable to both MBRL and LLM alignment.

### Academic Context

- **Inheritance / Response**: Connects to the RLxF programme and safe RL. Provides structural analysis of why current MBRL safety approaches fail. The outcome-supervised feedback model g_psi is structurally analogous to RLHF reward models.
- **Implicit Connection**: This paper strengthens LeCun's position: internal model metrics (prediction error, uncertainty) don't capture what matters for real-world performance. The "world feedback" emphasis mirrors JEPA's focus on latent-space prediction quality over pixel reconstruction. The finding that prediction error doesn't correlate with task success echoes 2607.10362 (Control Theory of Predictability).
- **Research Line**: World Model Evaluation — world-feedback signals over model-internal proxies.

- **Future Directions**: Extend RLxF principles to JEPA-based planners; test with more complex safety constraints.
- **GitHub**: To be checked

---

## 9. [2026-07-04] Separating Representation from Reconstruction Enables Scalable Text Encoders

- **arXiv**: [2607.04011](https://arxiv.org/abs/2607.04011)
- **Authors**: Megi Dervishi, Mathurin Videau, Yann LeCun
- **Abstract**: While decoders have rapidly scaled, encoders have remained largely unchanged since BERT. We revisit this disparity by frozen backbone evaluation via probing. Under this lens, the representations of BERT encoders become increasingly unexploitable by frozen probes, despite improved perplexity. The misalignment originates in BERT's flat design, which couples representation learning to the token reconstruction loss. We propose CrossBERT, a two-part architecture that separates the learning of high-quality encoded representations from the rigid grounding of token reconstruction. This design further enables high masking ratios (≥50%) and gradient collection over all tokens via a Complementary Masking Strategy, respectively increasing throughput by 1.5 to 2× and sample efficiency by 2×. Overall, CrossBERT demonstrates monotonic scaling and superior performance on MTEB(eng, v2) and frozen GLUE benchmarks.
- **Compute Scale**: Mid (24G): MTEB/GLUE benchmarks with 1.5-2× throughput improvement.
- **LeCun Alignment**: MEDIUM — LeCun co-author. The philosophy of separating representation learning from reconstruction is JEPA-aligned (JEPA separates representation from pixel reconstruction; CrossBERT separates representation from token reconstruction). Not a world model, but demonstrates the JEPA principle in NLP.

### What / Why / Solve

- **Proposal**: CrossBERT — A two-part text encoder that separates representation learning from token reconstruction, unlike BERT's flat design. Uses Complementary Masking Strategy for 2× efficiency.
- **Motivation**: BERT encoders become "unexploitable" by frozen probes as they scale, despite improving perplexity. The coupling of representation and reconstruction is the root cause.
- **Problem Solved**: Demonstrates that decoupling representation from reconstruction enables monotonic scaling in text encoders. 1.5-2× throughput and 2× sample efficiency improvements.

### Academic Context

- **Inheritance / Response**: Builds on BERT and masked autoencoding. The "separate representation from reconstruction" philosophy directly parallels JEPA's core design principle.
- **Implicit Connection**: Although in NLP rather than vision/robotics, this paper validates a core JEPA insight across modalities: coupling representation quality to reconstruction fidelity is harmful to scalability. LeCun's name on this paper signals an intentional cross-modal research programme.
- **Research Line**: JEPA Philosophy — decoupling representation from reconstruction across modalities.

- **Future Directions**: Extend to multilingual and multimodal encoders; integrate with JEPA-style predictive objectives.
- **GitHub**: To be checked

---

## 10. [2026-06-07] Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks

- **arXiv**: [2606.08775](https://arxiv.org/abs/2606.08775)
- **Authors**: Raktim Gautam Goswami, Prashanth Krishnamurthy, Yann LeCun, Farshad Khorrami
- **Abstract**: Visual world models have shown great potential in learning complex system dynamics. Recent advancements leverage these models as transition functions within Model Predictive Control (MPC) frameworks to solve various control tasks. When applied to robotics, however, they are limited to single-stage tasks such as reaching or grasping, and struggle with multi-stage ones that demand complex sequential planning. In this work, we introduce WorldDP, a world model framework designed for multi-stage robotic manipulation. Our hierarchical approach utilizes a high-level world model as a transition function to optimize for feasible subgoals during runtime, which are subsequently reached by a low-level Diffusion Policy. To further aid in learning dynamics and planning, we incorporate object-centric representations that decouple environmental entities and enable us to plan sequentially with respect to each. Evaluated across several robotics benchmarks, WorldDP consistently outperforms existing baselines, validating that coupling the world model's physically grounded planning with diffusion policy's efficient execution yields superior multi-stage performance.
- **Compute Scale**: Mid (24G): Standard robotic manipulation benchmarks.
- **LeCun Alignment**: MEDIUM-HIGH — LeCun co-author. Hierarchical world model + diffusion policy. Object-centric representations align with LeCun's modular agent architecture (separate entity representations). However, uses generative diffusion for low-level execution rather than purely predictive latent-space approach.

### What / Why / Solve

- **Proposal**: WorldDP — Hierarchical framework: high-level object-centric world model plans subgoals via MPC; low-level Diffusion Policy executes. Object-centric representations decouple entities for sequential planning.
- **Motivation**: Current world model approaches are limited to single-stage tasks (reach, grasp). Multi-stage manipulation requires hierarchical planning with object-level decomposition.
- **Problem Solved**: Outperforms baselines on multi-stage robotic manipulation by combining world model planning (physically grounded) with diffusion policy execution (efficient, reactive).

### Academic Context

- **Inheritance / Response**: Bridges world model literature (Dreamer, TD-MPC) with diffusion policy work. Object-centric representations connect to slot attention and entity-based reasoning.
- **Implicit Connection**: From LeCun's group. The hierarchical architecture (high-level world model → low-level execution) mirrors LeCun's modular agent design. Object-centric decoupling aligns with the configurator + world model separation. However, the low-level Diffusion Policy is generative rather than JEPA-style predictive — a practical compromise for reactive control.
- **Research Line**: Hierarchical World Models — bridging model-based planning with learned reactive policies.

- **Future Directions**: Replace low-level diffusion with JEPA-style predictive policy; extend to more complex multi-object scenes.
- **GitHub**: To be checked

---

## 11. [2026-07-20] AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Learning

- **arXiv**: [2607.15295](https://arxiv.org/abs/2607.15295)
- **Authors**: Benjamin Robson, Santeri Mentu, Wenshuai Zhao, Arno Solin
- **Abstract**: We present AV-JEPA, an elegant multimodal extension of LeJEPA to audio-visual self-supervised learning. Using an early-fusion Vision Transformer and modality dropout as masking, the model is trained to align the embeddings of global and per-modality local views, while the SIGReg objective encourages a theoretically optimal distribution. This achieves cross-modal alignment in the latent space, resulting in a remarkably clean architecture with no decoder, EMA teacher, complex multi-term losses, or contrastive negatives. The proposed AV-JEPA backbone delivers competitive classification performance on VGGSound (57.1% top-1) and AudioSet (32.7 mAP) and supports zero-shot audio-video retrieval out of the box.
- **Compute Scale**: Mid (24G): Audio-visual ViT on VGGSound/AudioSet.
- **LeCun Alignment**: HIGH — Multimodal JEPA with clean architecture (no decoder, no EMA, no contrastive negatives).

### What / Why / Solve

- **Proposal**: AV-JEPA — Extends LeJEPA (stable JEPA variant) to audio-visual self-supervised learning via early-fusion ViT with modality dropout.
- **Motivation**: JEPA has been vision-only or audio-only. A multimodal JEPA that jointly processes audio and video demonstrates the generality of the framework.
- **Problem Solved**: First audio-visual JEPA using LeJEPA's SIGReg stabilization. Achieves cross-modal alignment without decoders, EMA teachers, or contrastive losses.

### Academic Context

- **Inheritance / Response**: Directly builds on LeJEPA/LeWorldModel (2603.19312) and SIGReg. Extends JEPA to audio-visual modality.
- **Implicit Connection**: Clean architecture validates LeCun's vision of simple, non-generative SSL. With A-JEPA and S-JEPA, completes JEPA coverage of audio+vision+speech.
- **Research Line**: Multimodal JEPA — audio-visual joint embedding without generation.

- **Future Directions**: Action-conditioned AV-JEPA for embodied agents; larger-scale training.
- **GitHub**: To be checked

---

## 12. [2026-07-15] The SIGReg Objective as Variational Free Energy: A Theoretical Active-Inference Account of JEPA World Models

- **arXiv**: [2607.13612](https://arxiv.org/abs/2607.13612)
- **Authors**: Fabio Arnez, Alexandra Gomez-Villa
- **Abstract**: Joint-Embedding Predictive Architectures (JEPAs) are the dominant design for latent world models, yet they are usually justified by empirical performance rather than a normative principle. We show that the choice of anti-collapse regulariser determines whether a JEPA's training objective (prediction loss + weighted embedding regulariser) is a valid Active Inference (AIF) variational free energy. We organise four non-contrastive regularisers (VICReg, LogDet, PairDist, SIGReg) into an entropy-estimator hierarchy indexed by a prior-miscalibration gap, and show that SIGReg eliminates the gap. We prove a correspondence theorem: under SIGReg enforcement (isotropic-Gaussian embeddings), the gap vanishes, the objective becomes an exact information bottleneck, and the latent goal cost becomes an exact proxy for AIF pragmatic value. We identify the one AIF term no current JEPA world model computes: the state-epistemic value, a future-state coverage signal. Full proofs are in Appendix A; the algebraic core of every result is machine-verified in Lean 4.
- **Compute Scale**: Small (8-12G): Theoretical paper with Lean 4 formal verification.
- **LeCun Alignment**: HIGH — Provides the normative principle that JEPA has been lacking. Connects JEPA to Active Inference and Free Energy Principle.

### What / Why / Solve

- **Proposal**: Proves that under SIGReg (isotropic Gaussian regularization), the JEPA training objective becomes EXACTLY the variational free energy from Active Inference. Provides a first-principles justification for JEPA architecture choices.
- **Motivation**: JEPA works empirically but lacks theoretical grounding. Why should latent-space prediction + anti-collapse regularization produce good world models? This paper answers that question.
- **Problem Solved**: Establishes JEPA as a theoretically principled architecture (not just an empirical hack). Shows SIGReg is uniquely correct among regularizers (VICReg/LogDet are "unsafe").

### Academic Context

- **Inheritance / Response**: Builds on LeWorldModel (2603.19312), I-JEPA (2301.08243), and Active Inference theory (Friston et al.).
- **Implicit Connection**: This is potentially the most important THEORETICAL paper for the JEPA program. It provides the normative foundation LeCun's vision has been missing — JEPA isn't just efficient, it's the CORRECT objective under Active Inference.
- **Research Line**: JEPA Theory — normative foundations connecting predictive architectures to free energy.

- **Future Directions**: Implement the missing state-epistemic value term; empirical validation of AIF predictions.
- **GitHub**: To be checked

---

## 13. [2026-07-14] Mind the Gap: Promises and Pitfalls of Hierarchical Planning in LeWorldModel

- **arXiv**: [2607.12547](https://arxiv.org/abs/2607.12547)
- **Authors**: Niccolò Caselli, Francesco Massafra, Samuele Punzo, Salvatore Lo Sardo, Ippokratis Pantelidis, Sathya Kamesh Bhethanabhotla
- **Abstract**: We investigate whether temporal hierarchy can improve LeWorldModel on long-horizon goal-conditioned control. We introduce Hi-LeWM, an extension that freezes the pretrained low-level LeWM and adds high-level planning over latent subgoals. Hierarchy does not automatically improve performance: at short horizons, the best configuration uses a one-step high-level horizon, while longer horizons reveal a mismatch between the learned high-level action space and the inference-time search distribution. Constraining search around macro-actions encoded from training trajectories, with appropriate subgoal execution timing, recovers useful hierarchical regimes, improving over flat LeWM by +11.3 percentage points at medium-range horizons and +14.7 percentage points at the longest PushT horizon.
- **Compute Scale**: Mid (24G): Two-level planning over frozen LeWM.
- **LeCun Alignment**: HIGH — Directly investigates hierarchical planning in LeCun's LeWorldModel.

### What / Why / Solve

- **Proposal**: Hi-LeWM — Adds hierarchical planning to LeWorldModel. High-level planner proposes latent subgoals; frozen low-level LeWM executes them. Investigates when hierarchy helps vs. hurts.
- **Motivation**: LeCun's architecture calls for hierarchical planning, but no one had tested it on the actual LeWorldModel. Does it actually work?
- **Problem Solved**: Provides empirical evidence that hierarchy CAN help (+14.7pp) but only with careful constraint. Random subgoal search in latent space fails. The bottleneck is high-level subgoal generation, not low-level execution.

### Academic Context

- **Inheritance / Response**: Directly builds on LeWorldModel (2603.19312). Connects to hierarchical RL and HWM (2604.03208).
- **Implicit Connection**: This is essential practical feedback for the LeWorldModel research line. Shows that LeCun's hierarchical vision is viable but requires careful design — unconstrained latent search produces "favorable-looking" but ineffective subgoals.
- **Research Line**: Hierarchical WAM — practical investigation of multi-level planning in JEPA world models.

- **Future Directions**: Learned subgoal generation; better latent-action space design; multi-level (3+) hierarchies.
- **GitHub**: To be checked

---

## 14. [2026-07-13] From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence

- **arXiv**: [2607.11689](https://arxiv.org/abs/2607.11689)
- **Authors**: Yuanzhi Liang, Xufeng Zhan, Haibin Huang, Chi Zhang, Xuelong Li
- **Abstract**: Artificial general intelligence ultimately requires agents that can reason and act in the physical world. World Action Models (WAMs) are particularly promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented: models use incompatible action spaces and prediction targets, datasets follow different conventions, and runtime systems expose limited interfaces. We review the evolution toward WAMs and organize these limitations into three coupled gaps: model roles and representations, objectives and standardization, and system composition. We propose a co-evolution roadmap centered on the "embodied brain", a long-term model target for integrating multimodal context, comparing candidate interventions, and issuing state-transition or capability requests rather than direct actuator commands. WAMs provide promising prototypes for its predictive functions, while a physical harness grounds model outputs through tools, controllers, verification, and trace logging.
- **Compute Scale**: N/A (roadmap/position paper)
- **LeCun Alignment**: HIGH — Explicitly about WAMs as the path to physical intelligence. Coins "embodied brain" concept aligned with LeCun's modular agent architecture.

### What / Why / Solve

- **Proposal**: A roadmap positioning World Action Models (WAMs) as the core predictive component of an "embodied brain" — a modular architecture where WAMs predict consequences of interventions rather than generating pixels or tokens.
- **Motivation**: The field is fragmented: different models use incompatible action spaces, datasets, and interfaces. A unified framework is needed to make progress toward physical intelligence.
- **Problem Solved**: Identifies three fragmentation gaps (representations, standardization, system composition) and proposes a modular stack centered on WAMs with tool-based physical grounding.

### Academic Context

- **Inheritance / Response**: Synthesizes world model literature (Dreamer, JEPA, VLA models) and robotic learning. Positions WAMs as the unifying abstraction.
- **Implicit Connection**: This paper crystallizes the WAM research agenda. The "embodied brain" concept directly mirrors LeCun's modular agent architecture (world model + cost + actor + configurator). It's essentially a 2026 update to LeCun's 2022 vision paper.
- **Research Line**: WAM Architecture — system-level design for physical intelligence.

- **Future Directions**: Standardized WAM interfaces; shared benchmarks; closed-loop post-training.
- **GitHub**: To be checked

---

## 15. [2026-07-11] A Control Theory of Predictability in Latent World Models

- **arXiv**: [2607.10362](https://arxiv.org/abs/2607.10362)
- **Authors**: Hanzhe You, Yonggang Zhang, Maohao Ran, Zhiqin Yang, Zhenyuan Zhang, Wei Xue, Jun Song, Xinmei Tian, Yike Guo
- **Abstract**: Latent world models are trained to predict future states and then deployed inside a planner that selects actions by simulating them forward. Current practice adopts prediction error as the training objective, assuming lower error yields better control. We show this assumption is unreliable for a structural reason: a planner does not query the model on the training distribution but on the states that its candidate actions reach, which generally leave the data manifold. We prove the planner's suboptimality is bounded by twice the discrepancy between predicted and true plan-cost, whereas data-averaged prediction error neither bounds nor tracks it. Under a linear-control premise, the discrepancy separates into on-manifold residual (small) and off-manifold divergence (binding). Experiments confirm the decoupling: across seeds, single-step validation error is essentially uncorrelated with control success, whereas a fidelity score on the planner-reachable measure tracks it.
- **Compute Scale**: Mid (24G): Synthetic + MPC experiments.
- **LeCun Alignment**: HIGH — Foundational finding that reshapes how we should evaluate world models.

### What / Why / Solve

- **Proposal**: Proves that prediction error on held-out data does NOT predict control performance for latent world models. The planner queries off-manifold states where the model has never been trained, making data-averaged error irrelevant.
- **Motivation**: Everyone trains world models to minimize prediction error, assuming better predictions = better control. This paper shows that's wrong, structurally and empirically.
- **Problem Solved**: Provides a control-theoretic framework for evaluating world models: measure discrepancy on planner-reachable states, not on training data. Identifies off-manifold divergence as the binding constraint.

### Academic Context

- **Inheritance / Response**: Builds on world model literature (Dreamer, TD-MPC, JEPA-based planners). Connects to control theory.
- **Implicit Connection**: This is a WAKE-UP CALL for the field. If prediction error doesn't correlate with control, then all world model benchmarks based on prediction error are misleading. JEPA's focus on latent-space prediction (rather than pixel reconstruction) is reinforced — what matters is whether the latent space supports planning, not whether it reconstructs well.
- **Research Line**: World Model Evaluation — control-theoretic metrics beyond prediction error.

- **Future Directions**: Planner-reachable fidelity metrics; training objectives that target control-relevant error.
- **GitHub**: To be checked

---

## 16. [2026-07-17] Orbis 2: A Hierarchical World Model for Driving

- **arXiv**: [2607.15898](https://arxiv.org/abs/2607.15898)
- **Authors**: Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso, Karim Farid, Jonannes Dienert, Rajat Sahay, Thomas Brox
- **Abstract**: Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks. We present a hierarchical driving world model that factorizes future prediction across two levels operating at distinct temporal and abstraction scales: a high-level predictor that forecasts semantic occupancy and traffic flow, and a low-level decoder that generates high-fidelity video conditioned on the high-level predictions.
- **Compute Scale**: Large (40G+): Two-level video prediction for driving.
- **LeCun Alignment**: MEDIUM — Hierarchical architecture is aligned, but generative (pixel-space) approach is what LeCun argues against. Important counterpoint.

### What / Why / Solve

- **Proposal**: Orbis 2 — Two-level hierarchical world model for autonomous driving. High level predicts semantic occupancy and traffic flow; low level generates video from those predictions.
- **Motivation**: Single-level world models can't capture both abstract scene semantics and fine-grained perceptual detail needed for driving.
- **Problem Solved**: Demonstrates that hierarchy improves both semantic reasoning AND perceptual quality in driving world models. However, it uses pixel-space generation (diffusion-based), unlike JEPA's latent-space approach.

### Academic Context

- **Inheritance / Response**: Builds on video diffusion world models (GAIA-1, Sora-like approaches). Hierarchy is the key contribution.
- **Implicit Connection**: Represents the GENERATIVE counterpoint to JEPA-based driving models (Drive-JEPA). Shows that generative approaches are still pushing forward on hierarchical architectures. The tension between Orbis 2's pixel generation and JEPA's latent prediction is the central debate in world model design.
- **Research Line**: Generative World Models — hierarchical video prediction for driving.

- **Future Directions**: JEPA-style latent prediction at both levels; real-time inference optimization.
- **GitHub**: To be checked

---

## 17. [2026-07-04] SiamJEPA: On the Role of Siamese Student Encoders in JEPA

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

## 18. [2026-06-30] AdaJEPA: An Adaptive Latent World Model

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

## 19. [2026-06-22] SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors

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

## 20. [2026-06-17] S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Representation Learning

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

## 21. [2026-06-14] You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences

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

## 22. [2026-05-25] When Does LeJEPA Learn a World Model?

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

## 23. [2026-05-25] UWM-JEPA: Predictive World Models That Imagine in Belief Space

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

## 24. [2026-05-20] stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation

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

## 25. [2026-05-15] DiLA: Disentangled Latent Action World Models

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

## 26. [2026-05-10] Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models

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

## 27. [2026-05-05] Text-Conditional JEPA for Learning Semantically Rich Visual Representations

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

## 28. [2026-04-03] Hierarchical Planning with Latent World Models

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

## 29. [2026-03-20] Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations

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

## 30. [2026-03-15] V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning

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

## 31. [2026-03-13] LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

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

## 32. [2026-03-07] Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction

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

## 33. [2026-03-05] Probabilistic Dreaming for World Models

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

## 34. [2026-02-12] JEPA-VLA: Video Predictive Embedding is Needed for VLA Models

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

## 35. [2026-01-29] Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving

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

## 36. [2025-11-21] DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture

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

## 37. [2025-10-07] Gaussian Embeddings: How JEPAs Secretly Learn Your Data Density

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

## 38. [2025-09-29] Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers

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

## 39. [2025-06-11] V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

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

## 40. [2024-10-25] Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning

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

## 41. [2024-08-14] CNN-JEPA: Self-Supervised Pretraining Convolutional Neural Networks Using Joint Embedding Predictive Architecture

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

## 42. [2024-05-06] Sora and V-JEPA Have Not Learned The Complete Real World Model -- A Philosophical Analysis of Video AIs Through the Theory of Productive Imagination

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

## 43. [2024-05-06] Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond

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

## 44. [2024-04-25] Point-JEPA: A Joint Embedding Predictive Architecture for Self-Supervised Learning on Point Cloud

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

## 45. [2024-03-16] Dreaming of Many Worlds: Learning Contextual World Models Aids Zero-Shot Generalization

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

## 46. [2024-03-08] Sora as a World Model? A Complete Survey on Text-to-Video Generation

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

## 47. [2023-11-27] A-JEPA: Joint-Embedding Predictive Architecture Can Listen

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

## 48. [2023-09-29] GAIA-1: A Generative World Model for Autonomous Driving

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

## 49. [2023-07-24] MC-JEPA: A Joint-Embedding Predictive Architecture for Self-Supervised Learning of Motion and Content Features

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

## 50. [2023-07-14] SafeDreamer: Safe Reinforcement Learning with World Models

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

## 51. [2023-01-19] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture

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

## 52. [2022-06-28] DayDreamer: World Models for Physical Robot Learning

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

## 53. [2022-02-19] TransDreamer: Reinforcement Learning with Transformer World Models

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


*Generated: 2026-07-31 | Papers: 77 | Daily scan: 5 new (Physical Parameter Identifiability, DLAM, Action from Adjacent Set, WCM, Mental World Modeling)*
