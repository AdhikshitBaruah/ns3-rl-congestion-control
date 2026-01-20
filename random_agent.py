import numpy as np

class RandomAgent:
    def act(self, n_classes, n_flows):
        return {
            "scheduler": np.random.randn(n_classes),
            "aqm": np.random.uniform(-1, 1),
            "flows": list(range(n_flows)),
            "mapping": np.random.randint(0, n_classes, n_flows)
        }
