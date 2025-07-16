# utils.py

def format_output(time, state):
    """
    Formats simulation output for display.
    Example: Time: 1.0s | Position: 4.90 m | Velocity: 0.20 m/s
    """
    return f"Time: {time:.2f}s | Position: {state['position']} m | Velocity: {state['velocity']} m/s"

def validate_inputs(mass, velocity, acceleration, time):
    """
    Validates user input values.
    Returns True if all values are non-negative and mass > 0.
    """
    if mass <= 0:
        return False
    if time < 0:
        return False
    return True

def compute_kinematic_values(u, a, t):
    """
    Calculates final velocity and displacement using physics formulas:
    v = u + at
    s = ut + 0.5 * a * t²
    Returns a dictionary with both values.
    """
    v = u + a * t
    s = u * t + 0.5 * a * t ** 2
    return {"final_velocity": round(v, 2), "displacement": round(s, 2)}

import json
from datetime import datetime

def log_simulation_to_json(filename, session_data):
    try:
        with open(filename, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(session_data)

    with open(filename, "w") as f:
        json.dump(logs, f, indent=2)