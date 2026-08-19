# WAM Research Log — Deep Analysis

> Curated papers from Yann LeCun's World Models/JEPA ecosystem, with detailed architectural analysis, research lineage, and LeCun alignment assessment.

> **184 papers** (2022—2026) | Daily monitoring at 08:00 UTC | Last scan: 2026-08-19 (22 papers added: 14 from the Aug 15–17 window — CaliBench, HarnessEval-W, τ₀-VLA, SCALE, Orbit-Planner, DriveCache, GaussianDWM++, Beyond Visual CoT, Gaussian-JEPA, AlignJEPA, Physiological WMs, Low-Rank Latent Carriers, SCOPE, Evidence of Absence — plus 8 backfills from Aug 12–14 — hint², Objective-Is-the-Bottleneck, ACPC diagnostic, Probabilistic-JEPA=HMM, CardioState-JEPA, ForeWAM, WMRL, EBM-tabular; arXiv stream ends at Aug 17 submission date)

---

## 📊 Paper Index

| # | Date | Paper | Alignment | Compute |
||---|------|-------|-----------|--------|
| 1 | 2026-08-17 | [CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?](https://arxiv.org/abs/2608.16829) | HIGH — Closed-form reference distributions (Galton boards, dice, roulette) test whether video WMs' stochastic outputs are physically calibrated; 6 I2V models consistently miscalibrate (Veo 3.1 collapses dice to one outcome) — direct empirical support for the generative-WM critique. | N/A (benchmark): 6 image-to-video models × 9 scenes, 32 generations/cell. |
| 2 | 2026-08-17 | [HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://arxiv.org/abs/2608.16859) | MEDIUM — Agentified WM evaluation: harness paradigm decomposes each eval case into subproblems for tool-equipped sub-agents, yielding verifiable evidence-tree reasoning chains instead of scalar scores; 18 WMs × 330 cases. | N/A (benchmark/evaluation pipeline). |
| 3 | 2026-08-17 | [τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885) | MEDIUM — Compute-scalable high-level subtask generation via execution-memory-guided search before committing; test-time compute allocation as deliberation. | Large (40G+): 40,115 hrs real-world data, multimodal co-training. |
| 4 | 2026-08-17 | [Orbit-Planner: Towards Latent World Models for On-Orbit Obstacle Avoidance of Satellite Agents](https://arxiv.org/abs/2608.16651) | MEDIUM-HIGH — Two-stage latent WM for satellites: action-conditioned latent rollouts + Physics Probe decoding physical state from imagined trajectories; 91.7% closed-loop success in Isaac Sim. | Small-Mid (8-24G): latent dynamics + probe on Isaac Sim. |
| 5 | 2026-08-17 | [DriveCache: Action-Aware Caching for Driving World Model Inference](https://arxiv.org/abs/2608.16354) | LOW-MEDIUM — Training-free cache controller for diffusion driving WMs using planned ego motion + causal drift check; generative-side inference efficiency only. | N/A training-free; underlying generators Large (40G+). |
| 6 | 2026-08-17 | [SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry](https://arxiv.org/abs/2608.16287) | HIGH — Regularizes LeWM embeddings so pairwise latent distances correlate with task-relevant state distances (DINO-WM-like geometry); improves every task-solver-budget combo; planning needs the right geometry, not just decodable state. | Mid (24G): LeWM + lightweight training-time regularizer, 5 tasks × 3 solvers × 5 budgets. |
| 7 | 2026-08-17 | [GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model](https://arxiv.org/abs/2608.16234) | LOW-MEDIUM — Foundation-feature Gaussian tokenizer distills Qwen/SigLIP features into 3DGS primitives for unified understanding/editing/generation; explicit 3D structure but generative dynamics. | Large (40G+): foundation-feature Gaussian field + adapters. |
| 8 | 2026-08-16 | [Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning](https://arxiv.org/abs/2608.15869) | MEDIUM-LOW — MLLMs can internalize visual reasoning in hidden states instead of generating reasoning images; latent-space thinking removes Visual CoT inference overhead — evidence for reasoning in representation space, though no world dynamics. | Mid-Large (24-40G+): MLLM video reasoning. |
| 9 | 2026-08-16 | [Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats](https://arxiv.org/abs/2608.15651) | HIGH — JEPA for 3DGS tokens: online encoder + EMA stop-gradient multi-scale targets, no input-space decoder; more consistent under resampling and better frozen features than reconstruction pretraining. | Small-Mid (8-24G): 3DGS encoder + EMA target on part segmentation/classification transfer. |
| 10 | 2026-08-16 | [AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models](https://arxiv.org/abs/2608.15456) | MEDIUM — JEPA-inspired masked prediction of text embeddings from visual tokens for RS foundation models; parameter-efficient but retains contrastive retrieval. | Small-Mid (8-24G): lightweight aligner on frozen AnySat + RemoteCLIP. |
| 11 | 2026-08-15 | [Physiological World Models for Human State Transitions](https://arxiv.org/abs/2608.15309) | MEDIUM-LOW — Event-conditioned whole-person physiological WM framework (HumanState Transition Tokens); separates prediction from causal inference; bounded intervention planning as top capability. | N/A (framework: 4 capability levels, 6 benchmark tasks). |
| 12 | 2026-08-15 | [Low-Rank Dynamics-Effective Latent Carriers for Counterfactual Rollout in Learned World Models](https://arxiv.org/abs/2608.15156) | HIGH — Rank-4 hidden-state patch redirects 12-step autonomous rollouts in a recurrent WM; preregistered replication + negative controls; defines "dynamics-effective" interventions and shows edit success alone is insufficient evidence. | Small-Mid (8-24G): 192-dim recurrent WM, controlled collision env. |
| 13 | 2026-08-15 | [SCOPE: Score-Isolated Agentic Optimization for Video World Models](https://arxiv.org/abs/2608.15043) | MEDIUM-LOW — Auditable inference-time adaptation of frozen video WMs: typed control state, evidence-gated updates, freeze-before-eval; +14.24 on Physics-IQ with honest attribution. | Small-Mid (8-24G): inference-time framework on Physics-IQ. |
| 14 | 2026-08-15 | [Evidence of Absence: Cross-Modal Abductive Risk Perception to Sustain World Models When Vision Fails](https://arxiv.org/abs/2608.14952) | MEDIUM-HIGH — Absence of expected visual co-evidence triggers abductive inference of hidden road users from acoustics; structured world-state survives vision failure; Neyman-Pearson cueing + identifiability analysis. | Small (8-12G): microphone-array front-end, real occluded-approach recordings. |
| 15 | 2026-08-14 | [Revisiting Energy-based Tabular Anomaly Detection: Energy and Reconstruction are Complementary](https://arxiv.org/abs/2608.14186) | LOW — BACKFILL. DBM mean-field energy revived (motivated by EBM/JEPA revival) complements AE reconstruction scores via rank fusion; EBM lineage data point, no world modeling. | Small (8-12G): 2-layer DBM on tabular benchmarks. |
| 16 | 2026-08-13 | [hint²: Hierarchical World Models for Inference-Time Temporal Logic Guidance](https://arxiv.org/abs/2608.13678) | MEDIUM-HIGH — BACKFILL. Two WM abstraction levels steer short-horizon policies toward LTL satisfaction: high-level proposition transitions guide LTL automaton progress, low-level dynamics give local safety; real UR5e validation. | Mid (24G): hierarchical WMs + CALVIN + real UR5e. |
| 17 | 2026-08-13 | [The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use](https://arxiv.org/abs/2608.12959) | HIGH — BACKFILL. LeWM reproduction shows the CEM squared-latent-distance objective (not the predictor) limits long-horizon planning; replacing only the cost lifts TwoRoom offset-100 goals 26%→98%; reachability ≠ proximity. | Small (8-12G): reproduction on ~$25 rented compute. |
| 18 | 2026-08-13 | [Your Probabilistic JEPA Is Secretly a Hidden Markov Model](https://arxiv.org/abs/2608.13621) | HIGH — BACKFILL. PIB-VJEPA exposes HMM structure (filtering encoder, Markov predictor, emission); MCJEPA's learned transition matrix gives exact multi-horizon Chapman-Kolmogorov consistency; state-space foundation for temporal JEPA. | Small (8-12G): theory + controlled synthetic experiments. |
| 19 | 2026-08-13 | [CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation](https://arxiv.org/abs/2608.12944) | MEDIUM — BACKFILL. ECG/PPG/PCG share one encoder; masked latent cardiac-state prediction + learned delay aligner; +8.2/+18.8/+15.5 AUROC over best SSL baseline across 25 tasks. | Mid (24G): shared transformer + delay aligner on multimodal cardiac data. |
| 20 | 2026-08-13 | [Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency](https://arxiv.org/abs/2608.12939) | HIGH — BACKFILL. Bisimulation-grounded ACPC diagnostic bounds perturbation-induced prediction/planner-cost divergence; Invariance Radius + Separation Rate screen JEPA WMs on visual control tasks. | Mid (24G): LeWM/PLDM on 4 visual control tasks. |
| 21 | 2026-08-12 | [Scaling Automatic Research Agents via World Models](https://arxiv.org/abs/2608.12564) | LOW-MEDIUM — BACKFILL. WMRL replaces sandbox execution with a learned world model for agent RL post-training (3-4× speedup) with debiasing/denoising; transfers to embodied VLA post-training. | Mid-Large (24-40G+): 4B/9B agent post-training. |
| 22 | 2026-08-12 | [Foresight Without Seeing: Latent Futures for World Action Models](https://arxiv.org/abs/2608.11605) | HIGH — BACKFILL. ForeWAM exposes predictive dynamics to the Action DiT via Future-KV from a single Video DiT prefill over stochastic future slots; no future video decoding at deployment; 96.7% LIBERO, 61.6% LIBERO-Plus. | Mid (24G): Video DiT prefill + Action DiT on LIBERO. |
|||||||||| 1 | 2026-08-14 | [Marionette: Predicting World States, Rendering Geometry, Painting Appearance](https://arxiv.org/abs/2608.14530) | HIGH — Explicit 276-dim 3D world-state prediction + zero-parameter graphics bridge (closed-form geometry/occlusion) + separate appearance diffusion; state-level repair cuts penetration 66% with zero observation-model changes. | Mid-Large (24-40G+): lightweight state dynamics + video-diffusion observation model (Alaya Lab). |
|||||||||| 2 | 2026-08-14 | [Traj-LeWM: Path-Aware World-Model Planning via Latent Trajectory Cost](https://arxiv.org/abs/2608.14125) | HIGH — Direct LeWorldModel extension: goal-conditioned latent trajectory cost complements endpoint ranking in training + planning; +3/+14/+7/+7 pp over LeWM. | Small-Mid (8-24G): Push-T, OGBench-Cube, Reacher, Two-Room. |
|||||||||| 3 | 2026-08-14 | [Ontology-Grounded World Models for Failure Diagnosis and Closed-Loop Repair in Physical AI Systems](https://arxiv.org/abs/2608.13901) | MEDIUM-HIGH — Symbolic ontology + verification-gated correction interface layered above EV-WM; typed failure predicates, route labels, predicate-gated acceptance; 94.05% LIBERO-Goal corrected-window. | Small-Mid (8-24G): symbolic layer + EV-WM backbone on PointMaze/LIBERO. |
|||||||||| 4 | 2026-08-14 | [Twin: Playing an Unknown Game with a Test-Time Digital Twin](https://arxiv.org/abs/2608.14490) | MEDIUM — Executable code world models gated by replay validation before acting; counterexample-driven repair; 97.8% of ARC-AGI-3 levels vs 7.8-61.1% direct agents. | Small (8-12G): program world models + frontier LLM API code synthesis. |
|||||||||| 5 | 2026-08-14 | [ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models](https://arxiv.org/abs/2608.14022) | LOW-MEDIUM — Generative counterpoint: 4-stage causal distillation of a bidirectional video generator into 1/2/4-step interactive WMs with aligned keyboard/mouse controls. | Large (40G+): video diffusion training/distillation (8 GPUs). |
|||||||||| 1 | 2026-08-13 | [A Unifying Perspective on Causal World Models: From Observations to Representations to Structure](https://arxiv.org/abs/2608.13456) | HIGH — Formal task-grounded definition of Causal WMs (entity properties + entity-entity + entity-environment interactions); unifies CRL, object-centric learning, causal discovery, SCMs; maps identifiability of each WM component. | N/A (position/theory paper). |
||||||||| 2 | 2026-08-13 | [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](https://arxiv.org/abs/2608.13438) | MEDIUM-HIGH — Latent world model rolls forward under policy's own actions to predict post-contact failure BEFORE contact; no pixel prediction; abort signal without policy modification. | Small-Mid (8-24G): Latent WM + lightweight failure probe on real robot trajectories. |
||||||||| 3 | 2026-08-13 | [BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving](https://arxiv.org/abs/2608.12854) | MEDIUM-HIGH — Two specialized action-oriented pathways (semantic VLA + predictive world modeling) coordinated at compact action-representation level; asynchronous rectified-flow inference; 89.5 PDMS NAVSIM v1 / 89.6 EPDMS v2. | Large (40G+): VLA + WAM pathways with video denoising. |
||||||||| 4 | 2026-08-13 | [S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation](https://arxiv.org/abs/2608.13103) | MEDIUM-HIGH — Learned sparse event evidence schedules event-level manager + Event Transition Model predicts variable-duration segment boundaries/durations/rewards; 98.7% PegTransfer (+22.7pp over DreamerV3). | Mid (24G): SurRoL simulation, PegTransfer task. |
||||||||| 5 | 2026-08-13 | [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552) | MEDIUM — 171 long-horizon interactive scenarios pursued by multimodal agent players; 4 core dimensions (geometry consistency, interaction fidelity, out-of-sight evolution, insight evolution); 9 SOTA video WMs found unreliable. | N/A (benchmark): 9 world models evaluated. |
||||||||| 6 | 2026-08-13 | [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](https://arxiv.org/abs/2608.13049) | MEDIUM — Cross-embodiment benchmark: human demos → robot manipulation videos; 5 dimensions incl. functional contact transfer + embodiment correctness; 11 models across 6 manipulation families, 2 embodiments. | N/A (benchmark): 11 video generation models evaluated. |
||||||||| 7 | 2026-08-13 | [Decoding Task Progress from VLA Representations](https://arxiv.org/abs/2608.13474) | MEDIUM — Task progress linearly readable from π0.5 residual stream; signal present in pretrained PaliGemma backbone before robot data; label-free OOD/stall detector competitive with SOTA. | Small-Mid (8-24G): Linear probes on frozen VLA checkpoints. |
||||||||| 8 | 2026-08-13 | [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) | LOW-MEDIUM — Video WM with per-arm SE(3) PRoPE-style geometric encoding + depth branch + SAM3 masks with frozen V-JEPA teacher for object consistency; top ranks on WorldArena 2.0 (T1 1st, T2 2nd). | Large (40G+): Video world model + few-step distillation. |
||||||||| 9 | 2026-08-13 | [Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology](https://arxiv.org/abs/2608.13518) | MEDIUM-LOW — Cross-domain world model: latent patient state evolved through time-ordered post-intervention events; training-only follow-up imaging supervision; AUROC 0.756 recurrence prediction on DECAAF-II. | Small-Mid (8-24G): DECAAF-II ablation cohort. |
||||||||| 10 | 2026-08-13 | [AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN](https://arxiv.org/abs/2608.12835) | MEDIUM — Structured current-map latent jointly supervised by reconstruction + future-trajectory prediction; causal attention propagates to future-map reasoning; cross-space planning consistency loss; SOTA OpenUAV/AerialVLN-S. | Mid (24G): UAV-VLN benchmarks. |
||||||||| 11 | 2026-08-13 | [Alaya-EVOKE: From Linear-Scaling Supervision to Endless World](https://arxiv.org/abs/2608.13546) | LOW-MEDIUM — Generative interactive world model counterpoint: external camera-indexed world-state bank + linear-scaling sparse-attention teacher distills a 3-step student; bounded denoiser context enables open-ended "endless" generation; SOTA WBench. | Large (40G+): Single H200, 2.11s per 1.5s chunk. |
||||||||| 12 | 2026-08-13 | [V-RAE: Rethinking Video Latent Spaces for Generation](https://arxiv.org/abs/2608.13556) | MEDIUM-LOW — Compact generative latents on frozen vision-foundation representations; reconstruction ≠ generative utility (tFVD diagnostic); improves future video prediction on Cityscapes — generative-side evidence for representation-space modeling. | Mid-Large (24-40G+): K600/UCF101 video generation; 6× faster convergence. |
||||||||| 13 | 2026-08-13 | [AlayaWorld: Interactive Long-Horizon World Modeling — Full Technical Report (v1.1)](https://arxiv.org/abs/2608.13492) | LOW-MEDIUM — BACKFILL. Generative interactive WM v1.1 conditioning redesign: streaming 3D point-cache renderer replaces depth-warping spatial memory; conditioning unified into the causal-VAE latent space with matched temporal statistics; camera AdaLN removed — viewpoint control folded entirely into re-rendered spatial condition; best overall Consistency 89.5 on WBench navigation split (158 cases). No latent predictive dynamics — generative counterpoint to JEPA. | Large (40G+): chunk-wise autoregressive generation (Alaya Lab). |
|||| 1 | 2026-08-06 | [PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models](https://arxiv.org/abs/2608.05720) | HIGH — Identifies three JEPA world model failure modes (physical invariance/identifiability/counterfactual collapse); three training pathways to fix them; MPC success 70→78.1% on OGBench-Cube, 81→98% on TwoRooms. | Mid (24G): Standard JEPA backbone + physics-aware training objectives. |
||| 2 | 2026-08-06 | [ω-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation](https://arxiv.org/abs/2608.06375) | HIGH — Latent predictive WAM for real-world humanoid whole-body control; avoids pixel reconstruction, uses compact future observation embeddings + diffusion action head; 40+ hr real-world dataset (ω-HOME). | Mid-Large (24-40G+): Multi-view encoder + latent predictor + diffusion action head. |
||| 3 | 2026-08-06 | [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374) | MEDIUM — Cross-embodiment VLA with future-prediction objective for shared dynamics priors; MoE action head for native-space control; no manual action realignment needed. | Large (40G+): VLM backbone + dynamics prediction + MoE action heads. |
|||| 4 | 2026-08-03 | [LeDXA: Self-supervised DXA representations encode multi-system disease risk, biological aging and heritability](https://arxiv.org/abs/2608.02208) | MEDIUM — LeCun co-author; JEPA-based SSL for medical imaging (DXA scans); learns latent health representations without pixel reconstruction; 150K× fewer training images than DINOv3, better disease prediction. | Small-Mid (8-24G): JEPA from scratch on 11,540 unlabeled scans; evaluated on 47,400 UKBB scans. |
|||| 5 | 2026-08-06 | [GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions](https://arxiv.org/abs/2608.06332) | LOW-MEDIUM — Interactive world model via visual actions (URDF-rendered robot overlays); autoregressive video prediction; decouples embodiment kinematics from environment dynamics; zero-shot OOD generalization. Counterpoint: uses pixel generation, not JEPA latent prediction. | Large (40G+): Pretrained video generative model + autoregressive prediction with robot kinematic control. |
||||| 1 | 2026-08-01 | [HP-JEPA: Hierarchical Partitioning for Multi-Resolution Graph Joint-Embedding Predictive Learning](https://arxiv.org/abs/2608.00491) | HIGH — LeCun co-author; hierarchical multi-resolution JEPA for graph SSL; coarse-to-fine partition bank with online/target encoder + predictor; 6/8 benchmark wins over Graph-JEPA. | Mid (24G): Graph classification/regression benchmarks, multi-resolution encoders. |
||| 2 | 2026-08-03 | [CoWAM: Coordination Contracts for Selective Policy Intervention with WAMs](https://arxiv.org/abs/2608.02578) | MEDIUM-HIGH — Selective WAM intervention via typed coordination contracts; preserves nominal policy unless alternative clears all gates; 9.6pp closed-loop improvement, <1% harmful interventions. | Mid (24G): 8 simulated bimanual manipulation tasks. |
|||| 3 | 2026-08-03 | [WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603) | MEDIUM — 4-level diagnostic benchmark (Visual Quality → World Reactivity); evaluates whether video-gen world models understand inherent dynamics vs. just appearance; 1,474 cases, 20 models evaluated; exposes capability split across camera/action/language paradigms. | N/A (benchmark): 20 representative models evaluated. |
|||| 4 | 2026-08-02 | [Asleep at the Wheel: JEPA's Limitations in Evaluating Novel Driving Data](https://arxiv.org/abs/2608.01336) | MEDIUM — Reveals JEPA-based novelty detection for driving fails on fair single-dataset benchmarks; success on cross-dataset protocols is domain-shift artifact, not genuine novelty recognition. | Small-Mid (8-24G): Frozen V-JEPA encoder + lightweight predictor head. |
|||| 5 | 2026-08-03 | [Faster-WAM: Do World Action Models Need Deep Action Modules?](https://arxiv.org/abs/2608.02365) | MEDIUM-HIGH — Dock of Transformer (DoT) design; docks single-layer action head onto 30-layer video backbone; 3.2× speedup over Fast-WAM with competitive performance. | Mid (24G): Pretrained video backbone + single-layer action head. |
|||| 6 | 2026-08-04 | [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](https://arxiv.org/abs/2608.03701) | HIGH — Compact latent reasoning space jointly shaped by future-state prediction + action generation; single 24GB GPU end-to-end training; 90.48% RoboTwin success. | Mid (24G): Single GPU training, lightweight encoder + latent reasoning. |
||||| 1 | 2026-07-31 | [WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2607.29613) | HIGH — LeJEPA-based world critic for VLA RL; joint latent prediction + value estimation; 149 tasks + 7 real-world. | Mid (24G): Lightweight LeJEPA + Pi0/Pi0.5/OpenVLA-OFT backbones. |
|||| 2 | 2026-07-31 | [AquaJEPA: Action-Conditioned Multimodal Predictive Representations for Underwater Robot Dynamics](https://arxiv.org/abs/2607.29393) | HIGH — JEPA for underwater robots; RGB+sonar+proprioception fusion; preregistered 120-env replication. | Small-Mid (8-24G): Stonefish simulator, 120 environments. |
|||| 3 | 2026-07-31 | [Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.29031) | HIGH — Action-oriented JEPA world model; predicts future driving intent instead of full dense world; 91.3 PDMS on NAVSIM v1; 2.97× intent change from agent occlusion. | Mid (24G): Frozen visual encoder + intent predictor + trajectory memory. |
|||| 4 | 2026-07-31 | [EEG-JEPA: Structured Latent Prediction for EEG Foundation Models](https://arxiv.org/abs/2608.00114) | MEDIUM — Cross-domain JEPA: structured latent prediction for EEG; Neurotopology-Aware Multi-scale Masking (N-MET); 50.42% frozen 14-task accuracy vs 40.49% waveform reconstruction. | Mid (24G): EEG foundation model pretraining. |
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
|||| 74 | 2026-08-05 | [DreamWAM: Beyond RGB Future Prediction for World Action Models](https://arxiv.org/abs/2608.04996) | HIGH — Beyond-RGB future prediction (motion+geometry+semantics); shared attention between VideoDiT and ActionDiT; 74.4% real-world (vs 55.6%); all aux branches disabled at inference. | Large (40G+): VideoDiT + ActionDiT with multi-modal supervision. |
|||| 75 | 2026-08-04 | [SJEPA: Learning Elegant Latent Dynamics with Hybrid Symbolic-Neural Predictors](https://arxiv.org/abs/2608.04060) | HIGH — Reconstruction-free JEPA with symbolic-neural hybrid transitions; formalizes induced-dynamics complexity; exposes representation-collapse shortcut from unconstrained compression. | Small (8-12G): Pendulum experiments; theoretical analysis. |
|||| 76 | 2026-08-02 | [FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels](https://arxiv.org/abs/2608.01049) | HIGH — Factorized JEPA world model decomposing futures into layout/entity/interaction channels; DENSEWORLD-115k dataset (22 Global South cities); visibility gate + separated subspaces. | Large (40G+): 2B/1B V-JEPA 2.1 backbones on 1,000 hrs video. |
|||| 77 | 2026-08-05 | [NodeJEPA: Structure-Conditioned Latent Prediction for Node-Level Graph SSL](https://arxiv.org/abs/2608.04381) | MEDIUM — JEPA extended to node-level graph tasks; structure-conditioned predictor with spectral/centrality cross-attention; EMA target encoder. | Small-Mid (8-24G): Node classification benchmarks. |
|||| 78 | 2026-08-03 | [ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching](https://arxiv.org/abs/2608.01926) | MEDIUM-HIGH — JEPA-style hyperbolic world model with goal-conditioned progress order; hyperbolic entailment learning + future discrimination; +9.67pp over LeWM. | Mid (24G): Four visual goal-reaching tasks. |
||||| 79 | 2026-08-05 | [Faster-WAM: Efficient Inference-Time Future Conditioning for Robust World Action Models](https://arxiv.org/abs/2608.04404) | MEDIUM-HIGH — SparseMoT replaces layer-wise fusion with selective video-action interaction; Interval KV-Fusion; 73.57% LIBERO-Plus (vs 49.14%); 2.21× faster than Joint-WAM. | Large (40G+): VideoDiT + action diffusion. |
||||| 80 | 2026-08-05 | [MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight](https://arxiv.org/abs/2608.04657) | MEDIUM — First WAM for mobile manipulation; Mixture-of-Transformers with locomotion/manipulation/shared expert routing; Chain-of-Foresight latent prediction; real ARX Lift2 deployment. | Large (40G+): Video diffusion backbone + action expert. |
||||| 81 | 2026-08-06 | [XEWorld: Can Action-Conditioned World Models Generalize to Unseen Robot Embodiments?](https://arxiv.org/abs/2608.05799) | HIGH — Cross-embodiment world model testbed; exposes that current models are 2D visual pattern matchers governed by visual similarity, not physical kinematics; zero-shot cross-embodiment requires pixel-space actions + spatial-temporal alignment. | Mid (24G): Controlled cross-embodiment evaluation framework. |
||||| 82 | 2026-08-06 | [GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models](https://arxiv.org/abs/2608.05948) | HIGH — Real-world-grounded diagnostic benchmark; 22 task families across rigid bodies/flexibles/textiles/deformables; finds video world models produce correct equation form but wrong physics parameters; directly validates LeCun's generative world model critique. | N/A (benchmark): 6 image-to-video models + 3 physics engines evaluated. |
||||| 83 | 2026-08-06 | [LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models](https://arxiv.org/abs/2608.05706) | MEDIUM-HIGH — Multi-view invariant latent action tokenization; geometric alignment to 3D foundation model; non-injective RGB-D reconstruction prevents future-frame appearance leakage; JEPA-aligned latent action pretraining principle. | Mid (24G): Two-stage human video pretraining + robot finetuning. |
|||||| 84 | 2026-08-06 | [MASS: Multiplayer World Models with Authoritative Shared State](https://arxiv.org/abs/2608.06257) | MEDIUM — Disentangles world dynamics (learned Logic Engine) from view rendering (learned Rendering Engine); authoritative typed state as sole recurrent memory; 1,024 concurrent players × 10,000 steps; disentanglement principle aligns with JEPA's state-vs-rendering separation. | Large (40G+): 1,024-player multi-agent simulation. |
|||||| 85 | 2026-08-06 | [TaskSense: Focusing on What Matters in World Models](https://arxiv.org/abs/2608.06544) | MEDIUM — Task-centric world model with differentiable stochastic spatial attention + inverse-dynamics objective; reconstructs ONLY attended regions (JEPA-aligned principle); outperforms DreamerV3 on Distracting Control Suite. | Mid (24G): DreamerV3 backbone + attention mechanism. |
|||||| 86 | 2026-08-07 | [PSG-JEPA: Is Forward Prediction Enough? Physical State Grounding for JEPA World Models](https://arxiv.org/abs/2608.06799) | HIGH — Direct JEPA extension: two complementary physical grounding objectives (proprioceptive state + multi-horizon joint-angle changes) beyond forward prediction; improves latent identifiability, planning, and real-robot policy learning with zero inference overhead. | Mid (24G): Standard JEPA backbone + grounding heads (training-only). |
|||||| 87 | 2026-08-07 | [Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection](https://arxiv.org/abs/2608.06706) | MEDIUM-HIGH — Borrows dueling decomposition from RL to isolate action-controllable latent channels; subtracts action-mean prediction to cancel distractor motion; zero auxiliary loss, works post hoc on frozen pretrained models; proven exact in finite samples. | Mid (24G): Works with any action-conditioned world model. |
|||||| 88 | 2026-08-07 | [PILOT: Decoupling Intention from Trajectory — A Representational Deduction Framework for World Action Models](https://arxiv.org/abs/2608.06994) | MEDIUM-HIGH — Decouples high-level physical condition evolution from low-level action trajectory in WAMs via motion chain-of-thought tokens; representational deduction bridges visual prediction and action generation; improves WAM success rate and physical interpretability. | Large (40G+): Mainstream WAM architectures + RD module. |
|||||| 89 | 2026-08-07 | [DPWM: Beyond Myopic World Models — Long-Horizon End-to-End Training for Direct Future Prediction](https://arxiv.org/abs/2608.07420) | MEDIUM-HIGH — Non-recursive Direct Prediction World Model; compresses arbitrary-length action sequences into a single embedding and predicts endpoint in one forward pass; avoids recursive rollout error amplification; objective (not architecture) drives long-horizon accuracy. | Mid (24G): Single-pass predictor, no recurrent unrolling. |
||||||| 90 | 2026-08-07 | [Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking](https://arxiv.org/abs/2608.07077) | MEDIUM — Shows Transformers DO develop linearly decodable emergent world models but FAIL to use them for planning; validates LeCun's claim that having a world model ≠ being able to use it. | Small (8-12G): Small Transformers trained from scratch on Hanoi traces. |
||||||| 91 | 2026-08-11 | [JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling](https://arxiv.org/abs/2608.09381) | HIGH — Directly integrates V-JEPA latent space with WAM; couples latent transition prediction and continuous action generation through shared predictor; avoids pixel reconstruction; first end-to-end JEPA-based WAM. | Mid (24G): Pretrained V-JEPA encoder + shared predictor. |
||||||| 92 | 2026-08-11 | [Energy-Structured Latent World Models with Neural Time Fields for Physically Consistent Open-World Motion Planning](https://arxiv.org/abs/2608.09876) | HIGH — Energy-structured latent WM with physical Hamiltonian formulation; neural time fields encode continuous-time dynamics; explicit physical knowledge reuse; EBMs meet world models. | Mid (24G): Energy-structured latent space + neural time fields. |
||||||| 93 | 2026-08-11 | [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771) | MEDIUM-HIGH — Compact 0.5B latent interaction model; self-supervised predictive latents for robot manipulation; avoids pixel reconstruction and heavy VLM backbones; action-grounded future prediction. | Small-Mid (8-24G): 0.5B parameters, compact enough for single GPU. |
||||||| 94 | 2026-08-11 | [4D-WAM: Infusing Spatiotemporal Awareness into World Action Models through Trajectory Fields](https://arxiv.org/abs/2608.08023) | MEDIUM-HIGH — Injects 3D trajectory field knowledge into WAMs via representation alignment; bridges 2D video representation and 3D action execution gap; model-agnostic training strategy. | Mid (24G): WAM backbone + 3D trajectory field alignment. |
||||||| 95 | 2026-08-11 | [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](https://arxiv.org/abs/2608.09516) | MEDIUM-HIGH — Agentic framework adding VLM-based Task Manager to WAMs; evidence-grounded scene graph for cross-stage memory; planning+verification+recovery on top of WAM prediction. | Large (40G+): WAM + VLM task manager + scene graph. |
||||||| 96 | 2026-08-11 | [CausalNav: Reliability-Certified Causal World Models for Control under Physical-Parameter Shift](https://arxiv.org/abs/2608.07809) | MEDIUM-HIGH — Causal world model with signed action-conditioned transition graph; deployment-time reliability certificate via policy-margin and argmax-agreement gates; safety-preserving fallback. | Small-Mid (8-24G): Causal graph inference + controller. |
||||||| 97 | 2026-08-11 | [WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation](https://arxiv.org/abs/2608.09298) | MEDIUM — Diagnostic benchmark testing ACWM simulator fidelity through observable capabilities (reproducibility, controllability, prefiguration); exposes gap between visual quality and physical simulator faithfulness. | N/A (benchmark): Multiple ACWM architectures evaluated. |
||||||| 98 | 2026-08-11 | [Rethink Before You Execute: Adaptive Execution for World Action Models (TempoWAM)](https://arxiv.org/abs/2608.09492) | MEDIUM — Adaptive execution horizon for WAMs via Recurrent Progress Monitor; replanning triggered by task progress, not fixed step count; plug-and-play for existing WAMs. | Mid (24G): Lightweight progress monitor + WAM backbone. |
||||||| 99 | 2026-08-11 | [GWM-VLA: Geometry-Aware Latent World Modeling for Vision-Language-Action Learning](https://arxiv.org/abs/2608.07619) | MEDIUM — Geometry-aware multi-view latent world model for VLA; global context-conditioned target-view prediction; improves VLA robustness under visual/environmental shifts. | Mid (24G): Multi-view geometry encoding + VLA backbone. |
||||||| 100 | 2026-08-11 | [SpikeWorld: Fast-State Adaptation for Frozen Spiking World Models](https://arxiv.org/abs/2608.07712) | MEDIUM — 1.45M-parameter sparse spiking world model; frozen pretrained weights + fast external adaptation states; neuromorphic approach to continual world model adaptation; JEPA-like separation of dynamics and semantics. | Small (8-12G): 1.45M spiking parameters. |
||||||| 101 | 2026-08-11 | [Twin Rollouts: Noise-Coupled Counterfactual Branching in Interactive Video World Models](https://arxiv.org/abs/2608.08982) | LOW-MEDIUM — Counterfactual generation in video world models via noise-coupled twin rollouts; critiques factual-only evaluation; uses pixel generation (not JEPA-aligned). | Mid (24G): Interactive video world models. |
|||||||| 102 | 2026-08-11 | [Vid2WAM: Distilling Video Diffusion Priors into World Action Models](https://arxiv.org/abs/2608.08558) | MEDIUM — Offline distillation transfers video diffusion priors into compact WAM student; reduces reliance on expert demonstrations; counterpoint: uses generative video priors rather than JEPA. | Mid (24G): Teacher video diffusion + student WAM. |
|||||||| 103 | 2026-08-11 | [Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning](https://arxiv.org/abs/2608.11204) | MEDIUM — Action-free surgical video pretraining → closed-loop control under fixed action-label budget; Cosmos Policy generative backbone (pixel prediction counterpoint); 63.5%→77.8% avg success, +20pp PegTransfer. | Large (40G+): Cosmos Policy video backbone + surgical fine-tuning. |
|||||||| 104 | 2026-08-11 | [Capturing Uncertainty in Human Motion for Representation Learning in Soccer](https://arxiv.org/abs/2608.11203) | LOW — Cross-domain predictive SSL: multimodal future-motion prediction objective with uncertainty conditioning; no planning/control; JEPA-philosophy data point (prediction as objective, not reconstruction). | Small-Mid (8-24G): Skeleton-based models on player tracking data. |
|||||||| 105 | 2026-08-11 | [VIScore: Diagnosing Planning-Relevant Quality in Latent World Models](https://arxiv.org/abs/2608.11174) | HIGH — Balestriero co-author; Veracity-Influence-Sobriety metric spans encoder+predictor+planner; shows SIGReg (JEPA-standard) doesn't transfer to planning while VISReg does; Spearman >0.75 with success rate, only metric calibrated across all scenarios. | Small-Mid (8-24G): Latent WM training + metric evaluation. |
|||||||| 106 | 2026-08-11 | [Flex-π: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860) | MEDIUM-HIGH — 6B WAM supervising RGB + 3D pointmaps + DINO semantics in one shared VAE latent (pointmaps encode losslessly in RGB VAE — "free lunch"); per-stream dropout → one checkpoint, any stream subset at inference; 2-7× over baselines on real bimanual tasks. | Large (40G+): 6B MoT backbone; inference faster than π0.5. |
|||||||| 107 | 2026-08-11 | [Toward the Cognitive–Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](https://arxiv.org/abs/2608.10618) | MEDIUM — Learns predictive world models from near-limit successes AND failures (real-vehicle data at 256.3 km/h); closed-loop world-state → future-aware reasoning → near-limit control refinement; 88.3% interaction success in full-scale simulated racing. | Mid-Large (24-40G+): Real-vehicle data + full-scale racing simulation. |
|||||||| 108 | 2026-08-11 | [Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving](https://arxiv.org/abs/2608.10386) | LOW-MEDIUM — Dreamer-family RSSM + latent-space off-policy SAC for driving; inverted-U rollout-horizon vs performance (model bias); n-step targets beat one-step TD; reconstruction-based counterpoint to JEPA. | Small-Mid (8-24G): DreamerV3-scale RSSM + SAC. |
|||||||| 109 | 2026-08-10 | [FACT: Failure-Aware Causal Training for World-Action Models](https://arxiv.org/abs/2608.10232) | MEDIUM-HIGH — Xiaolong Wang / Nicklas Hansen group; action-conditioned future-video + task-progress prediction lets failure rollouts supervise action consequences; kills success-biased future hallucination; optional action-candidate scoring at inference. | Mid-Large (24-40G+): Video prediction + progress predictor, sim + real bimanual. |
|||||||| 110 | 2026-08-12 | [StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization](https://arxiv.org/abs/2608.12314) | LOW-MEDIUM — Explicit persistent 3D world state (elements + cameras) as the core working representation; state construction/evolution/access replaces one-shot generation; philosophically aligned with the world-state critique of generative video, but no dynamics prediction or control. | Mid-Large (24-40G+): 3D world construction + off-the-shelf video enhancement. |
|||||||| 111 | 2026-08-12 | [Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models](https://arxiv.org/abs/2608.12078) | HIGH — Controlled OCWM study for visual MPC: planning success tracks slot quality (FG-ARI/mBO) until saturation; well-bound slots obviate proprioception + masking; under distribution shift OCWMs beat end-to-end LeWM, but DINO-WM stays competitive → pretrained features drive robustness. | Mid (24G): OCWM training comparable to LeWM. |
|||||||| 112 | 2026-08-12 | [Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL](https://arxiv.org/abs/2608.12063) | MEDIUM — Sample-based MPC as automated simulation expert generates massive offline datasets; off-policy RL with purely sparse rewards (no reward shaping); sim-to-real on arm-equipped Spot + G1 humanoid, surpassing the MPC teacher. | Mid-Large (24-40G+): Simulation-scale SMPC data + off-policy RL. |
|||||||| 113 | 2026-08-12 | [Predicting Functions, Not Features: KANs with Function-Space Joint-Embedding Predictive Learning for Medical Image Segmentation](https://arxiv.org/abs/2608.12050) | MEDIUM-HIGH — FS-JEPA: masked online branch predicts multi-radius signatures of KAN edge functions vs EMA full-context target; moves JEPA into pre-aggregation function space; +2.25pp Dice over strongest KAN competitor; predictive branch removed at inference. | Small-Mid (8-24G): KAN segmentation on 5 medical benchmarks. |
|||||||| 114 | 2026-08-12 | [How Can Driving World Models Do Counterfactual Prediction?](https://arxiv.org/abs/2608.11601) | HIGH — Formalizes the abduction-action-prediction gap: direct action-conditioned prediction ignores factual continuations, so it fails counterfactual matching on a new matched-counterfactual benchmark; a training-free evidence-injection pipeline substantially closes the gap. | Mid (24G): Controlled simulation benchmark + 2 representative driving WMs. |
|||||||| 115 | 2026-08-12 | [Keep the Future, Drop the Rollout: RIFT for World Action Models](https://arxiv.org/abs/2608.11521) | HIGH — Causal interventions show WAMs consume future K/V cache values but not the iterative rollout process; RIFT learns anticipation tokens that build the full future cache in ONE pass — 98.8% LIBERO with 68-89% latency cut; best RoboTwin 2.0 (92.9/92.6%). | Mid-Large (24-40G+): Trains on pretrained video WAMs (Joint, Cosmos-2). |
|||||||| 116 | 2026-08-11 | [JEPA-WAM: Stage-Level Joint-Embedding Prediction for World-Action Models in Robot Manipulation](https://arxiv.org/abs/2608.10780) | HIGH — BACKFILL (missed by Aug 12-13 scans). Stage-JEPA (goal-conditioned JEPA on frozen V-JEPA2) adds stage-level semantic future to a Motus WAM; 90.25% over 50 RoboTwin 2.0 tasks, 5.97% fewer execution steps. | Mid-Large (24-40G+): Motus WAM + V-JEPA2 + Stage-JEPA. |
|||||||| 117 | 2026-08-10 | [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730) | MEDIUM-HIGH — BACKFILL. World Adapter turns VLM features into world tokens conditioning a future-video denoiser (training-time world model) AND the action expert; world branch removed at deployment → VLA latency with world-model-shaped representations. | Mid (24G): 2B VLM + World Adapter + training-time denoiser. |
|||||||| 118 | 2026-08-10 | [VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction](https://arxiv.org/abs/2608.09448) | MEDIUM — BACKFILL. TTT for VLAs learns from future visual consequences; candidate updates isolated, evidence-gated, reversible; +3.2pp SimplerEnv WidowX over TTT baseline. | Small-Mid (8-24G): TTT on SimplerEnv + Google Robot. |




---

## [2026-08-17] CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?

- **arXiv**: [2608.16829](https://arxiv.org/abs/2608.16829)
- **Authors**: Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice, Sirish Srinivasan, Benjamin Graham, Jeffrey Hawke
- **TL;DR**: A benchmark that scores video world models' stochastic outputs in physically interpretable discrete outcome spaces (die faces, Galton-board bins, roulette colours) against known closed-form reference distributions, decomposing accuracy into scorability and calibration (total-variation distance).
- **Problem**: Existing WM benchmarks score individual generations or compare distributions coarsely over whole datasets, so the fine-grained aleatoric uncertainty of specific physical phenomena is never tested; a single accuracy metric conflates "produces a scoreable outcome" with "matches the true distribution."
- **Architecture**: N/A (benchmark). Curated outcome spaces with exact references (binomial Galton boards, Bernoulli forks, uniform dice/cards/lottery, skewed roulette); chi-squared calibration test (miscalibration-only evidence, N=32 per cell); scorability × calibration decomposition; mean normalized total variation (mnTV) metric. Applied to 9 scenes × 6 image-to-video models (WAN-2.7, SeeDance-2.0, HappyHorse-1.0, Veo 3.1, Runway Gen-4.5, Cosmos3-Super).
- **Compute Scale**: N/A (benchmark): 6 I2V models, 32 generations per cell.
- **LeCun Alignment**: HIGH — Direct empirical support for the core LeCun critique: generative video models do not learn the true stochastic structure of physics. Findings: models concentrate probability mass on few outcomes; most scene-model pairs significantly miscalibrated; Veo 3.1 collapses dice to a single outcome; no model dominates all nine scenes. Complements GAUGE (2608.05948) and WorldExam (2608.02603) in the vault's "generative WMs ≠ physical world models" evidence line, here testing *aleatoric calibration* rather than deterministic fidelity.
- **GitHub**: Not provided (protocol + mnTV metric released with paper).

## [2026-08-17] HarnessEval-W: Agentifying the Evaluation of Visual Worlds

- **arXiv**: [2608.16859](https://arxiv.org/abs/2608.16859)
- **Authors**: Weiliang Chen, Haowen Sun, Jun Gao, Jiawei Chi, et al. (large multi-institution collaboration incl. Ziwei Liu, Ming-Yu Liu)
- **TL;DR**: Brings the LLM "harness" evaluation paradigm to world models: an agentified pipeline decomposes each evaluation case into measurable subproblems, spawns tool-equipped sub-agents, and produces a verifiable evidence-tree reasoning chain justifying every score.
- **Problem**: Judging a WM rollout requires understanding whether physics, causality, and world state evolve correctly — humans spot violations naturally, but existing WM benchmarks compute brute-force metrics with no reasoning chain that can be examined or verified.
- **Architecture**: Hierarchical agent pipeline: parent agent interprets case context → decomposes the evaluation question → specialized sub-agents (each with tailored context and diagnostic tools) reason over subproblems → parent validates evidence and summarizes a verdict. Applied to 18 representative world models over 330 cases; judgments align with human preferences.
- **Compute Scale**: N/A (evaluation harness; runs as an agentic pipeline over frozen WMs).
- **LeCun Alignment**: MEDIUM — Evaluation infrastructure rather than architecture. Aligns with the vault's evaluation-theory line (VIScore 2608.11174, WorldExam 2608.02603) in demanding *reasoned, verifiable* judgments instead of scalar metrics — a prerequisite for honest measurement of progress toward autonomous intelligence.
- **GitHub**: Open-sourced as a live benchmark (link in paper; not in abstract).

## [2026-08-17] τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **arXiv**: [2608.16885](https://arxiv.org/abs/2608.16885)
- **Authors**: Xiaowei Cai, Yunuo Cai, Bingao Chen, et al. (40+ authors)
- **TL;DR**: A hierarchical VLA whose high-level subtask generator is a compute-scalable inference problem: using execution memory, it generates a subtask and, when needed, searches over alternatives before committing — allocating extra test-time computation to difficult or consequential decisions.
- **Problem**: Hierarchical VLA models make every high-level decision in a single forward pass, with no mechanism to spend more computation on hard choices; long-horizon manipulation requires both reliable individual skills and coherent sequencing.
- **Architecture**: High-level policy (world-model-guided: execution memory → subtask proposal → alternative search when needed) + low-level policy executing subtasks across embodiments. Trained on 40,115 hours of heterogeneous real-world data with multimodal co-training. Not a JEPA encoder/predictor/target stack — the "world model" is execution memory over agent history guiding deliberation.
- **Compute Scale**: Large (40G+): robot foundation model, 40K+ hours of real-world data.
- **LeCun Alignment**: MEDIUM — Implements one plank of LeCun's vision — deliberation as compute-scalable search over imagined alternatives at test time — but the search is over language-level subtasks guided by memory, not over latent world-state rollouts from a predictive model. Useful counterpoint: test-time compute for planning, minus a learned predictive world model.
- **GitHub**: Not provided.

## [2026-08-17] Orbit-Planner: Towards Latent World Models for On-Orbit Obstacle Avoidance of Satellite Agents

- **arXiv**: [2608.16651](https://arxiv.org/abs/2608.16651)
- **Authors**: Zhijian Li, Chao Ren, Peijin Wang, Xian Sun
- **TL;DR**: A two-stage latent world model for satellite agents: action-conditioned spacecraft dynamics are learned for future-state rollouts in latent space, and a Physics Probe decodes physical state changes from imagined latent trajectories; 91.7% closed-loop obstacle-avoidance success in Isaac Sim.
- **Problem**: On-orbit navigation needs collision-risk prediction from limited onboard observations; conventional planners rely on predefined maps and fixed environmental assumptions that break in dynamic scenarios.
- **Architecture**: (1) Latent world model: encoder → action-conditioned latent dynamics → long-horizon latent rollouts (no pixel prediction). (2) Physics Probe: training-time decoder mapping imagined latent trajectories to physical state changes (Δposition etc.), grounding the latent in physics without reconstruction loss at inference. Closed-loop navigation uses imagined rollouts for obstacle avoidance.
- **Compute Scale**: Small-Mid (8-24G): latent dynamics + probe, Isaac Sim evaluation.
- **LeCun Alignment**: MEDIUM-HIGH — Textbook JEPA-shaped world model: predict in latent space, decode only what matters for control (physical state changes) via a probe, plan from imagination. The Physics Probe is a lightweight instance of "grounding without reconstruction" (cf. PSG-JEPA 2608.06799). Domain (space robotics) is novel for the vault.
- **GitHub**: https://github.com/ZhijianLi2003/Orbit_Planner

## [2026-08-17] DriveCache: Action-Aware Caching for Driving World Model Inference

- **arXiv**: [2608.16354](https://arxiv.org/abs/2608.16354)
- **Authors**: Jianchun Yang, Jian Liang, Xianda Guo, Pinhan Fu, Yanlun Peng, Conglang Zhang, Wenke Huang, Mang Ye
- **TL;DR**: A training-free, action-aware cache controller for diffusion driving world models that uses planned ego motion (speed, trajectory) to allocate feature reuse across scenes and denoising steps, with a causal drift check that refreshes features when generation departs from calibration.
- **Problem**: Diffusion-based driving generators repeatedly evaluate large backbones over denoising steps, limiting throughput; existing cache methods omit driving signals available before generation (ego speed, planned trajectories).
- **Architecture**: Controller over an existing diffusion generator: cache-tolerance model conditioned on ego translation/rotation, denoising progress, and reuse length; dynamic programming allocates reuse under a response budget; causal drift check replans the schedule mid-generation.
- **Compute Scale**: N/A (training-free controller); underlying generators are Large (40G+).
- **LeCun Alignment**: LOW-MEDIUM — Generative counterpoint. Relevant only as deployment-side evidence that even the generative WM community is attacking inference cost; no latent predictive component, no planning utility demonstrated. Include for the efficiency line of the vault.
- **GitHub**: Not provided ("code will be publicly available").

## [2026-08-17] SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry

- **arXiv**: [2608.16287](https://arxiv.org/abs/2608.16287)
- **Authors**: Jiaming Hu, Yan Zheng, Tian Wang
- **TL;DR**: SCALE is a lightweight training-time regularizer that gives LeWM's end-to-end learned embeddings DINO-WM's favorable geometry — pairwise latent distances are correlated with distances in a standardized task-relevant state space — so high-variance state directions actually dominate the Euclidean costs planners consume.
- **Problem**: DINO-WM (pretrained features) and LeWM (SIGReg end-to-end) both encode decodable task state, but DINO-WM's leading principal components retain substantially more state information. Since Euclidean planning costs are dominated by high-variance directions, LeWM's state information doesn't shape candidate selection — the planner consumes the wrong geometry.
- **Architecture**: LeWM encoder unchanged + one regularizer correlating sampled pairwise latent distances with standardized task-relevant state distances (training-time only, zero planning overhead). Controls: a latent-to-state regression that matches SCALE's decodability but not its geometry yields inconsistent gains — proving geometry (not just information) is what matters.
- **Compute Scale**: Mid (24G): LeWM backbone on 5 tasks × 3 planning solvers × 5 compute budgets.
- **LeCun Alignment**: HIGH — Direct LeWorldModel lineage. The result sharpens the vault's planning-quality thesis (VIScore 2608.11174; "Objective Is the Bottleneck" 2608.12959): planning depends not only on whether task-relevant information is *present* in the latent, but on whether it *shapes the geometry the planner consumes*. Every task-solver average improves over LeWM.
- **GitHub**: Not provided.

## [2026-08-17] GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model

- **arXiv**: [2608.16234](https://arxiv.org/abs/2608.16234)
- **Authors**: Tianchen Deng, Xuefeng Chen, Shuang Wu, Qu Chen, Jiajun Zhu, Bo Dai, Jianfei Yang, Hesheng Wang
- **TL;DR**: A driving world model that distills Qwen/SigLIP foundation features into 3D Gaussian primitives to build an open-vocabulary Gaussian semantic field, unifying scene understanding, language-grounded reasoning, controllable 4D editing, and multi-modal generation in one framework.
- **Problem**: Driving WMs focus on conditional scene generation and lack explicit 3D scene understanding, language grounding, and controllable 4D editing; point-cloud/occupancy/BEV representations can't align text finely with 3D structure.
- **Architecture**: (1) Foundation-feature Gaussian tokenizer (visual-language features distilled into 3DGS primitives); (2) geometry-aware Gaussian adapter (importance-aware hierarchical selection + text-conditioned Perceiver cross-attention → compact world tokens); (3) KL-based Gaussian-image distribution alignment; (4) instruction-controllable editing (weather, vehicle manipulation). Generative — no latent predictive dynamics.
- **Compute Scale**: Large (40G+): foundation-feature Gaussian field + VLM distillation.
- **LeCun Alignment**: LOW-MEDIUM — Explicit, structured 3D representation is a step toward the state-vs-appearance separation, but dynamics remain generative and there is no planning loop. Include as the generative driving-WM counterpoint.
- **GitHub**: Not provided ("will release code and datasets").

## [2026-08-16] Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning

- **arXiv**: [2608.15869](https://arxiv.org/abs/2608.15869)
- **Authors**: Xiaoyu Zhu, Xinke Deng, Suresh Taddewadikar, Arnab Kumar Mondal, Zhongyu Jiang, Ian Fasel, Joerg Liebelt (Google)
- **TL;DR**: Shows MLLMs can learn to perform "visual chain-of-thought" reasoning internally in hidden states — internalized visual thinking — instead of generating intermediate reasoning images, retaining visual foresight benefits without the inference overhead of Visual CoT.
- **Problem**: Visual CoT gives MLLMs an intuitive mechanism for visual foresight in spatial/temporal/embodied environments, but generating intermediate reasoning images imposes substantial inference overhead, particularly for proactive video reasoning.
- **Architecture**: MLLM with internalized latent visual reasoning stages (no world-model encoder/predictor/target structure; video reasoning, not dynamics prediction).
- **Compute Scale**: Mid-Large (24-40G+): MLLM video reasoning.
- **LeCun Alignment**: MEDIUM-LOW — Evidence for a LeCun-adjacent thesis: reasoning should happen in compact latent/representation space, not in generated token/image space. No world dynamics, planning, or control — include as a representation-space-reasoning data point.
- **GitHub**: Not provided.

## [2026-08-16] Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats

- **arXiv**: [2608.15651](https://arxiv.org/abs/2608.15651)
- **Authors**: Bin Ren, Qi Ma, Yue Li, Zongyan Han, Yidi Li, Yuqian Fu, Rao Muhammad Anwer, Theo Gevers, Fahad Shahbaz Khan, Salman Khan
- **TL;DR**: First JEPA for 3D Gaussian splatting: predicts representations of held-out Gaussian token blocks from visible context using an online encoder with a shared EMA stop-gradient target encoder supplying multi-scale targets — no input-space decoder.
- **Problem**: Fixed-budget encoders see the same object through different primitive realizations; reconstruction-based SSL ties supervision to one sampled realization and requires an input-space decoder; latent prediction for Gaussian tokens needs targets accommodating coupled attributes and heterogeneous spatial support.
- **Architecture**: JEPA stack: online context encoder → predictor for held-out blocks; EMA target encoder provides stop-gradient multi-scale targets; complementary target projections + feature-space grounding replace Gaussian-attribute reconstruction. Evaluated under Gaussian resampling, partial observations, and renderable shape completion; transfers to part segmentation and object classification.
- **Compute Scale**: Small-Mid (8-24G): 3DGS encoder + EMA target; standard transfer benchmarks.
- **LeCun Alignment**: HIGH — Faithful JEPA extension to the 3D modality (complements Point-JEPA 2404.16432): predict latent structure, skip reconstruction. Evidence that JEPA's non-reconstruction objective generalizes to unstructured 3D primitive sets, with better resampling consistency and frozen-feature quality than matched reconstruction pretraining.
- **GitHub**: Project page: https://amazingren.github.io/Gaussian-JEPA/

## [2026-08-16] AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models

- **arXiv**: [2608.15456](https://arxiv.org/abs/2608.15456)
- **Authors**: Md Aminur Hossain, Omkumar Vaghasiya, Rajeev Ranjan Dwivedi, Vinod Kurmi, Biplab Banerjee
- **TL;DR**: A JEPA-inspired predictive alignment framework for remote sensing: predicts text embeddings from masked visual foundation-model tokens (instead of global contrastive alignment alone), training only a lightweight mask-aware multi-scale aligner on frozen AnySat + RemoteCLIP encoders.
- **Problem**: RS foundation models are weakly aligned with natural language, limiting natural-language archive search, retrieval, and question-conditioned analysis; global image-text contrastive alignment alone is insufficient.
- **Architecture**: Frozen AnySat visual encoder + RemoteCLIP text encoder; trainable predictive alignment network: mask-aware multi-scale aggregator (fine/regional/global) + cross-scale Transformer + learned query pooling → predicts text embeddings; combined semantic prediction + bidirectional contrastive retrieval objectives.
- **Compute Scale**: Small-Mid (8-24G): lightweight aligner on frozen encoders (BigEarthNet.txt, RSICD, RSVQA).
- **LeCun Alignment**: MEDIUM — JEPA-style masked prediction as the alignment mechanism (prediction target lives in representation space — text embeddings, not pixels), and parameter-efficient by construction. But text is a supervised anchor, and contrastive retrieval is retained — a hybrid that LeCun's purely self-supervised world model would treat as a separate, language-grounded module.
- **GitHub**: Not provided.

## [2026-08-15] Physiological World Models for Human State Transitions

- **arXiv**: [2608.15309](https://arxiv.org/abs/2608.15309)
- **Authors**: Chongyang Zhang, Rendong Wang, Hao Zheng, Hanwen Zhang, Yang Liu, Xiaolong Wei, Bin Chong
- **TL;DR**: A framework paper defining Physiological World Models: event-conditioned models of how whole-person physiological states change in response to events, behaviors, contexts, and interventions — with HumanState Transition Tokens, four capability levels, and six benchmark tasks.
- **Problem**: Health AI systems recognize current states, estimate risks, or analyze biomarkers, but do not model how physiological states *change* in response to real-world events and interventions.
- **Architecture**: Framework specification: HumanState Transition Token connects pre-event state + event/action + context + intervention → post-event trajectory + outcomes + data quality. Four capability levels (state representation → forecasting → individualized response prediction → bounded intervention planning); six benchmark tasks; explicit separation of prediction from causal inference with uncertainty/safety/governance made explicit.
- **Compute Scale**: N/A (framework paper — no trained model).
- **LeCun Alignment**: MEDIUM-LOW — Cross-domain adoption of the world-model program: event-conditioned state transitions, planning over interventions, and a hard separation of prediction from causal inference — all LeCun-shaped commitments. No JEPA-style architecture yet; include for the "world models as the organizing abstraction outside embodied AI" line.
- **GitHub**: Not provided.

## [2026-08-15] Low-Rank Dynamics-Effective Latent Carriers for Counterfactual Rollout in Learned World Models

- **arXiv**: [2608.15156](https://arxiv.org/abs/2608.15156)
- **Authors**: Yang Liu, Yuming Chen
- **TL;DR**: Shows a single rank-4 patch of a recurrent world model's 192-dim hidden state — learned from training-time factual-to-counterfactual differences — is sufficient to redirect a 12-step autonomous rollout, with preregistered replication across checkpoints and negative controls.
- **Problem**: World models predict the future without making clear which parts of the hidden state drive predictions; it is unknown whether a small, directly addressable hidden-state change can place the model on an intended counterfactual trajectory and sustain it autonomously.
- **Architecture**: Analysis over a recurrent WM (192-dim hidden state) in a controlled two-object 2D collision environment: low-rank carriers learned from factual→counterfactual hidden differences; a map from (factual state, requested velocity edit) → carrier coefficients; rank-4 anchor patch; position-edit stress test as negative contrast.
- **Compute Scale**: Small-Mid (8-24G): recurrent WM + controlled environment, preregistered replication rule.
- **LeCun Alignment**: HIGH — Intervention-level identifiability for world models: defines "dynamics-effective" as interventions that change future computation in a sustained, target-specific way, and demonstrates that successful *editing alone* is insufficient evidence (controls can pass raw rollout criteria). Directly relevant to counterfactual planning and to the vault's identifiability line (2607.22430, 2607.27017).
- **GitHub**: Not provided.

## [2026-08-15] SCOPE: Score-Isolated Agentic Optimization for Video World Models

- **arXiv**: [2608.15043](https://arxiv.org/abs/2608.15043)
- **Authors**: Yuhua Jiang, Jiaming Wang, Qingbin Liu, Feifei Gao
- **TL;DR**: A framework for auditable inference-time adaptation of frozen video world models: external controls live in a typed state, updates are bounded by development evidence, and the policy is frozen before held-out evaluation — +14.24 on Physics-IQ with attributable gains.
- **Problem**: Inference-time optimization of video WMs entangles prompts, samplers, verifiers, and selectors so gains can't be attributed and held-out feedback can leak into the deployed policy.
- **Architecture**: Framework (not an architecture): typed control state; evidence-bounded updates; freeze-before-eval discipline; ablations isolate gains from scene specification, sampling, and learned selection. Cross-backbone evaluation shows useful updates don't transfer uniformly — a principled update-selection mechanism is needed.
- **Compute Scale**: Small-Mid (8-24G): inference-time adaptation on Physics-IQ.
- **LeCun Alignment**: MEDIUM-LOW — Methodology paper about honest evaluation of WMs (the vault's recurring evaluation-rigor theme), but operates on generative video WMs; the "which updates deserve to be deployed" conclusion echoes the evidence-gating principles in the vault's verification-gated repair line (Onto-EV-WM 2608.13901, Twin 2608.14490).
- **GitHub**: https://github.com/YuhuaJiang2002/SCOPE

## [2026-08-15] Evidence of Absence: Cross-Modal Abductive Risk Perception to Sustain World Models When Vision Fails

- **arXiv**: [2608.14952](https://arxiv.org/abs/2608.14952)
- **Authors**: Cong Xu, Ravi Sankar
- **TL;DR**: Treats the *absence* of expected cross-modal co-evidence as evidence of a hidden cause: when an acoustic signature is present but visual co-evidence is absent, abductive inference posits a hidden road user and emits a calibrated risk advisory — sustaining a structured world-state when vision fails.
- **Problem**: Structured world-states presume observations to populate them; when the primary visual modality is occluded or degraded, those observations are missing and the world model loses the very content it exists to preserve.
- **Architecture**: Modality-agnostic abductive framework instantiated acoustically: microphone-array front-end (bearing, Doppler/looming approach-rate evidence) → event classification ("signature present, visual co-evidence absent") → abductive inference of hidden road user → Neyman-Pearson cueing under explicit false-alarm budget. Identifiability analysis separates shared vs modality-unique information.
- **Compute Scale**: Small (8-12G): real-time audio front-end; real occluded-approach recordings at blind junctions (warns 1.7s before line-of-sight entry, 42% fewer false alarms than baseline).
- **LeCun Alignment**: MEDIUM-HIGH — Robustness of the world-state under perception failure is a precondition LeCun's architecture assumes but rarely tests; this is the missing-perception complement to the vault's robustness-diagnostic line (ACPC 2608.12939, XEWorld 2608.05799). Abductive inference + calibrated (non-command) outputs also echo the cost/confidence separation in LeCun's modular design.
- **GitHub**: Not provided.

## [2026-08-14] Revisiting Energy-based Tabular Anomaly Detection: Energy and Reconstruction are Complementary

- **arXiv**: [2608.14186](https://arxiv.org/abs/2608.14186)
- **Authors**: Junichiro Niimi
- **TL;DR**: BACKFILL. Revives the Deep Boltzmann Machine for tabular anomaly detection, motivated by the EBM revival (Energy-Based Transformers, JEPA): DBM mean-field energy is complementary to reconstruction scores, and rank fusion of the two beats all baselines.
- **Problem**: Tabular anomaly detection relies on density proxies, reconstruction detectors, and non-parametric scorers; explicit energy-based models are largely absent despite the EBM revival in deep learning.
- **Architecture**: Two-hidden-layer DBM; mean-field energy score; rank fusion with an Autoencoder. Beats 7 of 8 baselines alone; fusion yields significant AUROC gains on both benchmarks where all non-DBM base models fail to improve the AE.
- **Compute Scale**: Small (8-12G): DBM on UCI Bank Marketing + NSL-KDD.
- **LeCun Alignment**: LOW — EBM-lineage data point (explicit energy functions as complements to reconstruction), but no world modeling, prediction, or control. Include only as evidence the EBM revival LeCun seeded is reaching applied domains.
- **GitHub**: Not provided.

## [2026-08-13] hint²: Hierarchical World Models for Inference-Time Temporal Logic Guidance

- **arXiv**: [2608.13678](https://arxiv.org/abs/2608.13678)
- **Authors**: Moritz Zoellner, Anastasios Manganaris, Ahmed H. Qureshi, Rohan Paleja
- **TL;DR**: BACKFILL. Guides short-horizon manipulation policies toward satisfying complex LTL specifications at inference time using two world models at different abstraction levels: a high-level model predicts action-induced transitions in atomic propositions to steer LTL automaton progress; a low-level dynamics model predicts immediate state evolution for local safety.
- **Problem**: Modern policies generate short-horizon action chunks and replan in closed loop, while LTL specifications are evaluated over long-horizon trajectories — a temporal-structure mismatch that language-conditioned policies handle poorly.
- **Architecture**: Hierarchical WM guidance: high-level proposition-transition predictor → LTL automaton progress objective; low-level dynamics predictor → local safety objective; both injected as inference-time steering. Outperforms LTL-guided diffusion methods and inference-time steering baselines on CALVIN; validated on a real UR5e.
- **Compute Scale**: Mid (24G): two WM levels + CALVIN + real UR5e.
- **LeCun Alignment**: MEDIUM-HIGH — Two-timescale world models for planning is exactly the hierarchical decomposition in LeCun's architecture (abstract proposition-level model + concrete dynamics-level model); here applied as a steerer over existing policies rather than as the planner itself. Safety constraints expressed in formal logic echo the cost-module separation.
- **GitHub**: Not provided.

## [2026-08-13] The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use

- **arXiv**: [2608.12959](https://arxiv.org/abs/2608.12959)
- **Authors**: Joyjeet Singh
- **TL;DR**: BACKFILL. Independent LeWorldModel reproduction on TwoRoom showing the binding constraint on long-horizon planning is the planner's *objective*, not the predictor: CEM minimizes squared latent distance, which saturates at ~80 arena units and *decreases* beyond 120 — moving away from the goal can lower the cost.
- **Problem**: Latent WMs are judged by prediction quality, so long-horizon planning failure is attributed to predictor degradation; but the predictor's imagined state 75 steps ahead is only 0.189 as wrong as a frozen world, while the planner never imagines beyond 25.
- **Architecture**: Analysis over LeWM: ridge probe recovers position at R²=0.9922 from the frozen embedding; the pathology is present in the authors' released weights; replacing only the objective (a head learned from frame separation that charges +24% to cross walls where squared latent distance charges −4%) lifts goals-at-offset-100 from 26.0% to 98.0% with nothing retrained and no GPU.
- **Compute Scale**: Small (8-12G): reproduction on ~$25 rented compute, laptop-CPU evaluation.
- **LeCun Alignment**: HIGH — The cleanest demonstration yet of the vault's central planning thesis (prediction accuracy ≠ planning adequacy; cf. 2607.10362, 2607.14169, VIScore 2608.11174): the cost must encode *reachability*, not proximity. Direct, falsifiable evidence about the flagship LeWM model's planner — with the fix costing a single head.
- **GitHub**: Not provided.

## [2026-08-13] Your Probabilistic JEPA Is Secretly a Hidden Markov Model: A State-Space Interpretation of Joint-Embedding Predictive Learning

- **arXiv**: [2608.13621](https://arxiv.org/abs/2608.13621)
- **Authors**: Yongchao Huang
- **TL;DR**: BACKFILL. Shows full time-indexed PIB-VJEPA has HMM computational structure — stochastic context encoder = amortized filtering distribution, probabilistic predictor = latent transition, decoder/inverse target encoder = emission — and introduces MCJEPA, whose learned transition matrix guarantees exact multi-horizon Chapman-Kolmogorov consistency.
- **Problem**: Temporal JEPA's relationship to classical state-space models was informal; a principled state-space interpretation was missing, leaving its predictive guarantees unclear.
- **Architecture**: Theory: four progressively stronger correspondence levels with sufficient conditions for exact sequence-level HMM equivalence; MCJEPA replaces the latent predictor with a learned transition matrix (matrix powers give exact multi-horizon consistency); conditioned discrete transitions, continuous Markov kernels, and continuous-time dynamics as extensions; deterministic temporal JEPA = degenerate Dirac-kernel case. Information-bottleneck view: compression ↔ minimality, residual predictability ↔ sufficiency.
- **Compute Scale**: Small (8-12G): theory + controlled synthetic experiments.
- **LeCun Alignment**: HIGH — Places temporal JEPA on a classical state-space foundation (HMM/Kalman lineage), connecting LeCun's world-model program to the filtering/transition/emission decomposition it intuitively mirrors. The exact multi-horizon consistency result gives temporal JEPA a property autoregressive pixel models lack by construction.
- **GitHub**: Not provided.

## [2026-08-13] CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation

- **arXiv**: [2608.12944](https://arxiv.org/abs/2608.12944)
- **Authors**: Hamza Shafiq, Hung Manh Pham, Bin Zhu, Pan Zhou, Jun Hu, Aaqib Saeed
- **TL;DR**: BACKFILL. A cardiac foundation model that learns a single shared representation across ECG, PPG, and PCG by predicting masked latent cardiac states, with a learned delay aligner handling the temporal offsets between electrical, mechanical, and hemodynamic events.
- **Problem**: Cardiac foundation models are single-modality, leaving shared physiology across sensors unexploited; cross-modal prediction must handle systematic temporal offsets between signal types, and synchronized multi-sensor recordings are scarce.
- **Architecture**: JEPA stack: heterogeneous waveforms → common token space → single shared Transformer encoder; masked latent cardiac-state prediction (target = shared physiology, not waveform appearance); learned delay aligner; staged pretraining (unimodal structure → paired latent-time alignment). Frozen evaluation across 25 tasks: +8.2 AUROC (PPG), +18.8 (PCG murmur), +15.5 (ECG) over the best SSL baseline.
- **Compute Scale**: Mid (24G): shared transformer + delay aligner, multimodal cardiac data.
- **LeCun Alignment**: MEDIUM — Cross-domain JEPA validation with a genuinely JEPA-relevant twist: predicting shared latent *physiology* rather than reconstructing sensor waveforms, and explicitly modeling cross-sensor latency — the multimodal-world-model alignment problem in miniature. The staged pretraining (unimodal first, paired alignment second) is a scalable recipe for scarce paired data.
- **GitHub**: Not provided.

## [2026-08-13] Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency

- **arXiv**: [2608.12939](https://arxiv.org/abs/2608.12939)
- **Authors**: Guo An, Zijing Wu, Honghua Dong, Yuhao Yan, Zixuan Gui, Haochong Chen, Shanzhao Ruan, Xiang Wang, Yurong Ling, Qi Tian
- **TL;DR**: BACKFILL. An ACPC diagnostic grounded in bisimulation: measures how far a clean history and a visually perturbed view of it diverge after being rolled forward under the same action sequence — proven to bound the perturbation-induced change in multi-step prediction error and planner cost.
- **Problem**: JEPA world models predict in latent space, but that provides no guarantee against visual perturbations: perturbed inputs can alter encodings and downstream action-conditioned predictions even while training loss improves.
- **Architecture**: Diagnostic (not an architecture): pairwise ACPC divergence; Invariance Radius (clean-perturbed rollout spread) and Separation Rate (distinguishability of different states after rollout) as complementary summary measures. Validated on LeWM and PLDM across four visual control tasks; the IR-SR screen transfers across tasks and stays informative under blur and resize.
- **Compute Scale**: Mid (24G): diagnostics on LeWM/PLDM, 4 visual control tasks.
- **LeCun Alignment**: HIGH — Formulates the correct invariance criterion for JEPA world models: what matters is not appearance-invariance but *action-consequence*-invariance (bisimulation). Gives the JEPA line a principled, transferable robustness screen — the representation-level complement to GAUGE-style behavioral benchmarks.
- **GitHub**: Not provided.

## [2026-08-12] Scaling Automatic Research Agents via World Models

- **arXiv**: [2608.12564](https://arxiv.org/abs/2608.12564)
- **Authors**: Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li, Huiyuan Chen, Haiyang Zhang, Chenlei Guo, Jingrui He, Zhenyu Liao
- **TL;DR**: BACKFILL. WMRL replaces sandbox environment execution with a learned world model for RL post-training of AutoResearch agents (3-4× speedup), adding Online Debiasing and Inverse-Variance Denoising to correct the world model's biased, noisy rewards — with convergence guarantees.
- **Problem**: Scaling RL for research agents hits a fundamental tension: agent generation scales via batching, but each environment execution occupies an exclusive sandbox and real machine time — execution dominates training cost as trajectories grow.
- **Architecture**: World Model RL: learned environment surrogate for training-time execution; debiasing + inverse-variance denoising of surrogate rewards; proven strict convergence improvement; 4B/9B agents beat 48B/120B open-weight agents; transfers to embodied VLA post-training.
- **Compute Scale**: Mid-Large (24-40G+): 4B/9B agent post-training.
- **LeCun Alignment**: LOW-MEDIUM — Uses "world model" in the surrogate-environment sense (train policies against a learned model of outcomes rather than the real world) — the same compute argument LeCun makes, but applied to LLM agent RL, with no latent predictive architecture or physical grounding. Useful as a scaling-economics data point.
- **GitHub**: Not provided.

## [2026-08-12] Foresight Without Seeing: Latent Futures for World Action Models

- **arXiv**: [2608.11605](https://arxiv.org/abs/2608.11605)
- **Authors**: Jiakai Huang, Zhongbo Wu, Zheng Zhang, Zihan Wang, Shan You, Tao Huang
- **TL;DR**: BACKFILL. ForeWAM is a dynamics-conditioned direct-policy WAM: a single Video DiT prefill over the current visual latent plus stochastic future slots produces Future-KV states reused throughout action denoising — the Action DiT sees predictive dynamics without any future video decoding.
- **Problem**: Explicit-future WAMs expose predicted scene evolution but pay iterative video-denoising cost; direct-policy WAMs are fast but lack an inference-time interface exposing predictive dynamics to the action pathway.
- **Architecture**: Video DiT prefill (current latent + stochastic future slots) → layer-wise Future-KV cache → reused across Action DiT denoising; dynamics registers supervised by a frozen latent action teacher capture interaction-induced transitions (object motion, contact, progress). Ground-truth futures + teacher are training-only; deployment generates no future video.
- **Compute Scale**: Mid (24G): 96.7% (standard) / 96.9% (accelerated) LIBERO, 61.6% LIBERO-Plus.
- **LeCun Alignment**: HIGH — The JEPA-WAM position executed inside the WAM paradigm: predictive dynamics exposed in *latent* form without pixel decoding (cf. JEPA-WAM 2608.09381, RIFT 2608.11521). Strong evidence the field is converging on latent futures as the efficient predictive interface for action generation.
- **GitHub**: Not provided.

---

## [2026-08-14] Marionette: Predicting World States, Rendering Geometry, Painting Appearance

- **arXiv**: [2608.14530](https://arxiv.org/abs/2608.14530)
- **Authors**: Zian Meng, Zhen Li, Chuanhao Li, Qiang Li, Kaipeng Zhang (Alaya Lab)
- **TL;DR**: An interactive game world model that decomposes simulation into three modules — an autoregressive dynamics model predicting an explicit, interpretable 276-dim 3D world state (multi-entity articulated skeletons, metric root trajectories, rotations), a zero-parameter graphics bridge computing world-space geometry and occlusion in closed form, and a control-conditioned video-diffusion model that only paints appearance on top — so long-horizon structure lives in the state and can be repaired there.
- **Problem**: Interactive game world models that autoregressively generate observations in pixel/latent space force structured properties (pose, geometry, occlusion) to be implicitly maintained by the same generative sequence; errors in these latent properties accumulate over long horizons, making consistency and controllability fragile (unconstrained rollouts drift to 21.2 m apart vs 5 m in recorded sessions; a third of frames show ground penetration).
- **Architecture**: Three-stage modular pipeline. (1) **State dynamics**: two-stage autoregressive model predicting a 276-dim explicit world state — multi-entity articulated skeletons, metric root trajectories, rotations. (2) **Graphics bridge**: fixed, zero-parameter renderer converts the predicted state into pose-control videos; geometry and occlusion are computed in closed form, never learned. (3) **Observation model**: control-conditioned video diffusion synthesizes photorealistic RGB from the structured controls. Not a JEPA encoder/predictor/target stack, but the state/dynamics/render decomposition is LeCun's modular recipe instantiated inside a generative system.
- **Compute Scale**: Mid-Large (24-40G+): lightweight state dynamics + video-diffusion observation model (Alaya Lab infrastructure).
- **LeCun Alignment**: HIGH — STRENGTHS: (1) Dynamics are predicted in an explicit, interpretable, low-dimensional state space rather than pixels — the core JEPA stance. (2) Geometry/occlusion are delegated to a zero-parameter renderer: exact computation replaces learned approximation, matching LeCun's argument that the world model should not burn capacity on rendering. (3) Controllability evidence: forcing a mismatched action stream shifts root-aligned joint error by 31% across 48 held-out segments — the state, not the appearance model, determines behavior. (4) Repairability evidence: two rules imposed on the explicit state (terrain collider, separation cap) cut ground penetration 66% and keep characters engaged with zero changes to the observation model; routing appearance through the predicted state costs almost no fidelity (FVD 831 vs 799). WEAKNESSES: (1) Appearance is still a diffusion generative model — no latent predictive objective, and no planning/control loop demonstrated. (2) The 276-dim state is hand-designed for articulated characters rather than learned. Overall: the strongest architectural statement in this batch — the generative world-model line converging on exactly the state-vs-renderer separation JEPA encodes through latent prediction.
- **GitHub**: https://github.com/AlayaLab/Marionette (project page: https://alayalab.github.io/Marionette/)

### What / Why / Solve

- **Proposal**: Marionette — predict an explicit world state, render geometry deterministically via a zero-parameter graphics bridge, and leave only appearance synthesis to the neural network.
- **Motivation**: Autoregressive pixel/latent generation entangles physics with appearance; the same generative sequence must implicitly maintain pose, geometry, and occlusion, and long-horizon errors in these latent properties accumulate uncontrollably.
- **Problem Solved**: Direct state controllability (31% joint-error shift under mismatched actions) and state-level long-horizon repair (66% penetration reduction) without touching the observation model, at negligible appearance fidelity cost.

### Academic Context

- **Inheritance / Response**: From Alaya Lab, the team behind AlayaWorld (2608.13492) and Alaya-EVOKE (2608.13546) — the generative interactive world-model line — now moving the state out of the denoiser entirely into an explicit predicted representation, a step past EVOKE's external world-state bank. Complements Robot-Factored World Models (2607.22535) and StateFlow (2608.12314) in the state-vs-rendering decomposition literature.
- **Implicit Connection**: Direct architectural instantiation of LeCun's modular agent: the world model predicts abstract state; a fixed renderer handles geometry; generation is confined to the appearance module. Also validates the GAUGE (2608.05948) finding that video WMs need explicit physical state to be trustworthy.
- **Research Line**: Structured Interactive World Models — explicit-state prediction with deterministic rendering.
- **Future Directions**: Learned (rather than hand-designed) state spaces; JEPA-style latent prediction replacing the diffusion appearance model; closing the loop with planning/control (the paper stops at simulation).
- **GitHub**: https://github.com/AlayaLab/Marionette

---

## [2026-08-14] Traj-LeWM: Path-Aware World-Model Planning via Latent Trajectory Cost

- **arXiv**: [2608.14125](https://arxiv.org/abs/2608.14125)
- **Authors**: Xiaodi Huang, Ziyi Ding, Jingtian Wan, Yuchen Liu, Yuan Zhang, Xiao-Ping Zhang, Jiayu Chen, Zhang Zhang, Tao Huang
- **TL;DR**: Extends LeWM with a goal-conditioned Latent Trajectory Cost (LTC) that aggregates trajectory-level information — as trajectory-preference supervision during training and as a path-aware complement to endpoint distance during planning — so candidates are ranked by the quality of the full predicted path, not just the predicted endpoint.
- **Problem**: LeWM learns only local next-step transitions without ever evaluating complete trajectories against the task goal, and ranks planning candidates solely by predicted endpoint distance. Since model predictions deviate from actual execution, the candidate with the closest predicted endpoint is often not the best when executed — endpoint ranking is both information-poor and prediction-error-fragile.
- **Architecture**: LeWM backbone retained (encoder → latent dynamics → endpoint scorer). Two additions: (1) **Goal-conditioned LTC head** over the shared latent representation; (2) **Dual supervision/ranking**: training adds LTC-based trajectory-preference supervision to the local next-step objective; planning combines LTC with endpoint distance for candidate ranking. Ablations verify the complementary roles of trajectory-level representation shaping and path-aware ranking.
- **Compute Scale**: Small-Mid (8-24G): lightweight visual world model on Push-T, OGBench-Cube, Reacher, Two-Room.
- **LeCun Alignment**: HIGH — Direct extension of LeWorldModel (2603.19312), the end-to-end JEPA-style latent world model line. STRENGTHS: (1) Fixes a planning-time flaw — endpoint-only scoring — with trajectory-aware latent costs: +3 pp Push-T, +14 pp OGBench-Cube, +7 pp Reacher, +7 pp Two-Room over LeWM. (2) Training-time trajectory-preference supervision is a mode-2 objective: the model learns to evaluate complete imagined futures, not just next states. (3) The finding that predicted-endpoint ranking misleads under prediction error adds empirical weight to the vault's recurring theme that prediction accuracy ≠ planning adequacy (complements TD-JEPA 2607.25337, "A Control Theory of Predictability" 2607.10362, and VIScore 2608.11174). WEAKNESSES: (1) Evaluation only on LeWM's lightweight benchmarks — no real-robot or long-horizon deployment. (2) LTC is a scalar cost; multi-modal trajectory distributions remain unaddressed. Overall: a practical, low-cost planning upgrade to the LeCun-lineage latent world model stack.
- **GitHub**: https://github.com/XiaodiHuang-code/Traj_LeWM

### What / Why / Solve

- **Proposal**: Traj-LeWM — goal-conditioned latent trajectory cost complementing LeWM's endpoint score in both training and planning.
- **Motivation**: Endpoint distance discards intermediate-path information and is unreliable under model prediction error; full predicted trajectories carry complementary signal about execution quality.
- **Problem Solved**: +3/+14/+7/+7 pp over LeWM across four benchmark tasks, with controlled ablations attributing gains to the combination of trajectory-level representation shaping and path-aware ranking.

### Academic Context

- **Inheritance / Response**: Directly builds on LeWM (LeWorldModel, 2603.19312); shares the "train the planner against trajectory-level information" agenda with TD-JEPA (2607.25337) and SAGE (2607.17973).
- **Implicit Connection**: Implements in the cost function what LeCun's architecture assigns to the cost module — evaluation of complete imagined trajectories against the goal — strengthening the mode-2 deliberation loop of latent world models.
- **Research Line**: Latent World Model Planning — trajectory-level cost shaping for JEPA-style models.
- **Future Directions**: Multi-modal trajectory costs; extension to hierarchical planning (LeWM hierarchical planning line, 2607.12547); real-robot validation.
- **GitHub**: https://github.com/XiaodiHuang-code/Traj_LeWM

---

## [2026-08-14] Ontology-Grounded World Models for Failure Diagnosis and Closed-Loop Repair in Physical AI Systems

- **arXiv**: [2608.13901](https://arxiv.org/abs/2608.13901)
- **Authors**: Kailin Wang, Haoxiang Jie, Yaoyuan Yan, Jiacheng Zhou, Zhiyou Heng
- **TL;DR**: A symbolic, ontology-grounded diagnosis and verification-gated correction interface layered above (not replacing) the EV-WM world model: task-local TBox predicates record unmet task conditions, routing labels point to correction mechanisms, and predicate-gated acceptance decides retries — turning raw world-model failure signals into typed, repairable records.
- **Problem**: EV-WM represents candidate quality with feature and event scores, but these scores do not record which task predicate failed, which correction route applies, or whether a post-correction attempt was accepted — so failure diagnosis is shallow and repair decisions are ad hoc.
- **Architecture**: Interface layer above EV-WM, not a replacement architecture. (1) **Task-local ontology TBox**: entity types, predicate signatures, constraints. (2) **Source-specific grounding**: maps predicted/simulator-observed states to task ABoxes. (3) **Deterministic rules**: retain each missing predicate and its arguments when assigning route labels. (4) **Verification-gated acceptance**: native task predicates decide acceptance; a bounded protocol decides whether a failed verification is retried. Learned/heuristic proposers remain separate from the symbolic interface.
- **Compute Scale**: Small-Mid (8-24G): symbolic layer is cheap; EV-WM backbone on PointMaze and LIBERO.
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) Implements in symbolic form the verifier/cost machinery that sits alongside the world model in LeCun's modular architecture: predicted states are checked against explicit predicates and routed to repair — a closed-loop diagnosis-repair cycle over world-model rollouts. (2) Results: 94% PointMaze (mean final-state distance 0.61 vs 0.91 for raw EV-WM), 94.05±0.30% LIBERO-Goal corrected-window success, 8,526/10,030 (85.0%) on the LIBERO-Plus registry, with separately budgeted search reaching 100% on PointMaze. (3) Deterministic, inspectable predicates give failure records semantics — a step toward the interpretable cost module LeCun wants. WEAKNESSES: (1) The ontology is hand-authored per task — manual transfer cost, not learned. (2) The ontology-only causal contribution is not isolated; real-robot recovery is not evaluated. Overall: a practical demonstration that explicit, verifiable failure semantics layered on a world model measurably improves closed-loop repair.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Onto-EV-WM — an ontology-grounded diagnosis and verification-gated correction interface layered above the EV-WM world model rather than a replacement architecture.
- **Motivation**: Feature/event scores fail silently about what went wrong; typed failure records (missing predicate + arguments + correction route) make diagnosis actionable and repair auditable.
- **Problem Solved**: Closed-loop failure diagnosis and repair over world-model rollouts, with corrected-window success of 94.05±0.30% on LIBERO-Goal and 85.0% across the 10,030-task LIBERO-Plus registry.

### Academic Context

- **Inheritance / Response**: Builds on EV-WM, a world-model-based planning system for manipulation; related to CoWAM (2608.02578) in selective-intervention contracts and to WorldSimProbe (2608.09298) in diagnosability concerns, but uses symbolic verification rather than learned probes.
- **Implicit Connection**: Predicate-gated acceptance over predicted states is a symbolic analogue of LeCun's cost module arbitrating between world-model proposals; the bounded retry protocol echoes the deliberation budget question in mode-2 planning.
- **Research Line**: Verified World Models — symbolic diagnosis and repair interfaces for world-model-based physical AI.
- **Future Directions**: Learned predicate grounding to reduce manual ontology authoring; isolation of the ontology's causal contribution; real-robot recovery experiments.
- **GitHub**: Not found

---

## [2026-08-14] Twin: Playing an Unknown Game with a Test-Time Digital Twin

- **arXiv**: [2608.14490](https://arxiv.org/abs/2608.14490)
- **Authors**: Alexy Skoutnev, Kirill Acharya, Gaston Longhitano, Madeleine Udell, Kevin Ellis, Iddo Drori (Cornell / Columbia)
- **TL;DR**: Test-time World-model Inference (Twin): a frontier coding agent writes an executable world model for each unknown ARC-AGI-3 game from simulation and interaction alone; the harness gates every action until the program reproduces all previously observed transitions in a twin replay, and every mismatch becomes a counterexample that repairs the world model.
- **Problem**: Unknown grid games hide their rules and goals; hand-engineered world models don't transfer across tasks, and direct-policy agents act without understanding the game's mechanics. Played directly, the base model scores 7.8%; a naive harness raises it to only 61.1%.
- **Architecture**: Code-as-world-model. (1) An inductive prior over grid games guides program synthesis. (2) **Replay validation**: an action is not made until the twin reproduces every previously observed game transition. (3) **Counterexample-driven repair**: each mismatch between world-model prediction and actual result becomes a counterexample used to patch the program. (4) Goal inference precedes any reward in 87.2% of cleared levels; remaining goals are found by search. Clears 179/183 levels (97.8%), more efficiently than humans on 88.3% of cleared levels.
- **Compute Scale**: Small (8-12G): world models are executable programs (negligible compute); a frontier LLM API performs code synthesis and repair.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) A sharp empirical statement of the mode-2 principle: act only after the world model passes consistency checks against reality — the twin raises the same base model from 61.1% (harness-only) to 93.3%. (2) Counterexample-driven repair is a concrete mechanism for keeping a world model honest, echoing LeCun's insistence that world models be judged by predictive consistency, not fluency. (3) Corroborates the vault's recurring finding that the world model is often the easier half: "Building a usable world model is simpler than anticipated, whereas the harder problem is inferring the right goal" — the cost-module problem. WEAKNESSES: (1) No learned latent predictive architecture — the world model is synthesized code over a narrow grid-game prior. (2) Discrete, deterministic domains only; unclear transfer to continuous, noisy physical dynamics. Overall: an LLM-native counterpoint demonstrating the value of explicit, verifiable world models for deliberation.
- **GitHub**: https://github.com/Alexyskoutnev/TWIN-ARC-AGI-3

### What / Why / Solve

- **Proposal**: Twin — an executable digital twin world model synthesized at test time, validated by replay, and repaired from counterexamples, gating a coding agent's actions.
- **Motivation**: In unknown environments, acting without a validated model of transitions is guessing; hand-engineered models don't scale across tasks.
- **Problem Solved**: 97.8% of 183 ARC-AGI-3 levels cleared vs 7.8% direct and 61.1% harness-only baselines, beating human first-time efficiency on 88.3% of cleared levels.

### Academic Context

- **Inheritance / Response**: Extends program-synthesis world modeling (Ellis line) into interactive test-time use; complements "When a Verified World Model Still Loses" (2607.14169) by showing verification-gated action pays off when the goal is inferred correctly.
- **Implicit Connection**: The replay-validation gate is a discrete analogue of JEPA's predictive-consistency criterion — the model earns the right to act by predicting correctly, not by generating plausibly.
- **Research Line**: Verified Programmatic World Models — code-level world models with counterexample-driven repair.
- **Future Directions**: Continuous and noisy domains; hybrid program + learned latent world models; using the twin for multi-step planning rather than single-action gating.
- **GitHub**: https://github.com/Alexyskoutnev/TWIN-ARC-AGI-3

---

## [2026-08-14] ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models

- **arXiv**: [2608.14022](https://arxiv.org/abs/2608.14022)
- **Authors**: Xinye Li, Lingshuai Lin, Lei Wang, Liuzhou Zhang, Jialin Cui, Qingshan Li, Guanchu Wang, Qingbin Liu, Xi Chen, Jiang Bian, Wai Lam
- **TL;DR**: A four-stage progressive recipe — domain adaptation, teacher-forced causal training, causal consistency distillation, and on-policy distribution matching against a bidirectional teacher — that converts an action-conditioned video generator into 1/2/4-step causal world models whose discrete keyboard states and continuous mouse motion stay aligned with temporally compressed latent chunks, plus replay-time refinement for the one-step draft.
- **Problem**: Causal distillation to one- or few-step synthesis breaks down for interactive world models: discrete keyboard states and continuous mouse motion must remain aligned with temporally compressed latent chunks during causal training and autoregressive rollout, and naive distillation destroys action alignment.
- **Architecture**: Bidirectional action-conditioned video generator as teacher → budget-specialized causal students at 1, 2, and 4 denoising steps; dual-path deployment combining latency-critical 1-step interaction with optional replay-time refinement (re-noising and refining the saved draft). Evaluated on paired Minecraft trajectories and transferred to gamepad-controlled FPS gameplay.
- **Compute Scale**: Large (40G+): video diffusion training/distillation (repo targets 8 GPUs).
- **LeCun Alignment**: LOW-MEDIUM — Generative counterpoint. STRENGTHS: (1) Best-in-class action alignment: leads evaluated systems on imaging quality, reference-aligned motion-profile agreement, action-sign accuracy, and mouse-control accuracy with the lowest reference LPIPS. (2) Replay-time refinement matches four-step reference quality while staying ~3× closer to the experienced trajectory than regeneration from noise — a deliberation budget over generation, distantly echoing mode-2. WEAKNESSES: (1) Pixel-space diffusion world model; no latent predictive dynamics, no planning. (2) The entire effort is spent making generative world models fast enough to be interactive — the efficiency gap JEPA-style latent prediction sidesteps by construction. Logged to track the generative frontier against which latent world models must compete on latency.
- **GitHub**: https://github.com/asdfo123/ForgeWM

### What / Why / Solve

- **Proposal**: ForgeWM — a progressive causal training pipeline producing few-step action-conditioned video world models with preserved action alignment and replay-time refinement.
- **Motivation**: Interactive world models need low-latency causal generation and reliable response to game-native controls; standard few-step distillation breaks the action conditioning.
- **Problem Solved**: 1/2/4-step interactive world models leading on action fidelity and imaging quality in Minecraft and FPS settings, with dual-path deployment for latency-critical interaction.

### Academic Context

- **Inheritance / Response**: Extends causal-distillation world models (AlayaWorld/Alaya-EVOKE line, 2608.13546) with a progressive on-policy recipe; the temporal-compression-aware action-alignment problem is the interactive counterpart of the conditioning-mismatch problem in AlayaWorld v1.1 (2608.13492).
- **Implicit Connection**: Generative world models keep paying a distillation tax to reach interactive latency — evidence for the latent-prediction argument that the world model should never have generated pixels in the first place.
- **Research Line**: Efficient Generative World Models — few-step causal distillation for interactive video.
- **Future Directions**: Latent-space (JEPA-style) action-conditioned dynamics to eliminate the distillation pipeline; longer-horizon rollout stability under the 1-step budget.
- **GitHub**: https://github.com/asdfo123/ForgeWM

---

## [2026-08-13] AlayaWorld: Interactive Long-Horizon World Modeling — Full Technical Report (v1.1)

- **arXiv**: [2608.13492](https://arxiv.org/abs/2608.13492)
- **Authors**: AlayaWorld Team, Alaya Lab — Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge, Yuanyang Yin, Jiaming Tan, Kang He, Liaoyuan Fan, Mingliang Zhai, Ruicong Liu, Xiaojie Xu, Xuangeng Chu, Zhen Li, Zhengyuan Lin, et al. (alphabetical by first name)
- **TL;DR**: A v1.1 technical report for the AlayaWorld interactive world model that keeps the chunk-wise autoregressive backbone and training data unchanged but redesigns the entire conditioning pipeline around one principle — conditioning signals must match the generated content in both latent representation and temporal structure — replacing depth-warped spatial memory with a streaming 3D point-cache renderer and unifying all visual conditioning into the causal-VAE latent space.
- **Problem**: In the previous AlayaWorld release, conditioning signals (image conditions, spatial memory, camera control) and the generated video latents were processed through different pathways and lived in different representations: visual conditions were encoded independently, temporal memory was misaligned with the VAE's causal structure, and camera trajectories were injected through a separate AdaLN branch. This mismatch degraded long-horizon coherence and viewpoint control in interactive generation.
- **Architecture**: (1) **Streaming 3D point-cache renderer** replaces the depth-warping-based spatial memory; re-rendered spatial memory is causally encoded as a continuous sequence, so the model receives a view-consistent 3D-geometry stream. (2) **Conditioning-to-content unification**: static-frame image conditioning replaced by motion-aware latent conditioning (nine-frame causal-VAE encoding pattern matched to the chunk-to-chunk handoff); temporal-memory window aligned in pixel space; hard memory dropout removes memory tokens rather than zeroing them; VAE encode/decode protocol unified across training and inference. (3) **Camera AdaLN branch removed** — viewpoint control now flows entirely through the re-rendered spatial condition. Backbone remains chunk-wise autoregressive generation.
- **Compute Scale**: Large (40G+): chunk-wise autoregressive video generation (same Alaya Lab infrastructure family as Alaya-EVOKE, which runs on a single H200).
- **LeCun Alignment**: LOW-MEDIUM — STRENGTHS: (1) The guiding principle — conditioning must match generated content in *latent representation* and temporal statistics — is a representation-space consistency argument echoing JEPA's prediction-in-latent-space stance, applied to the conditioning interface of a generative model. (2) The streaming 3D point cache is an explicit, persistent, declarative world-state representation driving viewpoint control — the same architectural separation (state vs. renderer) LeCun argues for, albeit as a geometry cache rather than a learned predictive state. (3) Removing the camera AdaLN shortcut forces the model to respect the rendered spatial state, i.e., control becomes state-conditioned. WEAKNESSES: (1) Core mechanism remains chunk-wise autoregressive generation in causal-VAE/pixel space — no latent predictive dynamics, no planning/control downstream. (2) The "world state" is a rendered cache of past observations, not a predicted future state; counterfactual and out-of-sight evolution are unsupported. Overall: generative-world-model counterpoint documenting that the generative line is converging on explicit spatial state and representation-matched conditioning — the same desiderata JEPA encodes through latent prediction.
- **GitHub**: https://github.com/AlayaLab/AlayaWorld (project page: https://alaya-lab.github.io/AlayaWorld/)

### What / Why / Solve

- **Proposal**: AlayaWorld v1.1 — a conditioning-and-memory redesign of the AlayaWorld interactive long-horizon world model: streaming 3D point-cache spatial memory plus latent-space-matched, temporally-aligned conditioning, with viewpoint control folded into the rendered spatial condition.
- **Motivation**: Conditioning signals that differ from generated content in latent representation or temporal structure inject distribution mismatch into every generation step, degrading long-horizon consistency and controllability.
- **Problem Solved**: Best overall Consistency score of 89.5 and a Video Quality average of 79.1 (best Imaging 67.7, Aesthetic 62.6) on the WBench navigation split (158 interactive navigation cases), with coherent long-horizon navigation under the interactive evaluation protocol.

### Academic Context

- **Inheritance / Response**: Self-revision of the AlayaWorld line; sibling to Alaya-EVOKE (2608.13546, which attacks the memory-vs-latency tradeoff via an external world-state bank and 3-step distillation). Where EVOKE moved state *out* of the denoiser, v1.1 moves conditioning *into* the generator's own latent/temporal statistics.
- **Implicit Connection**: The "conditioning must live in the same representation space as content" principle parallels the JEPA argument that prediction should happen in representation space, not pixel space — here applied to the input interface rather than the objective.
- **Research Line**: Generative Interactive World Models — persistent spatial state and conditioning alignment for long-horizon interactive simulation.
- **Future Directions**: Whether rendered point-cache state can support counterfactual viewpoints and physical interaction (the report flags physical interaction modeling as an open problem); whether representation-matched conditioning transfers to latent predictive architectures (JEPA-conditioned decoders).
- **GitHub**: https://github.com/AlayaLab/AlayaWorld

---

## [2026-08-13] Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

- **arXiv**: [2608.13546](https://arxiv.org/abs/2608.13546)
- **Authors**: Yuanyang Yin, Gongxuan Wang, Yifan Zhan, Chuanhao Li, Kaipeng Zhang, Feng Zhao (Alaya team)
- **TL;DR**: An interactive generative world model that externalizes persistent world state in a camera-indexed memory bank and redesigns the diffusion teacher's sparse attention for linear-scaling long-horizon supervision, distilling a three-step student that generates open-ended "endless" worlds with bounded denoiser context and no classifier-free guidance.
- **Problem**: Interactive world models face three conflicting demands — persistent memory over long sessions, responsive low-latency interaction, and long-horizon coherence. Keeping history in the denoiser context or KV cache grows cost unboundedly; few-step generation capability is bounded by its teacher; and long-horizon rollouts suffer content drift that stays locally plausible within short windows.
- **Architecture**: (1) **External world state bank**: scene geometry maintained in a camera-indexed external memory; only view-relevant information is retrieved into the denoiser context, keeping context bounded as sessions grow. (2) **Redesigned teacher** for long-horizon supervision: sparse attention combining chunk-wise grouping, retrieval of selected distant frames, and a linear-attention global state — linear growth in memory and compute over horizon. (3) **Distillation**: a 30-second distribution-matching objective under self-forced rollouts transfers long-horizon coherence to a three-step student without classifier-free guidance; per-chunk conditioning enables prompt changes and event control mid-sequence.
- **Compute Scale**: Large (40G+): single H200 at 384×640; each 1.5 s chunk generated in 2.11 s (near-realtime interactive rates).
- **LeCun Alignment**: LOW-MEDIUM — STRENGTHS: (1) The externalized, bounded-context world-state bank is an architectural admission that generative video models need an explicit persistent state — a step toward the world-state/prediction separation LeCun argues for, even if implemented as rendering memory rather than latent dynamics. (2) The anti-drift long-horizon supervision objective tackles the compounding-error problem that motivates latent prediction. (3) Open-ended interactivity is a requirement for world simulators used in agent training. WEAKNESSES: (1) Core mechanism remains chunk-wise generative denoising in pixel space — no latent predictive dynamics, no planning/control downstream. (2) The "world state" is a retrieval memory of past content, not a learned predictive state. Overall: strong generative-world-model counterpoint — evidence of what the diffusion line is converging on architecturally (external state, bounded context) while JEPA pursues the same properties via latent prediction.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Evoke: externalize persistent world state and redesign the teacher for linear-scaling, long-horizon interactive generation, distilling a 3-step student for open-ended world simulation.
- **Motivation**: Interactive world models must balance persistent memory, responsive interaction, and long-horizon generation; existing approaches trade session length against retained memory and are bounded by short-horizon teachers.
- **Problem Solved**: Bounded denoiser context with recurrent external memory supports open-ended, continuously evolving generation; SOTA on WBench, competitive on VBench-Long and VBench-2.0 as a three-step world model.

### Academic Context

- **Inheritance / Response**: Builds on the AlayaWorld interactive world-model line; responds to the fundamental memory-vs-latency tradeoff in diffusion world models by moving state out of the denoiser context.
- **Implicit Connection**: The explicit world-state bank + bounded-context design converges on the same architectural separation (state vs. rendering) that JEPA encodes in its latent predictor — but via retrieved geometry rather than predicted representations.
- **Research Line**: Generative Interactive World Models — architectural scaling of persistent state for long-horizon simulation.
- **Future Directions**: Whether retrieved-geometry world state supports counterfactual intervention and physical consistency as well as predictive latent state; integration with agent training loops (RL in the endless world).
- **GitHub**: Not found

---


## [2026-08-13] V-RAE: Rethinking Video Latent Spaces for Generation

- **arXiv**: [2608.13556](https://arxiv.org/abs/2608.13556)
- **Authors**: Minghui Guo, Shengqiong Wu, Hao Fei
- **TL;DR**: A video representation autoencoder that builds compact generative latents on top of frozen vision-foundation-model representations, showing that reconstruction-optimal latent spaces are not generation-optimal and that semantic latents support reconstruction, generation, and — notably — future video prediction better than conventional VAE tokenizer spaces.
- **Problem**: Video autoencoder latent spaces are optimized almost exclusively for pixel-level reconstruction, providing little high-level semantic organization; a reconstruction-optimal latent space need not be well suited to generative modeling, and reconstruction quality alone is insufficient to characterize generative utility.
- **Architecture**: (1) **Frozen vision foundation encoder** (four representative encoders evaluated) provides semantic features. (2) **Lightweight temporal pooling** module removes temporal redundancy while preserving semantic structure, producing compact generative latents. (3) **Video decoder** reconstructs continuous motion from the compressed features. (4) **tFVD**: a temporal-coherence diagnostic that correlates more reliably with downstream generation quality than reconstruction metrics. Also improves future video prediction on Cityscapes over the Wan 2.2 VAE latent space under matched prediction settings.
- **Compute Scale**: Mid-Large (24-40G+): video reconstruction/generation on K600 and UCF101; up to 6× faster convergence than reconstruction-tuned VAEs under matched generation settings.
- **LeCun Alignment**: MEDIUM-LOW — STRENGTHS: (1) "Representation first, reconstruction second" — building latents on frozen semantic encoders rather than optimizing for pixel reconstruction — is philosophically aligned with JEPA's prediction-in-representation-space principle, and the paper's predictive-modeling result (better future prediction on Cityscapes) is direct evidence for it. (2) The tFVD finding (reconstruction quality ≠ downstream utility) echoes the log's recurring evidence that pixel fidelity is a poor proxy for world-model quality. WEAKNESSES: (1) Primary application is video generation — the decoder still reconstructs pixels, and no planning/control is involved. (2) The frozen semantic encoder is not trained by prediction, so the latents are not dynamics-organized. Overall: a useful counterpoint/data-point showing that semantic latents (not reconstruction latents) are what predictive modeling wants — consistent with the JEPA critique of autoencoders.
- **GitHub**: https://v-rae.github.io/ (project page)

### What / Why / Solve

- **Proposal**: V-RAE — a video representation autoencoder that builds compact, semantically organized generative latents on frozen vision-foundation representations with a lightweight temporal pooling module.
- **Motivation**: Reconstruction-optimal video latent spaces are semantically disorganized and demonstrably suboptimal for generation and prediction; reconstruction metrics mislead model selection.
- **Problem Solved**: 2.13 rFVD on K600 (beating large-scale pretrained video VAEs), latents retaining substantially more semantic information, up to 6× faster convergence under matched generation settings, improved future prediction on Cityscapes, and a new tFVD diagnostic that correlates with generation quality.

### Academic Context

- **Inheritance / Response**: Responds to the video-tokenizer line (Wan 2.2 VAE, etc.) by moving representation selection upstream into frozen foundation models instead of co-optimizing latents with reconstruction.
- **Implicit Connection**: Strengthens the JEPA position that what matters is the representation space, not pixel reconstruction — here demonstrated from the generative side: even generators benefit from semantic (foundation-model) latents, and future prediction improves in them.
- **Research Line**: Video Representation Learning — generative-side evidence for representation-space modeling.
- **Future Directions**: Whether frozen semantic latents can be trained predictively (JEPA-style) rather than inherited from classification/alignment pretraining, closing the loop with latent prediction objectives for world models.
- **GitHub**: https://v-rae.github.io/ (project page)

---


## [2026-08-13] A Unifying Perspective on Causal World Models: From Observations to Representations to Structure

- **arXiv**: [2608.13456](https://arxiv.org/abs/2608.13456)
- **Authors**: Avinash Kori, Fabrizio Russo
- **TL;DR**: A position/theory paper that gives Causal World Models (CWMs) a formal, task-grounded definition — a useful WM must capture entity properties, entity-to-entity interactions, and entity-to-environment interactions that explain dynamics — and unifies world modeling with causal representation learning, object-centric learning, causal discovery, structural causal models, and model-based decision-making, while mapping the identifiability landscape for each WM component.
- **Problem**: "World model" is used loosely across communities with no shared formal account of what structure a WM must acquire to support prediction, planning, and acting beyond the training distribution. Generative capability alone is insufficient: a model can synthesize plausible video without possessing the causal structure needed for intervention reasoning.
- **Architecture**: Conceptual, across three abstraction levels: (1) **perceptual observations** → (2) **representations** (causal representation learning level) → (3) **structure** (SCM-level entity graph: entity properties + entity-entity + entity-environment interactions). Key moves: a CWM is defined by the tasks it supports (prediction, planning, counterfactual reasoning, informed decision-making), so which components must be identifiable is task-determined. The paper then connects each component to identifiability theory — clarifying when WM components can be recovered from data and up to which equivalence classes (permutation/scaling/affine vs. full isomorphism).
- **Compute Scale**: N/A (position/theory paper — no model trained).
- **LeCun Alignment**: HIGH — STRENGTHS: (1) This is the most direct formal articulation of the requirement at the core of the "Path Towards Autonomous Machine Intelligence" position: useful world models must go beyond generative capability and acquire abstract causal structure — entity-level properties and interactions that explain dynamics. (2) Explicitly ties WM adequacy to prediction + planning + OOD action, LeCun's own evaluative criteria. (3) Provides the formal language (identifiability classes) that recent JEPA identifiability work in this log (e.g., "On the Identifiability of Controlled World Models") can build on. WEAKNESSES: (1) No empirical instantiation of the CWM blueprint. (2) Does not prescribe the training objective (JEPA vs. reconstruction) — it specifies the target structure, leaving the how open. Overall: foundational reference point that can anchor evaluation of JEPA variants — what structure should the learned latent actually contain.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: A formal definition and multi-level framework for Causal World Models, grounded in the downstream tasks (prediction, planning, decision-making) they must support, with an explicit mapping of identifiability guarantees for each WM component.
- **Motivation**: World models are increasingly claimed as the foundation for intelligent agents, yet the term is used inconsistently and most treatments ignore causal structure — leading to models that generate but do not explain or intervene.
- **Problem Solved**: Provides a unifying conceptual framework connecting world modeling to causal representation learning, object-centric learning, causal discovery, SCMs, and model-based RL, and clarifies what can be recovered from data and under which equivalences.

### Academic Context

- **Inheritance / Response**: Synthesizes the causal representation learning literature (Schölkopf et al. line) and the world-model literature; responds to generative video models being labeled "world models" without causal grounding.
- **Implicit Connection**: Supplies the structural specification that JEPA's latent prediction objective is supposed to converge to — JEPA is a candidate mechanism for acquiring CWM-grade representations; this paper defines the bar.
- **Research Line**: Causal World Models / Identifiability — structure of representations that support planning and intervention.
- **Future Directions**: Empirically instantiating CWM objectives (e.g., JEPA variants whose latents provably recover entity-level structure); benchmark suites that test causal, not just predictive, adequacy of world models.
- **GitHub**: Not found

---


## [2026-08-13] ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models

- **arXiv**: [2608.13438](https://arxiv.org/abs/2608.13438)
- **Authors**: Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi
- **TL;DR**: A pre-contact execution monitor for chunked visuomotor policies: a latent world model trained on unlabeled robot trajectories predicts compact multi-view visual embeddings under the policy's own planned actions, and a lightweight failure probe aborts execution if the predicted post-contact latent signals likely failure — before the robot ever touches the object.
- **Problem**: Contact-rich manipulation failures are usually detected only after the robot has committed to contact. In wrist-camera setups, close views help observe contact, but by then a poor approach has already pushed, missed, slipped, or disturbed the object — conventional detectors react too late.
- **Architecture**: (1) **Latent world model**: trained from unlabelled robot trajectories to predict compact multi-view visual embeddings of future observations conditioned on planned actions — explicitly avoiding pixel-level video prediction (JEPA-style latent targets). (2) **Failure probe**: lightweight classifier trained on a small labeled set of pre-contact clips on top of the predicted latent. (3) **Deployment loop**: anchor prediction just before an imminent contact event, roll the world model forward under the policy's own action chunk, verify the predicted post-contact latent, and emit an abort signal if failure is likely — no modification to the underlying policy. Validated against direct and corrupted-action ablations, with live-robot transfer.
- **Compute Scale**: Small-Mid (8-24G): Latent WM + lightweight failure probe; runs alongside deployed visuomotor policies on real robots.
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) Action-conditioned latent predictive dynamics with no reconstruction is precisely the world-model form LeCun's architecture prescribes — the model predicts in representation space, not pixel space. (2) The WM is put to a concrete real-world control use (pre-contact abort), demonstrating that predictive latents, not pixels, are what execution monitoring needs. (3) Trained from unlabeled trajectories — SSL-friendly supervision story. WEAKNESSES: (1) Short-horizon monitoring only; no planning/MPC over the latent dynamics. (2) Binary failure classification, not general state prediction. Overall, a practical validation of latent world models as cheap, deployable dynamics simulators for real robots.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Pre-contact execution monitoring: roll a latent, action-conditioned world model forward under the policy's own planned actions and abort before contact when the predicted post-contact latent indicates failure.
- **Motivation**: Contact-rich failures happen at the approach phase, but observation close to contact means detection comes after damage is done; post-hoc detectors cannot prevent the disturbance.
- **Problem Solved**: Predicts failure before contact commitment, transfers to live robots without touching the policy, and outperforms direct and corrupted-action ablations across real contact-rich manipulation tasks.

### Academic Context

- **Inheritance / Response**: Builds on latent world models for robot learning (Dreamer/Latent Action Model lines) and execution monitoring; responds to the latency problem of post-contact failure detectors.
- **Implicit Connection**: Latent-prediction-without-reconstruction is the JEPA design principle; this paper shows that principle operating as a lightweight safety layer in deployment.
- **Research Line**: Latent World Models for Robot Execution Monitoring — predictive latents as runtime safety signals.
- **Future Directions**: Longer-horizon latent rollouts for full trajectory certification; JEPA-pretrained encoders to improve latent quality; multi-step abort policies (retry vs. re-plan).
- **GitHub**: Not found

---


## [2026-08-13] BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving

- **arXiv**: [2608.12854](https://arxiv.org/abs/2608.12854)
- **Authors**: Bing Zhan, Shuyao Shang, Jiahao Gu, Shuo Lu, Yuan Xu, Zhao Wang, Yida Wang, Xueyang Zhang, Kun Zhan, Lue Fan, Zhaoxiang Zhang
- **TL;DR**: A driving WAM that converts semantic reasoning (VLA-style VLM priors) and predictive world modeling into two specialized action-oriented pathways and coordinates them at the level of compact action representations — with asynchronous rectified-flow inference decoupling video and action denoising — reaching SOTA 89.5 PDMS on NAVSIM v1 and 89.6 EPDMS on NAVSIM v2.
- **Problem**: End-to-end driving models emphasize only one side of planning: VLAs exploit semantic priors, WAMs provide future-aware prediction. Naively fusing both through joint token-level attention fails — an attention-allocation mismatch lets semantic shortcuts dominate the shared attention space and suppress the predictive dynamics pathway.
- **Architecture**: (1) **Two specialized action-oriented pathways**: a semantic reasoning pathway (VLM priors) and a predictive world-modeling pathway (future video/world rollouts), kept functionally separate. (2) **Action-space coordination**: the two pathways are aligned at compact action representations — not at token level — mirroring neuroscience evidence that complex behavior arises from coordination among functionally specialized systems. (3) **Asynchronous rectified-flow inference**: decoupled video and action denoising shortens latency while preserving planning-relevant predictive context.
- **Compute Scale**: Large (40G+): VLA-scale backbone + world-modeling pathway with video denoising.
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) Implements the modular-agent decomposition of LeCun's AMI blueprint — separate semantic/world-model modules coordinated by a shared interface — instead of one monolithic net. (2) The central negative result (semantic shortcuts suppress predictive dynamics under naive fusion) is empirical evidence that the world-model module must be architecturally protected, supporting the case for dedicated predictive architectures. (3) Coordination at compact action representations echoes JEPA's compress-away-detail principle. WEAKNESSES: (1) The predictive pathway remains generative (rectified-flow video), not JEPA latent prediction. (2) No explicit latent planning — prediction feeds action denoising directly. Overall, strong driving-domain evidence for modular predictive architectures.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: BrainWAM: structure the driving planner as two specialized action-oriented pathways (semantic priors + predictive dynamics) coordinated in action space, with asynchronous rectified-flow inference for latency control.
- **Motivation**: Driving needs both semantic constraints and predictive dynamics, but existing end-to-end models pick one side; naive joint attention fails because semantic shortcuts dominate and suppress prediction.
- **Problem Solved**: Achieves state-of-the-art NAVSIM v1/v2 performance by protecting the predictive pathway from attention suppression, consistently outperforming VLA-only and WAM-only baselines.

### Academic Context

- **Inheritance / Response**: Builds on VLA driving models and generative driving WAMs; responds to the fusion failure modes of combined semantic+world-model planners.
- **Implicit Connection**: The "protect the world model module" result is a driving-domain instance of the architectural argument LeCun makes for separate world-model and cost/actor modules.
- **Research Line**: Modular World Action Models for Driving — coordination of semantic and predictive pathways.
- **Future Directions**: JEPA-style latent predictive pathway replacing video denoising; hierarchical planning over the coordinated action representations.
- **GitHub**: Not found

---


## [2026-08-13] S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation

- **arXiv**: [2608.13103](https://arxiv.org/abs/2608.13103)
- **Authors**: Shuzhe Zhang, Xin Zhu, Yinling Qian, Qiong Wang
- **TL;DR**: A hierarchical world model for long-horizon surgical manipulation that learns sparse event evidence from primitive latent trajectories to schedule an event-level manager, plus an Event Transition Model (ETM) predicting variable-duration segment boundaries, durations, and rewards — achieving 98.7% success on SurRoL PegTransfer, 22.7pp over a flat GAS DreamerV3 baseline.
- **Problem**: Long-horizon surgical tasks have sparse rewards and meaningful interaction changes at irregular intervals. Flat world-model agents imagine at primitive-step resolution, so variable-duration task progress stays implicit; manually specified stages have task-specific boundaries that misalign with state-dependent interaction transitions.
- **Architecture**: (1) **Primitive-step worker**: actor-critic learning at latent primitive resolution. (2) **Event-level manager**: sparse event evidence learned from primitive latent trajectories schedules manager goal updates; each selected latent goal conditions the worker's primitive actions until the next update. (3) **Event Transition Model (ETM)**: the learned event evidence forms variable-duration segments; ETM predicts the next boundary stochastic state, segment duration, and accumulated segment reward — chaining these event-level predictions extends imagination beyond the primitive horizon for manager learning.
- **Compute Scale**: Mid (24G): SurRoL surgical simulation, PegTransfer task; hierarchical training at DreamerV3-comparable scale.
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) Hierarchical latent planning with learned (not hand-specified) temporal abstraction is the multi-level predictive architecture of LeCun's AMI (H-JEPA: abstractions at multiple time scales). (2) Variable-duration event segments are a concrete instance of predicting "what will change and when" rather than every primitive step — the abstraction principle JEPA is built on. (3) Latent imagination for the worker with a separate coarse dynamics model. WEAKNESSES: (1) Dreamer-family RSSM lineage with reconstruction-flavored objectives, not JEPA. (2) Simulation-only evaluation. Overall, strong evidence that learned event-level abstraction substantially improves world-model planning in a high-stakes domain.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: S2-HWM: learn sparse event evidence from primitive latent trajectories to structure a two-level (event manager + primitive worker) world-model agent, with an Event Transition Model predicting variable-duration segment outcomes for extended imagination.
- **Motivation**: Long-horizon surgical manipulation has sparse rewards and irregular interaction changes; primitive-step imagination hides task structure, while hand-designed stages misalign with state-dependent transitions.
- **Problem Solved**: Achieves 98.7% PegTransfer success by scheduling manager updates on learned event boundaries and chaining event-level predictions beyond the primitive imagination horizon.

### Academic Context

- **Inheritance / Response**: Builds on hierarchical world models and DreamerV3-family agents for surgical robotics; responds to the fixed-resolution imagination limitation and manual stage engineering.
- **Implicit Connection**: Temporal abstraction with predictive event models is the H-JEPA vision at small scale — abstraction levels tied to dynamics structure, not fixed step counts.
- **Research Line**: Hierarchical Latent World Models — learned event-level temporal abstraction.
- **Future Directions**: JEPA-style event-level prediction without reconstruction; real surgical robot deployment; multi-task event vocabulary transfer.
- **GitHub**: Not found

---


## [2026-08-13] PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives

- **arXiv**: [2608.13552](https://arxiv.org/abs/2608.13552)
- **Authors**: Kaixin Ding, Xi Chen, Minghong Cai, Zhiyuan Xu, Yiyang Wang, Yuxiang Lu, Junyi Li, Shuyang Chen, Yuan Gao, Xin Tao, Pengfei Wan, Hengshuang Zhao
- **TL;DR**: A benchmark that evaluates video world models the way humans do — by having multimodal agent players pursue 171 specified long-horizon objectives through interaction — and finds that nine SOTA world models remain unreliable on spatial consistency and persistent state evolution.
- **Problem**: Fairly comparing interactive world models is hard: fixed action-conditioned evaluation is unsuitable because the action sequences needed to achieve the same objective vary per model, and human evaluation does not scale. Pixel-metric evaluation misses the long-horizon consistency properties that actually matter.
- **Architecture**: (1) **Agent players**: multimodal LLM agents interact with world models toward specified long-horizon objectives (e.g., turn 360° and check environment consistency; walk into water and check ripples). (2) **171 scenarios**, each with a specified objective. (3) **Four core evaluation dimensions**: geometry consistency, interaction fidelity, out-of-sight evolution, insight evolution — plus basic video quality and controllability metrics. (4) Nine SOTA world models evaluated; results show current models fail at maintaining spatial consistency and persistent state evolution over long horizons.
- **Compute Scale**: N/A (benchmark): evaluation harness over 9 world models.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) Evaluates exactly the properties LeCun argues generative video models lack — persistent world state, physical consistency, long-horizon coherence — and finds them missing, providing systematic empirical support for the generative-WM critique. (2) Goal-directed interactive evaluation (agent pursues objectives) matches the planning-based usage of world models, not passive viewing. WEAKNESSES: (1) Targets video world models; no JEPA/latent-predictive baselines. (2) Evaluation of appearance-level consistency, not latent-state or control utility. Overall, a useful tool for the "video generators ≠ world models" argument.
- **GitHub**: https://github.com/kxding/PlayWorld

### What / Why / Solve

- **Proposal**: PlayWorld: benchmark world models via multimodal agent players pursuing 171 long-horizon interactive objectives, scoring four consistency dimensions plus basic quality metrics.
- **Motivation**: Human-style evaluation of world models is goal-directed and interactive; fixed action-conditioned benchmarks cannot compare models fairly, and human evaluation does not scale.
- **Problem Solved**: Provides a scalable, objective-grounded evaluation protocol and demonstrates that current world models remain unreliable on long-horizon spatial consistency and persistent state evolution.

### Academic Context

- **Inheritance / Response**: Responds to the interactive world model evaluation gap left by fixed-sequence benchmarks; complements WorldSimProbe and GAUGE (both in this log) with goal-directed agentic probing.
- **Implicit Connection**: Persistent-state and out-of-sight evolution failures are precisely the failure modes LeCun predicts for generative video; this benchmark operationalizes those predictions into metrics.
- **Research Line**: World Model Evaluation — interactive, objective-driven benchmarks.
- **Future Directions**: Extending agent-player evaluation to latent/JEPA world models; reward-based scoring of task completion inside imagined rollouts.
- **GitHub**: https://github.com/kxding/PlayWorld

---


## [2026-08-13] H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models

- **arXiv**: [2608.13049](https://arxiv.org/abs/2608.13049)
- **Authors**: Dingyi Rong, Yue Shi, Chaofan Ma, Jiezhang Cao, Zongrui Wang, Zeyu Zhang, Yao Mu, Guangtao Zhai, Ning Liu
- **TL;DR**: A benchmark for cross-embodiment human-to-robot manipulation video generation: models must transform egocentric human demonstrations into robot manipulation videos under specified embodiments; eleven SOTA video models across six manipulation families are scored on goal completion, action events, functional contact transfer, embodiment correctness, and quality — and leading models still fail at embodiment consistency and functional interaction.
- **Problem**: Robot demonstration data is expensive and hard to scale, while egocentric human videos are abundant; video world models promise to convert human observations into robot-centric training resources, but their cross-embodiment transfer capability is entirely unevaluated.
- **Architecture**: (1) **Benchmark instances**: human demonstration video + target embodiment constraints + source-grounded annotations (task goals, action events, functional contacts, object responses). (2) **Five evaluation dimensions**: goal-state completion, action-event completion, functional contact transfer, embodiment correctness, general video quality. (3) Eleven SOTA video generation models evaluated across six manipulation families and two robot embodiments.
- **Compute Scale**: N/A (benchmark): 11 video generation models evaluated.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) Embodiment correctness and functional contact transfer probe physical faithfulness — whether generated video respects kinematics and contact physics — the exact property LeCun argues pixel-level generative models lack. (2) The negative result (pixel-plausible transfer ≠ task-executable transfer) echoes the "generative video is an inefficient path to world models" argument. WEAKNESSES: (1) Generative video framing throughout; no latent/JEPA transfer baselines. (2) Evaluates synthesis quality, not downstream policy utility of the generated data. Overall, a diagnostic resource for the cross-embodiment data-scaling hypothesis.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: H2R-Bench: a benchmark for evaluating whether video world models can translate egocentric human demonstrations into robot manipulation videos, scored across five dimensions including embodiment correctness and functional contact transfer.
- **Motivation**: Human videos are a cheap, abundant behavioral resource, but cross-embodiment transfer via world models is unexplored and unevaluated; without a benchmark, claims of transfer capability are unverifiable.
- **Problem Solved**: Provides a systematic diagnostic framework revealing that current video world models fail at embodiment consistency, functional interaction, and task execution in human-to-robot transfer.

### Academic Context

- **Inheritance / Response**: Builds on video world model evaluation literature; responds to the data-scaling bottleneck in robot learning by testing the cross-embodiment synthesis hypothesis.
- **Implicit Connection**: The contact/embodiment failure patterns corroborate the physical-fidelity critique that motivates latent predictive architectures over pixel generation.
- **Research Line**: Cross-Embodiment World Model Evaluation — human-to-robot transfer benchmarks.
- **Future Directions**: Latent-space cross-embodiment transfer (JEPA-style); closing the loop by training robot policies on H2R-generated data and measuring real task success.
- **GitHub**: Not found

---


## [2026-08-13] Decoding Task Progress from VLA Representations

- **arXiv**: [2608.13474](https://arxiv.org/abs/2608.13474)
- **Authors**: Atiksh Bhardwaj, Edward Weiyi Duan, Prithwish Dan, Wei-Chiu Ma, Preston Culbertson
- **TL;DR**: A mechanistic-interpretability study of π0.5 showing that task progress (normalized time remaining) is linearly readable from the residual stream — the signal exists in the pretrained PaliGemma backbone before any robot-specific training — and serves as a competitive label-free OOD/stall detector for deployed visuomotor policies.
- **Problem**: VLAs are moving toward deployment as general-purpose manipulation policies, but we lack basic tools for understanding what they represent internally or monitoring them at runtime — a safety and reliability gap.
- **Architecture**: (1) **Linear probes** on the π0.5 residual stream decode task progress. (2) **Key findings**: a single linear probe generalizes to unseen tasks; the signal is present in the pretrained PaliGemma backbone prior to robot training; trained on multi-prompt data, the probe varies under language counterfactuals; the signal is readable but does not enable meaningful steering. (3) **Application**: the probe as a label-free OOD detector that flags stalled task progress, competitive with SOTA methods.
- **Compute Scale**: Small-Mid (8-24G): Linear probing of frozen VLA checkpoints.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) Evidence that visuomotor policies form linearly-readable semantic state (task progress) — the kind of abstract state a world model should predict and a monitor should verify, supporting the JEPA-style claim that predictive objectives build task-relevant latent state. (2) Readability-without-steerability is a useful boundary result for thinking about what latent states are good for. WEAKNESSES: (1) Post-hoc probing of a generative VLA substrate; no predictive training objective involved. (2) Single-quantity decoding (progress), not full state estimation. Overall, a measurement tool that could later validate whether JEPA-trained encoders yield richer, more linear progress representations.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Use linear probes on VLA residual streams to decode task progress, and deploy the probe as a label-free runtime OOD/stall detector for visuomotor policies.
- **Motivation**: Deployed VLAs need internal-representation tooling and runtime monitoring; interpretability provides a lightweight, interpretable path without retraining the policy.
- **Problem Solved**: Shows task progress is linearly readable (even from the pretrained vision-language backbone), generalizes across unseen tasks, and detects stalled progress competitively with SOTA OOD methods.

### Academic Context

- **Inheritance / Response**: Applies mechanistic interpretability (linear probing literature) to robotics VLAs; responds to the deployment-monitoring gap in visuomotor policies.
- **Implicit Connection**: If task progress is a linear function of a VLA's latent state, world models that predict such states (JEPA-style) could supply monitoring signals without generative decoding — a convergence point between interpretability and predictive architectures.
- **Research Line**: VLA Interpretability & Monitoring — linearly readable semantic state in deployed policies.
- **Future Directions**: Probe JEPA-trained encoders for the same signals; use progress probes to gate world-model rollouts; investigate why steering fails despite readability.
- **GitHub**: Not found

---


## [2026-08-13] DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

- **arXiv**: [2608.13489](https://arxiv.org/abs/2608.13489)
- **Authors**: DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, Qingfeng Shi, Datao Tang, Jing Tang, Jun Wang, Pengfei Zhang
- **TL;DR**: An action-conditioned video world model for manipulation that injects per-arm SE(3) transformations into attention via PRoPE-style geometric encoding, adds a depth branch for scene geometry, and uses SAM3 masks with a frozen V-JEPA teacher for object consistency — distilled into a few-step student; ranked 1st (Track 1) and 2nd (Track 2) on the WorldArena 2.0 Challenge.
- **Problem**: Realism alone does not guarantee faithfulness in action-conditioned video prediction: a convincing rollout can still move the wrong arm or lose the manipulated object. Action control alone does not constrain scene geometry or the evolution of small manipulated objects.
- **Architecture**: (1) **Video world model** conditioned on observed frame + language instruction + prescribed action sequence (end-effector poses + gripper states). (2) **PRoPE-style geometric encoding** injects per-arm SE(3) transformations into attention, preserving arm identity and rigid-motion structure. (3) **Lightweight depth branch** for scene-level geometry. (4) **SAM3 masks + frozen V-JEPA teacher** maintain object consistency throughout grasping — a JEPA model supervising a generative one. (5) **Distribution-matching distillation** into a few-step student for deployment efficiency.
- **Compute Scale**: Large (40G+): Multi-step video generator training + few-step distillation.
- **LeCun Alignment**: LOW-MEDIUM — STRENGTHS: (1) The use of a frozen V-JEPA teacher for object-consistency supervision is a notable convergence of the generative and JEPA research lines — generative video borrowing representational quality from a JEPA model. (2) Geometric SE(3) grounding and depth explicitly target physical faithfulness, the known weakness of generative WMs. WEAKNESSES: (1) Primary method is pixel-space video prediction — the exact approach LeCun's position argues is inefficient and insufficient for planning. (2) No latent dynamics or planning; the model is a renderer, not a reasoner. Overall, a strong generative counterpoint whose JEPA-teacher component is worth tracking.
- **GitHub**: https://github.com/AMAP-ML/DreamX-Phi

### What / Why / Solve

- **Proposal**: DreamX-Phi 1.0: a geometrically-grounded action-conditioned video world model with SE(3) arm encoding, depth supervision, and V-JEPA-based object consistency, distilled to few steps for efficient deployment.
- **Motivation**: Action-conditioned video models for manipulation must be faithful, not just realistic — commanded paths must be respected, objects must persist, geometry must be honored.
- **Problem Solved**: Achieves top WorldArena 2.0 Challenge rankings by grounding generation in per-arm geometry, scene depth, and object-consistency supervision from a frozen V-JEPA teacher.

### Academic Context

- **Inheritance / Response**: Builds on action-conditioned video world models for robotics (WorldArena line); responds to the realism-vs-faithfulness gap with geometric and representational grounding.
- **Implicit Connection**: The V-JEPA teacher role is early evidence that JEPA representations are becoming standard infrastructure even inside generative pipelines — the representation quality JEPA produces is the value, regardless of decoder.
- **Research Line**: Action-Conditioned Video World Models — geometric grounding and object consistency.
- **Future Directions**: Full JEPA-based dynamics + rendering separation (predict in latent, render on demand); policy learning inside DreamX-Phi rollouts.
- **GitHub**: https://github.com/AMAP-ML/DreamX-Phi

---


## [2026-08-13] Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology

- **arXiv**: [2608.13518](https://arxiv.org/abs/2608.13518)
- **Authors**: Yunsung Chung, Yingshuo Liu, Abboud F. Hassan, Han Feng, Mary M. Maleckar, Nassir Marrouche, Jihun Hamm
- **TL;DR**: A clinical world model for post-operative forecasting in atrial fibrillation ablation: a structured latent patient state evolves through time-ordered post-intervention events (procedural context, medications, physiology), supervised only at training time by follow-up imaging via a latent forecasting objective — reaching AUROC 0.756 for recurrence prediction on DECAAF-II.
- **Problem**: Most clinical prediction models treat post-intervention outcome as a one-step mapping from baseline to endpoint, but recovery unfolds as an irregular trajectory: asynchronous clinical observations, medication changes, and repeat interventions change risk assessment over time.
- **Architecture**: (1) **Encoder**: baseline imaging → 3D spatial latent patient state. (2) **Dynamics**: state updated through time-ordered post-intervention events using procedural context, static covariates, elapsed time, and peri-event physiological embeddings. (3) **Supervision**: follow-up imaging provides training-only supervision through a latent forecasting objective — not needed at inference. (4) **Queries**: learned state supports recurrence-risk prediction at different horizons and retrospective input editing of blanking-period records; scar-extent MAE 2.971pp without follow-up MRI intensities at inference.
- **Compute Scale**: Small-Mid (8-24G): DECAAF-II atrial fibrillation ablation cohort.
- **LeCun Alignment**: MEDIUM-LOW — STRENGTHS: (1) A genuine world-model form outside robotics: intervention-conditioned latent state evolution with training-only forecasting supervision — the same reconstruction-free, predictive-target design principle as JEPA. (2) Supports counterfactual-style queries (retrospective editing of past records), the kind of intervention reasoning world models exist to enable. WEAKNESSES: (1) Forecasting/risk prediction framing — no action optimization or planning loop (no decision module). (2) Domain-specific clinical modeling rather than general-purpose representation learning. Overall, a cross-domain validation that the predictive-latent-state paradigm transfers to medicine.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: An intervention-aware clinical world model: latent patient state evolved through time-ordered post-intervention events, with follow-up imaging as training-only supervision via latent forecasting.
- **Motivation**: Post-procedure recovery is an irregular, evidence-accumulating trajectory; static baseline-to-endpoint models cannot update risk as new clinical events arrive.
- **Problem Solved**: Achieves AUROC 0.756 / AUPRC 0.777 for 90-day recurrence prediction and scar-extent MAE 2.971pp without follow-up imaging at inference, supporting multi-horizon risk queries.

### Academic Context

- **Inheritance / Response**: Builds on clinical prediction modeling and structured latent-state models; responds to the static one-step prediction limitation in post-operative cardiology.
- **Implicit Connection**: Intervention-conditioned latent dynamics with imaging-free inference mirrors the JEPA recipe (predict latent outcomes, drop the decoder); the world-model abstraction carries beyond embodied AI.
- **Research Line**: Cross-Domain World Models — clinical latent dynamics.
- **Future Directions**: Closed-loop treatment optimization (planning over the learned state); multi-center validation; joint modeling of multiple procedures.
- **GitHub**: Not found

---


## [2026-08-13] AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN

- **arXiv**: [2608.12835](https://arxiv.org/abs/2608.12835)
- **Authors**: Yutong Liu, Xiaojie Li, Mingzhu Xu, Jianlong Wu
- **TL;DR**: A UAV vision-language navigation framework that learns a structured current-map latent jointly supervised by map reconstruction and future-trajectory prediction, propagates it to future-map reasoning via structured causal attention, and aligns prediction with planning through a cross-space planning consistency loss — achieving strong results on OpenUAV and AerialVLN-S.
- **Problem**: UAV-VLN requires inferring spatial structure from sparse multi-view observations and executing feasible 3D motion, but existing methods map vision-language inputs directly to actions with limited explicit scene grounding and no future-aware spatial reasoning.
- **Architecture**: (1) **Structured current-map representation** learned from multi-view observations. (2) **Joint supervision**: current-map reconstruction + future-trajectory prediction — the latent must encode both present scene structure and future motion intent. (3) **Structured causal attention** propagates current spatial knowledge into future-map reasoning. (4) **Aggregation**: current + future representations predict the next 3D waypoint. (5) **Cross-space planning consistency loss**: directional agreement between the predicted map-space trajectory and the expert action direction from ground-truth waypoint displacement — tying imagination to navigation utility.
- **Compute Scale**: Mid (24G): OpenUAV and AerialVLN-S benchmarks.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) An explicit future-prediction objective over a structured spatial latent (the map) is a predictive world model in navigation form — the agent imagines the future map before acting. (2) The planning-consistency loss directly couples prediction quality to action utility, implementing the world-model-must-serve-planning principle. WEAKNESSES: (1) Representation is reconstruction-supervised (map reconstruction), not purely predictive. (2) Domain-specific UAV-VLN instantiation rather than a general world model architecture. Overall, a navigation-domain example of imagination conditioned on plans.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: AirForesight: learn a structured current-map latent supervised by reconstruction and future-trajectory prediction, propagate it to future-map reasoning, and align imagined trajectories with expert action directions via cross-space planning consistency.
- **Motivation**: Direct vision-language-to-action mapping in UAV navigation lacks explicit scene grounding and future-aware spatial reasoning, degrading performance in complex outdoor environments.
- **Problem Solved**: Improves UAV-VLN performance on OpenUAV and AerialVLN-S, with ablations confirming the contribution of future-map imagination and planning consistency.

### Academic Context

- **Inheritance / Response**: Builds on LLM-based UAV-VLN methods; responds to their weak spatial grounding by adding an explicit current-to-future map imagination module.
- **Implicit Connection**: "Imagine the future state, then act" over a compressed spatial latent is the JEPA-agent loop specialized to navigation; the consistency loss is a lightweight substitute for MPC over the imagined map.
- **Research Line**: Predictive Spatial Representations for Navigation — future-map imagination.
- **Future Directions**: Multi-step future-map rollouts (longer horizons); dropping reconstruction supervision in favor of pure predictive objectives; transfer to ground robots.
- **GitHub**: Not found

---


## [2026-08-12] StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization

- **arXiv**: [2608.12314](https://arxiv.org/abs/2608.12314)
- **Authors**: Yuyang Yin, Zixiang Li, Longxuan Deng, Hongkai Li, Shifang Zhao, Junnan Liu, Weirong Huang, Mengyu Wang, Tianxiao Fu, Yikai Wang, Peng-Shuai Wang, Xiaojie Jin, Yao Zhao, Yunchao Wei
- **TL;DR**: StateFlow — a state-centric previsualization framework arguing that the missing ingredient in generative video is an explicit, persistent 3D world state; it constructs, evolves, and accesses an editable 3D world (scene elements + camera configurations), using off-the-shelf video models only to enhance visual fidelity when needed.
- **Problem**: Prompt-to-video synthesis jointly controls scene, action, and camera factors through one-shot generation, giving weak controllability and no support for iterative editing. In reality, different frames are produced by local modifications of a shared, persistent world state — the explicit state itself is the missing component.
- **Architecture**: (1) **Persistent structured 3D state** of scene elements and camera configurations as the core working representation. (2) **State construction**: prior-guided, conflict-aware dual-view initialization lifts generated 2D content into a coherent 3D world. (3) **State evolution**: user intent is translated into structured state transitions while preserving world memory — no full-scene regeneration per edit. (4) **State access**: render-feedback reflection refines camera plans into visually feasible trajectories, avoiding reliance on VLM semantics alone. (5) Off-the-shelf video models enhance quality only where higher fidelity is desired.
- **Compute Scale**: Mid-Large (24-40G+): 3D world construction pipeline + off-the-shelf video enhancement models.
- **LeCun Alignment**: LOW-MEDIUM — STRENGTHS: (1) The central argument — explicit persistent world state beats one-shot generation — is philosophically the same critique LeCun levels at generative video: a world is a state you modify, not a video you resample. (2) Factorized state (elements + cameras + transitions) superficially resembles a structured world model. WEAKNESSES: (1) No dynamics prediction, no planning, no control — the world state is edited by the user, not predicted by a model. (2) Creative-domain application (film/games/architecture). Overall, a counterpoint from the generative side that independently reaches the "explicit world state" conclusion; conceptually adjacent to world models but without predictive dynamics.
- **GitHub**: Project page: https://yuyangyin.github.io/StateFlow

### What / Why / Solve

- **Proposal**: A state-centric framework for generative previsualization: an explicit, editable 3D world state (scene structure, evolution, cameras) is the primary working representation, with video models as optional quality enhancers.
- **Motivation**: One-shot video synthesis conflates all scene/action/camera factors and cannot support iterative refinement; a persistent state that is locally modified and re-rendered matches how real production workflows operate.
- **Problem Solved**: Enables iterative editing and recombination of a shared world state, producing high-quality 3D worlds for video creation and game-like prototyping without full-scene regeneration.

### Academic Context

- **Inheritance / Response**: Responds to prompt-driven one-shot video generation methods; independently reaches the "persistent world state" position that world-model researchers argue for in embodied AI.
- **Implicit Connection**: Mirrors the JEPA critique of generative approaches (don't resample the world, model its state) in a creative domain — evidence that the explicit-state argument generalizes beyond robotics.
- **Research Line**: State-Centric Generative Frameworks — explicit world state as the interface for creation and editing.
- **Future Directions**: Predictive state transitions (learned dynamics over the 3D state); cross-domain transfer of the explicit-state interface to embodied world models.
- **GitHub**: Project page: https://yuyangyin.github.io/StateFlow

---


## [2026-08-12] Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models

- **arXiv**: [2608.12078](https://arxiv.org/abs/2608.12078)
- **Authors**: Shukrullo Nazirjonov, Sai Prasanna, Anna Manasyan, Georg Martius
- **TL;DR**: A controlled study of object-centric world models (OCWMs) for visual MPC: planning success tracks unsupervised slot-quality metrics (FG-ARI, mBO) until saturation; well-bound slots make proprioception and masking inductive biases unnecessary; under distribution shift, well-bound OCWMs beat end-to-end scene-centric LeWM — but DINO-WM stays competitive, pointing to pretrained features as the true robustness source.
- **Problem**: Prior OCWMs take the slot encoder as given and evaluate only in-distribution, leaving open whether the object-centric bias actually delivers for planning, and which component of the OCWM drives any benefit.
- **Architecture**: (1) **Controlled study axes**: object-centric representation quality and generalization under distribution shift, relative to scene-centric models. (2) **Finding (i)**: planning success correlates positively with unsupervised slot-quality metrics, saturating at high slot quality. (3) **Finding (ii)**: with well-bound slots, the auxiliary proprioception inputs and masking inductive bias that prior methods relied on become unnecessary. (4) **Finding (iii)**: under unseen distribution shifts, the well-bound OCWM is more robust than end-to-end trained scene-centric LeWM, while DINO-WM (frozen pretrained features) remains competitive — attributing robustness largely to pretrained features.
- **Compute Scale**: Mid (24G): OCWM training at LeWM-comparable scale; no massive pretraining of its own.
- **LeCun Alignment**: HIGH — STRENGTHS: (1) Directly interrogates the representation-inductive-bias question at the heart of JEPA — what structure should the encoder impose for the latent to support planning? (2) Evaluates under distribution shift, the regime world models must actually serve in deployment. (3) The honest negative result about pretrained features is a caution against over-crediting object-centric binding — directly relevant to JEPA design choices. (4) Martius group (MPI-IS), a core world-model community. WEAKNESSES: (1) Slot encoders remain reconstruction-driven, not JEPA-trained. (2) No real-robot transfer. Overall, a rigorous ablation clarifying when and why structured encoders help planning — evidence LeCun's program can use to argue for structured latent prediction over scene-centric pixel modeling.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: A controlled evaluation of OCWMs along representation quality and distribution-shift robustness, isolating what within an OCWM actually delivers planning benefit.
- **Motivation**: The object-centric inductive bias is widely claimed to improve sample efficiency and generalization, but no prior work tested the claim beyond in-distribution evaluation.
- **Problem Solved**: Establishes that slot quality causally improves planning success (with saturation), that good slots replace auxiliary inductive biases, and that pretrained features — not object binding per se — are a key robustness contributor.

### Academic Context

- **Inheritance / Response**: Builds on the object-centric world model line (slot-based OCWMs) and responds to LeWM/DINO-WM comparisons; corrects over-claims about object-centric inductive biases.
- **Implicit Connection**: The encoder-structure question is central to LeCun's vision (what representation is most useful for prediction and planning); this paper provides controlled evidence on the object-centric candidate.
- **Research Line**: Object-Centric World Models — representation quality and robustness under distribution shift.
- **Future Directions**: JEPA-trained slot encoders (reconstruction-free object binding); evaluation of OCWMs in MPC with hierarchical planners.
- **GitHub**: Not found

---


## [2026-08-12] Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL

- **arXiv**: [2608.12063](https://arxiv.org/abs/2608.12063)
- **Authors**: Martin Schuck, Maks Sorokin, Simone Manni, Duy Ta, Angela P. Schoellig, Marco Hutter, Simon Le Cleac'H, Jan Brüdigam
- **TL;DR**: Uses Sample-based Model Predictive Control (SMPC) entirely in simulation as an automated, rapidly tunable expert to generate massive offline datasets; an off-policy RL agent is then trained with purely sparse task rewards — eliminating dense reward shaping — and deployed sim-to-real on an arm-equipped Spot quadruped and a G1 humanoid, surpassing the MPC teacher.
- **Problem**: Scaling RL to loco-manipulation is bottlenecked by the slow, manual process of dense reward shaping; model-based expertise exists (SMPC) but had not been exploited as an automated dataset generator for sparse-reward RL.
- **Architecture**: (1) **SMPC expert in simulation** generates massive offline datasets — solving the fundamental exploration problem with optimal-control data. (2) **Off-policy RL agent** trained with purely sparse task rewards on that data. (3) **Hierarchical integration**: high-level RL agent + low-level dynamic stability controller. (4) **Result**: learned policies surpass the original optimal-control teacher; sim-to-real validated across morphologies (arm-equipped Spot, G1 humanoid).
- **Compute Scale**: Mid-Large (24-40G+): Simulation-scale SMPC data generation + off-policy RL training.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) MPC as the source of optimality and exploration is the model-based planning module LeCun's architecture assumes — here it supervises a reactive policy. (2) "Let the model do the exploration" is the world-model division of labor in miniature. WEAKNESSES: (1) No learned world model — SMPC uses a physics model, and the deployed policy is model-free. (2) A data-generation framing, not a predictive-architecture contribution. Overall, a strong systems result from top-tier labs (TUM/ETH/Utah/Georgia Tech) showing MPC expertise scales RL without reward engineering — adjacent to, not inside, the JEPA program.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Replace dense reward shaping with SMPC-generated offline datasets, enabling sparse-reward off-policy RL for loco-manipulation.
- **Motivation**: Dense reward design is the dominant bottleneck in scaling RL to complex whole-body tasks; MPC experts in simulation are cheap, tunable, and solve exploration automatically.
- **Problem Solved**: Learns loco-manipulation skills from sparse rewards that surpass the optimal-control teacher, validated sim-to-real on two morphologies.

### Academic Context

- **Inheritance / Response**: Builds on MPC-as-expert and offline-to-online RL lines; responds to the reward-shaping bottleneck in legged-robot RL.
- **Implicit Connection**: Demonstrates the LeCun-adjacent pattern of model-based planning producing data for reactive policies — a stepping stone toward learned world models replacing the physics-based MPC teacher.
- **Research Line**: Model-Based Data Generation — MPC experts as automated supervisors for sparse-reward RL.
- **Future Directions**: Replacing SMPC with a learned latent world model (JEPA-style) as the dataset generator; scaling to full-body mobile manipulation.
- **GitHub**: Not found

---


## [2026-08-12] Predicting Functions, Not Features: KANs with Function-Space Joint-Embedding Predictive Learning for Medical Image Segmentation

- **arXiv**: [2608.12050](https://arxiv.org/abs/2608.12050)
- **Authors**: Yungeng Liu, Xuanzi Fang, Yuge Zhang, Shuqi Ren, Haijin Zeng, Yongyong Chen
- **TL;DR**: FS-JEPA — moves JEPA-style masked predictive learning into the pre-aggregation function space of Kolmogorov-Arnold Networks: an online branch predicts multi-radius signatures of sampled KAN edge functions against an EMA full-context target branch; best average Dice on five medical segmentation benchmarks, +2.25pp over the strongest KAN competitor, with the predictive branch removed at inference.
- **Problem**: KAN-based segmentation models optimize edge functions only through objectives defined after edge aggregation; individual edge functions lack an explicit pre-aggregation learning target, leaving the function space under-structured.
- **Architecture**: (1) **Function-Space JEPA**: a masked online branch predicts structured multi-radius signatures (function evaluations around the input anchor) of sampled KAN edge functions, produced by a full-context EMA target branch. (2) **Shared edge indices** preserve correspondence between predictions and targets. (3) Multi-radius signatures capture local functional variation that a single response cannot. (4) The function-space objective is jointly optimized with the segmentation loss; **the predictive branch is removed at inference** (zero deployment overhead).
- **Compute Scale**: Small-Mid (8-24G): KAN-based segmentation models on 5 medical benchmarks.
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) Genuinely extends the JEPA recipe (online/target encoders, EMA, masked prediction in abstract space) to a new substrate — function space — rather than token or embedding space. (2) "Predict functions, not features" is a clean statement of the JEPA principle: predict structure, not raw inputs. (3) Auxiliary objective removed at inference, matching JEPA's efficiency argument. WEAKNESSES: (1) Medical segmentation domain — no planning/control downstream, so it validates JEPA generality rather than advancing world models. (2) Static images, no temporal dynamics. Overall, a creative cross-domain JEPA variant with an architecturally novel prediction target — logged as evidence of JEPA's expanding generality.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: FS-JEPA — function-space joint-embedding predictive learning that gives KAN edge functions an explicit pre-aggregation predictive target.
- **Motivation**: Post-aggregation objectives leave individual KAN functions without direct learning signals; the function space is where KANs' expressiveness actually lives.
- **Problem Solved**: Achieves best average Dice across five segmentation benchmarks, outperforming the strongest KAN-based competitor by +2.25pp, without any inference-time cost.

### Academic Context

- **Inheritance / Response**: Extends the JEPA family (I-JEPA/V-JEPA) and the KAN segmentation line; responds to the lack of pre-aggregation supervision in KANs.
- **Implicit Connection**: Demonstrates JEPA's flexibility — the online/target predictor structure transfers to function space — supporting the claim that latent prediction is a universal learning principle.
- **Research Line**: JEPA Variants — function-space predictive learning for structured networks.
- **Future Directions**: Function-space JEPA in other KAN applications; temporal function-space prediction for world models.
- **GitHub**: Not found

---


## [2026-08-12] How Can Driving World Models Do Counterfactual Prediction?

- **arXiv**: [2608.11601](https://arxiv.org/abs/2608.11601)
- **Authors**: Jiaru Zhang, Can Cui, Yi Xu, Xin Ye, Ruqi Zhang, Ziran Wang
- **TL;DR**: Formalizes the gap between the "counterfactual simulator" ambition of driving world models and direct action-conditioned prediction — which ignores factual continuations — using the causal recipe of abduction, action, and prediction; a new matched-counterfactual benchmark shows two representative world models fail counterfactual matching, while a simple training-free evidence-injection pipeline substantially closes the gap.
- **Problem**: Driving world models are asked "what would have happened under an alternative ego action?", but direct action-conditioned prediction conditions only on shared history + alternative action — it can generate plausible futures without preserving what actually happened in the episode.
- **Architecture**: (1) **Causal formalization**: abduction (infer latent state from the factual episode) → action (apply the alternative ego action) → prediction (roll forward). Direct prediction skips abduction. (2) **Controlled simulation benchmark** with factual outcomes and matched counterfactual outcomes (short horizon where the alternative ego action does not alter surrounding agents). (3) **Training-free constructive pipeline**: moves observed evidence into the counterfactual view and lets the frozen model complete the rest — substantially raises recovered fraction and reduces perceptual distance to the matched counterfactual on both models.
- **Compute Scale**: Mid (24G): Controlled simulation benchmark + two representative driving world models.
- **LeCun Alignment**: HIGH — STRENGTHS: (1) Counterfactual prediction is LeCun's canonical world-model capability — predict the outcome of alternative actions; this paper shows the standard action-conditioned paradigm systematically fails it. (2) The abduction-action-prediction recipe maps directly onto the world model's role in the JEPA agent loop. (3) Constructive: shows even a training-free evidence-injection fix helps. WEAKNESSES: (1) Short-horizon setting only; interaction effects deferred. (2) The fix is a pipeline hack, not a learned architecture — leaving the door open for a JEPA-style latent solution. Overall, a crisp theoretical + empirical diagnosis of a core failure mode in generative world models — exactly the class of limitation LeCun has long argued generative models carry.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: A causal diagnosis of why driving world models fail counterfactual prediction, plus a measurable benchmark and a training-free mitigation.
- **Motivation**: Counterfactual simulation is the primary use case for driving world models; if they cannot preserve factual continuations, their safety-critical applications are undermined.
- **Problem Solved**: Demonstrates the abduction-action-prediction gap empirically, and shows that injecting observed evidence into the counterfactual view substantially improves counterfactual matching.

### Academic Context

- **Inheritance / Response**: Builds on the counterfactual/causal inference literature and driving world model evaluation; responds to the counterfactual-simulator claims of current driving WMs.
- **Implicit Connection**: Counterfactual prediction under alternative actions is the defining test of LeCun's world model; this paper provides the first controlled benchmark and identifies abduction as the missing ingredient.
- **Research Line**: Counterfactual World Models — causal evaluation and correction of predictive simulators.
- **Future Directions**: Learned abduction modules (JEPA-style latent state inference); long-horizon counterfactual prediction with interacting agents.
- **GitHub**: Not found

---


## [2026-08-12] Keep the Future, Drop the Rollout: RIFT for World Action Models

- **arXiv**: [2608.11521](https://arxiv.org/abs/2608.11521)
- **Authors**: Chushan Zhang, Jinguang Tong, Xuesong Li, Yikai Wang, Hongdong Li
- **TL;DR**: RIFT — causal interventions across four WAMs show action generation needs the future's K/V cache VALUES but not the iterative rollout PROCESS that constructs them; RIFT learns anticipation tokens that build the complete future cache in ONE backbone pass — 98.8% LIBERO success with 68.2–89.1% lower action-chunk latency, and the best observed RoboTwin 2.0 scores (92.9/92.6% clean/randomized).
- **Problem**: WAMs condition actions on predicted futures, but iterative video rollout inflates deployment latency. Does action generation require the evolving rollout trajectory, or only its future representation?
- **Architecture**: (1) **Paired closed-loop interventions** over 4 WAMs × 40 LIBERO tasks: masking or reassigning future-cache values changes execution and reduces success → WAMs are sensitive to future values AND their assigned positions. (2) **Key separation**: for Joint and Cosmos-2, replaying a single fixed final-clean K/V cache nearly preserves execution (1.7–1.9 cm ADE, 97.9–98.2% success) → cache consumption ≠ cache production. (3) **RIFT**: learned anticipation tokens construct the complete future K/V cache in one backbone pass, retaining the original future-read interface. (4) Results: 98.8% LIBERO (vs 98.4–98.6% for rollout-based Joint/IDM/LingBot-VA) at 68.2–89.1% latency reduction; 92.9/92.6% RoboTwin 2.0 clean/randomized — highest observed.
- **Compute Scale**: Mid-Large (24-40G+): Trains on top of pretrained video WAM backbones (Joint, Cosmos-2); deployment drops iterative rollout → large latency savings.
- **LeCun Alignment**: HIGH — STRENGTHS: (1) Causal evidence that WAMs consume a future REPRESENTATION, not the rollout process itself — the empirical twin of JEPA's premise (predict latent futures; don't generate them). (2) Anticipation tokens are a latent predictive shortcut: one forward pass replaces N rollout steps — the efficiency argument for reconstruction-free prediction, demonstrated inside WAMs. (3) Best RoboTwin 2.0 results among evaluated methods. WEAKNESSES: (1) Built on generative video WAMs; the future cache is still a video-VAE latent, not a JEPA embedding. (2) Anticipation tokens are trained per-backbone. Overall, the strongest practical demonstration to date that rollout-free future conditioning is sufficient — a deployment-side vindication of latent prediction over pixel generation.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: RIFT — replace iterative video rollout in WAMs with one-pass anticipation tokens that construct the complete future K/V cache.
- **Motivation**: Rollout latency is the deployment bottleneck of WAMs; causal intervention analysis shows the evolving trajectory is not what actions actually consume.
- **Problem Solved**: Achieves rollout-competitive success (98.8% LIBERO, best RoboTwin 2.0) while cutting action-chunk latency by 68.2–89.1%.

### Academic Context

- **Inheritance / Response**: Builds on the WAM line (Joint, IDM, Cosmos-2, LingBot-VA); responds to WAM deployment-latency critiques with a mechanistic causal analysis.
- **Implicit Connection**: The cache-consumption vs cache-production separation is the JEPA argument (predict latent futures efficiently) proven causally inside generative WAMs — a bridge paper toward JEPA-native WAMs.
- **Research Line**: Efficient World-Action Models — rollout-free future conditioning for deployment.
- **Future Directions**: Anticipation tokens on JEPA latent caches (no video VAE); transferable future-cache constructors across WAM backbones.
- **GitHub**: Not found

---


## [2026-08-11] JEPA-WAM: Stage-Level Joint-Embedding Prediction for World-Action Models in Robot Manipulation

- **arXiv**: [2608.10780](https://arxiv.org/abs/2608.10780)
- **Authors**: Xiao Liu, Yuguang Yang, Xi Wang, Kai Jiang, Cheng Chi, Yong Xu, Wenchao Ding, Yilun Chen, Yan Wang
- **TL;DR**: JEPA-WAM — augments a Motus-based WAM with Stage-JEPA, a goal-conditioned JEPA predictor on a frozen V-JEPA2 encoder that predicts the latent target of the next inferred task stage; 90.25% success across 50 RoboTwin 2.0 tasks and 5.97% fewer execution steps than the strongest baseline. *(Backfill — missed by the Aug 12–13 scans.)*
- **Problem**: WAMs represent the future as a fixed short video-action chunk — local scene evolution for action execution — with no explicit stage-level semantic future describing how the task should progress from its current stage to the next.
- **Architecture**: (1) **Two complementary futures**: a short-term physical future (local scene evolution, the WAM's chunk) and a stage-level semantic future (task progress). (2) **Stage-JEPA**: a goal-conditioned JEPA predictor; a frozen V-JEPA2 encoder extracts the current-state representation and predicts the latent target of the next inferred stage, conditioned on the current observation and task instruction. (3) The Motus-based WAM backbone is augmented, not replaced.
- **Compute Scale**: Mid-Large (24-40G+): Motus WAM + frozen V-JEPA2 encoder + Stage-JEPA predictor across 50 RoboTwin 2.0 tasks (clean + randomized).
- **LeCun Alignment**: HIGH — STRENGTHS: (1) Direct JEPA-WAM hybrid using Meta's V-JEPA2 — the flagship LeCun-lineage encoder — for stage-level semantic prediction. (2) The physical/semantic future distinction mirrors the hierarchical abstraction LeCun's architecture demands (prediction at multiple abstraction levels). (3) Goal-conditioned latent prediction; no pixel targets. WEAKNESSES: (1) Frozen V-JEPA2 — no end-to-end adaptation to manipulation. (2) Stage inference mechanics are thin in the abstract. Overall, joins 2608.09381 in building WAMs natively on JEPA latents — among the clearest embodiments of LeCun's WAM blueprint to date.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: JEPA-WAM — a WAM with a Stage-JEPA predictor that represents the stage-level semantic future alongside the short-term physical future.
- **Motivation**: Task progress across stages is not captured by short video-action chunks; a stage-level latent future is needed for efficient multi-stage manipulation.
- **Problem Solved**: 90.25% overall success on 50 RoboTwin 2.0 tasks, with 5.97% fewer execution steps than the strongest baseline — stage-level prediction improves both success and efficiency.

### Academic Context

- **Inheritance / Response**: Builds on Motus WAM and V-JEPA2; responds to the short-horizon future representation limitation of current WAMs.
- **Implicit Connection**: Operationally realizes LeCun's hierarchical world model — semantic/stage-level latent prediction (JEPA) layered on physical/short-term prediction (WAM).
- **Research Line**: JEPA-Augmented World-Action Models — stage-level latent futures for manipulation.
- **Future Directions**: End-to-end Stage-JEPA adaptation; multi-level semantic futures; cross-embodiment stage prediction.
- **GitHub**: Not found

---


## [2026-08-10] World Tokens: Enhancing Embodied Policies with Training-Time World Modeling

- **arXiv**: [2608.09730](https://arxiv.org/abs/2608.09730)
- **Authors**: Qu Tang, Benhui Zhuang, Bo Yuan, Xue Yu, Longteng Guo, Junlan Feng
- **TL;DR**: World Tokens — a World Adapter converts VLM features into a fixed set of world tokens that condition a jointly fine-tuned future-video denoiser AND serve as the action expert's sole visual-language context; the world-model branch is removed at deployment, yielding VLA-level latency with world-model-shaped representations (competitive LIBERO, best reported SIMPLER averages). *(Backfill — missed by the Aug 12–13 scans.)*
- **Problem**: VLAs deploy efficiently but don't model physical scene evolution; WAMs model it but drag future generation or large video backbones into the control loop.
- **Architecture**: (1) **World Adapter**: transforms VLM features into a fixed set of world tokens. (2) **Shared conditioning**: the world tokens condition a jointly fine-tuned future-video denoiser (the training-time world model) and simultaneously serve as the action expert's sole visual-language context — gradients from future-video denoising directly shape the action representation. (3) **Exclusive routing** prevents the policy from bypassing that representation. (4) **Deployment**: the world-model branch is removed — only VLM + World Adapter + action expert remain, with no online video-model inference. (5) With a 2B backbone and no embodied action pretraining: competitive LIBERO, best reported SIMPLER averages, improved real-world R1 Pro success over a matched action-only baseline, at VLA-level latency.
- **Compute Scale**: Mid (24G): 2B VLM + World Adapter + training-time future-video denoiser.
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) "Train with a world model, deploy without it" — world modeling as representation distillation, the efficiency pattern JEPA advocates. (2) Exclusive routing forces the action policy to live in the world-conditioned representation — architectural honesty about what the policy consumes. WEAKNESSES: (1) The world-model branch is a generative future-video denoiser, not a JEPA predictor — gradients come from denoising, not latent prediction. (2) No explicit planning; world tokens shape one-step action chunks. Overall, strong evidence that world-model supervision improves embodied policies even when the world model never ships — a pattern JEPA-native versions could inherit.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: World Tokens — a World Adapter architecture that uses world modeling during training to enhance the action policy while preserving efficient deployment.
- **Motivation**: VLAs lack explicit physical-dynamics modeling; WAMs are too expensive to deploy; the middle path is training-time world modeling with a removed-at-deployment world branch.
- **Problem Solved**: Achieves WAM-grade success on LIBERO/SIMPLER and improved real-world success at VLA-level latency, without online video-model inference.

### Academic Context

- **Inheritance / Response**: Builds on VLA and WAM lines; responds to the deployment-cost critique of WAMs.
- **Implicit Connection**: The train-with-world-model/deploy-without pattern is JEPA's efficiency philosophy transposed to embodied policies — representation shaped by dynamics prediction, inference free of generation.
- **Research Line**: Training-Time World Modeling — dynamics supervision without deployment cost.
- **Future Directions**: Replacing the denoiser with a JEPA latent predictor; world-token-based planning heads.
- **GitHub**: Not found

---


## [2026-08-10] VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction

- **arXiv**: [2608.09448](https://arxiv.org/abs/2608.09448)
- **Authors**: Hongjin Ji, Guoyang Xia, Luoyang Sun, Fangxiang Feng, Lei Ren
- **TL;DR**: VANE — reliable test-time training for VLA policies: candidate prompt adaptations are isolated from the live policy, evaluated against future visual observations, and committed only when supported by future evidence; +3.2pp success on SimplerEnv WidowX over the TTT baseline. *(Backfill — missed by the Aug 12–13 scans.)*
- **Problem**: Test-time training for VLA policies is unreliable in closed-loop manipulation: a shared adaptation space mixes incompatible task corrections, and online updates can alter subsequent actions before their consequences are known.
- **Architecture**: (1) **Context-conditioned prompt adaptation** on the current vision-language context. (2) **Learn from the future visual consequences** of executed actions: candidate updates are isolated from the live policy, evaluated on subsequent observations, and committed only when supported by future evidence — making adaptation selective and reversible. (3) Future visual representation prediction serves as the supervision signal. (4) Results: +3.2pp over the TTT baseline on SimplerEnv WidowX; gains on Google Robot are task- and embodiment-dependent.
- **Compute Scale**: Small-Mid (8-24G): Test-time training on SimplerEnv WidowX + Google Robot.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) "Learn from future visual consequences" is a predictive-SSL stance — the future as supervision, exactly JEPA's signal source, transplanted into deployment-time adaptation. (2) Evidence-gated commitment is a safety pattern for autonomous systems. WEAKNESSES: (1) Adapts existing VLA policies; no latent dynamics model. (2) Gains are task/embodiment-dependent. Overall, a deployment-time predictive-learning data point; the evidence-gating mechanism is worth adopting for world-model online adaptation.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: A constrained, evidence-based test-time training framework that learns from future visual consequences before committing adaptations.
- **Motivation**: Unreliable TTT corrupts live policies; adaptation must be selective, reversible, and supported by observed future evidence.
- **Problem Solved**: +3.2pp average success over the TTT baseline on SimplerEnv WidowX, with deployment-time gains remaining task- and embodiment-dependent on Google Robot.

### Academic Context

- **Inheritance / Response**: Builds on test-time training for VLAs; responds to closed-loop reliability failures of naive TTT.
- **Implicit Connection**: Future-prediction-as-supervision and evidence-gated model updates echo the JEPA program's core signals and its demand for safe online adaptation.
- **Research Line**: Reliable Online Adaptation — evidence-gated predictive learning at deployment.
- **Future Directions**: Latent future prediction for adaptation supervision; combination with JEPA-style world models for update gating.
- **GitHub**: Not found

---

## [2026-08-11] Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning

- **arXiv**: [2608.11204](https://arxiv.org/abs/2608.11204)
- **Authors**: Wenrui Bao, Tianyun Jiang, Zhiben Chen, Ser-Nam Lim, Peter D. Peng, Yuzhang Shang
- **TL;DR**: Surgical WAM — a unified generative world-action model on Cosmos Policy that jointly predicts future endoscopic observations and executable action chunks, pretrained on cheap action-free surgical video then fine-tuned on a fixed action-labeled budget, lifting closed-loop surgical manipulation success from 63.5% to 77.8%.
- **Problem**: Surgical robot learning is bottlenecked by scarce action-labeled teleop demonstrations (synchronized video+kinematics on dVRK are costly), while surgical tasks demand precise contact handling, long-horizon reasoning, and bimanual coordination. Endoscopic video is abundant but is used almost entirely for simulation or policy evaluation — its dynamics knowledge is rarely translated into closed-loop control. Central question: under a FIXED budget of action-labeled demonstrations, does action-free video pretraining improve closed-loop surgical manipulation?
- **Architecture**: Surgical WAM — (1) **Unified generative backbone** built on Cosmos Policy that jointly predicts future endoscopic frames AND executable surgical action chunks. (2) **Two-stage training**: action-free video pretraining learns surgical visual dynamics (tissue deformation, tool interaction); fine-tuning on the fixed action-labeled budget grounds those dynamics into action generation. (3) **Deployment**: closed-loop receding-horizon controller — execute a short prefix of each predicted action chunk, then replan from the resulting observation. (4) **Results**: on four simulated surgical manipulation tasks, video pretraining improves average success from 63.5% → 77.8%, including +20pp on PegTransfer, with the largest gains on contact-rich and bimanual tasks.
- **Compute Scale**: Large (40G+): Cosmos Policy video backbone + surgical fine-tuning. Deployment runs receding-horizon closed-loop control (no rollout beyond a chunk prefix).
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) The core thesis — self-supervised dynamics learning from action-free observation, then minimal action-label grounding — is exactly the data-efficiency agenda of LeCun's self-supervised world model program. (2) The closed-loop receding-horizon controller treats the learned model as a predictive world model for control, not just a simulator. (3) Directly answers a falsifiable scientific question about whether video pretraining transfers to control. WEAKNESSES: (1) Predicts future video in pixel space (generative paradigm) rather than latent JEPA-style prediction — a counterpoint to reconstruction-free world models. (2) Surgical simulation evaluation, no real dVRK deployment yet. (3) No hierarchical/long-horizon abstraction — chunk-level autoregression. Overall, a clean demonstration that world-model pretraining on observation-only data is the practical path to scaling surgical robot learning, even if the architecture remains generative.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Surgical WAM — pretrain a joint video+action world-action model on abundant action-free endoscopic video, then fine-tune on a fixed action-labeled budget; deploy as a closed-loop receding-horizon controller.
- **Motivation**: Action-labeled surgical demonstrations are the scarce resource; endoscopic video is cheap and encodes rich manipulation dynamics. Translate video-learned dynamics into control.
- **Problem Solved**: Shows that under a fixed action-label budget, action-free video pretraining yields large, task-dependent gains (+20pp on PegTransfer; biggest wins on contact-rich and bimanual tasks) — video provides transferable visual dynamics priors for surgical control.

### Academic Context

- **Inheritance / Response**: Builds on Cosmos Policy (NVIDIA world-action foundation model) and the WAM literature; responds to the surgical-robotics status quo where world models serve simulation/evaluation rather than control.
- **Implicit Connection**: Implements the "learning from observation" premise of LeCun's self-supervised agenda in a high-stakes domain; the fixed-budget ablation is a clean test of whether world-model pretraining pays for itself in action efficiency.
- **Research Line**: Domain-Specialized World-Action Models — WAMs applied to surgical manipulation with observation-only pretraining.
- **Future Directions**: Real dVRK deployment; latent (JEPA-style) surgical dynamics to avoid pixel prediction; scaling video pretraining across procedures/embodiments.
- **GitHub**: Not found

---

## [2026-08-11] Capturing Uncertainty in Human Motion for Representation Learning in Soccer

- **arXiv**: [2608.11203](https://arxiv.org/abs/2608.11203)
- **Authors**: Yizhou Xu, Lars Bretzner, Tiesheng Wang, Atsuto Maki
- **TL;DR**: Self-supervised 3D skeleton representation learning for soccer via future motion prediction, adding a conditioning module that models a probabilistic distribution over discretized plausible futures so multimodality in human motion is explicitly captured.
- **Problem**: Using future motion prediction as the SSL objective for human motion is compromised by the inherent uncertainty/multimodality of motion — a single predicted future collapses the distribution and yields representations that capture only average dynamics, losing the contingency structure a world model needs.
- **Architecture**: (1) **3D skeleton encoder** for soccer player motion. (2) **Conditioning module for motion prediction** that models a probabilistic distribution over discretized future motions in 3D Euclidean space, with explicit supervision from future trajectories to learn multimodality. (3) **SSL objective = future prediction** (predictive-representation paradigm, no reconstruction of inputs). (4) **Evaluation**: substantially improved motion prediction accuracy on large-scale soccer tracking data; representations transfer to multiple downstream soccer tasks with strong cross-task generalization.
- **Compute Scale**: Small-Mid (8-24G): Skeleton-based transformer/encoder on large-scale player tracking data.
- **LeCun Alignment**: LOW — Cross-domain predictive SSL. STRENGTHS: (1) Shares JEPA's core philosophy — prediction of future states (not reconstruction) as the learning objective. (2) Explicit multimodality modeling of futures is precisely the uncertainty handling that latent world models need for planning over contingencies. WEAKNESSES: (1) No planning, control, or latent world-model abstraction downstream. (2) Predicts discretized motion bins rather than latent embeddings (closer to token prediction than JEPA embedding prediction). (3) No connection to the autonomous intelligence architecture. Logged as a data point on uncertainty-aware predictive representation learning outside the usual JEPA modalities.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Uncertainty-aware self-supervised representation learning for 3D human motion, where the prediction objective explicitly models a distribution over multiple plausible futures.
- **Motivation**: Human motion is inherently uncertain; single-future prediction objectives destroy the multimodal contingency structure that makes motion dynamics informative.
- **Problem Solved**: Multimodal future modeling substantially improves motion prediction accuracy, and the learned representations transfer broadly across downstream soccer tasks.

### Academic Context

- **Inheritance / Response**: Builds on self-supervised human motion representation learning (skeleton-based SSL); responds to the known failure of deterministic future-prediction objectives under uncertainty.
- **Implicit Connection**: Evidence that prediction-based SSL must handle multimodality explicitly — the same lesson JEPA world models face (e.g., UWM-JEPA's belief-space prediction) in a different modality.
- **Research Line**: Uncertainty-Aware Predictive SSL — multimodality modeling in prediction objectives across modalities.
- **Future Directions**: Latent-space (embedding) prediction instead of discretized motion bins; using the multimodal predictive model as a world model for game/tactical planning.
- **GitHub**: Not found

---

## [2026-08-11] VIScore: Diagnosing Planning-Relevant Quality in Latent World Models

- **arXiv**: [2608.11174](https://arxiv.org/abs/2608.11174)
- **Authors**: Haiyu Wu, Randall Balestriero, Morgan Levine
- **TL;DR**: VIScore — a Veracity-Influence-Sobriety metric spanning encoder, predictor, and planner that quantifies planning-relevant quality of latent world models, explaining planning success (Spearman > 0.75) far better than straightness, physical-state probing, or empowerment, and showing that the JEPA-standard SIGReg regularization does NOT transfer to planning while VISReg does.
- **Problem**: Regulating the latent space to an isotropic Gaussian gives a stable, information-maximized landscape — but latent geometry and planning success remain disconnected. Existing diagnostics focus only on the encoded latent and fail to predict planning performance, especially out-of-domain. The paper asks: what actually makes a latent world model plan well?
- **Architecture**: (1) **SIGReg vs VISReg comparison**: two regularization losses with the same isotropic-Gaussian target but different properties (VISReg gives finer control over center/scale/shape weighting; larger batches → finer distribution approximation). Finding: SIGReg — beneficial in SSL — does NOT help planning; VISReg improves planning success on OOD datasets. (2) **VIScore** decomposes planning success into three measurable components: **Veracity** (encoder's representation faithfulness), **Influence** (reachability/capacity of the predictor given the encoded features), and **Sobriety** (hallucination of the search-based planner). (3) **Validation**: on cross-task success rate pools over seen and unseen models/datasets, VIScore achieves Spearman > 0.75 with planning success — the only metric with calibration error below the constant fit across ALL test scenarios.
- **Compute Scale**: Small-Mid (8-24G): Latent world model training runs (SIGReg/VISReg variants) + metric computation; no large-scale pretraining.
- **LeCun Alignment**: HIGH — STRENGTHS: (1) **Balestriero co-authorship** places this directly in the LeCun/Meta FAIR research lineage. (2) Operates on the exact JEPA regularization toolkit — SIGReg is the I-JEPA/V-JEPA standard — and demonstrates that SSL-grade latent geometry does not by itself produce a usable world model for planning. (3) The metric's structure (encoder + predictor + planner) mirrors LeCun's modular architecture: perception, world model, and actor/configurator must be diagnosed jointly, not just the embedding. (4) Provides the missing evaluation instrument for the JEPA planning agenda — a way to tell whether a latent world model will actually support MPC/search before deployment. WEAKNESSES: (1) A diagnostic, not a new architecture. (2) Search-based planners only — not evaluated against JEPA+MPC specifically. Overall, this is the evaluation paper the latent world model community has needed: it disconnects representation quality from planning quality and gives a calibrated instrument for the latter.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: VIScore — a three-component metric (Veracity, Influence, Sobriety) covering encoder, predictor, and planner to quantify planning-relevant quality of latent world models.
- **Motivation**: Latent regularization (isotropic Gaussian) is treated as a proxy for planning quality, but the connection is unproven; planning success needs its own diagnostic.
- **Problem Solved**: Shows SIGReg's SSL benefits don't transfer to planning while VISReg's do, and VIScore explains planning success (Spearman > 0.75) and calibrates across all scenarios better than straightness, physical-state probing, and empowerment.

### Academic Context

- **Inheritance / Response**: Directly extends the JEPA regularization line (I-JEPA/V-JEPA SIGReg) and the world-model evaluation literature (straightness, probing); a corrective to latent-geometry-as-proxy thinking.
- **Implicit Connection**: Answers a question central to LeCun's program: when does a JEPA-style latent space become a *usable* world model? The answer involves the predictor's influence and the planner's sobriety — not the embedding alone.
- **Research Line**: World Model Evaluation & Diagnosis — planning-relevant metrics spanning the full encoder→predictor→planner stack.
- **Future Directions**: Using VIScore to guide world model training objectives; extending to JEPA+MPC pipelines; metric-driven architecture search.
- **GitHub**: Not found

---

## [2026-08-11] Flex-π: A Multi-Stream World-Action Model with Compute Flexibility

- **arXiv**: [2608.10860](https://arxiv.org/abs/2608.10860)
- **Authors**: Ge Yan, Jinghao Liu, Yuzhi Fan, Lei Cai, Minwen Liao, Jesse Zhang, Dieter Fox
- **TL;DR**: Flex-π — a 6B multi-stream world-action model that supervises RGB, 3D pointmaps, and DINO object semantics in ONE shared video-VAE latent space (pointmaps encode almost losslessly in the RGB VAE with zero pointmap-specific training), with per-stream dropout enabling a single checkpoint to run any stream subset — from fast action-only to full joint generation; beats strongest baselines 2-7× on real bimanual manipulation.
- **Problem**: WAMs predict only RGB latents trained purely for pixel reconstruction, with no explicit signal for the 3D geometry or object semantics that manipulation actually needs — a gap between what world models predict and what control requires.
- **Architecture**: (1) **Free lunch discovery**: the same frozen video-generation VAE that encodes RGB also encodes 3D pointmaps almost losslessly — no pointmap-specific training, no new sensors, no new pretraining. (2) **Multi-stream supervision**: 6B-parameter WAM supervised on 3D geometry + object-centric DINO semantics alongside RGB, all projected into the shared VAE latent space and denoised jointly with actions inside a Mixture-of-Transformers backbone. (3) **Per-stream dropout with cross-modality forcing**: a single trained checkpoint runs on ANY subset of streams at inference — action-only fast mode up to full joint generation — giving explicit compute/quality trade-offs. (4) **Results**: exceptionally demonstration-efficient, generalizes in and out of distribution on dexterous, precise, real-world bimanual manipulation tasks; faster than π0.5 at inference.
- **Compute Scale**: Large (40G+): 6B-parameter MoT backbone; inference faster than π0.5 despite the multi-stream supervision (streams can be dropped at runtime).
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) Moving beyond RGB pixel reconstruction toward multi-stream abstract state (geometry + semantics) is precisely the "learning abstract representations" priority of LeCun's agenda. (2) The single-checkpoint, compute-flexible stream gating aligns with the efficiency demands of embodied autonomous systems (configurator-like allocation of compute). (3) Frozen VAE + shared latent space is an elegant step toward reconstruction-free operation — signals live in one space without per-modality decoders. WEAKNESSES: (1) Still a generative denoising WAM — actions and future states are jointly diffused, not latent-predictive in the JEPA sense. (2) Relies on a pretrained video VAE (borrowed inductive bias). (3) NVIDIA-affiliated (Dieter Fox senior author) — an industrial counterpoint to FAIR's JEPA line. Overall: the strongest evidence yet that WAMs benefit from explicit multi-stream abstract supervision, and a model for compute-adaptive deployment.
- **GitHub**: Project site: https://flex-pi.github.io/

### What / Why / Solve

- **Proposal**: Flex-π — supervise a 6B WAM on 3D pointmaps and DINO semantics alongside RGB in a shared VAE latent space, with per-stream dropout for compute-flexible inference from a single checkpoint.
- **Motivation**: RGB-latent WAMs lack the geometric and semantic signals manipulation needs; those signals turn out to be nearly free inside the existing VAE.
- **Problem Solved**: 2-7× improvement over strongest baselines on dexterous real-world bimanual tasks, in and out of distribution, with run-time selectable stream subsets (compute flexibility) and no added sensors, pretraining, or inference latency.

### Academic Context

- **Inheritance / Response**: Builds on the π-family (π0.5) and Mixture-of-Transformers WAM designs; responds to the RGB-only latent bottleneck identified across the WAM literature.
- **Implicit Connection**: Operationally moves WAMs toward richer abstract state spaces — the representational direction LeCun argues generative models must take to become world models, though via multi-signal supervision rather than latent prediction.
- **Research Line**: Multi-Stream World-Action Models — abstract state supervision + compute-flexible WAM deployment.
- **Future Directions**: Latent prediction (JEPA-style) over the multi-stream space instead of joint denoising; stream-conditional planning; scaling to full 3D scene graphs.
- **GitHub**: Project site: https://flex-pi.github.io/

---

## [2026-08-11] Toward the Cognitive–Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent

- **arXiv**: [2608.10618](https://arxiv.org/abs/2608.10618)
- **Authors**: Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He, Bolin Zhao, Sheng Zhao, Zhouheng Li, Chee Kiong Ong, King Ho Holden Li, Chen Lv
- **TL;DR**: A world-model-centric autonomous racing agent that learns predictive world models from near-limit successes AND failures using real-vehicle data at up to 256.3 km/h, coupling world-state construction, future-aware reasoning, and near-limit control in a closed-loop refinement process; 88.3% interaction success in full-scale simulated racing.
- **Problem**: Embodied systems are evaluated within conservative safety margins, so their capability boundaries under extreme conditions are unknown; existing racing systems push speed but rarely model and refine cognitive and physical limits jointly.
- **Architecture**: (1) **Predictive world models learned from near-limit successes and failures** capturing interaction evolution, ego dynamics, and feasible-motion boundaries. (2) **Closed-loop pipeline**: world-state construction → future-aware reasoning → near-limit control, with joint refinement of world model and policy from outcomes. (3) **Data**: real-vehicle autonomous racing with robust localization/perception at 256.3 km/h and 26.8 m/s² peak lateral acceleration. (4) **Results**: 88.3% interaction success across challenging full-scale simulated racing scenarios; closed-loop refinement improves limit utilization, failure recovery, and generalization to unseen circuits.
- **Compute Scale**: Mid-Large (24-40G+): Real-vehicle data collection + full-scale racing simulation training with closed-loop refinement.
- **LeCun Alignment**: MEDIUM — STRENGTHS: (1) Learning world models from failures (near-limit outcomes) — the model must represent what is NOT feasible, not just what works — a key requirement for safe planning. (2) World model used for future-aware reasoning in a real high-speed control loop — an extreme testbed for the "predict then act" paradigm. (3) Closed-loop joint refinement of model and policy resembles the world model + actor interplay in LeCun's architecture. WEAKNESSES: (1) Model class unspecified in the abstract (not JEPA; likely learned dynamics on state data). (2) System-oriented — evaluation in simulation with real-vehicle data rather than fully real deployment. (3) Racing is a narrow domain. Overall, valuable as a boundary-aware world-model deployment study demonstrating that modeling near-limit failures is what buys generalization.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: World-model-centric racing agent that jointly models cognitive-physical limits by learning predictive world models from near-limit successes and failures, refined in closed loop.
- **Motivation**: Extreme-condition capability boundaries are understudied; racing offers a testbed where dynamics saturate and prediction errors are catastrophic.
- **Problem Solved**: 88.3% interaction success in full-scale simulated racing; closed-loop refinement improves utilization of limits, failure recovery, and generalization across unseen circuits.

### Academic Context

- **Inheritance / Response**: Builds on model-based racing/planning and world-model control literature; responds to the gap between high-speed performance systems and joint cognitive-physical limit modeling.
- **Implicit Connection**: Failure-inclusive world model training (cf. FACT in this scan) — world models must encode infeasible futures to support planning; validated at extreme physical regimes.
- **Research Line**: Boundary-Aware World Models — representing capability envelopes for safe embodied deployment.
- **Future Directions**: Fully real deployment at speed; JEPA-style latent dynamics for racing; explicit infeasibility prediction for safety certification.
- **GitHub**: Not found

---

## [2026-08-11] Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving

- **arXiv**: [2608.10386](https://arxiv.org/abs/2608.10386)
- **Authors**: Jiazhuo Li, Linjiang Cao, Qi Liu, Xi Xiong
- **TL;DR**: Dreamer-SAC — integrates a recurrent state-space world model with off-policy soft actor-critic trained directly in latent space for autonomous driving; short-horizon latent rollouts + n-step targets outperform DreamerV3, SAC, and PPO with substantially fewer real environment interactions, revealing an inverted-U relationship between rollout horizon and performance.
- **Problem**: World models reduce costly environment interactions, but policy optimization over learned dynamics is sensitive to prediction errors — the classic data-efficiency vs model-bias trade-off in model-based RL for driving.
- **Architecture**: (1) **Recurrent state-space world model** (Dreamer-family RSSM). (2) **Off-policy SAC trained in latent space** combining real interactions with short-horizon generated trajectories; n-step target estimation; multi-objective supervision (driving efficiency + safety). (3) **Key finding**: inverted-U relationship between rollout horizon and policy performance — short-horizon latent rollouts give the best trade-off between added training signal and accumulated model bias; n-step targets exploit predicted experience better than one-step TD.
- **Compute Scale**: Small-Mid (8-24G): DreamerV3-scale RSSM + SAC on autonomous driving scenarios.
- **LeCun Alignment**: LOW-MEDIUM — STRENGTHS: (1) A rigorous analysis of model bias in world-model RL — the inverted-U rollout-horizon finding is directly useful to anyone planning with learned dynamics. (2) Sample efficiency in a safety-critical continuous domain. WEAKNESSES: (1) Dreamer-family: reconstruction-based latent dynamics, a counterpoint to reconstruction-free JEPA world models. (2) No latent-prediction or energy-based objectives. (3) Driving simulation only. Logged as the Dreamer-line data point on off-policy latent-space learning.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Dreamer-SAC — off-policy SAC in the latent space of a recurrent world model, using short-horizon generated rollouts with n-step targets for sample-efficient autonomous driving.
- **Motivation**: Policy optimization over learned dynamics is error-sensitive; the right mixture of real and imagined data (short-horizon, n-step) minimizes model bias while maximizing sample efficiency.
- **Problem Solved**: Outperforms DreamerV3, SAC, and PPO with substantially fewer real interactions; quantifies the inverted-U rollout-horizon relationship and the advantage of n-step over one-step TD targets for value learning from predicted experience.

### Academic Context

- **Inheritance / Response**: Extends the Dreamer lineage with off-policy learning; responds to model-bias sensitivity in world-model policy optimization for driving.
- **Implicit Connection**: Quantifies precisely the failure mode LeCun cites for generative world models — compounding prediction error — and shows the mitigation (short horizons, n-step bootstrapping) within the Dreamer paradigm.
- **Research Line**: Off-Policy Model-Based RL — efficient use of imagined rollouts in latent world models.
- **Future Directions**: JEPA-style latent dynamics for the RSSM to reduce reconstruction bias; uncertainty-weighted rollout lengths; real-world driving deployment.
- **GitHub**: Not found

---

## [2026-08-10] FACT: Failure-Aware Causal Training for World-Action Models

- **arXiv**: [2608.10232](https://arxiv.org/abs/2608.10232)
- **Authors**: Quanquan Peng, Yutong Liang, Rui Yan, Nicklas Hansen, Xiaolong Wang
- **TL;DR**: FACT — a causal World-Action Model that conditions future-video and task-progress prediction on the executed action, so failure rollouts supervise action consequences; bad actions become valid future targets instead of being discarded, reducing success-biased future hallucination and optionally scoring action candidates at inference.
- **Problem**: WAMs co-train policies with future prediction, but the world model is trained mostly on successful demonstrations — it has little reason to predict the consequences of bad actions. This success bias causes future hallucination under bad actions and undermines using predicted futures for planning or candidate scoring.
- **Architecture**: (1) **Causal WAM**: future video + task progress predicted conditioned on the executed action (action-conditioned interface). (2) **Failure-aware training**: failure rollouts supervise action consequences — bad actions become valid future targets rather than discarded data. (3) **Inference option**: the progress predictor scores sampled action candidates (model-based action selection). (4) **Results**: outperforms many baselines on simulation and real-world bimanual manipulation; performance improves as failure data are incorporated; success-biased future hallucination under bad actions is reduced.
- **Compute Scale**: Mid-Large (24-40G+): Video prediction + task-progress predictor on simulation and real-world bimanual manipulation.
- **LeCun Alignment**: MEDIUM-HIGH — STRENGTHS: (1) From the Xiaolong Wang / Nicklas Hansen group — a leading world-model lab — lending ecosystem credibility. (2) Addresses a core gap in LeCun's vision: a world model must predict the consequences of ANY action, including bad ones, or planning over it is systematically biased. Failure-inclusive prediction is exactly what a planner needs to avoid infeasible branches. (3) The optional progress-scored action selection is a concrete world-model-driven planning mechanism. WEAKNESSES: (1) Still video-generative (pixel-level future prediction) rather than latent JEPA prediction. (2) Requires failure rollouts — relies on a source of failure data. (3) Progress prediction is scalar — limited abstraction. Overall, a principled fix for success-biased world models that pushes WAMs toward causal, action-conditional prediction of outcomes.
- **GitHub**: Project site: https://fact-wam.github.io/

### What / Why / Solve

- **Proposal**: FACT — make WAM future prediction action-conditional so failure rollouts supervise the consequences of bad actions, with task-progress prediction that can score action candidates at inference.
- **Motivation**: World models trained on successes hallucinate success under bad actions; failures are the informative cases for control.
- **Problem Solved**: Outperforms existing WAM baselines on sim and real bimanual manipulation, improves with failure data, and reduces success-biased future hallucination under bad actions.

### Academic Context

- **Inheritance / Response**: Builds on the video-model WAM line (co-training prediction + policies); responds to the unexamined success bias in demonstration-trained world models.
- **Implicit Connection**: Complements the racing agent (2608.10618, same scan) — both show failure-inclusive world model training improves generalization; implements the "consequences of actions, good and bad" requirement of LeCun's world model definition.
- **Research Line**: Causal World-Action Models — action-conditional outcome prediction including failure modes.
- **Future Directions**: Latent (JEPA-style) failure-aware prediction; failure data from on-policy exploration; progress-conditioned hierarchical planning.
- **GitHub**: Project site: https://fact-wam.github.io/

---

## [2026-08-11] JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling

- **arXiv**: [2608.09381](https://arxiv.org/abs/2608.09381)
- **Authors**: Yihan Lin, Jiawei He, Shifeng Bao, Chen Zhao, Yang Li, Xiaobo Wang, Yan Wang, Cheng Chi, Jing Zhang
- **TL;DR**: First end-to-end integration of V-JEPA latent space with World Action Models — couples latent transition prediction and continuous action generation through a shared predictor, completely avoiding pixel reconstruction.
- **Problem**: Video-generation WAMs introduce substantial deployment cost. Existing latent WAMs either compress predictive representations or separate predictive modeling from action generation. No prior work has built a WAM directly inside a pretrained JEPA latent space where prediction and action share the same representation.
- **Architecture**: JEPA-WAM — (1) **Pretrained V-JEPA encoder** provides a frozen, semantically rich latent space free from pixel-level reconstruction pressure. (2) **Shared predictor**: a single predictor network simultaneously outputs (a) a spatially structured joint current-future target embedding for latent transition prediction, and (b) continuous action parameters (e.g., end-effector delta poses). (3) **Dual training objectives**: SIGReg/contrastive loss on the latent prediction (JEPA-style, no decoder) + behavior cloning / diffusion loss on the action head. (4) **Key innovation**: the shared predictor forces the latent transition dynamics and the action generation to be mutually informative — what the model predicts about the future directly constrains what actions it generates. (5) **Inference**: at deployment, no pixel generation needed — the model runs entirely in latent space, predicting future embeddings and outputting actions directly.
- **Compute Scale**: Mid (24G): Pretrained V-JEPA encoder (frozen) + lightweight shared predictor. Inference is extremely efficient since no decoder/generation is needed.
- **LeCun Alignment**: HIGH — This is arguably the most direct architectural implementation of LeCun's vision for WAMs to date. STRENGTHS: (1) Uses V-JEPA — Meta's flagship JEPA model — as the visual backbone, directly connecting to LeCun's research program. (2) The shared predictor that jointly models latent transitions AND action generation is exactly the "world model + actor" integration that LeCun's architecture describes. (3) Complete avoidance of pixel reconstruction/generation — the model lives entirely in latent space at both training and inference, making it both efficient and philosophically aligned. (4) The mutually informative prediction-action coupling through the shared predictor is a clean, elegant design that mirrors how biological systems might couple perception, prediction, and action. WEAKNESSES: (1) Uses a frozen V-JEPA encoder — doesn't explore whether end-to-end JEPA+WAM training could yield better task-specific representations. (2) The action space appears to be continuous end-effector control — doesn't address discrete action spaces or language-conditioned planning. (3) Not from LeCun's group directly, though clearly inspired by and built upon Meta's V-JEPA. Overall, JEPA-WAM is a landmark paper that demonstrates the practical viability of LeCun's vision: you can build efficient, effective robot policies entirely within a JEPA latent space without ever generating pixels. This should be cited as the canonical example of JEPA-based WAMs.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: JEPA-WAM — A latent WAM that operates entirely within a pretrained V-JEPA latent space, using a shared predictor to jointly model future-state transitions and generate robot actions.
- **Motivation**: Pixel-generation WAMs are expensive and philosophically misaligned with the goal of learning abstract world models. JEPA provides the right representational foundation — semantically rich, reconstruction-free — and WAMs should be built directly on top of it.
- **Problem Solved**: Demonstrates that a shared JEPA latent predictor can simultaneously serve as a world model (predicting future states) and a policy (generating actions), with both functions benefiting from the shared representation. Eliminates the need for pixel reconstruction entirely.

### Academic Context

- **Inheritance / Response**: Directly builds on V-JEPA (Meta FAIR, 2024/2025/2026) and the WAM paradigm. Responds to the growing realization that pixel-generation world models are computationally wasteful for control tasks.
- **Implicit Connection**: This paper operationalizes the concept from LeCun's "Path Towards Autonomous Machine Intelligence" where the world model and the actor share a common latent representation. The shared predictor is the architectural realization of this conceptual coupling.
- **Research Line**: JEPA + Embodied AI — the integration of self-supervised JEPA representations with action generation for robot control.
- **Future Directions**: End-to-end training (unfreeze V-JEPA for task-specific adaptation), language conditioning via text-aligned JEPA variants, multi-task and cross-embodiment JEPA-WAMs, integration with hierarchical planning.
- **GitHub**: Not found

---

## [2026-08-11] Energy-Structured Latent World Models with Neural Time Fields for Physically Consistent Open-World Motion Planning

- **arXiv**: [2608.09876](https://arxiv.org/abs/2608.09876)
- **Authors**: Yapeng Liu, Yuanzhao Zhai, Bo Ding, Huaimin Wang, Lin Wang
- **TL;DR**: Structures a latent world model's dynamics using a physical Hamiltonian (energy-based) formulation with neural time fields — producing physically consistent, reusable motion representations for open-world navigation.
- **Problem**: Existing latent world models learn unconstrained future representations where absorbed physics remains implicit. This prevents the formation of reusable physical knowledge and compromises reliability in open-world navigation where the agent encounters novel physical scenarios. The model has no explicit notion of energy conservation, momentum, or physical constraints.
- **Architecture**: Energy-Structured Latent World Model (ELWM) — (1) **Hamiltonian-inspired latent dynamics**: The world model's latent transition is structured as an energy-conserving system — position-like and momentum-like latent variables evolve according to Hamiltonian mechanics, enforced through a symplectic integrator. This is an ENERGY-BASED MODEL (EBM) applied to world model dynamics — directly connecting to LeCun's EBM research program. (2) **Neural Time Fields**: Instead of discretizing time into fixed steps (as in RNNs or fixed-horizon predictors), neural time fields parameterize continuous-time dynamics. The model can be queried at arbitrary time resolutions, enabling smooth, physically plausible interpolations. (3) **Physical consistency constraints**: The Hamiltonian structure ensures energy conservation, while additional constraints enforce momentum conservation and contact dynamics. These are NOT learned from data but baked into the architecture as inductive biases. (4) **Open-world planning**: The structured latent space enables Model Predictive Control (MPC) where the planner can trust that imagined trajectories respect physical laws — no physically impossible rollouts. (5) **Reusability**: Because the physical structure is explicit, the learned dynamics can be transferred to new environments with different visual appearances but identical physics.
- **Compute Scale**: Mid (24G): Energy-structured latent space + neural time fields. The Hamiltonian integrator adds minimal computational overhead compared to standard latent predictors.
- **LeCun Alignment**: HIGH — This paper simultaneously advances TWO of LeCun's core research programs: energy-based models AND world models. STRENGTHS: (1) The Hamiltonian energy structure is a direct implementation of EBM principles for world model dynamics — the model learns an energy function that governs state transitions, exactly as LeCun has advocated. (2) The explicit physical structure (energy conservation, symplectic integration) addresses the key critique that learned world models lack physical grounding — they predict visually plausible futures without obeying physical laws. (3) The continuous-time neural fields align with LeCun's view that world models should operate at multiple temporal scales, not just fixed discrete steps. (4) The reusability argument (transfer physics knowledge across environments) is central to LeCun's vision of world models as general physical reasoners. (5) Energy-structured architectures naturally support planning via energy minimization — the planner finds trajectories that minimize a cost function defined over the energy landscape. WEAKNESSES: (1) The Hamiltonian assumption (energy conservation) may not hold for all physical systems — friction, contact, and deformation dissipate energy. (2) The approach is demonstrated on navigation, not manipulation — the Hamiltonian structure may be harder to apply to contact-rich manipulation where energy is frequently dissipated. (3) Not directly using JEPA — the latent space is learned, not pre-trained. Overall, ELWM represents an important convergence of energy-based models and world models. The explicit physical structure addresses a fundamental weakness of learned world models and provides a principled path toward physically consistent, reusable world knowledge.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: ELWM — A latent world model whose dynamics are explicitly structured as a Hamiltonian (energy-conserving) system, with neural time fields for continuous-time prediction, producing physically consistent trajectories for open-world planning.
- **Motivation**: World models that don't explicitly encode physics will inevitably generate physically impossible predictions. The solution is to bake physical structure (energy conservation, continuous time) into the architecture as an inductive bias, rather than hoping the model discovers physics from data.
- **Problem Solved**: Demonstrates that energy-structured latent dynamics produce physically consistent rollouts (no energy creation/destruction, smooth continuous motion) that enable reliable MPC in open-world navigation. The explicit structure enables reuse of physical knowledge across visually different environments.

### Academic Context

- **Inheritance / Response**: Builds on Hamiltonian Neural Networks (HNNs), Neural ODEs, and latent world models (Dreamer, LeWM). Uniquely combines energy-based physical structure with latent world model training — HNNs typically operate in state space, not learned latent space.
- **Implicit Connection**: This is the world model counterpart to LeCun's EBM research. Just as EBMs learn energy functions for inference (pattern completion, generation), ELWM learns an energy function for dynamics (trajectory prediction, planning). The two research threads — EBMs and world models — converge naturally in this formulation.
- **Research Line**: Physically Structured World Models — architectures that enforce physical laws as inductive biases rather than learning objectives.
- **Future Directions**: Extending to dissipative systems (adding friction/contact energy terms), combining with JEPA latent spaces (use V-JEPA encoder + Hamiltonian latent dynamics), multi-object physical interactions, real-robot deployment with learned dynamics.
- **GitHub**: Not found

---

## [2026-08-11] SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation

- **arXiv**: [2608.09771](https://arxiv.org/abs/2608.09771)
- **Authors**: Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou
- **TL;DR**: A compact 0.5B-parameter Self-supervised Latent Interaction Model (SLIM) that learns action-grounded predictive latents for robot manipulation — avoiding both heavy VLM backbones and pixel-level reconstruction.
- **Problem**: VLA policies use large multimodal backbones (7B+ parameters) where most capacity supports open-domain semantics irrelevant to continuous robot manipulation. Conversely, pixel-level world models predict visual details irrelevant to control. The field needs a compact model that learns ONLY what matters for manipulation: how actions change the world state.
- **Architecture**: SLIM (Self-supervised Latent Interaction Model) — (1) **Compact 0.5B architecture**: deliberately small — proves that manipulation doesn't need open-domain VLMs. (2) **Self-supervised latent interaction learning**: the model learns to predict how actions transform observations in a compact latent space. No pixel reconstruction — the training signal comes from latent prediction consistency (JEPA-aligned). (3) **Action-grounded prediction**: the predictor takes (latent_current, action) → latent_future. The action is directly embedded in the same latent space, so the model learns action-conditioned dynamics without needing language mediation. (4) **Two-stage training**: (a) SSL pretraining on diverse robot interaction data to learn general action-grounded dynamics; (b) task-specific finetuning for policy learning. (5) **Results**: competitive with much larger models on standard manipulation benchmarks despite being 10-20× smaller.
- **Compute Scale**: Small-Mid (8-24G): 0.5B parameters — trainable and deployable on a single consumer GPU. Inference latency is extremely low.
- **LeCun Alignment**: MEDIUM-HIGH — SLIM embodies the JEPA philosophy of "predict in latent space, not pixel space" for robot manipulation. STRENGTHS: (1) The action-grounded latent prediction is architecturally similar to JEPA: predict future latent states conditioned on actions, without reconstructing observations. (2) The deliberate compactness (0.5B) aligns with LeCun's view that world models should be efficient — the heavy lifting should be in the representation, not in brute-force scale. (3) The separation of SSL pretraining (learning dynamics) from task finetuning (learning policy) mirrors the JEPA research program: learn general world knowledge first, then adapt to specific tasks. (4) Avoids both VLM bloat and pixel reconstruction — the two main targets of LeCun's critique. WEAKNESSES: (1) Does not explicitly use JEPA architecture or training objectives — the similarity is philosophical, not architectural. (2) The latent space is learned from scratch rather than using pretrained JEPA features — misses the opportunity to leverage JEPA's semantic richness. (3) Focused on manipulation only — doesn't demonstrate the kind of general world knowledge that JEPA aims for. Overall, SLIM demonstrates that the "predict in latent space" approach works at surprising small scales for manipulation — providing empirical support for the efficiency claims of the JEPA research program.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: SLIM — A 0.5B-parameter model that learns action-grounded predictive latents for robot manipulation through self-supervised latent interaction modeling, proving that compact latent prediction beats large VLM backbones for continuous control.
- **Motivation**: Current VLA models are wildly overparameterized for manipulation — they carry the burden of open-domain visual and language understanding when all the robot needs is to know how its actions change the world. A focused, compact model should work better and be vastly more efficient.
- **Problem Solved**: Demonstrates that a 0.5B model trained on action-grounded latent prediction can match or exceed 7B+ VLA models on manipulation benchmarks, while being 10-20× smaller and running on a single GPU. The key insight is that predicting action effects in latent space is a more appropriate objective than multimodal language-vision alignment for continuous control.

### Academic Context

- **Inheritance / Response**: Responds to the VLA scaling trend (RT-2, Octo, OpenVLA) by showing that bigger multimodal models aren't necessary for manipulation. Builds on latent action models (LAMs) and predictive world models. The "action-grounded prediction" objective is spiritually aligned with JEPA.
- **Implicit Connection**: SLIM provides empirical evidence for a key claim of the JEPA program: you don't need to reconstruct pixels or align with language to build effective world models for action. The latent prediction objective is sufficient, and it's dramatically more efficient.
- **Research Line**: Efficient Robot Learning — compact models for manipulation that don't require massive multimodal pretraining.
- **Future Directions**: Combining SLIM's action-grounded latents with JEPA pretrained features (use V-JEPA as the visual encoder, SLIM-style predictor for action-conditioned dynamics), multi-task and cross-embodiment SLIM, language-conditioned SLIM via lightweight text encoders.
- **GitHub**: Not found

---

## [2026-08-11] 4D-WAM: Infusing Spatiotemporal Awareness into World Action Models through Trajectory Fields

- **arXiv**: [2608.08023](https://arxiv.org/abs/2608.08023)
- **Authors**: Lishan Yang, Wenxuan Song, Xi Wang, Pingyue Sheng, Zheng Fang, Ziyang Zhou, Junjie He, Haodong Yan, Jiayi Chen, Nan Sun
- **TL;DR**: A model-agnostic training strategy that injects 3D spatiotemporal knowledge from trajectory fields into WAMs through representation alignment — bridging the gap between 2D video prediction and 3D action execution.
- **Problem**: WAMs jointly model video prediction and action generation, but represent videos in 2D pixel space while actions are executed in 3D space. This representation gap means the model never truly understands the 3D geometry of the scene. Recent 3D-aware approaches add 3D information but fail to exploit 3D dynamics (how objects move through space over time).
- **Architecture**: 4D-WAM — (1) **Trajectory field extraction**: From demonstration data, extract dense 3D point trajectories over time (4D = 3D + time) using off-the-shelf point tracking. These trajectory fields capture how every visible surface point moves through 3D space. (2) **Two complementary alignment objectives**: (a) Spatial alignment: the WAM's internal features should be predictive of 3D point positions — a lightweight probe head predicts trajectory points from latent features. (b) Temporal alignment: the WAM's predicted future features should be consistent with the actual 3D motion — a temporal consistency loss enforces that predicted latent changes correspond to actual 3D displacements. (3) **Model-agnostic**: 4D-WAM is a training strategy, not a specific architecture — it can be applied to any existing WAM (pixel-based or latent). (4) **Training only**: the trajectory field alignment is used only during training — at inference, the WAM runs normally without 3D overhead. The model internalizes 3D spatiotemporal knowledge into its representations.
- **Compute Scale**: Mid (24G): Standard WAM backbone + trajectory field alignment objectives. Training adds moderate overhead (point tracking + probe heads); inference is unchanged.
- **LeCun Alignment**: MEDIUM-HIGH — Addresses a key architectural concern: the 2D/3D gap in world models. STRENGTHS: (1) The training-only 3D alignment (no inference overhead) is elegant — the model internalizes 3D structure without paying for it at deployment. This aligns with LeCun's view that world models should learn physical structure that transfers to efficient inference. (2) The trajectory field approach provides dense 3D supervision without requiring explicit 3D reconstruction — consistent with JEPA's philosophy of avoiding pixel reconstruction. (3) The model-agnostic design means it could be applied to JEPA-based WAMs (like JEPA-WAM) to add 3D awareness to latent prediction. WEAKNESSES: (1) Still operates primarily in pixel space for the base WAM — doesn't address the fundamental critique of pixel-based world models. (2) The 3D alignment relies on external point trackers — the 3D knowledge is injected, not discovered. (3) Evaluated on video prediction quality, not necessarily on improved action generation. Overall, 4D-WAM provides a practical bridge between 2D WAM architectures and 3D physical understanding — the training-only injection of 3D knowledge is a pattern that could be valuable for JEPA-based systems as well.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: 4D-WAM — Inject 3D spatiotemporal knowledge into WAMs during training via trajectory field alignment, so the model internalizes 3D geometry without any inference-time overhead.
- **Motivation**: The 2D pixel space that WAMs operate in is fundamentally disconnected from the 3D space where robots act. The model needs to understand 3D structure to make accurate action predictions, but shouldn't need to explicitly reconstruct 3D at inference time.
- **Problem Solved**: Demonstrates that training-time 3D alignment improves WAM video prediction quality and action accuracy without adding inference cost. The model learns to "think in 3D" while operating in 2D.

### Academic Context

- **Inheritance / Response**: Builds on point tracking (TAPIR, CoTracker), WAM architectures, and 3D-aware video models. The training-only alignment approach is inspired by knowledge distillation but applied to geometric structure rather than model outputs.
- **Implicit Connection**: The trajectory field approach — dense 3D motion supervision without explicit 3D reconstruction — is philosophically aligned with JEPA's "predict in latent space" approach. Both seek to inject structure (3D for 4D-WAM, semantics for JEPA) without forcing the model to generate high-dimensional outputs.
- **Research Line**: 3D-Aware World Models — bridging the 2D/3D gap in video prediction and action generation.
- **Future Directions**: Applying 4D-WAM training to JEPA-WAM (combine JEPA latent prediction with 3D trajectory alignment), using 4D-WAM's trajectory fields as a self-supervised signal (no external tracker needed), extending to deformable objects and multi-object scenes.
- **GitHub**: Not found

---

## [2026-08-11] HarnessWAM: Bridging Prediction and Deliberation in World Action Models

- **arXiv**: [2608.09516](https://arxiv.org/abs/2608.09516)
- **Authors**: Zhaopeng Gu, Bingke Zhu, Tianxi Lin, Guibo Zhu, Yingying Chen, Kai Wang, Tingyu Yuan, Chaoyang Zhao, Zhaowen Li, Peng Su
- **TL;DR**: An agentic framework that wraps a WAM with a VLM-based Task Manager, scene graph memory, and planning/verification/recovery loops — bridging the gap between short-horizon WAM prediction and long-horizon task deliberation.
- **Problem**: WAMs predict actions and future states over finite horizons, but complex embodied tasks require global planning, cross-stage state maintenance, execution verification, and failure recovery. WAMs alone lack the deliberative reasoning to handle these requirements — there's a "prediction-deliberation gap."
- **Architecture**: HarnessWAM — (1) **WAM Core**: any existing WAM (e.g., Fast-WAM, ω-0) that predicts actions and future states for short horizons. (2) **VLM-based Task Manager**: an LLM/VLM agent that maintains an evidence-grounded scene graph representing the current task state, past observations, and planned subgoals. The Task Manager decomposes high-level instructions into WAM-executable subgoals. (3) **Planning loop**: The Task Manager proposes a sequence of subgoals → WAM executes each subgoal → execution results are verified against expected outcomes → scene graph is updated → if verification fails, the Task Manager replans. (4) **Cross-stage memory**: The scene graph persists across WAM execution chunks, maintaining state information that would otherwise be lost between finite-horizon predictions. (5) **Recovery**: When execution fails, the Task Manager can identify the failure mode from the scene graph and propose recovery actions.
- **Compute Scale**: Large (40G+): WAM backbone + VLM Task Manager + scene graph maintenance. The VLM component dominates compute.
- **LeCun Alignment**: MEDIUM-HIGH — Addresses the "hierarchical planning" gap in LeCun's architecture. STRENGTHS: (1) The Task Manager + WAM decomposition mirrors LeCun's proposed agent architecture where a "configurator" module sets subgoals and the world model + actor execute them. HarnessWAM's Task Manager is a configurator. (2) The evidence-grounded scene graph is a form of working memory — a component LeCun's architecture requires for maintaining state across time. (3) The verification-and-recovery loop implements the kind of "deliberative reasoning" that LeCun argues separates intelligent agents from reactive policies. (4) The modular design (any WAM can be plugged in) aligns with LeCun's vision of composable agent components. WEAKNESSES: (1) The VLM-based Task Manager reintroduces the language-reliance that LeCun's vision tries to minimize — the configurator should operate on latent representations, not natural language. (2) The scene graph is symbolic — LeCun's vision favors learned, continuous representations. (3) The verification depends on the VLM's reasoning abilities, which can hallucinate. Overall, HarnessWAM demonstrates that the WAM prediction paradigm needs to be embedded within a larger deliberative framework for complex tasks — the WAM is a component, not a complete solution. This is consistent with LeCun's modular agent architecture, though the specific symbolic/VLM implementation diverges from his continuous, learned-representation preference.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: HarnessWAM — Embed a WAM within an agentic framework (Task Manager + scene graph + planning loop) to bridge the gap between short-horizon prediction and long-horizon deliberation.
- **Motivation**: WAMs predict actions for the next few seconds, but real tasks require reasoning about what to do over minutes and across multiple stages. The prediction capability needs to be harnessed by deliberative reasoning.
- **Problem Solved**: Demonstrates that adding a deliberative layer (Task Manager + scene graph) on top of a WAM significantly improves performance on long-horizon manipulation tasks by enabling planning, state maintenance, and recovery.

### Academic Context

- **Inheritance / Response**: Builds on the WAM paradigm and LLM/VLM agent literature. The Task Manager is essentially an LLM-based planner that uses the WAM as its action-execution module.
- **Implicit Connection**: HarnessWAM can be seen as a partial implementation of the hierarchical planning architecture that LeCun describes. The Task Manager is a symbolic/linguistic configurator; a more LeCun-aligned version would use a learned, continuous configurator operating in the same latent space as the WAM.
- **Research Line**: Agentic WAMs — embedding world-action models within larger deliberative reasoning frameworks.
- **Future Directions**: Replacing the VLM Task Manager with a learned, continuous configurator (JEPA-based hierarchical planner), end-to-end training of the Task Manager + WAM, multi-agent HarnessWAM for collaborative tasks.
- **GitHub**: Not found

---

## [2026-08-11] CausalNav: Reliability-Certified Causal World Models for Control under Physical-Parameter Shift

- **arXiv**: [2608.07809](https://arxiv.org/abs/2608.07809)
- **Authors**: Yiyao Zhang, Diksha Goel, Hussain Ahmad, Shixun Huang, Jun Shen
- **TL;DR**: A causal world model that certifies its own reliability at deployment time — only intervenes when its predictions are trustworthy, otherwise falls back to a safe policy.
- **Problem**: A world model is only useful if it changes what the agent does, and only safe if it declines to do so when it is wrong. Most world models lack both: they don't provide reliability certificates, and they don't have safety-preserving fallbacks when their predictions are unreliable.
- **Architecture**: CausalNav — (1) **Signed, action-conditioned transition graph**: the world model is a causal graph over identified state coordinates, where edges are signed (positive/negative effect) and conditioned on actions. This is a structured causal model, not a black-box neural network. (2) **Simulation-based advice**: at deployment, CausalNav simulates a small library of intervention sequences, converts their objective error into policy-logit advice (how much each action should be preferred/avoided). (3) **Three reliability gates**: the advice is only admitted if ALL three gates pass: (a) scale-free predictive-reliability certificate (quantifies how well the causal model fits recent observations), (b) policy-margin gate (advice must be sufficiently confident), (c) argmax-agreement gate (the advised action must be consistent with the base policy's top choice). (4) **Safe fallback**: if any gate fails, CausalNav falls back to a conservative base policy that doesn't use the world model — safety is preserved by declining to act on unreliable predictions.
- **Compute Scale**: Small-Mid (8-24G): Causal graph inference + simulation-based advice. The causal structure is lightweight; the main cost is the intervention simulation library.
- **LeCun Alignment**: MEDIUM-HIGH — Addresses the safety and reliability requirements that LeCun has identified as critical for deploying world models. STRENGTHS: (1) The causal, structured approach to world modeling aligns with LeCun's view that world models should learn causal relationships, not just correlations. (2) The reliability certification (model knows when it's wrong) is a practical implementation of the "uncertainty awareness" that LeCun argues is essential for safe deployment. (3) The fallback mechanism (decline to act when uncertain) is exactly the safe-operating-mode that autonomous systems need. (4) The signed causal graph provides interpretability — you can inspect WHY the model recommended an action. WEAKNESSES: (1) The causal graph requires identified state coordinates — doesn't scale to high-dimensional visual observations without a separate perception module. (2) The structured causal approach may be too rigid for complex, contact-rich dynamics. (3) Not JEPA-based — uses symbolic causal reasoning rather than learned latent representations. Overall, CausalNav demonstrates a crucial capability that most world model papers ignore: knowing when to trust the model and when to fall back. This reliability-awareness is essential for practical deployment and aligns with LeCun's safety-conscious approach to autonomous intelligence.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: CausalNav — A causal world model that certifies its own reliability before intervening, using three gates (predictive-reliability, policy-margin, argmax-agreement) and a safe fallback policy.
- **Motivation**: World models that are occasionally wrong can be worse than no world model at all if they confidently recommend dangerous actions. The model must know when it's unreliable and decline to act.
- **Problem Solved**: Demonstrates that reliability-certified world model advice improves control performance under physical-parameter shifts while maintaining safety through fallback — the model helps when it can and stays silent when it can't.

### Academic Context

- **Inheritance / Response**: Builds on causal inference, model-based RL safety, and uncertainty quantification. Uniquely combines causal structure with deployment-time reliability certification.
- **Implicit Connection**: The reliability-certification approach could be integrated with JEPA-based world models: use the JEPA prediction error as a reliability signal, and fall back to a safe policy when the error exceeds a threshold. The causal structure of CausalNav could inform how JEPA latents are organized.
- **Research Line**: Safe World Models — ensuring world model predictions don't cause harm when they're wrong.
- **Future Directions**: Integrating reliability certification with JEPA-based WAMs, extending to high-dimensional visual state spaces via learned causal representations, adaptive gating thresholds based on task criticality.
- **GitHub**: Not found

---

## [2026-08-11] WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation

- **arXiv**: [2608.09298](https://arxiv.org/abs/2608.09298)
- **Authors**: Peterson Co, Sicheng Hu, Chunxuan Jiao, Hongyang Cheng, Yulin Luo, Yijie Xu, Sixiang Chen, Zhongxia Zhao, Zihao Wang, DaFeng Chi
- **TL;DR**: A diagnostic benchmark that evaluates action-conditioned world models through observable simulator capabilities (reproducibility, controllability, prefiguration) — exposing that visual quality metrics don't correlate with simulator faithfulness.
- **Problem**: ACWMs are evaluated on visual quality or task outcomes, which confound visual generation ability with physical simulation fidelity. We need to test whether these models actually behave like simulators: can they produce the same outcome given the same actions? Can they produce different outcomes given different actions? Can their predictions inform action selection?
- **Architecture**: WorldSimProbe — (1) **Three simulator capabilities**: (a) Reproducibility: given the same initial state and action sequence, does the model produce consistent future predictions? Physical simulators are deterministic — ACWMs may not be. (b) Controllability: given different action sequences from the same initial state, do the predicted futures diverge appropriately? A faithful simulator should show action-dependent outcomes. (c) Prefiguration: do the model's predictions correlate with actual task outcomes? A useful simulator's predictions should indicate whether an action sequence will succeed. (2) **Benchmark design**: Controlled manipulation scenarios with ground-truth physics (simulated or real) where the correct simulator behavior is known. (3) **Multi-model evaluation**: Tests multiple ACWM architectures to identify common failure modes and architecture-specific weaknesses.
- **Compute Scale**: N/A (benchmark): Multiple ACWM architectures evaluated. The probe metrics are lightweight.
- **LeCun Alignment**: MEDIUM — Provides the evaluation framework needed to distinguish genuine world models from visual generators. STRENGTHS: (1) The three simulator capabilities directly test whether ACWMs have learned physics or just appearance — exactly the distinction LeCun emphasizes. (2) The finding that visual quality doesn't correlate with simulator faithfulness provides empirical support for LeCun's critique of pixel-generation world models. (3) The benchmark is designed to be architecture-agnostic — can evaluate both generative and JEPA-based world models. WEAKNESSES: (1) Doesn't propose a solution — purely diagnostic. (2) The benchmark scenarios may be too simple to expose subtle physical reasoning failures. (3) Not from LeCun's group. Overall, WorldSimProbe is a valuable contribution to the world model evaluation toolkit — it provides standardized tests for whether a model is actually a simulator or just a visual generator. Should be cited alongside GAUGE and XEWorld as part of the growing "world model evaluation" literature.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: WorldSimProbe — Evaluate ACWMs through three simulator capabilities (reproducibility, controllability, prefiguration) rather than visual quality, exposing the gap between looking like a simulator and being one.
- **Motivation**: The field calls these models "world simulators" but evaluates them as "video generators." We need evaluation protocols that test whether they actually simulate.
- **Problem Solved**: Establishes that current ACWMs have significant simulator faithfulness gaps — they generate plausible videos but don't consistently obey action-conditioned dynamics. Provides standardized protocols for testing simulator fidelity.

### Academic Context

- **Inheritance / Response**: Joins GAUGE, XEWorld, and the "Is Sora a World Simulator?" literature in critically evaluating what world models have actually learned. Provides complementary tests to GAUGE's physical-parameter approach.
- **Implicit Connection**: The reproducibility and controllability probes directly test the action-conditioning that is central to JEPA-WAM: does changing the action actually change the predicted future in a physically meaningful way? JEPA-based WAMs should perform better on these probes because they predict in a structured latent space rather than generating pixels.
- **Research Line**: World Model Evaluation — developing diagnostic probes for simulator faithfulness.
- **Future Directions**: Extending probes to JEPA-based world models, adding more complex multi-step causality tests, integrating with GAUGE's physical-parameter evaluation, real-world manipulation probes.
- **GitHub**: Not found

---

## [2026-08-06] XEWorld: Can Action-Conditioned World Models Generalize to Unseen Robot Embodiments?

- **arXiv**: [2608.05799](https://arxiv.org/abs/2608.05799)
- **Authors**: Yixiang Chen, Jiabing Yang, Yuan Xu, Qisen Ma, Keji He, Peiyan Li, Kai Wang, Ziheng He, Xiangnan Wu, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
- **TL;DR**: A controlled cross-embodiment testbed for world models that isolates embodiment rendering — exposing that current action-conditioned world models act as 2D visual pattern matchers governed by visual similarity, not physical kinematic understanding, and fail catastrophically on unseen robots.
- **Problem**: Action-conditioned world models are evaluated on training robots, but this fails to reveal whether they capture physical dynamics or merely memorize visual patterns. When deployed on a robot with different visual appearance (different embodiment) but identical physical dynamics, do world models generalize? The answer turns out to be a resounding NO — exposing a fundamental architectural limitation.
- **Architecture**: XEWorld — (1) **Controlled cross-embodiment testbed**: isolates embodiment rendering by evaluating held-out robots within physically identical scenes. The scene dynamics are identical — only the robot's visual appearance (kinematic structure) changes. (2) **Key findings**: Current models act primarily as 2D visual pattern matchers — generalization is governed by visual similarity between training and test embodiments, not by physical kinematic similarity. (3) **Critical failures**: Models struggle to translate abstract numeric joint actions into coherent visual trajectories, and fail to predict dynamic visual changes from static initial observations. (4) **Zero-shot cross-embodiment**: Successfully rendering an unseen embodiment zero-shot STRICTLY requires heavily grounded cues — specifically pixel-space actions and explicit spatial-temporal alignment. Without these, cross-embodiment performance collapses. (5) **Few-shot adaptation failure**: Even with few-shot finetuning on the new embodiment, the forced appearance recovery triggers catastrophic forgetting of seen embodiments. The model overwrites its dynamics knowledge with new visual patterns. (6) **Architectural bottleneck identified**: The root cause is the entanglement of visual appearance and underlying physical dynamics. Until world models can decouple "what it looks like" from "how it behaves," cross-embodiment generalization will fundamentally fail.
- **Compute Scale**: Mid (24G): Controlled cross-embodiment evaluation framework — evaluates existing world models on held-out embodiments.
- **LeCun Alignment**: HIGH — Provides direct empirical evidence for LeCun's core architectural argument. STRENGTHS: (1) The finding that current world models are 2D visual pattern matchers, not physics learners, is the most direct empirical validation of LeCun's critique of generative video world models. LeCun has consistently argued that pixel-level prediction entangles appearance with dynamics — XEWorld PROVES this entanglement causes cross-embodiment failure. (2) The decoupling requirement (appearance vs. dynamics) is exactly what JEPA architectures are designed for: predict in latent space where visual appearance is abstracted away, and let the action module handle embodiment-specific rendering. (3) The catastrophic forgetting finding (few-shot adaptation destroys prior dynamics knowledge) strongly supports the need for modular architectures where dynamics knowledge is preserved and only the embodiment interface is adapted. (4) The paper provides a clean, controlled experimental framework for testing a core claim of the JEPA research program. WEAKNESSES: (1) Only evaluates existing generative world models — doesn't test JEPA-based models that might fare better due to latent prediction. (2) The testbed is limited to visual rendering changes — doesn't test kinematic or dynamic differences between embodiments. (3) Not from LeCun's group. Overall, XEWorld is ESSENTIAL READING for the WAM community: it empirically demonstrates that the appearance-dynamics entanglement LeCun has warned about is not theoretical — it causes real, catastrophic failures in cross-embodiment transfer. This paper should motivate a shift toward JEPA-style latent prediction architectures.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: XEWorld — A controlled cross-embodiment testbed that holds scene dynamics constant while varying only the robot's visual appearance, isolating embodiment rendering as the sole variable.
- **Motivation**: World models that can't generalize across embodiments aren't learning physics — they're memorizing visual patterns. Cross-embodiment testing is the litmus test for whether a world model has learned abstract dynamics or superficial appearance.
- **Problem Solved**: Identifies the shared architectural bottleneck: visual appearance and physical dynamics are entangled in current world models. Zero-shot cross-embodiment requires pixel-space actions. Few-shot adaptation causes catastrophic forgetting. The decoupling of appearance from dynamics is identified as the necessary architectural innovation.

### Academic Context

- **Inheritance / Response**: Builds on the action-conditioned world model literature (GAIA-1, Genie, video world models) and provides the cross-embodiment evaluation that has been missing. Directly connects to the "Is Sora a World Simulator?" and "Sora and V-JEPA Have Not Learned The Complete Real World Model" critique literature.
- **Implicit Connection**: XEWorld provides the empirical ammunition for LeCun's architectural position. The paper doesn't propose a solution — it diagnoses the problem with surgical precision. The identified bottleneck (entanglement of appearance and dynamics) is exactly what JEPA's latent prediction is designed to solve. This paper should be cited by every JEPA/WAM paper as motivation for why latent prediction (not pixel generation) is necessary.
- **Research Line**: World Model Evaluation — rigorously testing what world models have actually learned vs. what they appear to have learned.
- **Future Directions**: Applying the XEWorld framework to JEPA-based world models (which should perform better due to latent prediction); extending to kinematic/dynamic embodiment differences (different arm lengths, joint configurations); developing decoupled architectures with explicit dynamics-appearance factorization.
- **GitHub**: Not found

---

## [2026-08-06] GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models

- **arXiv**: [2608.05948](https://arxiv.org/abs/2608.05948)
- **Authors**: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang
- **TL;DR**: A real-world-grounded diagnostic benchmark jointly evaluating numerical simulators AND generative video world models on their physical fidelity — revealing that video world models can produce trajectories with the correct equation form while getting the actual physics (acceleration, momentum transfer, oscillation timing) completely wrong.
- **Problem**: Existing evaluations of physical fidelity in simulators and world models are siloed (simulators vs. video models evaluated separately) and rely on perceptual similarity or human judgment — providing no insight into WHICH physical principles or parameters are violated. There is no unified benchmark that can say: "this model got the trajectory shape right but the gravitational constant wrong by 37%."
- **Architecture**: GAUGE — (1) **22 controlled task families**: rigid bodies, flexible cables, textiles, and volumetric deformable objects — each with ground-truth real-world trajectories, calibrated physical metadata, uncertainty annotations, and task-specific observables. (2) **Fundamental physical processes**: collision, friction, momentum transfer, oscillation, self-contact, and deformation across diverse materials and conditions. (3) **Dual evaluation**: 14 task families benchmark Isaac Sim, Genesis, and Newton simulators using generalized trajectory errors; 5 rigid-body tasks evaluate 6 image-to-video models on physical-law consistency and temporal stability of inferred parameters. (4) **Key simulator finding**: No uniformly faithful physics engine — largest discrepancies in impulsive contact, rapid textile motion, and volumetric deformation. (5) **Key video world model finding**: Video models can produce trajectories with the EXPECTED EQUATION FORM while recovering incorrect accelerations, momentum transfer, and oscillation timing. In other words: they look right but are physically wrong — they learn the visual statistics of physical motion without learning the actual physics.
- **Compute Scale**: N/A (benchmark): 6 image-to-video models + 3 physics engines evaluated on 22 task families.
- **LeCun Alignment**: HIGH — The most direct empirical validation of LeCun's "video generation ≠ world understanding" critique to date. STRENGTHS: (1) The core finding — video world models produce correct-looking trajectories with wrong physics — is EXACTLY LeCun's argument: generative models learn visual correlations, not causal physical laws. The model produces a bouncing ball trajectory that looks right but the acceleration due to gravity is wrong — it learned to draw bouncing balls, not to simulate gravity. (2) The measurement-grounded approach (real-world trajectories as ground truth) addresses the key weakness of previous evaluations that relied on human judgment or perceptual similarity. (3) The dual evaluation (simulators AND video models on the same tasks) provides a unified framework for comparing numerical and learned approaches to world modeling. (4) The finding that no simulator is uniformly faithful sets realistic expectations: even hand-crafted physics engines struggle with certain phenomena — we should expect learned world models to have domain-specific weaknesses too. WEAKNESSES: (1) Only evaluates video GENERATIVE world models — doesn't include JEPA-based models (which don't generate pixels, so can't be evaluated on visual fidelity). (2) The task families, while diverse, are still controlled laboratory conditions — real-world chaos may expose additional failure modes. (3) Large author list from industry (Huawei, etc.) — potential institutional bias toward simulators. Overall, GAUGE is a landmark benchmark that should become the standard for evaluating physical fidelity in world models. The "looks right but is physically wrong" finding should be cited by every paper arguing for JEPA over generative approaches.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: GAUGE — A unified, measurement-grounded benchmark for evaluating physical fidelity in BOTH numerical simulators and generative video world models, with real-world trajectories as ground truth and per-principle diagnostic metrics.
- **Motivation**: The field needs to know whether world models are learning physics or visual statistics. Current evaluations can't answer this because they conflate appearance quality with physical accuracy. GAUGE separates them: you can have great perceptual quality and terrible physics.
- **Problem Solved**: Establishes that video world models suffer from a "correct equation form, wrong parameters" failure mode — they learn the visual signature of physics without the causal structure. Identifies which physical phenomena (impulsive contact, rapid motion, deformation) are hardest for both simulators and learned models. Provides a standardized evaluation protocol.

### Academic Context

- **Inheritance / Response**: Builds on physics engine evaluation literature and video generation quality metrics. Uniquely bridges the simulator and learned model evaluation communities. Directly responds to the "Sora as a World Model" debate by providing EMPIRICAL evidence that generative models get physics wrong.
- **Implicit Connection**: GAUGE provides the evaluation framework that the JEPA community needs. JEPA models don't generate pixels, so existing visual-quality metrics can't evaluate them. GAUGE's physics-parameter-based evaluation (does the model recover the correct acceleration, momentum, oscillation timing?) can evaluate JEPA world models through their latent predictions decoded to physical observables. This is exactly the kind of evaluation that could demonstrate JEPA's advantage: JEPA should recover correct physics parameters even when it can't generate pretty pixels.
- **Research Line**: World Model Evaluation — developing diagnostic benchmarks that test what world models actually know about physics.
- **Future Directions**: Extending to JEPA-based world models (decode latents to physical observables for evaluation); adding more complex multi-object interactions; incorporating real-world robotic manipulation data as ground truth; using GAUGE as a training signal (physics-consistent world models).
- **GitHub**: Not found

---

## [2026-08-06] LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models

- **arXiv**: [2608.05706](https://arxiv.org/abs/2608.05706)
- **Authors**: Jiarui Yang, Jiale Zhange, Jiawei Li, Hang Guo, Wen Huang, Jinpeng Wang, Peidong Liu, Shu-Tao Xia
- **TL;DR**: Extends latent action models (LAMs) to 3D by learning multi-view invariant latent actions with geometric alignment constraints — the key innovation being a non-injective RGB-D reconstruction objective that PREVENTS future-frame appearance leakage, forcing the model to learn from motion cues with geometric significance rather than visual shortcuts.
- **Problem**: Latent action models (LAMs) learn action representations from unlabeled human videos in a self-supervised manner, avoiding expensive action annotations. However, most LAMs operate in 2D pixel space from single-view inputs. Simply adding multi-view videos to LAM training DOES NOT produce 3D-aware latent actions — the model finds shortcuts through future-frame appearance leakage and ignores cross-view geometric consistency. The challenge is to design LAM training that genuinely exploits multi-view geometry rather than circumventing it.
- **Architecture**: LAWM-3D — (1) **Multi-view invariant unified action tokenization**: learns latent actions that are consistent across camera viewpoints — the same physical movement should map to the same latent action regardless of which camera observes it. (2) **Geometric alignment constraint**: anchors intermediate encoder features to a pretrained 3D foundation model, explicitly providing cross-view geometric correspondences. This prevents the model from ignoring 3D structure by forcing internal features to align with known 3D geometry. (3) **Non-injective RGB-D joint reconstruction objective**: THE KEY INNOVATION. Standard reconstruction objectives allow the model to cheat by using future-frame appearance information (what the next frame LOOKS like) to predict actions, without learning actual motion dynamics. LAWM-3D's non-injective reconstruction prevents this shortcut — the model CANNOT uniquely recover the next frame from the latent action alone, forcing it to focus supervision on motion cues with geometric significance. This is JEPA-ALIGNED: the objective prevents pixel-level reconstruction from being the primary learning signal. (4) **Two-stage paradigm**: large-scale human video pretraining (learning 3D-aware latent actions from diverse human activities) followed by robot-specific finetuning (adapting the latent action space to the target robot embodiment). (5) **Results**: SOTA in generation quality, physical consistency, and generalization ability for world model-based control.
- **Compute Scale**: Mid (24G): Two-stage human video pretraining + robot finetuning. Geometric alignment adds modest overhead.
- **LeCun Alignment**: MEDIUM-HIGH — The non-injective reconstruction objective is directly JEPA-aligned. STRENGTHS: (1) The core design principle — preventing future-frame appearance from being the primary learning signal — is EXACTLY the motivation behind JEPA. JEPA predicts in latent space to avoid pixel reconstruction; LAWM-3D uses non-injective reconstruction to achieve the same goal. (2) The geometric alignment constraint explicitly injects 3D structure into the latent space — consistent with LeCun's view that world models should incorporate geometric and physical priors rather than learning everything from scratch. (3) The multi-view invariant action tokenization directly addresses the "appearance-dynamics entanglement" that XEWorld identified as the critical bottleneck. (4) The two-stage pretraining + finetuning paradigm mirrors the JEPA philosophy: learn general representations from diverse unlabeled data, then adapt to specific embodiments. WEAKNESSES: (1) Still uses reconstruction (RGB-D) as part of the objective — not purely latent prediction. (2) The geometric alignment relies on a pretrained 3D foundation model — the 3D structure is injected, not discovered. (3) Evaluated on video generation quality, which is not the JEPA evaluation paradigm. Overall, LAWM-3D is a bridge paper: it moves LAMs closer to JEPA by preventing appearance leakage and enforcing geometric consistency, while still operating partially in pixel space. The non-injective reconstruction trick is directly applicable to JEPA architectures.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: LAWM-3D — Multi-view invariant latent action tokenization + geometric alignment to 3D foundation model + non-injective RGB-D reconstruction that prevents future-frame appearance leakage. The three components are tightly coupled through a unified motivation: force LAMs to learn from 3D motion geometry, not 2D visual patterns.
- **Motivation**: Simply adding more camera views to LAM training doesn't produce 3D awareness — the model finds shortcuts through visual correlations. LAWM-3D systematically closes these shortcuts: multi-view invariance (no single-view cheating), geometric alignment (forced 3D consistency), non-injective reconstruction (no future-frame cheating).
- **Problem Solved**: Demonstrates that 3D-aware latent actions significantly improve world model generation quality, physical consistency, and cross-embodiment generalization. The non-injective reconstruction trick is a general technique for preventing appearance leakage in any prediction-based training objective.

### Academic Context

- **Inheritance / Response**: Builds on the latent action model (LAM) literature and the observation that naive multi-view LAMs fail. The non-injective reconstruction objective connects to the information bottleneck principle and the JEPA philosophy of avoiding reconstruction-based learning. The geometric alignment draws from 3D vision and multi-view geometry.
- **Implicit Connection**: LAWM-3D occupies the crucial middle ground between pixel-space LAMs and fully latent JEPA world models. The non-injective reconstruction trick demonstrates that you don't need to abandon reconstruction entirely — you just need to make it non-injective so the model can't cheat. This is a pragmatic lesson for the JEPA community: the goal is to prevent shortcuts, not to dogmatically avoid all reconstruction. The geometric alignment constraint also validates the importance of injecting physical/geometric priors into world models.
- **Research Line**: 3D-Aware Latent Actions — learning action representations that capture 3D motion geometry rather than 2D visual patterns.
- **Future Directions**: Fully reconstruction-free LAWM-3D (pure JEPA-style latent prediction); learned geometric priors (rather than pretrained 3D foundation model); combining with cross-embodiment XEWorld evaluation; extending to multi-object manipulation with 3D-aware object-centric latents.
- **GitHub**: Not found

---

## [2026-08-06] MASS: Multiplayer World Models with Authoritative Shared State

- **arXiv**: [2608.06257](https://arxiv.org/abs/2608.06257)
- **Authors**: Ziqi Cai, Siqi Yang, Yimu Wang, Zixian Gao, Yunheng Liu, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi
- **TL;DR**: Disentangles world dynamics (learned Logic Engine) from view rendering (learned Rendering Engine) in multi-agent environments — the Logic Engine advances a global authoritative typed state from joint actions as the sole recurrent memory, enabling consistent views for 1,024 concurrent players over 10,000 steps.
- **Problem**: Current video world models struggle in multiplayer environments because they entangle world state with view-dependent visual latents. This leads to three failures: (1) redundant compute — each agent's view is predicted separately even though they share the same underlying world; (2) view inconsistencies — different agents see incompatible versions of the same event; (3) poor scalability — the computational cost explodes with the number of agents, not with world complexity. The challenge is to separate "what happened" (world state) from "what it looks like" (view rendering), so that world dynamics are computed once and views are generated on demand.
- **Architecture**: MASS (Multiplayer world models with Authoritative Shared State) — (1) **Logic Engine**: a learned transition function that advances a global, authoritative typed state from joint actions. This is the world model — it predicts how the world evolves given all agents' actions. Crucially, it learns the transition function without any hand-written physics rules. The typed state (structured as typed entities and relations, not a monolithic vector) provides interpretable, factorized world state. (2) **Rendering Engine**: generates independent, consistent views for any requested camera on demand from the shared state. Different agents can request different viewpoints, and all views will be mutually consistent because they derive from the same authoritative state. (3) **Single recurrent memory**: the Logic Engine's state is the SOLE source of temporal memory — no per-view hidden states, no per-agent memory. This enforces the disentanglement: all temporal dynamics flow through the shared state. (4) **Inspiration**: multiplayer game architectures where a server maintains authoritative game state and clients render views locally. (5) **Scale**: 1,024 concurrent players for 10,000 recurrent steps — demonstrates that disentangling state from rendering dramatically improves scalability.
- **Compute Scale**: Large (40G+): 1,024-player multi-agent simulation with learned Logic Engine + Rendering Engine.
- **LeCun Alignment**: MEDIUM — Architecturally aligned in principle but uses generative rendering. STRENGTHS: (1) The Logic Engine / Rendering Engine separation is EXACTLY the kind of modular architecture LeCun envisions: a world model (Logic Engine) that predicts state transitions, and separate modules (Rendering Engine) that produce modality-specific outputs from that state. (2) The authoritative typed state is a concrete implementation of LeCun's "abstract representation of the world state" — it's structured, factorized, and serves as the single source of truth. (3) The disentanglement principle (state vs. view) validates a core JEPA insight: world dynamics should be modeled once, in a view-independent representation, not redundantly for each perspective. (4) The scalability result (1,024 players) demonstrates the practical benefit of disentanglement: when state and rendering are coupled, scaling to many agents is infeasible. WEAKNESSES: (1) The Rendering Engine generates pixels — this is the generative approach LeCun critiques. A JEPA-aligned version would decode the authoritative state into latent action representations, not pixels. (2) The typed state structure is pre-specified (similar to FactorJEPA's pre-specified factors) — the model doesn't learn what types of entities and relations exist. (3) Evaluated on multiplayer Snake — a relatively simple domain. Scaling to complex 3D environments remains open. Overall, MASS provides a compelling architectural template that bridges game engine design and learned world models. The authoritative shared state concept is directly applicable to JEPA architectures: the JEPA predictor could operate on a shared latent state, with separate "rendering" modules for different downstream tasks (action generation, planning, language description).
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: MASS — Separate world dynamics (Logic Engine) from view rendering (Rendering Engine) with an authoritative typed state as the sole recurrent memory. Inspired by multiplayer game architectures where a server maintains game state and clients render views.
- **Motivation**: Multi-agent world modeling is currently infeasible because state and rendering are entangled — each agent redundantly predicts the same world. Disentangling them enables: (1) compute scales with world complexity, not agent count; (2) all views are mutually consistent; (3) the world model can be evaluated independently of rendering quality.
- **Problem Solved**: Achieves superior state accuracy and lower cross-view inconsistency compared to multi-view baselines. Scales to 1,024 players for 10,000 steps — demonstrating that explicit authoritative state modeling provides a practical foundation for scalable multi-agent world simulation.

### Academic Context

- **Inheritance / Response**: Builds on video world models and multi-view learning. The game-engine-inspired architecture (authoritative server + client rendering) is novel in learned world models. Connects to the entity-centric and object-centric world model literature.
- **Implicit Connection**: MASS validates the disentanglement principle that underlies JEPA: world dynamics should be modeled independently of how they're observed or rendered. The Logic Engine is essentially a JEPA-style predictor operating on a structured latent state. The key contribution is demonstrating that this disentanglement is not just philosophically appealing but PRACTICALLY NECESSARY for multi-agent scalability. Future JEPA architectures for multi-agent systems should adopt the authoritative shared state concept.
- **Research Line**: Multi-Agent World Models — scaling learned world models to many interacting agents through architectural disentanglement.
- **Future Directions**: JEPA-style Logic Engine (predicting latent state transitions, not generating pixels); learned entity types and relations (not pre-specified); scaling to photorealistic 3D multi-agent environments; combining with FactorJEPA's factorized prediction channels; using the authoritative state for centralized multi-agent planning.
- **GitHub**: Not found

---

## [2026-08-06] PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models

- **arXiv**: [2608.05720](https://arxiv.org/abs/2608.05720)
- **Authors**: Xi Zeng, Haojie Ren, Ziying Song
- **TL;DR**: Identifies three specific failure modes in JEPA world models (physical invariance collapse, physical identifiability collapse, counterfactual dynamics collapse) and proposes three targeted training pathways to fix them — demonstrating that preventing global latent collapse is not enough for reliable JEPA world models.
- **Problem**: JEPA world models prevent representational collapse through objectives like SIGReg or variance regularization, but a non-collapsed latent space does NOT guarantee that the representation preserves physically meaningful states and action consequences. The model may learn a latent space that is varied but physically incoherent — where different physical states map to nearby latents, or where action consequences are not properly encoded. This means downstream planning/MPC fails even when the representation "looks" good by standard metrics.
- **Architecture**: PhyLatent — (1) **Three failure mode taxonomy**: Physical Invariance Collapse (PIC: different physical states map to indistinguishable latents), Physical Identifiability Collapse (PIDC: action consequences are ambiguous/entangled), Counterfactual Dynamics Collapse (CDC: model cannot represent "what if" scenarios). (2) **Three training pathways**: Physical Invariance (physical state grounding + static visual invariance), Physical Identifiability (future representation alignment across action sequences), Counterfactual Dynamics (separated counterfactual branches + latent denoising). (3) **Implementation**: augmentations on a standard JEPA encoder-predictor backbone with additional regularization objectives and auxiliary heads. (4) **Results**: OGBench-Cube: PIC 15.60→7.53%, PIDC 6.71→0.95%, CDC 8.41→4.62%; MPC success 70.0→78.1%. TwoRooms: 81.0→98.0%. Competitive on Reacher and PushT.
- **Compute Scale**: Mid (24G): Standard JEPA backbone (comparable to LeWM) + physics-aware training objectives with marginal overhead.
- **LeCun Alignment**: HIGH — Directly addresses a critical reliability gap in JEPA world models. STRENGTHS: (1) The taxonomy of failure modes provides a diagnostic framework for evaluating whether JEPA world models actually learn useful representations — going beyond "no collapse" to "physically coherent." (2) The counterfactual dynamics pathway is essential for planning — LeCun's vision explicitly requires world models that can answer "what if" questions, not just predict the most likely future. (3) The massive TwoRooms improvement (81→98%) demonstrates that physical coherence directly translates to planning success — validating the core premise of JEPA-based planning. (4) Operates purely in latent space, consistent with JEPA's reconstruction-free philosophy. WEAKNESSES: (1) Only tested on state-based environments (not visual/pixel-space) — scaling to image/video JEPA remains open. (2) The three failure modes are defined manually — ideally they would be discovered automatically. (3) Not from LeCun's group directly — independent validation of the JEPA paradigm. Overall, PhyLatent is essential reading for anyone building JEPA world models: it shows that preventing collapse is necessary but far from sufficient, and provides concrete remedies.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: PhyLatent — Three training objectives (physical invariance, physical identifiability, counterfactual dynamics) that ensure JEPA world model representations are not just non-collapsed but physically meaningful.
- **Motivation**: Standard JEPA regularization prevents collapsed representations but doesn't guarantee that the latent space encodes physical state transitions and action consequences. The result: great-looking representations that fail at planning. PhyLatent bridges this gap by directly optimizing for physical coherence.
- **Problem Solved**: 47-86% reduction in physical failure modes on OGBench-Cube; 8.1pp MPC improvement; 17pp improvement on TwoRooms. All with the same backbone architecture and planner — the gains come purely from better representation learning objectives.

### Academic Context

- **Inheritance / Response**: Builds on JEPA world model literature (LeWM, JEPA-WMs paper, V-JEPA-2-AC). Extends the theoretical understanding of JEPA collapse beyond global variance collapse to specific physical-semantic failure modes.
- **Implicit Connection**: This paper provides the diagnostic toolkit that the JEPA community has been missing. When a JEPA world model fails at planning, PhyLatent tells you WHY (which of the three collapse modes is the culprit) and HOW to fix it. This is directly useful for LeCun's long-term vision of reliable autonomous systems built on JEPA world models.
- **Research Line**: JEPA Reliability — ensuring JEPA representations are not just diverse but physically faithful.
- **Future Directions**: Scaling to visual/image domains; automatic discovery of failure modes rather than manual specification; integration with symbolic dynamics (SJEPA-style) for physics-grounded latent spaces.
- **GitHub**: Not found

---

## [2026-08-06] ω-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation

- **arXiv**: [2608.06375](https://arxiv.org/abs/2608.06375)
- **Authors**: Zhe Li, Zhenzhe Zhang, Yangyang Wei, Wenjie Zhang, Xichen Yuan, Peiyuan Zhi, Gen Li, Xinying Guo, Fengjie Gao, Jianfei Yang, Shanghang Zhang
- **TL;DR**: A latent predictive whole-body world-action model for real-world humanoid robots performing concurrent locomotion + manipulation — learns compact future observation embeddings instead of reconstructing pixels, coupling latent visual foresight with diffusion-based action generation.
- **Problem**: Humanoid household tasks require simultaneous locomotion and manipulation (loco-manipulation) — e.g., walking to a table while carrying an object, then placing it. Existing approaches either decompose the problem (separate walking + arm policies, leading to coordination failures) or use WAMs limited to tabletop manipulation (arm-centric) or video generation (computationally wasteful). No existing WAM handles whole-body humanoid control with real-world deployment.
- **Architecture**: ω-0 — (1) **Latent predictive objective**: rather than generating future video frames, predicts compact future observation embeddings — a lightweight alternative that captures task-relevant state changes without pixel-level reconstruction. (2) **Diffusion-based whole-body action generation**: action latents are decoded into controller-compatible joint commands via a diffusion process conditioned on the predicted latent future + language instruction + current proprioception. (3) **Multi-view input**: supports egocentric RGB, exocentric RGB, and exocentric depth inputs for robust state estimation. (4) **Controller-based simulation replay**: bridges sim-to-real gap by grounding publicly available visual-motion priors into robot-executable action latents through controller replay in simulation. (5) **ω-HOME dataset**: 40+ hours of real-world household humanoid data with synchronized multi-view observations — a significant contribution to the data-scarce humanoid domain.
- **Compute Scale**: Mid-Large (24-40G+): Multi-view encoder + latent predictor + diffusion action head. Training on humanoid-scale data with multi-view input requires substantial GPU memory but inference can be optimized.
- **LeCun Alignment**: HIGH — This is the closest realization of LeCun's WAM vision for full-body humanoid control seen to date. STRENGTHS: (1) Explicitly avoids pixel reconstruction — the core JEPA principle — using compact future observation embeddings as the predictive target. (2) Handles the full perception→prediction→action pipeline: multi-view sensing → latent world prediction → whole-body action. This is exactly the modular architecture LeCun describes. (3) Real-world deployment on humanoid hardware demonstrates that latent predictive WAMs work beyond simulation — a critical proof point. (4) The ω-HOME dataset advances the field by providing real humanoid data, addressing a major bottleneck. WEAKNESSES: (1) The action head uses diffusion, which while effective is computationally intensive — future work could use more efficient action generation. (2) The latent predictor is relatively simple — doesn't incorporate hierarchical or multi-scale prediction that LeCun's full architecture envisions. (3) Not from LeCun's group — independent validation of the WAM paradigm. Overall, ω-0 is a landmark paper showing that latent predictive WAMs can control real humanoid robots performing complex whole-body tasks — a compelling validation of the JEPA/WAM approach.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: ω-0 — Instead of generating video or decomposing locomotion/manipulation, predict latent future observation embeddings and decode them into whole-body actions via diffusion. Train on real humanoid data (ω-HOME) and deploy on real hardware.
- **Motivation**: Humanoid robots need coordinated whole-body control for household tasks. Pixel-level video generation wastes capacity on irrelevant details. Decomposed policies fail at coordination. Latent prediction + whole-body action generation solves both problems.
- **Problem Solved**: First latent predictive WAM for real-world humanoid loco-manipulation. Demonstrates that JEPA-style future-embedding prediction (not pixel generation) is sufficient for complex whole-body control on real hardware.

### Academic Context

- **Inheritance / Response**: Builds on the WAM paradigm (Fast-WAM, LeapBot-WA, LiLa-WAM) and extends it to humanoid whole-body control. The latent predictive objective is directly inspired by JEPA. The diffusion action head follows recent work on diffusion policies for robotics.
- **Implicit Connection**: ω-0 validates the central claim of LeCun's WAM vision: that effective action can be generated from latent predictions without requiring pixel-level reconstruction. The real-world deployment is the strongest evidence yet that JEPA-style world models scale to complex embodied tasks.
- **Research Line**: Embodied WAM — deploying world-action models on complex physical robots.
- **Future Directions**: Hierarchical prediction (coarse body plan → fine joint control); more efficient action generation (consistency models, flow matching); multi-robot coordination; longer-horizon household task chains.
- **GitHub**: Not found

---

## [2026-08-06] DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation

- **arXiv**: [2608.06374](https://arxiv.org/abs/2608.06374)
- **Authors**: Junfeng Li, Junjie He, Zhide Zhong, Yangyang Zheng, Pingyue Sheng, Jiayu Dong, Ruixin Li, Haodong Yan, Jiaguan Zhu, Tianran Zhang, Runze Yu, Wen Chen, Liuqing Yang, Yuxiang Gao, Haoang Li
- **TL;DR**: Cross-embodiment VLA that learns shared dynamics priors via a future-prediction objective on the VLM backbone, with embodiment-specific Mixture-of-Experts action heads — enabling a single model to control diverse robot embodiments without manual action space realignment.
- **Problem**: Training one VLA policy for multiple robot embodiments is hard because (1) shared dynamics (object motion, contact, scene changes) are underexploited across embodiments, and (2) different robots have incompatible action spaces requiring expensive manual preprocessing to unify. Existing cross-embodiment methods either ignore shared dynamics or rely on hand-crafted action space alignments.
- **Architecture**: DyPES-VLA — (1) **Shared Dynamics Priors**: the VLM backbone is trained with a future-prediction objective on cross-embodiment interaction data. This forces the shared query representation to capture embodiment-agnostic dynamics: object motion, contact events, and interaction-induced scene changes. The future-prediction objective is JEPA-aligned: predict what changes in the scene, not reconstruct pixels. (2) **Embodiment-Specific Mixture-of-Experts (MoE)**: each robot embodiment gets its own MoE action head that translates shared dynamics priors into native-space control commands. Shared attention layers capture common temporal patterns across embodiments while expert-specific layers handle embodiment-unique kinematics. (3) **No manual realignment**: the MoE heads learn to map from shared dynamics to embodiment actions directly — no need to pre-align different action spaces into a common format.
- **Compute Scale**: Large (40G+): Full VLM backbone with future-prediction training + multiple MoE action heads. Scaling to many embodiments increases expert count and memory.
- **LeCun Alignment**: MEDIUM — Interesting predictive dynamics approach within the VLA paradigm. STRENGTHS: (1) The future-prediction objective for learning shared dynamics is JEPA-aligned: predict what changes (dynamics) rather than reconstruct everything. (2) The decoupling of shared dynamics from embodiment-specific action is consistent with LeCun's modular architecture — world model (shared) vs. action module (embodiment-specific). (3) The cross-embodiment generalization addresses a key scalability requirement for autonomous intelligence. WEAKNESSES: (1) Still fundamentally a VLA/policy model, not a world model — doesn't support planning or counterfactual reasoning. (2) The future-prediction is on the VLM representation, not a dedicated world model latent space. (3) The architecture is complex (VLM + MoE) and compute-heavy. Overall, DyPES-VLA demonstrates that JEPA-style predictive objectives are useful even within the VLA paradigm — a bridge between policy learning and world modeling.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: DyPES-VLA — Learn shared dynamics priors through future prediction on cross-embodiment data, then use embodiment-specific MoE heads to translate these priors into native actions without manual realignment.
- **Motivation**: Different robots share underlying physics (objects fall, contacts cause motion) but have different ways of acting. A good cross-embodiment model should learn the shared dynamics once and specialize only the action interface — exactly what DyPES-VLA does.
- **Problem Solved**: Enables a single VLA model to control multiple robot embodiments by learning shared dynamics priors and embodiment-specific action heads. The future-prediction objective forces the model to understand what changes during interaction, improving cross-embodiment transfer.

### Academic Context

- **Inheritance / Response**: Builds on cross-embodiment VLA literature and the observation that JEPA-style predictive objectives improve representation learning for embodied tasks.
- **Implicit Connection**: The explicit separation of shared dynamics (world) from embodiment-specific action (actor) mirrors LeCun's modular agent architecture. While not a full world model, DyPES-VLA validates that predictive objectives help learn better dynamics representations even in policy-focused models.
- **Research Line**: Predictive VLAs — incorporating world-model-style objectives into policy learning.
- **Future Directions**: Extending from future-prediction to full planning; supporting novel embodiments not seen during training; reducing compute requirements for multi-embodiment training.
- **GitHub**: Not found

---

## [2026-08-06] GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions

- **arXiv**: [2608.06332](https://arxiv.org/abs/2608.06332)
- **Authors**: Chenghao Gu, Hanyang Yu, Jingbo Zhang, Haitao Lin, Wenyao Zhang, Jinghe Wang, Hanglei Jin, Shuzhao Xie, Jingyan Jiang, Zhi Wang
- **TL;DR**: Interactive world model using URDF-based visual actions (robot skeleton rendered onto video frames) for spatially grounded action control — decouples embodiment kinematics from environment dynamics, enabling zero-shot OOD generalization and closed-loop human/robot interaction via autoregressive video prediction.
- **Problem**: Existing action-conditioned world models suffer from (1) limited action controllability — actions don't spatially ground to the scene, and (2) poor OOD generalization — models overfit to training scene layouts and fail when environments change. Scaling robot evaluation across diverse real-world environments remains costly and challenging.
- **Architecture**: GeniWorld — (1) **Visual action representation**: uses URDF-based rendering to overlay robot kinematic poses onto video frames. Instead of conditioning on abstract action vectors, the model sees a visual representation of the robot's intended configuration — enabling spatially grounded, physically interpretable action control. (2) **Embodiment-environment decoupling**: explicitly separates the robot's kinematic structure (URDF skeleton) from the environment's visual dynamics. The robot is rendered as a visual overlay, so the model learns that environment dynamics are independent of which robot embodiment is acting. This prevents the model from overfitting specific robot-scene combinations. (3) **Autoregressive video prediction backbone**: builds on pretrained video generative models for next-frame prediction, augmented with high-frequency (50Hz) robot kinematic control signals. The model predicts future frames conditioned on both visual history and rendered action representations. (4) **Closed-loop interaction**: supports bidirectional interaction — human teleoperators can provide action inputs that the world model visualizes, and robot policies can query the model for outcome prediction. (5) **Applications**: serves as a scalable policy evaluator (test policies in simulated varied environments without real deployment) and a data augmenter (generates diverse manipulation trajectories from limited real demonstrations).
- **Compute Scale**: Large (40G+): Builds on pretrained video generative models (likely diffusion-based) with autoregressive rollout. URDF rendering adds modest overhead but the video generation backbone dominates compute.
- **LeCun Alignment**: LOW-MEDIUM — Directly uses pixel-level autoregressive video generation, which LeCun explicitly argues is inefficient and unnecessary for world models. STRENGTHS: (1) The embodiment-environment decoupling is architecturally aligned with LeCun's modular agent design — the world model should understand environment dynamics independently of the agent's specific form. (2) The visual action representation is an interesting bridge between abstract actions and pixel-space prediction — making actions spatially meaningful without full reconstruction objectives. (3) The closed-loop interactive capability (human-in-the-loop, policy evaluation) addresses practical world model requirements. WEAKNESSES: (1) Core prediction mechanism is pixel-level autoregressive generation — exactly the approach LeCun critiques as wasteful ("predicting every irrelevant detail"). (2) No latent predictive architecture — doesn't use JEPA-style encoder/predictor/target structure. (3) Computationally expensive (large video generative model) — violates LeCun's emphasis on efficient, non-generative world models. Overall, GeniWorld is a practical engineering contribution to the world model ecosystem that validates the importance of embodiment-dynamics decoupling, but its core approach (autoregressive pixel prediction) is architecturally at odds with LeCun's vision. It serves as a useful counterpoint: what does a generative approach get right (interactivity, generalization) vs. what JEPA approaches excel at (efficiency, latent reasoning).

- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: GeniWorld — Render robot actions as visual overlays (URDF skeletons) on video frames, then use autoregressive video prediction with embodiment-environment decoupling to achieve generalizable, interactive world models for robotic manipulation.
- **Motivation**: Abstract action vectors are difficult for world models to spatially ground. By converting actions into visual representations that show the robot's intended configuration, the model gains spatial understanding of action consequences. Decoupling embodiment from environment prevents the model from memorizing specific robot-scene combinations.
- **Problem Solved**: (1) Visual actions provide spatially grounded control — actions are rendered as physically meaningful robot poses rather than abstract numbers. (2) Embodiment-environment decoupling enables zero-shot generalization to highly randomized, unseen environments even when trained on limited fixed-scene data. (3) Closed-loop interaction enables both policy evaluation and human teleoperation within the world model.

### Academic Context

- **Inheritance / Response**: Builds on video generative world models and action-conditioned video prediction literature. The URDF-based visual action rendering is novel. Responds to the generalization limitations of existing world models (GAIA-1, Genie, etc.) by introducing embodiment-environment decoupling.
- **Implicit Connection**: While GeniWorld uses generative methods LeCun critiques, the embodiment-environment decoupling validates a key principle of LeCun's vision: the world model should be agent-agnostic. The paper's success with decoupled architectures (even in pixel space) suggests that JEPA-style latent world models would benefit even more from explicit embodiment factorization. The visual action representation also hints at a potential bridge: could JEPA predictors ingest visual action tokens rather than abstract action vectors?
- **Research Line**: Generative World Models — an alternative path to world modeling with strengths in interactivity and generalization, but at higher compute cost.
- **Future Directions**: Replace autoregressive pixel prediction with latent predictive architecture (JEPA-style) while keeping the visual action representation and embodiment decoupling; extend to multi-embodiment scenarios; integrate with policy learning for closed-loop training.
- **GitHub**: Not found

---

## [2026-08-03] LeDXA: Self-supervised DXA representations encode multi-system disease risk, biological aging and heritability

- **arXiv**: [2608.02208](https://arxiv.org/abs/2608.02208)
- **Authors**: Gil Sasson, Zachary Levine, Smadar Shilo, Sarah Kohn, Guy Lutsker, Anastasia Godneva, Adam Gabet, David Krongauz, Adina Weinberger, Yann LeCun, Randall Balestriero, Eran Segal
- **TL;DR**: LeCun & Balestriero co-authored JEPA-based SSL model for medical imaging (DXA body scans) — learns latent health representations without pixel reconstruction, outperforming DINOv3 with 150,000× fewer training images and 40× fewer parameters.
- **Problem**: DXA scans are routinely collected for bone density and body composition but their rich spatial structure is discarded — only a handful of tabular measurements are used clinically. Meanwhile, general-purpose vision models (DINOv3) require massive datasets and compute to learn useful representations. Can JEPA efficiently extract medical knowledge from limited unlabeled scan data?
- **Architecture**: LeDXA — (1) **JEPA backbone**: a vision model based on joint-embedding predictive architecture trained from scratch on only 11,540 unlabeled DXA scans. Learns by predicting latent representations of masked regions rather than reconstructing pixels — consistent with JEPA principles. (2) **Evaluation**: tested on 47,400 external UK Biobank scans for cross-cohort disease prediction, biomarker estimation, incident disease prediction over 4.3-year follow-up, and heritability analysis. (3) **Key result**: Outperforms DINOv3 (a SOTA general-purpose vision model) despite ~150,000× fewer training images and ~40× fewer parameters.
- **Compute Scale**: Small-Mid (8-24G): JEPA trained from scratch on ~11K medical images. Significantly more efficient than large-scale SSL approaches.
- **LeCun Alignment**: MEDIUM — LeCun co-author, uses JEPA architecture, but medical domain application rather than autonomous intelligence. STRENGTHS: (1) Direct validation of JEPA's data efficiency: 150K× fewer images than DINOv3 yet better performance — exactly the kind of efficient learning LeCun advocates. (2) LeCun co-author with Balestriero (Meta FAIR) — carries institutional weight. (3) Demonstrates JEPA's generality beyond robotics/video. WEAKNESSES: (1) Not about world models for planning or action — purely a representation learning application. (2) Medical imaging is a static domain — doesn't address temporal prediction or action-conditioned futures. Overall, valuable as a JEPA validation study showing data efficiency, but peripheral to the core world-model-for-autonomous-intelligence agenda.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: LeDXA — Apply JEPA-based SSL to DXA medical imaging to learn health-relevant representations that outperform general-purpose models with dramatically less data and compute.
- **Motivation**: Medical imaging data is expensive and privacy-constrained. JEPA's data efficiency (learning from prediction rather than reconstruction) makes it ideal for medical domains where massive unlabeled datasets aren't available.
- **Problem Solved**: 150K× data efficiency over DINOv3; better disease prediction and biomarker estimation; demonstrates JEPA's practical value in resource-constrained domains.

### Academic Context

- **Inheritance / Response**: Applies I-JEPA/V-JEPA principles to medical imaging. The LeCun & Balestriero co-authorship signals Meta FAIR's interest in JEPA for healthcare. 
- **Implicit Connection**: While not directly advancing world models for autonomous intelligence, LeDXA demonstrates JEPA's core value proposition — efficient learning from prediction without reconstruction — in a high-impact domain. The data efficiency result (150K× fewer images) is a powerful argument for JEPA over generative approaches.
- **Research Line**: JEPA Applications — extending JEPA beyond core world model research to domain-specific applications.
- **Future Directions**: Temporal JEPA for longitudinal medical imaging (disease progression prediction); action-conditioned JEPA for treatment planning; multi-modal JEPA combining imaging + genomics + clinical data.
- **GitHub**: Not found

---

## [2026-08-05] DreamWAM: Beyond RGB Future Prediction for World Action Models

- **arXiv**: [2608.04996](https://arxiv.org/abs/2608.04996)
- **Authors**: Shanglin Yuan, Weiheng Zhao, Xin Shi, Haoyi Jiang, Xianda Guo, Liu Liu, Wenyu Liu, Wei Sui, Xinggang Wang
- **TL;DR**: Reformulates WAM future prediction beyond RGB — jointly learning structured futures through appearance, motion, geometry, and semantics — with all beyond-RGB branches disabled at inference, achieving 74.4% real-world success (vs. 55.6% for Fast-WAM-Joint) with zero additional deployment cost.
- **Problem**: Most WAMs predict futures in RGB space, where task-relevant state transitions (object movement, gripper-object contact, spatial relationships) are entangled with nuisance variations in texture, illumination, and viewpoint. This entanglement means the model wastes capacity on predicting visual details irrelevant to action, and fails to generalize when visual conditions change (lighting, background) even if the underlying dynamics are identical. The challenge is to train WAMs to predict futures in a form that matters for action — not just what the world will *look* like, but how it will *behave*.
- **Architecture**: DreamWAM — (1) **Multi-view future prediction**: jointly predicts four complementary views of the future state: appearance (RGB), motion (optical flow), geometry (depth), and semantics (segmentation masks). Each view captures a different aspect of state relevant to manipulation. (2) **Gated residual branches**: lightweight decoder heads for geometry and semantics attach via gating mechanisms to the main video diffusion backbone — adding supervision signal during training without bloating the model. RGB and motion are handled via joint latent denoising in a shared space. (3) **Shared VideoDiT-ActionDiT attention**: the action prediction branch (ActionDiT) attends to future-state representations from the video branch (VideoDiT), allowing the action module to learn from the structured future predictions. (4) **Inference-mode**: all beyond-RGB branches are disabled — deployment uses only the standard RGB-only action model with zero additional cost. The structured supervision acts purely as a training signal. Evaluated on LIBERO (98.9%), LIBERO-Plus (63.4% → 75.5% with joint inference), RoboTwin 2.0, and real-world manipulation with lighting/background/layout perturbations.
- **Compute Scale**: Large (40G+): VideoDiT + ActionDiT with multi-modal supervision. Training overhead from auxiliary branches (disabled at inference); deployment is RGB-only.
- **LeCun Alignment**: MEDIUM-HIGH — Advances WAMs toward task-relevant prediction. STRENGTHS: (1) The core insight — predicting what matters for action rather than raw pixels — aligns with LeCun's emphasis on abstraction in world models. The structured futures (motion, geometry, semantics) are a step toward the kind of "abstract representation of the world state" LeCun advocates. (2) The training-only auxiliary branches (disabled at deployment) demonstrate that structured world knowledge can be distilled into action policies without runtime cost — efficiently transferring world understanding to action. (3) Dramatic improvement on real-world distribution shifts (74.4% vs 55.6%) validates the hypothesis that robust action requires understanding beyond surface appearance. WEAKNESSES: (1) Still uses generative diffusion backbone for video, not JEPA-style latent prediction. (2) The auxiliary views are hand-chosen (motion, depth, semantics) rather than learned — doesn't discover which abstractions matter. (3) The shared attention mechanism is still within the generative paradigm rather than the predictive architecture paradigm. Overall, DreamWAM makes a compelling empirical case that WAMs should predict structured futures beyond RGB — moving the field closer to LeCun's vision of world models that learn action-relevant abstractions, even if it does so within the generative framework rather than the predictive one.
- **GitHub**: [github.com/hustvl/DreamWAM](https://github.com/hustvl/DreamWAM)

### What / Why / Solve

- **Proposal**: DreamWAM — Replace RGB-only future prediction in WAMs with multi-view structured prediction (appearance, motion, geometry, semantics) during training. At deployment, only the action model runs — the structured supervision is a training-only signal that produces a more robust action policy.
- **Motivation**: RGB future frames entangle task-relevant dynamics with irrelevant visual details. By explicitly supervising the model to predict motion, depth, and semantics alongside RGB, the model learns representations that capture what actually changes during manipulation — and these representations transfer to the action model via shared attention. The result: robust action policies that work even when visual conditions change, because the model learned to focus on dynamics, not appearance.
- **Problem Solved**: 98.9% on LIBERO (no-rollout); 75.5% on LIBERO-Plus (joint inference, +6.3pp over baseline); 74.4% on real-world manipulation under distribution shift (vs. 55.6% for Fast-WAM-Joint). All gains come with zero additional inference cost — the auxiliary branches are training-only.

### Academic Context

- **Inheritance / Response**: Builds on Fast-WAM and the WAM paradigm. The multi-view prediction approach draws from multi-task learning and structured prediction literature. The key innovation is treating structured future prediction as a training-only auxiliary task — distillation through shared attention, not multi-task deployment.
- **Implicit Connection**: DreamWAM represents a pragmatic middle ground between generative WAMs (predict everything in RGB) and JEPA-style WAMs (predict only latent abstractions). By explicitly predicting motion, geometry, and semantics alongside RGB, DreamWAM effectively forces the model to extract action-relevant abstractions — but does so within the generative framework rather than switching to a predictive architecture. This is a bridge paper: it demonstrates empirically that structured prediction matters for WAM robustness, which motivates the next step of moving to purely latent (JEPA-style) prediction of these abstractions.
- **Research Line**: Structured WAM — enriching world-action models with auxiliary future-state prediction beyond RGB.
- **Future Directions**: Learned (rather than hand-specified) auxiliary views; JEPA-style latent prediction of motion/geometry/semantics rather than pixel-space prediction; combining with symbolic dynamics (SJEPA) for interpretable abstractions; extending to longer-horizon structured prediction.
- **GitHub**: [github.com/hustvl/DreamWAM](https://github.com/hustvl/DreamWAM)

---

## [2026-08-04] SJEPA: Learning Elegant Latent Dynamics with Hybrid Symbolic-Neural Predictors

- **arXiv**: [2608.04060](https://arxiv.org/abs/2608.04060)
- **Authors**: Yongchao Huang
- **TL;DR**: Introduces SJEPA, a JEPA framework with hybrid symbolic-neural transition predictors — the induced latent dynamics admit compact symbolic descriptions while neural corrections handle residual dynamics outside the selected grammar — formalizing the principle of "simplest adequate dynamics" and exposing a previously unknown collapse shortcut from unconstrained operator compression.
- **Problem**: JEPA models learn abstract states by predicting target embeddings from context embeddings, but their transition models (the predictor) are typically opaque neural networks. When the true underlying dynamics are simple (e.g., a pendulum following Newton's laws), a purely neural predictor may learn a complex, uninterpretable function that matches one-step predictions but fails on long-horizon rollouts and provides no insight into the physical laws governing the system. The challenge is to learn JEPA representations whose induced dynamics are simultaneously predictive and simple — discoverable as compact symbolic laws.
- **Architecture**: SJEPA — (1) **Hybrid symbolic-neural predictor**: the transition model combines a symbolic component (selected from a grammar of candidate equations, e.g., pendulum dynamics) with a regularized neural correction for dynamics outside the grammar's coverage. This enables parsimony when the world follows simple laws while retaining flexibility for residual complexity. (2) **Representation constraints**: prevent predictive-coordinate collapse by preserving informative, non-collapsed dimensions in the latent space — ensuring the representation retains structure from which symbolic dynamics can be extracted. (3) **Operator compression**: jointly minimizes predictive error and symbolic complexity, favoring simpler transitions that remain predictively adequate. (4) **Key theoretical finding**: unconstrained operator compression creates a direct shortcut to representation collapse — the model can satisfy the simplicity objective by collapsing the representation to a trivial state where everything is "predictable." This is a fundamental caution for any approach that jointly optimizes for representation quality and dynamics simplicity. (5) **Two learning modes**: alternating representation-equation learning (joint) and symbolic dynamics fitted to fixed representations (post-hoc). Experiments on controlled pendulum dynamics show joint learning discovers substantially simpler symbolic dynamics with lower long-horizon rollout error than post-hoc fitting.
- **Compute Scale**: Small (8-12G): Pendulum experiments; theoretical analysis. Framework is general but validation is on controlled low-dimensional dynamics.
- **LeCun Alignment**: HIGH — Directly addresses a core requirement of LeCun's vision. STRENGTHS: (1) Symbolic-neural hybrid transitions embody the kind of structured, interpretable world model LeCun envisions — the world model should capture physical laws, not just be a black-box predictor. (2) The principle of "simplest adequate dynamics" directly instantiates LeCun's argument that world models should learn abstractions (laws, invariants) rather than memorize transitions. (3) The collapse-shortcut finding is a significant theoretical contribution — it formalizes a failure mode that any joint representation+dynamics learning approach must guard against, providing direct guidance for JEPA architecture design. (4) Reconstruction-free: operates purely in latent space, maintaining JEPA's key property. (5) The grammar-based symbolic search connects to LeCun's emphasis on modular architectures where different components (symbolic reasoner, neural predictor) have distinct roles. WEAKNESSES: (1) Only validated on simple pendulum dynamics — scaling to high-dimensional visual domains (images, video) remains an open question. (2) The grammar of candidate equations must be pre-specified — doesn't discover novel physical laws, only selects from a known set. (3) Single-author work, not from LeCun's group directly — independent validation of the JEPA paradigm. Overall, SJEPA is a foundational contribution that bridges JEPA with symbolic AI — exactly the direction LeCun's vision points toward. The collapse-shortcut finding alone makes this paper essential reading for anyone designing JEPA architectures.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: SJEPA — Augment JEPA with hybrid symbolic-neural transition predictors. The central principle: learn the simplest adequate dynamics. Representation constraints prevent collapse, operator compression favors parsimony, and the hybrid architecture combines symbolic precision with neural flexibility.
- **Motivation**: Opaque neural transition models in JEPA undermine interpretability, long-horizon reliability, and scientific understanding. If the true dynamics are simple (pendulum, rigid body, conservation laws), a world model should discover and exploit that simplicity — not learn a complex neural approximation that drifts on long rollouts.
- **Problem Solved**: Joint symbolic-neural learning discovers simpler dynamics with lower long-horizon rollout error than post-hoc symbolic fitting. The collapse-shortcut experiment validates the theoretical analysis: unconstrained compression does lead to representation collapse. Grammar misspecification experiments show the neural correction properly captures residual dynamics while preserving the representable symbolic component.

### Academic Context

- **Inheritance / Response**: Builds on JEPA (I-JEPA, V-JEPA, LeWM) and symbolic regression / equation discovery literature. The hybrid symbolic-neural architecture connects to neuro-symbolic AI and physics-informed machine learning. The collapse-shortcut analysis extends the JEPA theoretical literature (Gaussian Embeddings, JEPA Paradox, What Can Latent World Models Know?) by identifying a specific failure mode in joint representation-dynamics optimization.
- **Implicit Connection**: SJEPA realizes a key component of LeCun's world model architecture that has been largely underexplored: the world model should capture physical laws and invariants, not just predict. The grammar-based symbolic search implements a form of the "configurator" module in LeCun's architecture — selecting which dynamics model applies based on the current situation. The finding that joint learning outperforms post-hoc fitting validates LeCun's end-to-end philosophy: representation and dynamics should be learned together, not separately. The collapse-shortcut is a direct caution for the JEPA research program: regularization and architectural constraints are not optional — they are necessary to prevent the model from taking the easy path of representation collapse.
- **Research Line**: Interpretable JEPA — making joint-embedding predictive architectures discover interpretable, symbolic dynamics.
- **Future Directions**: Scaling to visual domains with learned grammar of visual dynamics primitives; discovering novel physical laws beyond pre-specified grammars; integrating with hierarchical JEPA where different levels have different symbolic grammars; using the symbolic dynamics for formal verification of world model predictions.
- **GitHub**: Not found

---

## [2026-08-02] FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels

- **arXiv**: [2608.01049](https://arxiv.org/abs/2608.01049)
- **Authors**: Kapil Wanaskar, Gaytri Jena, Aman Chadha, Vinija Jain, Vasu Sharma, Amitava Das
- **TL;DR**: Factorizes JEPA world model futures into three semantically separated channels — layout (static scene structure), agents (dynamic entities), and interactions (agent-agent and agent-scene) — using a visibility gate and separated subspaces to handle the extreme occlusion and heterogeneity of Global South urban environments, introducing the DENSEWORLD-115k dataset.
- **Problem**: Existing JEPA world models encode the future as a monolithic latent — a single vector that must simultaneously capture static scene geometry, moving agents, and their interactions. In dense, chaotic environments (Global South urban traffic), this monolithic encoding breaks down: (1) partial observability means many agents are temporarily occluded, and a monolithic latent may silently drop them; (2) extreme agent heterogeneity (pedestrians, rickshaws, motorcycles, cars, animals) creates a combinatorial explosion of interaction types; (3) cross-factor shortcuts allow the model to predict layout from agent positions (or vice versa) without modeling genuine dynamics. The challenge is to factor the future into semantically meaningful components that can be predicted and evaluated independently.
- **Architecture**: FactorJEPA — (1) **Three prediction channels**: Layout (static scene geometry, road structure, buildings), Agents (dynamic entity positions, velocities, types), and Interactions (agent-agent relationships, agent-scene coupling). Each channel has its own latent subspace prediction target. (2) **Visibility gate**: a learned gating mechanism that explicitly models which agents are visible vs. occluded, preventing the model from silently dropping occluded entities and enabling partial-observability reasoning. (3) **Separated subspaces**: the latent representations for layout, agents, and interactions are kept in orthogonal subspaces, discouraging cross-factor shortcuts (e.g., predicting agent positions from layout alone) and enforcing that each factor captures only its designated semantics. (4) **DENSEWORLD-115k dataset**: 1,000 hours of video across 22 Global South cities (drive-through, walk-through, aerial), capturing the dense, unstructured traffic patterns absent from existing autonomous driving datasets. (5) **Evaluation metrics**: Future-frame L1 (prediction accuracy), Causal L1 (intervention sensitivity — does the model respond correctly to agent removal/addition?), Mask-ratio slope (robustness to reduced visual evidence), and Motion cosine (reproducible motion-information trade-off). Evaluated on 2B and 1B V-JEPA 2.1 backbones with consistent method rankings (ρ = 0.895–0.978).
- **Compute Scale**: Large (40G+): 2B/1B V-JEPA 2.1 backbones trained on 1,000 hours of video. Factorized prediction adds architectural overhead but improves data efficiency.
- **LeCun Alignment**: HIGH — Factorized world model is exactly LeCun's vision. STRENGTHS: (1) The factorized architecture (layout/agents/interactions) directly instantiates LeCun's core claim: world models should decompose the world into persistent objects, their attributes, and their interactions — not predict monolithic pixel arrays. (2) The visibility gate addresses a fundamental challenge in embodied world models: agents must reason about occluded entities that still exist and matter. This is exactly the kind of "belief state" reasoning LeCun's architecture requires. (3) The DENSEWORLD dataset fills a critical gap: existing world model benchmarks use structured, Western-centric driving data, missing the chaotic dynamics that truly test world understanding. (4) The factorized prediction is JEPA-style: prediction happens in latent space (per-channel), not pixel space. (5) The Causal L1 metric (intervention sensitivity) tests whether the model has genuine causal understanding — a direct operationalization of LeCun's argument that world models must capture causal structure. WEAKNESSES: (1) The factorization is pre-specified (layout, agents, interactions) rather than discovered — the model doesn't learn what factors matter. (2) Uses V-JEPA 2.1 as frozen backbone, so the factorization operates on already-learned representations rather than being jointly learned. (3) Large compute requirements limit accessibility. Overall, FactorJEPA is one of the most architecturally aligned papers with LeCun's vision — it takes the "factorized world model" concept from LeCun's position paper and implements it concretely for the hardest real-world domain: chaotic urban environments.
- **GitHub**: [DENSEWORLD-115k dataset](https://huggingface.co/datasets/anonymousML123/denseworld-115k) | [FactorJEPA checkpoints](https://huggingface.co/datasets/anonymousML123/factorjepa-outputs/tree/main/outputs/full/vjepa_2_1_vitg_1B/train/m09c_surgery_3stage_DI_diheavy_encoder)

### What / Why / Solve

- **Proposal**: FactorJEPA — Replace monolithic JEPA future prediction with a factorized architecture that separately models layout, agents, and interactions. Use visibility gates and separated subspaces to prevent cross-factor shortcuts and handle partial observability in dense, chaotic environments.
- **Motivation**: Monolithic latent encoding fails in complex real-world environments because it entangles semantically distinct aspects of the future. Factorized prediction is both more accurate (each factor can be specialized) and more interpretable (we can identify which factor failed). The Global South urban domain is the ultimate stress test: extreme density, heterogeneity, and occlusion expose the limits of monolithic prediction.
- **Problem Solved**: FactorJEPA improves future-latent accuracy (L1), intervention sensitivity (Causal L1), and robustness to reduced visual evidence (Mask-ratio slope) over monolithic JEPA baselines. Consistent method rankings across 2B and 1B backbones demonstrate the factorization principle is robust to scale. The DENSEWORLD-115k dataset provides a challenging new benchmark.

### Academic Context

- **Inheritance / Response**: Builds on V-JEPA 2.1 and the factorized world model concept from LeCun's "Path Towards Autonomous Machine Intelligence." The three-channel factorization draws from scene decomposition literature (object-centric learning, scene graphs). The visibility gate connects to belief-state modeling in partially observable domains. The evaluation metrics (Causal L1, Mask-ratio slope) advance the rigor of world model evaluation beyond simple prediction error.
- **Implicit Connection**: FactorJEPA is arguably the closest existing implementation to the world model LeCun envisioned in his 2022 position paper. The architecture has: (1) a perception module (V-JEPA backbone), (2) a world model that predicts future states in factorized latent space (layout/agents/interactions), (3) handling of partial observability (visibility gate), and (4) causal evaluation (Causal L1). What's missing is the planning/actor module — FactorJEPA only predicts, it doesn't plan. But as a world model, it implements the key architectural insight: the future should be predicted in a structured, factorized latent space, not as a monolithic pixel array.
- **Research Line**: Factorized World Models — decomposing world state into semantically meaningful factors for prediction and reasoning.
- **Future Directions**: Learning the factorization (rather than pre-specifying it); integrating with a planning/actor module to close the perception-prediction-action loop; extending to other domains beyond urban driving; combining with symbolic dynamics (SJEPA) for interpretable factor transitions.
- **GitHub**: [DENSEWORLD-115k dataset](https://huggingface.co/datasets/anonymousML123/denseworld-115k) | [FactorJEPA checkpoints](https://huggingface.co/datasets/anonymousML123/factorjepa-outputs/tree/main/outputs/full/vjepa_2_1_vitg_1B/train/m09c_surgery_3stage_DI_diheavy_encoder)

---

## [2026-08-05] NodeJEPA: Structure-Conditioned Latent Prediction for Node-Level Graph SSL

- **arXiv**: [2608.04381](https://arxiv.org/abs/2608.04381)
- **Authors**: Tinghe Zhang, Jian Xu, Jiaheng Chen, Jiaxing Li, Yucheng Xiao, Qiang Wang
- **TL;DR**: Extends JEPA to node-level graph representation learning — masking structure-aware k-hop ego-subgraphs and predicting target node latents via an EMA-updated target encoder with spectral/centrality cross-attention conditioning — providing a practical recipe for node-level JEPA-style self-supervised learning on graphs.
- **Problem**: Existing graph SSL is dominated by contrastive methods (sensitive to augmentation design) and generative methods (reconstruct node attributes in input space, entangling representations with low-level statistics). While JEPA has been applied to graph-level tasks (HP-JEPA), node-level JEPA — where each node needs its own representation — presents unique challenges: what structural information should the predictor condition on, how to design masking for node-centric prediction, and how to regularize the embedding geometry for hundreds of thousands of nodes.
- **Architecture**: NodeJEPA — (1) **Structure-aware masking**: masks k-hop ego-subgraphs around target nodes rather than random node subsets, ensuring the context encoder sees structurally meaningful neighborhoods. (2) **Structure-conditioned predictor**: integrates spectral descriptors (Laplacian eigenvalues) and centrality measures (degree, betweenness) through cross-attention, giving the predictor explicit structural information about the masked nodes' positions in the graph. (3) **EMA target encoder**: produces target latents with stop-gradient, following standard JEPA practice. (4) **Triple regularization**: variance regularization (prevent dimension collapse), covariance regularization (decorrelate features), and Laplacian spectral regularization (preserve graph structure in embedding geometry). (5) **Curriculum masking**: gradually increases masking difficulty during training. Evaluated on standard node classification benchmarks under linear probing and fine-tuning.
- **Compute Scale**: Small-Mid (8-24G): Node classification benchmarks. JEPA training on citation/co-purchase networks.
- **LeCun Alignment**: MEDIUM — Extends JEPA paradigm but to a non-embodied domain. STRENGTHS: (1) Demonstrates JEPA's generality — the predictive architecture works for yet another data modality (graphs, specifically node-level tasks), strengthening the claim that JEPA is a universal SSL paradigm. (2) The structure-conditioned predictor (using spectral and centrality features) is a principled way to inject domain knowledge into JEPA — the predictor shouldn't guess blindly, it should use available structural cues. This mirrors how embodied JEPA predictors should condition on actions and goals. (3) The triple regularization scheme addresses known JEPA failure modes (collapse, dimensional correlation) with graph-specific tools. WEAKNESSES: (1) Graph node classification is far from embodied AI — this is representation learning, not world modeling for planning. (2) No temporal/action component — purely spatial structure prediction. (3) The structural conditioning features (spectral, centrality) are hand-designed, not learned. Overall, NodeJEPA is a solid methodological contribution showing JEPA's applicability to node-level graph tasks, though its connection to LeCun's autonomous intelligence vision is indirect — it demonstrates JEPA generality rather than advancing the world model research program.
- **GitHub**: [github.com/OliverZ-dot/Node-Jepa](https://github.com/OliverZ-dot/Node-Jepa)

### What / Why / Solve

- **Proposal**: NodeJEPA — A JEPA framework for node-level graph SSL. Structure-aware masking, spectral/centrality-conditioned predictor, EMA target encoder, and triple regularization. Prediction in latent space, no input reconstruction.
- **Motivation**: Node-level tasks are the most common graph ML applications, but existing SSL methods (contrastive, generative) have known failure modes. JEPA's reconstruction-free, non-contrastive approach is theoretically appealing but hasn't been demonstrated for node-level tasks.
- **Problem Solved**: NodeJEPA achieves competitive performance on node classification benchmarks. Ablations clarify which design choices matter: structure conditioning helps, curriculum masking helps, and the regularization suite is necessary for stable training. Provides a practical recipe for node-level JEPA.

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA and HP-JEPA (graph-level JEPA). The node-level extension addresses a gap in the JEPA-for-graphs literature. The structure-conditioned predictor connects to positional encoding literature (spectral GNNs, centrality-based features).
- **Implicit Connection**: NodeJEPA and HP-JEPA together establish that JEPA is a viable alternative to contrastive and generative methods for graph representation learning at both graph and node levels. The structure-conditioned predictor is analogous to action-conditioned predictors in embodied JEPA — both provide task-relevant context that the predictor should use. The finding that structural conditioning helps validates the general JEPA design principle: the predictor should condition on available task-relevant information.
- **Research Line**: Graph JEPA — extending joint-embedding predictive architectures across graph learning tasks.
- **Future Directions**: Temporal/dynamic graph JEPA; action-conditioned graph JEPA for predicting graph edits; combining with HP-JEPA for hierarchical node+graph representations; extending to heterogeneous graphs and knowledge graphs.
- **GitHub**: [github.com/OliverZ-dot/Node-Jepa](https://github.com/OliverZ-dot/Node-Jepa)

---

## [2026-08-03] ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching

- **arXiv**: [2608.01926](https://arxiv.org/abs/2608.01926)
- **Authors**: Zihan Liu, Yuzhe Zhuang, Yuanzu Li, Wanshuang Gou, Jiahong Liu, Min Zhou, Menglin Yang
- **TL;DR**: Introduces a JEPA-style hyperbolic world model that organizes latent-space dynamics using goal-conditioned progress order — an asymmetric, coarse-to-fine structure naturally suited to hyperbolic geometry — maintaining directional progress and mitigating local ambiguity, achieving +9.67pp average success over LeWM on visual goal-reaching.
- **Problem**: JEPA-style visual world models learn local transition consistency (next-step latent prediction) but fail on long-horizon tasks because multi-step rollouts can remain locally plausible while drifting away from the goal. Two specific failures: (1) locally similar future states can correspond to substantially different long-term progress, and a Euclidean latent space optimized for local consistency cannot distinguish them; (2) rollouts accumulate small local errors into large global deviations because there is no mechanism to maintain directional progress toward the goal. The challenge is to structure the latent space so that progress toward a goal is explicitly represented and preserved during planning.
- **Architecture**: ProWorld — (1) **Goal-conditioned progress order**: a relative ordering of states according to how they advance toward a given goal. This order is asymmetric (A→B→C doesn't imply C→B→A) and coarse-to-fine (early states have broad future possibilities; later states concentrate on specific goal-relevant regions) — a structure naturally represented in hyperbolic geometry. (2) **Hyperbolic latent space**: states are embedded in hyperbolic space where the Poincaré ball model naturally captures hierarchical, coarse-to-fine relationships. (3) **Hyperbolic entailment learning**: enforces that if state A should precede state B on the path to a goal, then A's hyperbolic embedding should entail (be more general than) B's embedding — formalized through hyperbolic cones. (4) **Hyperbolic future discrimination**: distinguishes locally similar but progress-different states by their hyperbolic distances from goal-related reference points. (5) **Progress-aware planning**: scores candidate rollouts jointly by proximity to the goal AND sustained progress across intermediate states. Evaluated on four visual goal-reaching tasks against LeWM baseline.
- **Compute Scale**: Mid (24G): Four visual goal-reaching tasks. Hyperbolic operations have standard overhead.
- **LeCun Alignment**: MEDIUM-HIGH — Addresses a key limitation of current JEPA world models for planning. STRENGTHS: (1) Directly builds on JEPA-style visual world models (LeWM), extending them with a principled geometric solution to the long-horizon planning problem. (2) The progress-order concept addresses LeCun's hierarchical planning vision: different levels of the world model should track progress at different temporal scales. Hyperbolic geometry naturally captures hierarchical relationships. (3) The finding that locally consistent ≠ globally progressive is a direct empirical validation of the "predictive accuracy ≠ planning success" critique that LeCun has raised. (4) The progress-aware planning objective is exactly the kind of cost/reward module that LeCun's architecture places between the world model and the actor. WEAKNESSES: (1) The goal-conditioned progress order relies on having a known goal state — doesn't address open-ended exploration where goals are discovered. (2) Hyperbolic geometry is a design choice, not learned — the model doesn't discover that progress is naturally hyperbolic. (3) Only tested on visual goal-reaching, not on general robotic manipulation or navigation. Overall, ProWorld is a valuable contribution that identifies and addresses a specific failure mode of JEPA world models for planning — local predictive accuracy doesn't guarantee global progress — using a geometrically principled solution.
- **GitHub**: To be released after acceptance

### What / Why / Solve

- **Proposal**: ProWorld — Replace Euclidean latent spaces in JEPA world models with hyperbolic geometry, organized by goal-conditioned progress order. This naturally maintains directional progress during long-horizon planning and distinguishes locally similar states by their progress toward the goal.
- **Motivation**: Long-horizon planning with world models fails because local accuracy ≠ global progress. Hyperbolic geometry is mathematically suited to representing hierarchical, coarse-to-fine relationships — exactly the structure of progress toward a goal. The key insight: the latent space should explicitly represent how close each state is to achieving the goal, not just how similar states are to each other.
- **Problem Solved**: +9.67pp average success rate over LeWM on four visual goal-reaching tasks. Demonstrates that progress-aware latent structuring significantly improves long-horizon planning without requiring more accurate local predictions.

### Academic Context

- **Inheritance / Response**: Builds on LeWM and JEPA-style visual world models. The hyperbolic geometry approach draws from hyperbolic representation learning literature. The progress-order concept connects to goal-conditioned RL and hierarchical planning. Directly responds to the "control theory of predictability" paper (2607.10362) which proved prediction error ≠ control success — ProWorld provides a geometric solution to this decoupling.
- **Implicit Connection**: ProWorld represents the "planning layer" that JEPA world models need. LeCun's architecture places a planner/actor on top of the world model, and ProWorld shows that the latent space itself should be structured to support planning — not just prediction. The hyperbolic geometry provides a natural inductive bias for hierarchical planning, which aligns with LeCun's emphasis on multi-level world models. The paper also contributes to the growing literature on "closing the train-plan gap" (TD-JEPA, INTACT) by addressing it geometrically rather than through objective function design.
- **Research Line**: Structured Latent Spaces for World Model Planning — designing latent geometries that support effective planning, not just accurate prediction.
- **Future Directions**: Learned hyperbolic structure (rather than pre-specified); integrating with hierarchical JEPA where each level has its own progress metric; combining with symbolic dynamics for interpretable progress tracking; extending to open-ended exploration without pre-specified goals.
- **GitHub**: To be released after acceptance

---

## [2026-08-05] Faster-WAM: Efficient Inference-Time Future Conditioning for Robust World Action Models

- **arXiv**: [2608.04404](https://arxiv.org/abs/2608.04404)
- **Authors**: Weiheng Zhao, Haoyi Jiang, Xin Shi, Liu Liu, Fan Huang, Zhizhong Su, Wei Sui, Xinggang Wang
- **TL;DR**: Introduces SparseMoT and Interval KV-Fusion for efficient WAM inference — selectively reusing future representations at only a compact subset of network stages rather than every layer — achieving 73.57% LIBERO-Plus success (vs. 49.14% Fast-WAM) while running 2.21× faster than Joint-WAM.
- **Problem**: There is a fundamental trade-off in WAM deployment: Joint-WAMs maintain future-aware representations throughout inference (enabling robust temporal reasoning) but are computationally prohibitive; efficient WAMs remove future modeling at inference time to reduce cost, but lose the robustness benefits of temporal reasoning. The challenge is to preserve future-conditioned inference at low computational cost — not by removing future information, but by using it sparingly and strategically.
- **Architecture**: Faster-WAM — NOTE: This is a DIFFERENT paper from Faster-WAM (2608.02365, "Do World Action Models Need Deep Action Modules?"). Same name, different approach. Key components: (1) **SparseMoT**: replaces ubiquitous layer-wise video-action fusion (Joint-WAM) with selective interaction at only a compact subset of network stages. The future representation is computed once and selectively reused at designated layers, drastically reducing the number of cross-attention operations. (2) **Interval KV-Fusion**: aggregates multi-depth future representations (from different backbone layers) without increasing attention complexity. Instead of attending to future features from every layer, the model attends to a compressed interval representation that summarizes future information across depth ranges. (3) **Sparse future-conditioning framework**: future representations are computed once (shared across denoising steps) and selectively injected at designated stages. Evaluated on LIBERO, LIBERO-Plus (OOD), RoboTwin 2.0, and real-world manipulation. Key results: 73.57% on LIBERO-Plus (vs. 49.14% Fast-WAM, 61.92% Joint-WAM), 2.21× faster than Joint-WAM.
- **Compute Scale**: Large (40G+): VideoDiT backbone + action diffusion. Sparse conditioning reduces inference cost by ~2.2× compared to Joint-WAM.
- **LeCun Alignment**: MEDIUM-HIGH — Practical efficiency contribution. STRENGTHS: (1) Addresses the real-world deployment challenge: WAMs that are too slow to run in real-time are scientifically interesting but practically useless. SparseMoT makes future-conditioned inference practical without sacrificing robustness. (2) The finding that sparse interaction (selective, not ubiquitous) suffices validates LeCun's modular design philosophy: different modules (video backbone, action head) don't need to interact at every layer — strategic interfaces are enough. (3) The dramatic LIBERO-Plus improvement (73.57% vs 49.14%) demonstrates that efficient future conditioning doesn't just match expensive approaches — it can outperform them, suggesting sparse interaction may have a regularizing effect. WEAKNESSES: (1) Still uses generative video diffusion backbone — not JEPA-based. (2) Same confusing naming as the other Faster-WAM paper (different approach, same name). (3) The sparse interaction locations are pre-specified, not learned. Overall, Faster-WAM (this version) provides a practical recipe for efficient WAM deployment that preserves future-awareness — a necessary step toward real-time robotic world models.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Faster-WAM — Efficient future-conditioned WAM using SparseMoT (selective video-action interaction) and Interval KV-Fusion (compressed multi-depth future representations). Preserve future-awareness at inference without ubiquitous cross-attention.
- **Motivation**: Joint-WAMs are too slow for real-time deployment, but removing future conditioning (Fast-WAM approach) sacrifices robustness. Sparse interaction provides a middle ground: use future information strategically, not ubiquitously.
- **Problem Solved**: 73.57% on LIBERO-Plus (SOTA, +12.65pp over Joint-WAM), 2.21× faster than Joint-WAM. Real-world manipulation shows strong robustness. Demonstrates that sparse future interaction is both more efficient AND more effective than full interaction.

### Academic Context

- **Inheritance / Response**: Builds on Fast-WAM, Joint-WAM, and the Mixture-of-Transformers WAM design. The SparseMoT approach draws from sparse mixture-of-experts and selective attention literature. The Interval KV-Fusion connects to multi-scale feature aggregation methods. Notably different from the other Faster-WAM (2608.02365) which asks about action module depth — this paper asks about video-action interaction sparsity.
- **Implicit Connection**: Both Faster-WAM papers (2608.02365 and 2608.04404) arrive at the same conclusion from different angles: WAMs can be much more efficient than current designs. The first paper shows action modules don't need depth; this paper shows video-action interaction doesn't need density. Together, they suggest a design principle: modular WAM architectures where modules interact sparingly and strategically, not densely and ubiquitously. This aligns with LeCun's emphasis on modular, efficient architectures.
- **Research Line**: Efficient WAM Deployment — reducing the computational cost of world-action models while preserving (or improving) their robustness.
- **Future Directions**: Learned sparse interaction patterns (which layers to fuse); applying SparseMoT to JEPA-based WAMs; combining with the action-module-depth reduction from the other Faster-WAM; multi-timescale sparse interaction (different sparsity patterns for different temporal horizons).
- **GitHub**: Not found

---

## [2026-08-05] MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight

- **arXiv**: [2608.04657](https://arxiv.org/abs/2608.04657)
- **Authors**: Zehua Fan, Junjie He, Wenxuan Song, Xi Wang, Wenqi Lyu, Linge Zhao, Fuhao Li, Zihan You, Yifei Yang, Kaiming Xu, Qi Jiang, Yue Jiang, Haoang Li, Cheng Chi, Bailin Li, Yan Wang
- **TL;DR**: First WAM for mobile manipulation — a Mixture-of-Transformers architecture fusing video diffusion with a locomotion/manipulation expert mixture — using Chain-of-Foresight (sequential latent future prediction) for densified supervision; surpasses SOTA on ManiSkill-HAB and transfers to a real ARX Lift2 mobile manipulator.
- **Problem**: WAMs have been confined to tabletop manipulation with fixed-base arms. Mobile manipulation requires simultaneous locomotion (navigating the base) and whole-body manipulation (arm + gripper control) amid scene-scale dynamics — two heterogeneous control domains with different temporal characteristics. Existing mobile manipulation approaches use dynamics-blind visual encoders with hand-crafted coordination between locomotion and manipulation, lacking the predictive foresight that WAMs provide.
- **Architecture**: MobileWAM — (1) **Mixture-of-Transformers (MoT)**: fuses a pretrained video diffusion transformer (internet-scale motion priors) with a lightweight action expert through layerwise joint attention. (2) **Three-expert mixture per action FFN layer**: shared expert (general motion patterns), locomotion expert (base movement), and manipulation expert (arm/gripper control) — softly routed by motion intent encoded in action tokens. This allows the model to dynamically allocate capacity between moving and manipulating based on the task phase. (3) **Chain-of-Foresight (CoF)**: intermediate action representations sequentially predict a chain of future latent chunks, each step conditioned on its predecessor. This densifies the supervision signal for the action expert without requiring pixel-space future prediction. (4) **Deployment mode**: the WAM serves as a pure current-frame encoder — the foresight chain and video generation are discarded at inference, leaving only the action policy with zero additional cost. Evaluated on ManiSkill-HAB (mobile manipulation benchmark) and fine-tuned on a real ARX Lift2 mobile manipulator.
- **Compute Scale**: Large (40G+): Video diffusion backbone + action expert mixture. Inference is lightweight (foresight discarded at deployment).
- **LeCun Alignment**: MEDIUM — Expands WAM scope to an important new domain. STRENGTHS: (1) Extends WAMs beyond tabletop manipulation to mobile manipulation — a necessary step toward general-purpose embodied agents, which LeCun's vision ultimately requires. (2) The Mixture-of-Experts routing between locomotion and manipulation mirrors LeCun's modular architecture: different "expert" modules handle different aspects of behavior, and a gating mechanism (the motion intent router) dynamically selects which experts to engage. (3) Chain-of-Foresight is a JEPA-aligned training strategy: predict future latents sequentially without pixel generation, using the foresight as a training signal that distills temporal understanding into the action policy. (4) Zero-cost deployment (foresight discarded at inference) follows the DreamWAM philosophy: use structured future prediction during training, deploy only the action policy. WEAKNESSES: (1) The video backbone is generative diffusion — not JEPA-based. (2) The locomotion/manipulation factorization is hand-designed, not learned from data. (3) The Chain-of-Foresight predicts action latents, not world state latents — more of an action-chaining approach than a world model. Overall, MobileWAM is a significant domain expansion for WAMs, bringing predictive architectures to mobile manipulation with practical efficiency. Its contribution is more about the application domain than architectural innovation, but the domain matters: embodied agents need mobile manipulation, not just tabletop skills.
- **GitHub**: To be released

### What / Why / Solve

- **Proposal**: MobileWAM — First WAM for mobile manipulation. Mixture-of-Transformers with locomotion/manipulation expert routing, trained with Chain-of-Foresight (sequential latent future prediction) for densified supervision. Deploys as pure current-frame encoder.
- **Motivation**: WAMs have proven effective for tabletop manipulation but haven't been applied to mobile manipulation — a more challenging domain requiring simultaneous locomotion and manipulation amid scene-scale dynamics. The gap is both architectural (how to handle heterogeneous dynamics) and practical (mobile manipulation needs efficient inference).
- **Problem Solved**: Surpasses SOTA mobile manipulation policies on ManiSkill-HAB. Fine-tunes to a real ARX Lift2 mobile manipulator with strong generalization across diverse tasks. Demonstrates that WAMs can be extended beyond tabletop settings.

### Academic Context

- **Inheritance / Response**: Builds on WAM literature (Fast-WAM, Joint-WAM) and mobile manipulation. The Mixture-of-Transformers with domain-specific experts extends the MoT design pattern to heterogeneous action spaces. Chain-of-Foresight connects to action chunking and trajectory prediction literature.
- **Implicit Connection**: MobileWAM demonstrates the expandability of the WAM paradigm — as WAMs mature, they should scale from tabletop manipulation to full-body mobile manipulation to general-purpose embodied agents. The locomotion/manipulation expert mixture is a concrete example of LeCun's configurator module: based on the current state and intent, different behavioral modules are engaged. The finding that foresight can be discarded at deployment (training only) supports the JEPA philosophy: future prediction is for learning good representations, not for generating pixels at runtime.
- **Research Line**: Domain-Expanded WAM — extending world-action models to new embodiment types and task domains.
- **Future Directions**: Navigation-manipulation unified WAM; learned expert routing (beyond locomotion/manipulation dichotomy); integrating with JEPA-based video backbones; multi-embodiment transfer via the expert mixture framework.
- **GitHub**: To be released## [2026-08-01] HP-JEPA: Hierarchical Partitioning for Multi-Resolution Graph Joint-Embedding Predictive Learning

- **arXiv**: [2608.00491](https://arxiv.org/abs/2608.00491)
- **Authors**: Ruichen Xu, Jingxiang Qu, Wenhan Gao, Jiaxing Zhang, Linsey Pang, Ravid Shwartz-Ziv, Yann LeCun, Yuefan Deng
- **TL;DR**: Extends JEPA to graph-structured data with a novel hierarchical multi-resolution partitioning framework — organizing each graph into a coarse-to-fine partition bank and performing latent prediction at each resolution separately — achieving 6/8 benchmark wins over fixed-resolution Graph-JEPA.
- **Problem**: Existing graph JEPAs rely on a single predefined graph partition, biasing learned representations toward one structural granularity. Graphs contain complementary patterns at multiple scales (local neighborhoods, regional clusters, global topology), and a single partition cannot capture all of them simultaneously. The challenge is to design a JEPA that learns from multiple structural resolutions without sacrificing the reconstruction-free, non-contrastive properties that make JEPA attractive.
- **Architecture**: HP-JEPA — A hierarchical partitioning framework for graph JEPA. Key components: (1) **Coarse-to-fine partition bank**: each graph is organized into an ordered sequence of partitions at different resolutions (cluster-level → neighborhood-level → node-level). (2) **Per-resolution JEPA**: at each resolution, a standard JEPA pipeline operates — online context encoder → latent predictor → EMA target encoder. Masked prediction happens independently at each granularity. (3) **Resolution integration**: the resulting resolution-specific representations are concatenated or weighted by task-specific importance, allowing downstream models to combine complementary local, regional, and global structural information. (4) **Modality**: operates on graph-structured data (unlike image/video JEPA), extending the JEPA paradigm to a fundamentally different data structure. Evaluated on 7 graph classification benchmarks and 1 graph regression benchmark. Size-stratified analyses show HP-JEPA achieves higher accuracy in most graph-size quartiles.
- **Compute Scale**: Mid (24G): Graph classification/regression benchmarks (standard GNN-scale datasets). Multi-resolution encoders add modest overhead compared to single-resolution Graph-JEPA.
- **LeCun Alignment**: HIGH — LeCun co-author; direct JEPA variant. STRENGTHS: (1) Extends the JEPA paradigm to graph-structured data, demonstrating JEPA's generality beyond vision/audio — a key claim in LeCun's vision that the predictive architecture is universal. (2) The hierarchical multi-resolution design mirrors LeCun's emphasis on hierarchical world models — different levels of abstraction capture different temporal/spatial scales. (3) Maintains core JEPA properties: latent prediction (no reconstruction), EMA target encoder, non-contrastive. (4) The partition-bank approach is a principled way to handle the fundamental multi-scale nature of physical systems. WEAKNESSES: (1) Graph domain is farther from embodied AI than video/robot JEPAs — graph classification is a representation-learning benchmark, not a world model for planning. (2) No action conditioning — purely representation learning, not dynamics prediction. (3) The hierarchical resolution integration is task-specific (concatenation/weighting), not an end-to-end learned hierarchy. Overall, HP-JEPA is a significant architectural contribution showing that JEPA principles (hierarchical, multi-scale, reconstruction-free) apply to graph data, with LeCun's direct involvement confirming its alignment with the JEPA research program.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: HP-JEPA — Extend JEPA to graphs with a hierarchical multi-resolution partitioning scheme. Instead of a single fixed partition, use a bank of coarse-to-fine partitions and perform JEPA prediction at each resolution independently, then integrate the learned representations.
- **Motivation**: Graph data is inherently multi-scale. A single partition forces the model to commit to one granularity, losing information at other scales. Hierarchical partitioning is the natural solution — just as vision JEPA can use different patch sizes or masking strategies, graph JEPA should use different structural resolutions.
- **Problem Solved**: HP-JEPA outperforms the fixed-resolution Graph-JEPA baseline on 6 of 8 tasks, with size-stratified gains showing improvement across most graph-size quartiles. Demonstrates that multi-resolution partitioning is a straightforward but effective way to improve graph representation learning within the JEPA framework.

### Academic Context

- **Inheritance / Response**: Builds directly on I-JEPA (image) and extends to Graph-JEPA. The hierarchical partitioning approach draws from multi-scale graph representation learning and hierarchical pooling literature but adapts it to the JEPA predictive framework.
- **Implicit Connection**: The hierarchical design connects to LeCun's multi-level world model architecture — different levels of the hierarchy capture structure at different temporal/spatial scales. This paper demonstrates that even within a single modality (graphs), multi-resolution processing improves representation quality. The size-stratified analysis showing gains across graph sizes is particularly relevant: world models must handle systems at multiple scales simultaneously.
- **Research Line**: Graph JEPA — extending joint-embedding predictive architectures to graph-structured data.
- **Future Directions**: Learned (rather than predefined) partition strategies; temporal graph JEPA for dynamic networks; integration with embodied world models that represent scenes as graphs of objects; action-conditioned graph JEPA for predicting how graph structures evolve under interventions.
- **GitHub**: Not found

---

## [2026-08-03] CoWAM: Coordination Contracts for Selective Policy Intervention with WAMs

- **arXiv**: [2608.02578](https://arxiv.org/abs/2608.02578)
- **Authors**: Shuaijun Liu, Qifu Wen, Shuyang Hao, Qi Luo, Chenglong Zhang, Feiyang You, Chengyu Wu, Ningxin Su
- **TL;DR**: Introduces CoWAM, a selective intervention layer that uses typed coordination contracts (synchronization, role compatibility, collision convergence) to gate World Action Model predictions — only overriding the nominal bimanual policy when all active contracts clear, achieving 9.6pp higher closed-loop success with <1% harmful interventions.
- **Problem**: World Action Models (WAMs) can predict action-conditioned futures, but a plausible-looking future alone does not justify changing a robot's action. In bimanual coordination, the WAM's predicted futures may conflict with synchronization requirements, role assignments, or collision constraints — and blindly trusting the WAM's "best future" can introduce harmful interventions that degrade overall coordination. The challenge is to use WAM predictions selectively — intervening only when the evidence is clear and safe.
- **Architecture**: CoWAM — A coordination-contract-based selective intervention layer that sits between a bimanual policy and WAM-generated action proposals. Three contract types: (1) **Synchronization contracts**: verify temporal alignment between arms (e.g., both grippers close within tolerance). (2) **Role compatibility contracts**: check that proposed actions respect arm-role assignments (e.g., left arm holds while right arm manipulates). (3) **Collision convergence contracts**: ensure predicted trajectories don't lead to arm-arm or arm-object collisions. Each contract combines typed admissibility checks with event-conditioned verification and calibrated intervention gates. The key design: the nominal policy action is preserved unless an alternative satisfies every active obligation AND provides a clear, low-risk improvement. When even the nominal action is inadmissible, a predefined abstention fallback activates. All methods operate on identical candidate pools and commit decisions before shared oracle labeling — cleanly separating selector quality from proposal quality.
- **Compute Scale**: Mid (24G): 8 simulated bimanual manipulation tasks. Contract verification adds negligible overhead compared to WAM inference.
- **LeCun Alignment**: MEDIUM-HIGH — Practical WAM deployment architecture. STRENGTHS: (1) Directly addresses a key deployment challenge: WAMs make predictions, but trusting them blindly is dangerous — selective intervention is essential for safe deployment. (2) The contract-based gating is modular and interpretable, aligning with LeCun's emphasis on composable, transparent architectures. (3) The abstention fallback when all options are inadmissible is a safety-conscious design that echoes the "cost" module in LeCun's agent architecture (which should detect unsafe states). (4) Clean separation of selector quality from proposal quality is methodologically rigorous. WEAKNESSES: (1) Uses WAMs as a black-box oracle rather than advancing WAM architecture itself. (2) The contracts are hand-designed for bimanual tasks — not learned from data or generalizable to arbitrary coordination patterns. (3) The rejection-based approach (only intervene when clearly better) is conservative — may miss opportunities where WAM predictions are directionally useful. Overall, CoWAM addresses the critical safety-deployment gap in WAM research, showing that the question is not just "can WAMs predict?" but "when should we trust their predictions?" — a question at the heart of LeCun's vision of autonomous systems that plan safely.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: CoWAM — A coordination-contract layer for selective WAM intervention in bimanual manipulation. Contracts encode synchronization, role compatibility, and collision constraints. Interventions only occur when all contracts clear and the alternative is clearly better than the nominal action.
- **Motivation**: WAMs predict futures, but futures alone don't justify action changes — especially in coordinated multi-arm settings where one arm's action depends on the other's state. Blind trust in WAM predictions can cause more harm than good. Contracts provide a principled, verifiable interface between WAM predictions and policy execution.
- **Problem Solved**: CoWAM improves coordination-valid selection by 16.7pp over contract-only variant and raises closed-loop success by 9.6pp over strongest selective baseline, while keeping harmful interventions below 1%. Establishes coordination contracts as an effective interface for conservative WAM-based policy intervention.

### Academic Context

- **Inheritance / Response**: Builds on WAM literature (Fast-WAM, LingBot-VA, LeapBot-WA) and bimanual manipulation. The contract-based gating approach draws from formal methods and runtime verification but applies it to learned WAM predictions. The selective (rather than generative) use of WAMs connects to the broader theme of using world models for verification rather than generation.
- **Implicit Connection**: CoWAM represents the "safety layer" that LeCun's architecture implicitly needs — a module that verifies whether world-model-predicted futures are actually safe/feasible before executing corresponding actions. This is a practical instantiation of the cost/constraint module in the modular agent architecture. The finding that selective intervention (only when clearly beneficial) outperforms always-trust shows that WAMs are most useful as verification tools, not as replacement planners.
- **Research Line**: Safe WAM Deployment — making world action models trustworthy for real-world robotic execution.
- **Future Directions**: Learned contracts (rather than hand-designed); extension to higher-DOF manipulation and mobile manipulation; integration with JEPA-based WAMs; contracts that adapt online based on task context; combining with formal verification of learned world models.
- **GitHub**: Not found

---

## [2026-08-03] WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity

- **arXiv**: [2608.02603](https://arxiv.org/abs/2608.02603)
- **Authors**: Yuxue Yang, Shuyao Shang, Jiahe Wang, Zitong Zhou, Liang Tan, Junhan Zeng, Ruizhi Li, Junyan Li, Yu Liu, Xiao Yang, Yong Li, Jun Zhu, Hongsheng Li, Tieniu Tan, Lue Fan, Zhaoxiang Zhang
- **TL;DR**: A 4-level hierarchical diagnostic benchmark for evaluating video generation models as world models — from Visual Quality to World Reactivity (the ability to infer inherent dynamics and generate plausible consequences beyond explicit instruction) — exposing a capability split where no model combines broad task coverage with consistently strong reactivity.
- **Problem**: Controllable video generation models are increasingly positioned as world models, but existing benchmarks evaluate only visual quality or explicit instruction fulfillment — checking whether requested actions and interactions are realized. They don't evaluate inherent reactivity: the ability to infer from scene state how the world should react and generate plausible consequences not explicitly described in the input. Without measuring reactivity, we can't distinguish between models that understand world dynamics and those that merely interpolate visual patterns.
- **Architecture**: WorldExam — A 4-level hierarchical benchmark. (1) **Visual Quality**: standard visual fidelity metrics. (2) **Control Adherence**: whether the model faithfully executes specified actions (camera movement, object manipulation). (3) **Spatial Consistency**: whether generated sequences maintain coherent 3D spatial relationships. (4) **World Reactivity**: whether the model generates plausible world consequences (object responses, physical interactions, goal-directed behaviors) that go beyond what is explicitly specified in the input — this is the novel contribution. 1,474 cases across 8 dedicated tasks. Supports unified evaluation of three model paradigms: camera-driven, action-driven, and language-driven. Evaluates 20 representative models including SOTA video generation systems.
- **Compute Scale**: N/A (benchmark/diagnostic). 20 models evaluated; inference cost depends on evaluated model.
- **LeCun Alignment**: MEDIUM — Important diagnostic tool for the world model field. STRENGTHS: (1) The World Reactivity level directly tests whether models understand inherent physical dynamics — the core claim of world model research. Finding that high visual quality doesn't guarantee reactivity aligns with LeCun's critique that generative models ≠ world models. (2) The multi-paradigm evaluation (camera/action/language) provides a unified comparison framework that the field currently lacks. (3) The capability split finding — no model excels across all dimensions — validates LeCun's argument that current approaches are incomplete. WEAKNESSES: (1) Evaluates generative video models (pixel-space prediction), not JEPA-style latent predictive architectures — the benchmark implicitly assumes generative models are the primary world model candidates. (2) The "reactivity" metric, while novel, still operates in pixel space — it measures whether generated videos look reactive, not whether the underlying dynamics representation is correct. (3) Doesn't evaluate planning capability — reactivity is about single-step responses, not the multi-step planning that LeCun's vision requires. Overall, WorldExam is a valuable diagnostic tool that empirically validates LeCun's skepticism about generative video models as world models, but the benchmark itself operates within the generative paradigm rather than testing the predictive-architecture alternative.
- **GitHub**: Project website: [WorldExam.github.io](https://WorldExam.github.io)

### What / Why / Solve

- **Proposal**: WorldExam — A 4-level benchmark for evaluating video generation models as world models, with World Reactivity as the novel top level that tests whether models understand inherent dynamics beyond explicit instruction.
- **Motivation**: The field lacks a unified framework for evaluating world models that goes beyond visual quality. As models are increasingly deployed as world simulators for robotics and planning, we need to know whether they actually understand dynamics or just generate visually plausible videos.
- **Problem Solved**: Evaluation of 20 models reveals a clear capability split: camera-driven models excel at camera control but can't handle dynamic interaction; action-driven models control subjects precisely but leave the world unresponsive; language-driven models handle interaction better but follow complex controls less faithfully. No model achieves consistent performance across all four levels. High visual quality and explicit instruction fulfillment do NOT guarantee inherent reactivity.

### Academic Context

- **Inheritance / Response**: Builds on video generation evaluation literature (FVD, IS, etc.) but adds the critical World Reactivity dimension. Positioned as a diagnostic tool complementary to existing benchmarks. The finding that models fail at reactivity while succeeding at appearance connects to the broader critique of generative models as world simulators (Is Sora a World Simulator?, Sora and V-JEPA Have Not Learned the Complete Real World Model).
- **Implicit Connection**: WorldExam provides empirical evidence for LeCun's core argument: generative video models that predict pixels do NOT understand world dynamics — they can produce visually impressive outputs that fail on basic physical reactivity. The benchmark paradigm (hierarchical, diagnostic, multi-paradigm) is exactly what the world model field needs to move beyond "it looks good" evaluations. However, what's missing is a JEPA-specific evaluation level — testing whether latent predictive architectures (which don't produce pixels) capture reactivity better than generative ones. This benchmark could be extended with a "Latent Reactivity" level that probes the internal representations of JEPA models.
- **Research Line**: World Model Evaluation — developing rigorous benchmarks that test whether models understand dynamics, not just generate appearances.
- **Future Directions**: Adding JEPA-specific evaluation protocols (probing latent representations for reactivity without pixel generation); extending to physical robot interaction scenarios; incorporating multi-step planning evaluation; developing "reactivity scores" that correlate with downstream planning success.
- **GitHub**: Project website: [WorldExam.github.io](https://WorldExam.github.io)

---

## [2026-08-04] LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation

- **arXiv**: [2608.03701](https://arxiv.org/abs/2608.03701)
- **Authors**: Fan Yang, Yuting Su, Xiaobo Wang, Yuncheng You, Fugui Fan, Yuting Wu, Minghui Wu, Chenxu Zhao, JiaHong Ning, Peiguang Jing
- **TL;DR**: A lightweight world-action model that reasons about the future in a compact latent space jointly shaped by future-state prediction and action generation — trainable end-to-end on a single 24GB GPU and achieving 90.48% success across 50 RoboTwin tasks.
- **Problem**: Existing WAMs incur substantial computational overhead. Pixel-space methods waste capacity on visual details irrelevant to control; latent-space methods require multi-stage training to construct the reasoning space. Both make WAMs hard to train under modest computational budgets, limiting accessibility for the broader research community.
- **Architecture**: LiLa-WAM — End-to-end trainable on a single 24GB GPU. Core design: (1) **Compact latent reasoning space**: jointly shaped by future-state prediction (what will the world look like?) and action generation (what action should I take?). These two objectives share a common latent space that remains lightweight while well-aligned with control. (2) **Visual Transition Token (VTT)**: a language-free task representation that encodes each task as a direction in visual feature space — eliminating the need for language descriptions while maintaining task specificity. (3) **Single-stage training**: unlike multi-stage WAMs that require separate pretraining and alignment phases, LiLa-WAM is trained end-to-end. Evaluated on RoboTwin 2.0 (90.48% across 50 tasks), LIBERO, and real-robot tasks.
- **Compute Scale**: Mid (24G): Single GPU end-to-end training. Lightweight encoder + compact latent reasoning space. Designed for accessibility.
- **LeCun Alignment**: HIGH — Embodies core LeCun principles: (1) Predicts in latent space, not pixels — the joint future-state/action latent space is a JEPA-aligned design choice. (2) Modular, efficient architecture that decouples perception from reasoning — the visual encoder provides features while the latent reasoning space handles dynamics. (3) Single-GPU training democratizes WAM research, aligning with the vision of practical, deployable autonomous systems rather than datacenter-only approaches. (4) The VTT (visual transition token) as a language-free task specifier mirrors LeCun's emphasis on learning from observation rather than language grounding. WEAKNESSES: (1) The joint prediction space still includes reconstruction-like elements (future-state prediction), not purely JEPA-style latent prediction. (2) VTT is limited to tasks within the visual feature space distribution — abstract reasoning tasks may not be well-represented. Overall, LiLa-WAM demonstrates that efficient, accessible WAMs are achievable, validating the guess that world-action models don't need massive compute to be useful.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: LiLa-WAM — A lightweight WAM with a compact latent reasoning space shared between future-state prediction and action generation, trained end-to-end on a single GPU with a language-free visual task representation (VTT).
- **Motivation**: Current WAMs are too computationally expensive for broad research adoption. Pixel-generation WAMs waste capacity; multi-stage latent WAMs have complex training pipelines. A single-GPU, end-to-end WAM would dramatically expand who can contribute to world model research.
- **Problem Solved**: 90.48% success across 50 RoboTwin 2.0 tasks with single-GPU training. Competitive performance on LIBERO and real-robot tasks. Demonstrates that lightweight latent reasoning can match or exceed heavier approaches.

### Academic Context

- **Inheritance / Response**: Builds on WAM literature (Fast-WAM, LeapBot-WA, Faster-WAM) and latent world model work. The VTT approach draws from visual feature direction work. Responds to the accessibility gap in WAM research — most WAMs require multi-GPU setups, excluding many researchers.
- **Implicit Connection**: LiLa-WAM represents the "democratization" direction within WAM research. LeCun's vision of autonomous intelligence requires practical, deployable systems — a world model that needs a datacenter GPU per robot defeats the purpose. LiLa-WAM shows that the efficiency frontier is farther than assumed: with careful design, WAMs can be both capable and accessible. The joint latent space design also prefigures the kind of unified representation LeCun envisions for world models that simultaneously support prediction and planning.
- **Research Line**: Efficient WAM — making world-action models practical and accessible.
- **Future Directions**: Extension to longer-horizon tasks; integration with VTT-based task libraries; combining with JEPA-style purely predictive objectives (eliminating reconstruction); multi-embodiment transfer via the VTT abstraction.
- **GitHub**: To be checked

---

## [2026-08-03] Faster-WAM: Do World Action Models Need Deep Action Modules?

- **arXiv**: [2608.02365](https://arxiv.org/abs/2608.02365)
- **Authors**: Liheng Ma, Rui Heng Yang, Zhanguang Zhang, Mateo Clemente, Ziwen Hu, Tongtong Cao, Yingxue Zhang
- **TL;DR**: Introduces Dock of Transformer (DoT), a video-centric design principle that docks lightweight output-heads onto a pretrained video backbone — showing that a single-layer action head can match deep action modules, achieving 3.2× inference speedup.
- **Problem**: Existing WAMs with shared-backbone or Mixture-of-Transformers designs tie the depth of the action module to the video backbone, resulting in substantial computational overhead and high inference latency. The assumption that action prediction needs deep processing alongside video understanding has not been empirically tested.
- **Architecture**: Faster-WAM — (1) **Dock of Transformer (DoT)** design principle: treats a pretrained video Transformer as a representation hub. Output heads (action, video, etc.) connect through "docking interfaces" that provide direct access to representations from ALL layers of the backbone, not just the final layer. This enables flexible head design independent of backbone depth. (2) **Faster-WAM instantiation**: docks a single-layer action head onto a 30-layer video backbone. The docking interface fuses keys and values from all video layers and applies RoPE realignment to maintain temporal consistency. (3) **No additional embodied pretraining** — uses the frozen video backbone as-is. Evaluated on LIBERO, RoboTwin 2.0, and LIBERO-Plus (out-of-distribution). Achieves 66.5ms per inference — 3.2× faster than Fast-WAM — with competitive action prediction and strong OOD generalization.
- **Compute Scale**: Mid (24G): Pretrained video backbone + single-layer action head. Inference latency 66.5ms (vs. 212ms for Fast-WAM).
- **LeCun Alignment**: MEDIUM-HIGH — Addresses a critical efficiency question for WAM deployment. STRENGTHS: (1) Empirical demonstration that deep action modules are unnecessary — the video backbone already captures sufficient dynamics for action prediction, supporting the argument that world models should be efficient. (2) The DoT design principle (backbone as hub, lightweight heads) mirrors LeCun's modular architecture where the world model provides representations consumed by the actor with minimal additional processing. (3) Strong out-of-distribution generalization suggests the video backbone's representations are robust, not overfit. WEAKNESSES: (1) Still uses generative video backbone (not JEPA-based), so the underlying representations come from a generative objective. (2) The action head is single-layer but still operates on deterministic representations — doesn't address uncertainty. Overall, Faster-WAM provides strong evidence that WAM action modules can be dramatically simplified, closing the gap between WAMs and deployable systems.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Faster-WAM — Test the hypothesis that WAM action modules don't need to be deep. The DoT design allows output heads to access all backbone layers, and experiments show a single-layer action head suffices.
- **Motivation**: WAMs are slow because action modules are unnecessarily deep. If action prediction can be done with a shallow head, WAMs become much more practical for real-time control. The key insight: the video backbone already captures rich dynamics — the action head just needs to read it out, not recompute it.
- **Problem Solved**: 3.2× inference speedup over Fast-WAM (66.5ms vs 212ms) with competitive performance. Strong OOD generalization on LIBERO-Plus. Demonstrates that action module depth is not the bottleneck in WAM performance.

### Academic Context

- **Inheritance / Response**: Builds on Fast-WAM and the Mixture-of-Transformers WAM design. The DoT principle generalizes beyond WAMs to any video-centric architecture. The finding that deep action modules are unnecessary challenges the prevailing WAM design philosophy.
- **Implicit Connection**: Faster-WAM and LiLa-WAM together establish a clear message: WAMs can be much more efficient than current practice assumes. Faster-WAM attacks the action module depth assumption; LiLa-WAM attacks the latent space complexity assumption. Both align with LeCun's emphasis on efficiency and modularity. The DoT design (backbone as hub) mirrors the world model module in LeCun's architecture: the world model is the central representation from which other modules (actor, cost) read.
- **Research Line**: Efficient WAM Architecture — questioning design assumptions to reduce computational overhead.
- **Future Directions**: DoT with JEPA-based backbones (rather than generative video backbones); multi-task heads docked on shared backbone; learned docking interfaces that adapt per task.
- **GitHub**: To be checked

---

## [2026-08-02] Asleep at the Wheel: JEPA's Limitations in Evaluating Novel Driving Data

- **arXiv**: [2608.01336](https://arxiv.org/abs/2608.01336)
- **Authors**: Advait Pavuluri, Shamik Karkhanis, Uzma Mushtaque
- **TL;DR**: Reveals that JEPA-based novelty detection for autonomous driving clips succeeds on cross-dataset protocols due to domain-shift artifacts, not genuine novelty recognition — collapsing to chance-level on fair single-dataset benchmarks.
- **Problem**: Autonomous driving fleets record far more video than humans can review. An automatic, label-free clip triage mechanism is needed to surface rare and review-worthy clips. JEPA-based prediction error seems like a natural solution — clips that are hard to predict should be novel/interesting. But does this actually work, or is it a domain-shift artifact?
- **Architecture**: A frozen V-JEPA video encoder is paired with a lightweight predictor head. The predictor reconstructs masked clip embeddings from context, and clips with high prediction error are flagged as "interesting/novel." Evaluated under two protocols: (1) Cross-dataset: train predictor on dataset A, test on dataset B — appears highly effective. (2) Single-dataset (fair benchmark): train and test on the same dataset — collapses to chance level, on par with simple no-training baselines. A lightly supervised probe on the same frozen embeddings achieves almost double the average precision, indicating the bottleneck is the self-supervised objective, not the representation quality.
- **Compute Scale**: Small-Mid (8-24G): Frozen V-JEPA encoder + lightweight predictor head. Inference only (no training of V-JEPA).
- **LeCun Alignment**: MEDIUM — Important cautionary finding for the JEPA research program. STRENGTHS: (1) Identifies a genuine limitation of JEPA representations: prediction error in latent space does not necessarily correspond to meaningful novelty — it can simply reflect domain shift. (2) The finding that a supervised probe dramatically outperforms JEPA prediction error suggests JEPA representations are good but the self-supervised objective is insufficient for certain downstream tasks. (3) Methodologically rigorous: demonstrates the danger of cross-dataset evaluation protocols that silently reward domain separation. WEAKNESSES: (1) Only tests one specific use case (clip triage/novelty detection) — doesn't evaluate JEPA for the core world model tasks (dynamics prediction, planning). (2) Uses frozen V-JEPA; fine-tuning might recover the gap. Overall, this is a valuable methodological contribution to the JEPA evaluation literature, highlighting the need for careful benchmark design and the limitations of self-supervised prediction error as a universal signal.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Asleep at the Wheel — Critically evaluate JEPA-based novelty detection for autonomous driving. Show that apparent success on cross-dataset benchmarks is an artifact of domain shift, not genuine novelty detection.
- **Motivation**: Self-supervised methods are increasingly proposed for safety-critical applications like autonomous driving. But evaluation protocols matter: cross-dataset evaluations can make methods look effective when they're just detecting domain differences, not meaningful anomalies.
- **Problem Solved**: Demonstrates that JEPA prediction error is not a reliable novelty signal on fair benchmarks. Provides a methodological template for evaluating self-supervised methods in safety-critical domains: always include a fair single-dataset baseline.

### Academic Context

- **Inheritance / Response**: Builds on V-JEPA and self-supervised anomaly detection literature. The core insight — cross-dataset evaluation can silently reward domain separation — is relevant to the broader SSL evaluation community, not just JEPA.
- **Implicit Connection**: This paper serves as a methodological check on the JEPA research program. The finding that JEPA representations are rich (supervised probe works well) but the self-supervised prediction error signal is unreliable is consistent with other JEPA critiques: JEPA learns good representations, but what you DO with those representations matters. The prediction error ≠ novelty finding parallels the prediction error ≠ control success finding (2607.10362) — in both cases, the raw self-supervised signal is insufficient for the downstream task without additional structure.
- **Research Line**: JEPA Evaluation & Limitations — understanding where and why JEPA-based approaches succeed or fail.
- **Future Directions**: Multi-objective JEPA for safety-critical tasks; combining JEPA prediction error with uncertainty quantification; developing JEPA-specific evaluation protocols that avoid domain-shift confounds.
- **GitHub**: To be checked

---

## [2026-07-31] Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving

- **arXiv**: [2607.29031](https://arxiv.org/abs/2607.29031)
- **Authors**: Jiwei Yang, Zhengxian Chen, Chaosheng Huang, Jun Li
- **TL;DR**: An action-oriented JEPA world model for autonomous driving that predicts future driving "intent" (a latent aligned with future ego trajectory) instead of dense future-world reconstruction — achieving 91.3 PDMS on NAVSIM v1 with a frozen visual encoder and no explicit perception annotations.
- **Problem**: Existing autonomous-driving world models perform dense prediction of future videos, occupancy states, BEV representations, or agent motion. Planning doesn't need to reconstruct the complete future world — it only needs to focus on scene features that affect future ego action. Dense prediction wastes capacity on planning-irrelevant details.
- **Architecture**: Auto-JEPA — (1) **Frozen visual encoder** processes visual observations (no fine-tuning needed). (2) **Intent predictor** takes visual features, egomotion history, and navigation commands to predict an "intent embedding" — a latent representation aligned with the future ego trajectory's latent representation. This is pure JEPA-style latent prediction: the target is the EMA encoder's representation of the actual future trajectory. (3) **Trajectory memory**: a fixed bank of executable trajectories. The predicted intent retrieves the closest trajectory from this memory (no learned trajectory generator). (4) **Candidate selection module**: scene-conditioned ranking of retrieved trajectories. Key findings: 91.3 PDMS on NAVSIM v1, 89.1 EPDMS on NAVSIM v2. Semantic occlusion experiments: masking dynamic-agent regions induces an average intent change 2.97× that of equal-area random masking. Crucially, occluding vehicles that affect future driving substantially changes predicted intent+trajectory, while occluding non-influential vehicles leaves both unchanged — demonstrating that intent prediction forces the model to focus on planning-relevant visual features.
- **Compute Scale**: Mid (24G): Frozen visual encoder + lightweight intent predictor + fixed trajectory memory. No perception annotations, no learned trajectory generator.
- **LeCun Alignment**: HIGH — This is one of the cleanest instantiations of LeCun's world model vision for a specific domain. STRENGTHS: (1) Pure JEPA: predicts in latent space (intent embedding) rather than pixels/BEV/occupancy — directly instantiates the core JEPA principle. (2) Action-oriented: the prediction target (future ego trajectory) is what matters for planning, not what the whole world looks like — aligning with LeCun's argument that world models should predict abstractions relevant to action. (3) Frozen encoder + lightweight predictor: follows the JEPA pattern of learning the predictor while the encoder provides stable targets. (4) The semantic occlusion experiments are a beautiful demonstration that the model learns to attend to causally relevant features — exactly the kind of "understanding" LeCun argues is missing from generative approaches. (5) No explicit perception annotations (no object detection, lane detection, etc.) — the model discovers planning-relevant structure from the predictive objective alone. WEAKNESSES: (1) The trajectory memory is fixed — doesn't learn or adapt. (2) Limited to short-horizon prediction (trajectory retrieval), not open-ended planning. (3) Evaluated only in simulation (NAVSIM), not real-world driving. Overall, Auto-JEPA is a compelling demonstration that JEPA principles can be applied to autonomous driving, producing a model that focuses on causally relevant features without needing dense world reconstruction.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Auto-JEPA — Replace dense future-world prediction in autonomous driving world models with intent prediction: learn to predict a latent embedding aligned with future ego trajectory, and use it to retrieve executable trajectories. The model learns to attend to planning-relevant scene features without explicit supervision.
- **Motivation**: Dense prediction (video, BEV, occupancy) is the wrong objective for driving world models — most predicted information is irrelevant to the driving decision. Intent prediction in latent space is cheaper, more focused, and yields better planning by construction.
- **Problem Solved**: 91.3 PDMS on NAVSIM v1 (competitive with dense-prediction approaches at lower cost). Semantic occlusion experiments prove the model attends to causally relevant agents — a qualitative property that dense prediction approaches don't guarantee.

### Academic Context

- **Inheritance / Response**: Builds on JEPA (I-JEPA, V-JEPA) and applies it to autonomous driving. Responds to the dense-prediction world model paradigm (UniAD, VAD, GAIA-1) by proposing a leaner alternative. The intent embedding approach connects to trajectory prediction and motion forecasting literature.
- **Implicit Connection**: Auto-JEPA provides a concrete domain-specific validation of LeCun's core argument: predicting the right abstraction (intent) is more efficient and more causally grounded than predicting everything (pixels/occupancy). The semantic occlusion experiments are exactly the kind of causal probing that LeCun advocates for evaluating whether world models truly "understand" their domain. This paper could serve as a template for JEPA-based world models in other domains: identify the action-relevant abstraction, predict it in latent space, and validate with causal interventions.
- **Research Line**: JEPA for Autonomous Driving — applying predictive architectures to replace dense world reconstruction for ego-motion planning.
- **Future Directions**: Learned trajectory generation (beyond fixed memory); multi-modal intent prediction (multiple plausible futures); real-world deployment; hierarchical intent prediction (short-term trajectory + long-term route); combining with JEPA-based prediction of other agents' intents.
- **GitHub**: To be checked

---

## [2026-07-31] EEG-JEPA: Structured Latent Prediction for EEG Foundation Models

- **arXiv**: [2608.00114](https://arxiv.org/abs/2608.00114)
- **Authors**: Jinhao Li, Zhiyuan Ma, Xueqiao Han, Zhongye Xia, Xinche Zhang, Shanghong Xie, Yixuan Liu, Yongjian Li, Runmin Gan, Tianlin Huo, Sen Song
- **TL;DR**: Applies JEPA to EEG foundation modeling with structured latent prediction — replacing waveform reconstruction with Neurotopology-Aware Multi-scale Electrode-Temporal Masking (N-MET) — improving 14-task frozen accuracy from 40.49% to 50.42%.
- **Problem**: EEG foundation models are typically pretrained via masked waveform reconstruction, but applying supervision directly to noisy EEG encourages models to recover predictable background activity, acquisition effects, and artifacts rather than neural structure that transfers across tasks. What should an EEG model predict to learn transferable representations?
- **Architecture**: EEG-JEPA — A structured latent-prediction framework with three design dimensions: (1) **Target content**: what representation is predicted (contextual latent states from an EMA target encoder observing the complete input, rather than raw voltages). (2) **Target support**: where prediction occurs, defined by Neurotopology-Aware Multi-scale Electrode-Temporal Masking (N-MET) — structured electrode–time region masks informed by known neurophysiological topology rather than random patches. (3) **Target depth**: at which encoder layers supervision is applied (multi-layer rather than only final-layer). Trained with the standard JEPA pipeline: context encoder (masked input) → predictor → target encoder (full input, EMA). Evaluated via controlled objective comparisons, frozen multitask transfer (14 tasks), and full fine-tuning (9 tasks). Under protocol-matched full fine-tuning, improves 9-task average balanced accuracy from 68.98% to 70.65%.
- **Compute Scale**: Mid (24G): EEG foundation model pretraining. Standard EEG datasets (TUH EEG, etc.).
- **LeCun Alignment**: MEDIUM — Cross-domain JEPA validation with domain-specific structural innovations. STRENGTHS: (1) Pure JEPA architecture applied to a novel modality — demonstrates JEPA's generality beyond vision/audio. (2) The three-dimensional target design (content, support, depth) is a principled framework for adapting JEPA to structured sensor data — the N-MET masking strategy in particular incorporates domain knowledge (neurophysiological topology) into the masking pattern, a practice LeCun advocates (build in known structure rather than learning it from data). (3) Strong frozen transfer results suggest JEPA representations are more task-agnostic than reconstruction-based representations. WEAKNESSES: (1) EEG is a clinical/scientific modality, far from embodied AI — doesn't directly advance the autonomous intelligence agenda. (2) No action conditioning — purely representation learning. (3) The N-MET masking strategy is domain-specific and doesn't generalize to other sensor modalities. Overall, EEG-JEPA is valuable cross-domain validation showing that JEPA's structured latent prediction beats raw reconstruction for scientific sensor data, continuing the pattern of Crys-JEPA, Rad-JEPA 3D, and IQ-JEPA.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: EEG-JEPA — Apply JEPA to EEG with structured latent prediction guided by neurophysiological topology (N-MET masking). Shift the pretraining objective from "reconstruct missing voltages" to "infer latent neural states from structured electrode-time context."
- **Motivation**: EEG is noisy. Reconstruction-based pretraining learns to recover noise and artifacts rather than neural structure. JEPA's latent prediction in a structured target space forces the model to learn the underlying neural dynamics that generalize across tasks.
- **Problem Solved**: EEG-JEPA improves 14-task frozen macro balanced accuracy from 40.49% (waveform reconstruction baseline) to 50.42%. Multi-source continuation further raises this to 52.94% — the highest among EEG foundation models on EEG-FM-Bench. Full fine-tuning also improves (68.98% → 70.65%).

### Academic Context

- **Inheritance / Response**: Builds on I-JEPA, the EEG foundation model literature (CBraMod, etc.), and masked pretraining for time-series data. The three-dimensional target design framework (content, support, depth) generalizes the JEPA masking strategy beyond vision.
- **Implicit Connection**: EEG-JEPA continues the pattern of cross-domain JEPA validation (Crys-JEPA for materials, Rad-JEPA 3D for CT, IQ-JEPA for ultrasound, JEPA-CFM for wireless). The common thread: reconstruction is a bad objective for scientific sensor data because it learns noise and artifacts; JEPA's latent prediction focuses on the underlying structure. This validates LeCun's claim that predicting in representation space is superior to reconstructing in input space, across a remarkably diverse set of domains. The N-MET masking strategy also demonstrates how domain knowledge can be incorporated into JEPA through structured masking — a design pattern applicable to other sensor modalities with known spatial/topological structure.
- **Research Line**: Scientific JEPA — adapting JEPA to scientific sensor modalities where reconstruction-based pretraining fails.
- **Future Directions**: Multi-modal EEG+fMRI JEPA; real-time clinical deployment; extension to other biosignals (ECG, EMG); learned (rather than predefined) neurophysiological topologies for N-MET.
- **GitHub**: To be checked

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

## [2026-08-07] PSG-JEPA: Is Forward Prediction Enough? Physical State Grounding for JEPA World Models

- **arXiv**: [2608.06799](https://arxiv.org/abs/2608.06799)
- **Authors**: Haodong Yan, Jiaguan Zhu, Mingyuan Jia, Ruiqing Yin, Junjie He, Zhide Zhong, Junfeng Li, Jinxuan Lu, Hengtao Li, Tianran Zhang, Jiayi Chen, Wenxuan Song, Wen Chen, Yuxiang Gao, Haoang Li
- **TL;DR**: Extends JEPA world models with two training-only physical grounding objectives — proprioceptive state regression and multi-horizon joint-angle change prediction — to enforce reliable identifiability of robot-centric physical state without adding inference overhead.
- **Problem**: JEPA-based world models learn action-conditioned latent dynamics from observations, but their forward-prediction objectives do not explicitly enforce that individual latents encode robot proprioceptive state or that latent pairs encode joint-angle changes. This limits identifiability and degrades downstream planning/policy performance.
- **Architecture**: PSG-JEPA — (1) Standard JEPA encoder-predictor backbone for action-conditioned latent dynamics. (2) Two complementary grounding heads applied ONLY during training: **Proprioceptive grounding**: predicts robot's physical state (joint positions, velocities) from individual latent vectors — ensures each latent carries robot-relevant physical information. **Motion grounding**: predicts multi-horizon joint-angle changes from latent pairs — ensures latent transitions encode physically meaningful motion. (3) Both heads are removed at inference — zero computational overhead. (4) Evaluated at three levels: latent identifiability (probing), goal-conditioned planning on frozen latents, and policy learning in simulation + real robot.
- **Compute Scale**: Mid (24G): Standard JEPA backbone with lightweight grounding heads added during training only.
- **LeCun Alignment**: HIGH — Directly addresses a core challenge in JEPA world models. STRENGTHS: (1) Explicitly grounded in LeCun's architectural philosophy — the question "Is forward prediction enough?" mirrors LeCun's argument that predictive objectives alone don't guarantee structured representations. (2) The training-only heads with zero inference overhead align with JEPA's efficiency principle: learn better during training, keep inference simple. (3) Multi-level evaluation (identifiability → planning → real robot) provides comprehensive validation. (4) The proprioceptive grounding directly connects latent space to physical reality — addressing the "grounding problem" that LeCun identifies as critical for world models. WEAKNESSES: (1) Relies on access to proprioceptive state during training — assumes robot-specific sensors. (2) Large author list suggests industry involvement. Overall, PSG-JEPA is a natural next step for the JEPA world model research program.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Two complementary physical grounding objectives (proprioceptive + motion) that supplement JEPA's forward-prediction loss during training, with zero inference overhead.
- **Motivation**: Forward prediction alone produces latents that may not be identifiable or control-relevant. Physical grounding ensures latent space structure aligns with robot physics.
- **Problem Solved**: Improved latent identifiability, better planning from frozen latents, and superior real-robot policy learning — all without architectural changes at inference time.

### Academic Context

- **Inheritance / Response**: Builds directly on JEPA world models (LeWM, MC-JEPA, V-JEPA) and addresses a documented weakness: the gap between predictive accuracy and control utility.
- **Implicit Connection**: The "training-only heads" pattern mirrors JEPA's own design philosophy (target encoder exists only during training). PSG-JEPA shows this pattern generalizes to physical grounding.
- **Research Line**: JEPA World Model Grounding — ensuring JEPA latents encode physically meaningful information.
- **Future Directions**: Extending to other modalities (force/torque, tactile); multi-embodiment grounding; theoretical analysis of when grounding objectives are necessary vs. when forward prediction suffices.
- **GitHub**: Not found

---

## [2026-08-07] Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection

- **arXiv**: [2608.06706](https://arxiv.org/abs/2608.06706)
- **Authors**: Jiazhuo Li, Yiming Fei, Zhiruo Zhou, Heikichi Hayashi
- **TL;DR**: Borrows the dueling network decomposition from DRL — subtracting the action-mean from latent predictions cancels action-independent distractors, isolating a clean controllable channel with zero auxiliary loss and working post hoc on frozen models.
- **Problem**: Latent world models go "action-blind" when scenes contain motion the agent doesn't control — predictions for different actions become indistinguishable even as training loss improves. Existing remedies add reconstruction, task reward, or auxiliary objectives.
- **Architecture**: Dueling World Models — (1) **Core insight**: In latent dynamics, subtracting the mean effect over actions cancels whatever the actions share (action-independent variation where distractors live), leaving a clean controllable channel. (2) **Zero-overhead design**: This is only a subtraction at readout time — no auxiliary losses, no reward signal, no distractor-specific machinery. (3) **Post hoc applicability**: Works on ANY action-conditioned world model, including frozen pretrained ones. (4) **Theoretical guarantee**: Proves exact cancellation in finite samples for both discrete and sampled action sets. (5) **Validated across**: Gridworld, synthetic generators with known factors, distracting continuous control, and natural-pixel Atari.
- **Compute Scale**: Mid (24G): Works with any existing action-conditioned world model at readout time — negligible overhead.
- **LeCun Alignment**: MEDIUM-HIGH — Elegant and principled approach to a practical problem. STRENGTHS: (1) The minimal-intervention philosophy (subtraction at readout, no auxiliary objectives) aligns with JEPA's emphasis on architectural simplicity. (2) Post hoc applicability to frozen models is powerful — you can retrofit existing world models with distractor robustness. (3) The theoretical guarantee (exact cancellation) provides rigor rare in world model research. (4) Directly addresses the "action-blindness" problem that undermines world model planning. WEAKNESSES: (1) Mathematical limitation: distractors whose motion tracks the action cannot be cancelled (acknowledged in appendix). (2) Evaluated on relatively simple domains — real-world validation pending. (3) Does not propose a new architecture — it's a technique that can be applied to existing models. Overall, a clever, principled contribution that deserves attention from the WAM community.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Dueling decomposition for latent dynamics — subtract action-mean to isolate controllable channels, no training changes needed.
- **Motivation**: World models fail silently under distractors, with training loss improving while discriminability collapses. A minimal readout-time fix is preferable to adding complex auxiliary objectives.
- **Problem Solved**: Distractor rejection in action-conditioned world models with zero additional training cost, working even on frozen pretrained models.

### Academic Context

- **Inheritance / Response**: Borrows from the dueling network architecture (Wang et al., 2016) in DRL and applies the decomposition to latent world model dynamics rather than value functions.
- **Implicit Connection**: The action-mean subtraction is conceptually similar to JEPA's latent prediction — both avoid modeling the full observation distribution and instead focus on what changes with the action.
- **Research Line**: Robust World Models — making latent dynamics robust to uncontrolled scene variation.
- **Future Directions**: Real-robot validation; combining with JEPA architectures; extending to multi-agent scenarios with multiple controllable agents.
- **GitHub**: Not found

---

## [2026-08-07] PILOT: Decoupling Intention from Trajectory — A Representational Deduction Framework for World Action Models

- **arXiv**: [2608.06994](https://arxiv.org/abs/2608.06994)
- **Authors**: Xiangkai Ma, Yue Ma, Junjie Wang, Sheng Xu, Mingyang Li, Han Zhang, Yuzheng Zhuang, Wenzhong Li, Zhihao Yuan
- **TL;DR**: Introduces Representational Deduction (RD) for WAMs — motion chain-of-thought tokens that decouple high-level physical condition evolution from low-level action trajectory, bridging the gap between visual prediction and action generation.
- **Problem**: Existing WAM visual branches predict static future observations rather than reflecting state transition information. This entangles high-level physical condition evolution with low-level action trajectory generation in the Action Model, creating a structural bottleneck.
- **Architecture**: PILOT — (1) **Representational Deduction (RD)**: Encourages the action branch to explicitly model potential state transition tokens, which are retained as chain-of-thought (CoT) in the reasoning space to guide fine-grained motion trajectory. (2) **Decoupling principle**: RD separates "what the world will look like" (visual prediction) from "how we should move" (action generation) — the visual branch handles prediction, RD in the action branch handles motion semantics. (3) **State transition supervision**: RD introduces abundant state transition signals that alleviate sparse supervision in action generation, enabling efficient few-shot real-robot finetuning. (4) **Scalability**: Demonstrates superior scalability for migration to mainstream WAM architectures.
- **Compute Scale**: Large (40G+): Mainstream WAM architectures (video backbone + action diffusion) with additional RD module.
- **LeCun Alignment**: MEDIUM-HIGH — Addresses the representation entanglement problem that LeCun identifies as critical. STRENGTHS: (1) The explicit decoupling of "world state evolution" from "action trajectory" mirrors LeCun's modular agent architecture where the world model and the actor are separate modules with different objectives. (2) Motion chain-of-thought as a native model capability aligns with the idea that planning should emerge from the architecture, not be bolted on. (3) The few-shot real-robot finetuning capability demonstrates practical value. WEAKNESSES: (1) Operates in pixel space (video generation) rather than latent space — not fully JEPA-aligned. (2) Adds complexity to already-large WAM architectures. (3) Large author list. Overall, PILOT moves WAMs toward better representation structure — the RD concept could be adapted to JEPA-based WAMs.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Representational Deduction — explicit state transition tokens as chain-of-thought in the action branch, decoupling physical condition evolution from trajectory generation.
- **Motivation**: Current WAMs conflate "predicting what happens" with "deciding what to do" — these are fundamentally different computations that should be architecturally separated.
- **Problem Solved**: Improved WAM success rate, generalization, and physical interpretability; efficient few-shot real-robot finetuning via abundant state transition supervision.

### Academic Context

- **Inheritance / Response**: Builds on the WAM literature (Fast-WAM, Joint-WAM) and identifies a structural bottleneck in their unified visual-action architecture.
- **Implicit Connection**: The decoupling principle aligns with LeCun's modular agent architecture where the world model predicts state transitions and the actor/policy uses those predictions for planning.
- **Research Line**: WAM Architecture Design — improving the interface between visual prediction and action generation.
- **Future Directions**: Adapting RD to JEPA-based WAMs (latent prediction instead of pixel prediction); theoretical analysis of the decoupling guarantee.
- **GitHub**: Not found

---

## [2026-08-07] DPWM: Beyond Myopic World Models — Long-Horizon End-to-End Training for Direct Future Prediction

- **arXiv**: [2608.07420](https://arxiv.org/abs/2608.07420)
- **Authors**: Xinyi Li, Zaishuo Xia, Chenjie Hao, Yubei Chen
- **TL;DR**: Proposes Direct Prediction World Model (DPWM) — a non-recursive architecture that compresses arbitrary-length action sequences into a single embedding and predicts the endpoint in one forward pass, avoiding the recursive error amplification that plagues autoregressive world models.
- **Problem**: World models are trained with local few-step prediction objectives but deployed via recursive rollout — creating a fundamental mismatch where small local errors amplify through the trajectory and transitions with different downstream influence are treated uniformly during training.
- **Architecture**: DPWM — (1) **Non-recursive design**: Compresses an action sequence of arbitrary length into a single embedding via a sequence encoder, then predicts the endpoint observation in a single forward pass. No recurrent rollout in either prediction or gradient propagation. (2) **Key insight**: The training objective (long-horizon endpoint prediction), not the backbone architecture, is the main driver of long-horizon accuracy. Recurrent baselines benefit similarly when retrained with the same endpoint objective. (3) **Empirical results**: DPWM substantially improves long-horizon endpoint prediction over recursive world-model baselines on continuous-control and pixel-based benchmarks, with larger gains as prediction horizon increases.
- **Compute Scale**: Mid (24G): Single-pass predictor, no recurrent unrolling — actually more efficient at long horizons than recursive alternatives.
- **LeCun Alignment**: MEDIUM-HIGH — The philosophy of "predict what matters, not the intermediate steps" aligns with JEPA's emphasis on abstract prediction. STRENGTHS: (1) The direct prediction paradigm avoids the compounding error problem that LeCun identifies as a weakness of autoregressive generation. (2) The finding that the objective (not architecture) drives accuracy is important — it supports the JEPA argument that what you predict matters more than how you generate. (3) Non-recursive design is inherently more efficient at long horizons — consistent with JEPA's emphasis on computational efficiency. (4) The paper shifts focus from "local transition modeling" to "long-horizon predictive accuracy" — exactly the shift LeCun advocates. WEAKNESSES: (1) Still operates in observation space (pixel prediction) rather than latent space — endpoint prediction could be even more effective in JEPA's latent space. (2) The action sequence compression may lose fine-grained control information. (3) Short author list from a single institution — limited external validation. Overall, DPWM provides strong empirical evidence for a key JEPA principle: how you train matters more than what architecture you use.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Direct Prediction World Model — compress action sequence into embedding, predict endpoint in one pass, no recursive rollout.
- **Motivation**: Recursive rollout amplifies errors; long-horizon prediction needs direct optimization of the endpoint, not local transition fidelity.
- **Problem Solved**: Substantially improved long-horizon endpoint prediction; demonstrated that training objective (not architecture) is the key driver.

### Academic Context

- **Inheritance / Response**: Challenges the dominant recursive world model paradigm (Dreamer, RSSM-based models) by showing that direct endpoint prediction outperforms recursive approaches at long horizons.
- **Implicit Connection**: The non-recursive, single-pass design echoes JEPA's philosophy of predicting the abstract future state directly rather than iteratively generating intermediate states. Combining DPWM's endpoint objective with JEPA's latent prediction could be powerful.
- **Research Line**: Training Objectives for World Models — rethinking how we train world models for the timescales where they're actually used.
- **Future Directions**: Latent-space DPWM (JEPA + direct prediction); multi-horizon endpoint prediction; integration with planning algorithms that only need endpoint states.
- **GitHub**: Not found

---

## [2026-08-06] TaskSense: Focusing on What Matters in World Models

- **arXiv**: [2608.06544](https://arxiv.org/abs/2608.06544)
- **Authors**: SM Mazharul Islam, Manfred Huber
- **TL;DR**: Task-centric world model with stochastic spatial attention + inverse-dynamics objective — reconstructs ONLY task-relevant attended regions (not full observations), improving robustness to visual distractors over DreamerV3.
- **Problem**: World models for visual control reconstruct full observations, encouraging latent representations to preserve all visual information — but task-relevant content occupies a small fraction of the observation. This biases latents toward task-irrelevant content and degrades performance under visual distractions.
- **Architecture**: TaskSense — (1) **Differentiable stochastic spatial attention**: Conditioned on the previous latent state, attends to task-relevant regions BEFORE latent encoding. (2) **Inverse-dynamics auxiliary objective**: Steers attention toward control-relevant regions by predicting actions from latent pairs. (3) **Partial reconstruction**: Reconstructs ONLY the attended regions, encouraging latents to discard irrelevant visual content. Decoder conditioned on attention map for consistent reconstruction despite stochastic sampling. (4) **Results**: Competitive with DreamerV3 on standard DMC, consistently outperforms on Distracting Control Suite.
- **Compute Scale**: Mid (24G): DreamerV3 backbone + attention mechanism + inverse dynamics head.
- **LeCun Alignment**: MEDIUM — The partial reconstruction principle is JEPA-aligned. STRENGTHS: (1) "Reconstruct what matters, not everything" is philosophically aligned with JEPA's "predict in latent space, not pixel space." (2) Inverse-dynamics for attention steering is a clean, unsupervised way to identify task-relevant regions. (3) Outperforms DreamerV3 on distractors — practical validation of the principle. WEAKNESSES: (1) Still uses pixel reconstruction (partial) rather than pure latent prediction. (2) Built on DreamerV3, not JEPA. (3) Short author list. Overall, TaskSense provides additional evidence that reconstruction-free or partial-reconstruction approaches outperform full-reconstruction world models under distraction.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Task-centric world model with attention + inverse dynamics that only reconstructs task-relevant regions.
- **Motivation**: Full observation reconstruction wastes capacity on distractors. Task-relevant attention before encoding + partial reconstruction solves this.
- **Problem Solved**: Improved robustness to visual distractions over DreamerV3, while maintaining competitive clean-scene performance.

### Academic Context

- **Inheritance / Response**: Builds on DreamerV3 and addresses its known weakness with visual distractors. The partial-reconstruction approach is a step toward JEPA's no-reconstruction paradigm.
- **Implicit Connection**: TaskSense validates a key JEPA motivation: reconstructing full observations hurts world model quality. As a "halfway" approach (partial reconstruction), it provides a bridge between Dreamer-style world models and JEPA.
- **Research Line**: Distractor-Robust World Models — making world models focus on what matters for control.
- **Future Directions**: Full latent prediction (JEPA-style) with task-centric attention; combining with dueling world models for complementary distractor robustness.
- **GitHub**: Not found

---

## [2026-08-07] Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking

- **arXiv**: [2608.07077](https://arxiv.org/abs/2608.07077)
- **Authors**: Devin Pereira, Willem Zuidema
- **TL;DR**: Mechanistic interpretability study showing Transformers DO develop linearly decodable emergent world models (geometrically faithful Sierpinski triangle representations of the Tower of Hanoi state space) but FAIL to use them effectively for planning — the architecture limits planning even when the world model is present.
- **Problem**: Large reasoning models struggle with the Tower of Hanoi puzzle. Using mechanistic interpretability, the authors investigate whether this is because they lack world models or because they can't use them.
- **Architecture**: N/A (interpretability study) — (1) **Small Transformers trained from scratch** on precomputed Hanoi solution traces. (2) **Interpretability techniques** reveal a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle). (3) **Key finding**: The world model IS present and IS accurate — but the Transformer architecture cannot effectively USE it for multi-step planning. (4) **Large reasoning models** (GPT-4, Claude, etc.) show the same pattern: they have the knowledge but can't execute the plan.
- **Compute Scale**: Small (8-12G): Small Transformers trained from scratch on synthetic puzzle data.
- **LeCun Alignment**: MEDIUM — Indirect but important validation of LeCun's architectural argument. STRENGTHS: (1) The core finding — "having a world model ≠ being able to use it for planning" — directly supports LeCun's claim that architecture determines planning capability, not just knowledge. (2) The mechanistic evidence (linearly decodable world model that the model fails to use) is compelling. (3) Extends to large models (GPT-4, Claude), showing this is not just a small-model phenomenon. WEAKNESSES: (1) About Transformers/LLMs, not JEPA or WAMs directly. (2) The Tower of Hanoi is a discrete puzzle — may not generalize to continuous control. (3) No proposed solution. Overall, this paper provides ammunition for the argument that world models need dedicated planning architectures — exactly what JEPA-based MPC and hierarchical planning aim to provide. Worth citing as evidence that "emergence" is not enough.
- **GitHub**: Not found

### What / Why / Solve

- **Proposal**: Mechanistic interpretability study demonstrating the gap between having a world model and using it for planning.
- **Motivation**: Understanding WHY large models fail at planning tasks requires looking inside — are they missing world knowledge or missing planning capability?
- **Problem Solved**: Provides clear evidence that planning failure is architectural, not knowledge-based: the world model is there but the architecture can't leverage it.

### Academic Context

- **Inheritance / Response**: Builds on mechanistic interpretability literature and the "world models in LLMs" debate. Provides empirical grounding for the theoretical argument that world models need appropriate planning architectures.
- **Implicit Connection**: Directly supports LeCun's architectural position: you can't just train a big model and expect planning to emerge — you need architectures designed for planning (like JEPA + MPC). The paper's title "The Illusion of Thinking" echoes LeCun's skepticism about LLM reasoning.
- **Research Line**: World Model Utilization — understanding when and why learned world models succeed or fail at supporting planning.
- **Future Directions**: Testing whether JEPA-based architectures + MPC planning can solve the Tower of Hanoi variants that Transformers fail on; extending the interpretability framework to continuous-control world models.
- **GitHub**: Not found


*Generated: 2026-08-18 | Papers: 162 | Daily scan: 5 papers (Marionette, Traj-LeWM, Onto-EV-WM, Twin, ForgeWM); Aug 14 batch — arXiv stream ends at Aug 14 submission date*
