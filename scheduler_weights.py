import numpy as np

class SchedulerWeightController:
    def __init__(self, n_classes):
        self.n_classes = n_classes

    def apply(self, action):
        exp = np.exp(action - np.max(action))
        return exp / exp.sum()
