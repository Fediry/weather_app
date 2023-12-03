from weather import get_grid_location, get_weather
from location import gps
from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)


# location_info = gps.get_current_gps_coordinates()
# city, coordinates = location_info
# latitude, longitude = coordinates
# local_weather = get_weather(get_grid_location(coordinates))


@app.route('/', methods=['GET'])
def index():
    location_info = gps.get_current_gps_coordinates()
    city, coordinates = location_info
    latitude, longitude = coordinates
    local_weather = get_weather(get_grid_location(coordinates))
    return render_template('index.html', city=city, latitude= latitude, longitude=longitude)
