# tee ratkaisu tänne
# needed for the sqrt function
import math


# Write your solution here
# read the file
def read(filename: str):
    lines = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.split(";")
            if line[0] == "Longitude":
                continue
            lines.append(line)
    return lines


# retrieve the data and return the location and coordinate as a dictionary
def get_station_data(filename: str):
    station_data = {}
    file_data = read(filename)
    for line in file_data:
        station = line[3]
        coordinate = (float(line[0]), float(line[1]))
        station_data[station] = coordinate
    return station_data


# the distance between two stations
def distance(stations: dict, station1: str, station2: str):
    # assigning data to variables
    # station 1
    coordinate1 = stations[station1]
    longitude1 = coordinate1[0]
    latitude1 = coordinate1[1]

    # station 2
    coordinate2 = stations[station2]
    longitude2 = coordinate2[0]
    latitude2 = coordinate2[1]

    # calculating the distance
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    # returning the distance calculated
    return distance_km


stations = get_station_data("stations1.csv")
d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)
