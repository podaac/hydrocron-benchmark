from enum import Enum

class TimeseriesFeature(Enum):
    Reach = 1
    Node = 2

    @staticmethod
    def from_str(env):
        if env.lower() in ["reach"]:
            return TimeseriesFeature.Reach
        elif env.lower() in ["node"]:
            return TimeseriesFeature.Node
        else:
            NotImplemented
    