from enum import Enum

class TimeseriesOutput(Enum):
    csv = 1
    geojson = 2

    @staticmethod
    def from_str(env):
        if env.lower() in ["csv"]:
            return TimeseriesOutput.csv
        elif env.lower() in ["geojson", "json"]:
            return TimeseriesOutput.geojson
        else:
            NotImplemented
    