import json
import random


class Driver:
    def __init__(self, name, speed_rating, team):
        self.name = name
        self.speed_rating = speed_rating
        self.team = team

    def __str__(self) -> str:
        return f"Name:{self.name}, Speed:{self.speed_rating}, Team:{self.team}"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def get_lap_time_for_driver(self, race):
        return int(race.fastest_lap + (2 * (1 - self.speed_rating) + random.random()) * 1000)
