# simulator.py

def run_simulation(body, time_step, duration):
    """
    Simulates the motion of a single Body object over time.
    Uses kinematic updates and stores the state at each time step.
    Returns a dictionary of {time: state}.
    """
    total_time = body.time
    num_steps = int(duration / time_step)
    #rest of the logic
    history = {}
    current_time = 0.0

    for _ in range(num_steps + 1):
        state = body.get_state()
        history[round(current_time, 2)] = state
        body.update(time_step)
        current_time += time_step

    return history