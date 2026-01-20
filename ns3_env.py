class Ns3Env:
    def __init__(self, controllers):
        self.controllers = controllers
        self.t = 0

    def reset(self):
        self.t = 0
        return self._state()

    def step(self, action):
        weights = self.controllers["scheduler"].apply(action["scheduler"])
        aqm = self.controllers["aqm"].apply(action["aqm"])
        mapping = self.controllers["mapping"].apply(
            action["flows"], action["mapping"]
        )

        state = self._state()
        reward = -state["avg_delay"] - 10 * state["packet_loss"]

        self.t += 1
        return state, reward, False, {
            "weights": weights,
            "aqm": aqm,
            "mapping": mapping
        }

    def _state(self):
        return {
            "avg_delay": 50 + self.t,
            "packet_loss": 0.01 * self.t
        }
