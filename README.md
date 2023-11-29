## Weather App

A simple webbased frontend to check the weather at your location utilizing the [US National Weather Service API](https://www.weather.gov/documentation/services-web-api).
Built using Flask.

The app should auto-detect your devices location, though will fall back to asking for your zipcode if this fails. Using the latitude and longitude to query the api for the nearest grid to you and then query the api again using that grid info to get the current weather data.