import geocoder

def get_current_gps_coordinates():
    g = geocoder.ip('me') #this function is used to find the current information using our IP Address
    if g.latlng is not None:
        return (g.city, g.latlng)
    else:
        return None

if __name__ == "__main__":
    location_info = get_current_gps_coordinates()
    if location_info is not None:
        city, coordinates = location_info
        latitude, longitude = coordinates
        print(f"Your current GPS coordinates are:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"City: {city}")
    else:
        print("Unable to retrieve your GPS coordinates.")