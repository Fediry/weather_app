from weather import get_grid_location, get_weather
from location import gps
from flask import Flask

# app = Flask(__name__)

local_coordinates = gps.get_current_gps_coordinates()
print(local_coordinates)
local_weather = get_weather(get_grid_location(local_coordinates))
print(local_weather)
