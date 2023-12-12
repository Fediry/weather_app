from src import weather, gps, zipcode_lookup
from flask import Flask, flash, redirect, url_for, request, render_template, session

app = Flask(__name__)


def format_weather_periods():
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        zipcode = request.form['zip code']

        if not zipcode:
            flash('Please enter your zip code.')
        if len(zipcode) < 1 or len(zipcode) > 5:
            flash('Please enter a valid, 5-digit zip code.')
        else:
            location_info = zipcode_lookup.get_coordinates_from_zipcode(zipcode)
            latitude, longitude = location_info
            local_weather = weather.get_weather(weather.get_grid_location((latitude, longitude)))
            return render_template('index.html', city=zipcode, latitude=latitude, longitude=longitude, local_weather=local_weather)


    location_info = gps.get_current_gps_coordinates()
    city, coordinates = location_info
    latitude, longitude = coordinates
    local_weather = weather.get_weather(weather.get_grid_location(coordinates))
    return render_template('index.html', city=city, latitude=latitude, longitude=longitude, local_weather=local_weather)
