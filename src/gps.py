import geocoder

def get_current_gps_coordinates():
    """ Uses geocoder module and the machines IP address to find the latitude and longitude. 
        Warning: if a VPN is being used, the IP address lookup will not be accurate.
        Returns the City and a tuple of Latitude and Longitude as a tuple.
    """
    g = geocoder.ip('me') #'me' uses this machine's IP address
    if g.latlng is not None:
        return (g.city, g.latlng)
    else:
        return None

if __name__ == "__main__":
    # For testing
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