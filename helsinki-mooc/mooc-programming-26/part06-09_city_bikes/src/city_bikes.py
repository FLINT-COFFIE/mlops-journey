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


# finding the greatest distance
def greatest_distance(stations: dict):
    max_distance = -1
    station = []

    # populating the list with station names
    for keys, values in stations.items():
        station.append(keys)

    # looping through stations
    for i in range(len(station)):
        for j in range(i + 1, len(station)):
            # define readings
            station1 = station[i]
            station2 = station[j]

            # finding the distance
            d = distance(stations, station1, station2)

            # assigning max distance
            if d > max_distance:
                max_distance = d

                # getting the two stations
                first_station = station1
                second_station = station2
    print(first_station, second_station, max_distance)


greatest_distance(get_station_data("stations1.csv"))
