from flask import Flask, jsonify

from encoders import CustomJSONEncoder
from repository import load_drivers, load_races
from utils import convert_to_times

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
races = load_races()
drivers = load_drivers()


@app.route('/races')
def get_races():
    return races


@app.route('/drivers')
def get_drivers():
    return drivers


@app.route('/')
def hello():
    return 'Hello, World!'


# Generates a lap time for a single driver
@app.route('/lap/<int:race_id>/<int:driver_id>')
def generate_lap_times(race_id, driver_id):
    race = races[race_id]
    driver = drivers[driver_id]
    lap_time = driver.get_lap_time_for_driver(race)

    return {'race': race, 'driver': driver, 'lap_time': lap_time}


@app.route('/driver/<int:driver_id>')
def get_driver_by_id(driver_id):
    return drivers[driver_id]


@app.route('/race/<int:race_id>')
def get_race_by_id(race_id):
    return races[race_id]


@app.route('/lap/<int:race_id>')
def generate_lap_times_for_all_drivers(race_id):
    lap_times = []
    for driver in drivers:
        lap_time = {"driver": driver.name, "time": driver.get_lap_time_for_driver(races[race_id])}
        lap_times.append(lap_time)
    lap_times.sort(key=lambda x: x['time'])
    for lap in lap_times:
        lap["time"] = convert_to_times(lap["time"])
    return lap_times
