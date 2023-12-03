import requests
from dataclasses import dataclass


@dataclass
class WeatherData:
    # from JSON root: ['properties']['periods'][LIST of 0...1...2...]
    name: str  # ['name']
    start_time: str  # ['startTime']
    end_time: str  # ['endTime']
    temperature: int  # ['temperature']
    temp_unit:str   # ['temperatureUnit']
    details: str  # ['detailedForecast']


def get_weather(url):
    periods = []
    response = requests.get(url).json()
    for period in response['properties']['periods']:
        name = period['name']
        start_time = period['startTime']
        end_time = period['endTime']
        temperature = period['temperature']
        temp_unit = period['temperatureUnit']
        details = period['detailedForecast']
        periods.append(WeatherData(name, start_time, end_time, temperature, temp_unit, details))
    return periods

def get_grid_location(coordinates):
    lat, lng = coordinates
    url = f"https://api.weather.gov/points/{lat},{lng}"
    response = requests.get(url).json()
    forecast_url = response['properties']['forecast']
    return forecast_url


if __name__ == "__main__":
    grid_locale = get_grid_location((37.3306,-121.904))
    weather_periods = get_weather(grid_locale)
    for period in weather_periods:
        print(period.name)
        print(f'\t Temp: {period.temperature} ({period.temp_unit}°)')
        print(f'\t {period.details}')