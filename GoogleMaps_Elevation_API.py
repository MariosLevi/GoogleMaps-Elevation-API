from pprint import pprint #pip install pprint
import googlemaps #pip install googlemaps

API_KEY = "AIzaSyAybh8hXbXTIvOaHglmZPbyvJrYJ1ujFUc"

map_client = googlemaps.Client(API_KEY)

pprint(dir(map_client))

#location of the spot you want the elevation to
location = 28.4723325,25.0608467


response = map_client.elevation(location) #in meters
pprint(response)
