## Weather App

A simple web-based frontend to check the weather at your location utilizing the [US National Weather Service API](https://www.weather.gov/documentation/services-web-api).
Built using Flask.

The app should auto-detect your devices location, though if this fails, or the ip detection isn't your actual location(possibly from using a VPN), you can enter your zip code. The app uses your latitude and longitude to query the US Weather Service API for the nearest grid to you and then query the api again, using the grid info it gets from the first query,to get the current weather data.