from pprint import pprint #pip install pprint
import googlemaps #pip install googlemaps
import math
import ast

API_KEY = "YOUR KEY"

map_client = googlemaps.Client(API_KEY)

#location of the spot you want the elevation to
location = 28.4723325,25.0608467

response = map_client.elevation(location) #Creates an elevation list
response_no_brackets = ast.literal_eval((str(response)[1:-1])) #converting the list into a dictionary

pure_elevation = response_no_brackets["elevation"] #outputs a float like 139.9674987792969
output_elevation = str(math.ceil(pure_elevation*100)/100) #Ceiling function rounds up to 2 decimal points -> 139.97

print("The elevation of provided coordinates '" + str(location) + "' is " + output_elevation + " meters.")
