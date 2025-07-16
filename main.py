#motion_simulator/
#├── main.py              # Entry point for local testing
#├── app.py               # Streamlit interface
#├── motion.py            # Body class + kinematics logic
#├── simulator.py         # Runs simulation with time steps
#├── utils.py             # Input checks, formatting tools
#├── data/
#│   └── history.json     # Optional session logging
#├── requirements.txt
#└── README.md            # Project overview + usage

# main.py

from motion import Body
from simulator import run_simulation
from utils import format_output

# Create a body with initial parameters
obj = Body(position=0, velocity=10, acceleration=-9.8)

# Set simulation parameters
time_step = 0.1  # seconds
duration = 2.0   # total time in seconds

# Run simulation
history = run_simulation(obj, time_step, duration)

# Output results
for t, state in history.items():
    print(format_output(t, state))