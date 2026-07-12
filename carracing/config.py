"""
CarRacing x LeCun World Model — Hyperparameters
"""

class Config:
    # ── Environment ──
    env_name = "CarRacing-v2"
    frame_size = 96
    frame_stack = 1        # We use GRU memory instead of stacking
    action_dim = 3         # [steer, gas, brake]
    action_bounds = [
        (-1.0, 1.0),       # steer
        (0.0, 1.0),        # gas
        (0.0, 1.0),        # brake
    ]

    # ── Perception ──
    s_dim = 256            # Visual representation dimension
    h_dim = 256            # GRU hidden state dimension
    cnn_channels = [32, 64, 128, 256]
    cnn_kernel = 3
    cnn_stride = 2
    res_blocks = 2

    # ── World Model (JEPA) ──
    dynamics_hidden = 512
    dynamics_layers = 3
    ema_decay = 0.999      # Target encoder EMA rate

    # ── Cost Head ──
    cost_hidden = [128, 64]
    cost_dims = 4          # [progress, on_track, speed, energy]
    w_progress = 1.0
    w_track = 5.0          # Most important: stay on road!
    w_speed = 0.5
    w_energy = 0.1

    # ── Configurator ──
    scene_classes = 4      # [straight, turn_L, turn_R, chicane]
    scene_history = 10     # Frames to average for auto-labeling

    # ── Actor (CEM) ──
    plan_horizon = 8       # Planning horizon H
    cem_candidates = 64    # Number of candidate sequences K
    cem_elites = 8         # Number of elite sequences M
    cem_iterations = 3     # CEM refinement rounds
    cem_gamma = 0.95       # Discount factor
    cem_sigma_init = 0.3   # Initial exploration noise

    # ── Training ──
    lr = 3e-4
    batch_size = 128       # Reduced for 8G VRAM safety
    buffer_capacity = 50000
    total_env_steps = 100000
    grad_clip = 1.0
    weight_decay = 1e-5

    # ── Exploration ──
    eps_start = 1.0
    eps_end = 0.05
    eps_decay_steps = 50000

    # ── Checkpointing ──
    save_interval = 5000   # Save model every N env steps
    eval_interval = 2000   # Evaluate every N env steps
    eval_episodes = 5

    # ── Device ──
    device = "cuda"
