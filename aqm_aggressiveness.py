class AqmAggressivenessController:
    def __init__(self, theta_min=0.0, theta_max=0.05):
        self.theta_min = theta_min
        self.theta_max = theta_max

    def apply(self, action):
        return self.theta_min + (action + 1) / 2 * (
            self.theta_max - self.theta_min
        )
