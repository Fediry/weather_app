import csv
from dataclasses import dataclass
import geocoder
import pandas as pd

@dataclass
class ZipcodeCoordinates:
    #City?
    zipcode: str 
    latitude: str
    longitude: str

def get_coordinates_from_zipcode(zipcode):
    """ Takes a zipcode, finds it in the dataframe and returns a tuple of latitude and longitude.
    """
    if type(zipcode) is str:
        zipcode = int(zipcode)
    
    data = load_zipcodes()
    zip_lookup = data[data['ZIP'] == zipcode]
    coordinates = (zip_lookup['LAT'].iloc[0], zip_lookup['LNG'].iloc[0])

    return coordinates
    # city = city_lookup(coordinates)
    # return city, coordinates

def load_zipcodes():
    """ Load the CSV file of Zip Codes to Latitude and Longitude into a Pandas Data Frame and return it.
        (Local copy of US Census data for zip codes to lattitude/longitude.)
    """
    FILE = 'location/USZip2GPS.txt'
    data = pd.read_csv(FILE)
    return data

# def city_lookup(coordinates):
#     """ Takes lattitude and longitude as a tuple and does a reverse lookup to find the city.
#         (Could have used a striaght forward lookup with this api, but decided to use the local copy of US Census data)
#     """
#     g = geocoder.osm(coordinates, method='reverse')
#     return g.city

if __name__ == '__main__':
    zipcode = '95126'
    coordinates = get_coordinates_from_zipcode(zipcode)
    print(coordinates)