import json


class Race:
    def __init__(self, name, fastest_lap, laps):
        self.name = name
        self.fastest_lap = fastest_lap
        self.laps = laps
        self.id = None

    def __str__(self) -> str:
        return f"Name:{self.name}, Fastest Lap:{self.fastest_lap}, Laps:{self.laps}"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)



