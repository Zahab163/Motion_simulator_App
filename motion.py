# motion.py

class Body:
    def __init__(self, position=0.0, velocity=0.0, acceleration=0.0, time=0.0):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.time = time

    def update(self, time_step):
        """
        Updates the position and velocity using simple kinematic equations.
        Assumes constant acceleration over the time step.
        """
        self.position += self.velocity * time_step + 0.5 * self.acceleration * (time_step ** 2)
        self.velocity += self.acceleration * time_step

    def get_state(self):
        """
        Returns the current position and velocity as a dictionary.
        """
        return {
            "position": round(self.position, 2),
            "velocity": round(self.velocity, 2)
        }