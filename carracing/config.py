"""
CarRacing x LeCun World Model — Hyperparameters
"""

class Config:
    # ── Environment ──
    env_name = "CarRacing-v2"
    frame_size = 96
    # Image crop: remove bottom dashboard + side margins
    crop_top = 0
    crop_bottom = 84       # Cut off bottom black dashboard area
    crop_left = 6          # Cut off left edge noise
    crop_right = 90        # Cut off right edge noise
    cropped_size = crop_bottom - crop_top  # 84
    cropped_width = crop_right - crop_left  # 84
    # Frame skip: repeat same action for N env steps
    frame_skip = 5         # 1 action → 5 env steps (accumulate reward)
    # We use GRU memory instead of FrameStack
    frame_stack = 1        # GRU handles temporal memory internally
    action_dim = 3          # [steer, gas, brake]
    action_bounds = [
        (-1.0, 1.0),       # steer
        (0.0, 1.0),        # gas
        (0.0, 1.0),        # brake
    ]
    # Out-of-track detection
    out_of_track_penalty = -10.0  # Reward penalty when car leaves road

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
    total_env_steps = 100000  # Physical env steps (with frame_skip=5, ~20K RL steps)
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
