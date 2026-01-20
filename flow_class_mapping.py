class FlowClassMappingController:
    def __init__(self, n_classes):
        self.n_classes = n_classes

    def apply(self, flow_ids, action):
        return {
            fid: int(action[i]) % self.n_classes
            for i, fid in enumerate(flow_ids)
        }
