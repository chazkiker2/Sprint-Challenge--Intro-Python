import csv


# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"City(name={self.name}, lat={self.lat}, lon={self.lon})"


# We have a collection of US cities_list with population over 750,000 stored in the
# file "cities_list.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `city_reader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities_list" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def city_reader(cities_list=None):
    if cities_list is None:
        cities_list = []

    # TODO Implement the functionality to read from the 'cities_list.csv' file
    # Ensure that the lat and lon values are all floats
    # For each city record, create a new City instance and add it to the
    # `cities_list` list
    with open("cities.csv", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        headers = {i: header for i, header in enumerate(next(reader))}
        for row in reader:
            row_dic = {headers[i]: row[i] for i in range(len(row))}
            try:
                lat = float(row_dic["lat"])
                lon = float(row_dic["lng"])
            except ValueError:
                raise
            else:
                cities_list.append(City(name=row_dic["city"], lat=lat, lon=lon))

    return cities_list


city_reader(cities)

# Print the list of cities_list (name, lat, lon), 1 record per line.
for c in cities:
    print(c)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `city_reader_stretch` function, along
# with the `cities_list` list that holds all the City instances from the `city_reader`
# function. This function should output all the cities_list that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities_list.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `city_reader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


# TODO Get latitude and longitude values from the user

def city_reader_stretch(lat1, lon1, lat2, lon2, cities_list=None):
    if cities_list is None:
        cities_list = []

    lat_low, lat_high = (lat1, lat2) if lat1 < lat2 else (lat2, lat1)
    lon_low, lon_high = (lon1, lon2) if lon1 < lon2 else (lon2, lon1)

    # within will hold the cities_list that fall within the specified region
    # Go through each city and check to see if it falls within
    # the specified coordinates.
    return [
        city for city in cities
        if lat_low <= city.lat <= lat_high and lon_low <= city.lon <= lon_high
    ]


def user_prompt():
    coords_one = input(">> Enter lat1,lon1: ")
    coords_two = input(">> Enter lat2,lon2: ")

    args1 = coords_one.strip().split(',')
    if len(args1) < 2:
        raise InputError(args1, "Not enough arguments given")

    args2 = coords_two.strip().split(',')
    if len(args2) < 2:
        raise InputError(args2, "Not enough arguments given")

    try:
        lat1, lon1 = [float(num) for num in args1]
    except ValueError:
        print(f"{args1[0], args1[1]} could not be parsed as numbers!")
    else:
        try:
            lat2, lon2 = [float(num) for num in args2]
        except ValueError:
            print(f"{args2[0], args2[1]} could not be parsed as numbers!")
        else:
            print("your input was good enough!")
            lst = city_reader_stretch(
                lat1=lat1,
                lon1=lon1,
                lat2=lat2,
                lon2=lon2,
                cities_list=cities
            )
            print(lst)


if __name__ == '__main__':
    user_prompt()
