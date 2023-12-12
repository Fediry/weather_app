from dataclasses import dataclass
import pandas as pd

@dataclass
class ZipcodeCoordinates:
    zipcode: str 
    latitude: str
    longitude: str

def get_coordinates_from_zipcode(zipcode):
    """ Takes a zip code, finds it in the dataframe and returns a tuple of latitude and longitude.
    """
    
    try:
        if type(zipcode) is str:
            zipcode = int(zipcode)
    except ValueError as e:
        print(f"Error: {e}, zipcode should be 5-digit str.")
    
    data = load_zipcodes()
    zip_lookup = data[data['ZIP'] == zipcode]
    coordinates = (zip_lookup['LAT'].iloc[0], zip_lookup['LNG'].iloc[0])

    return coordinates

def load_zipcodes():
    """ Load the CSV file of Zip Codes to Latitude and Longitude into a Pandas Data Frame and return it.
        (Local copy of US Census data for zip codes to lattitude/longitude.)
    """
    FILE = 'data/USZip2GPS.txt'
    data = pd.read_csv(FILE)
    return data


if __name__ == '__main__':
    zipcode = '95126'
    coordinates = get_coordinates_from_zipcode(zipcode)
    print(coordinates)
