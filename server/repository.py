import json

from domain.driver import Driver
from domain.race import Race
from utils import convert_to_milliseconds


def load_races():
    with open("races.json", "r") as data:
        races_json = json.load(data)
        races = [Race(race['name'], race['fastest_lap'], race['laps']) for race in races_json['races']]
        race_id = 0
        for race in races:
            race.id = race_id
            race_id += 1
            race.fastest_lap = convert_to_milliseconds(race.fastest_lap)

    return races


def load_drivers():
    with open("drivers.json", "r") as data:
        drivers_json = json.load(data)
        drivers = [Driver(driver['name'], driver['speed_rating'], driver['team']) for driver in drivers_json['drivers']]
    return drivers
