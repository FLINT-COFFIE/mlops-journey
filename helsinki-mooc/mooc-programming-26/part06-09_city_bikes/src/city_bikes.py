# tee ratkaisu tänne
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


def get_station_data(filename: str):
    station_data = {}
    file_data = read(filename)
    for line in file_data:
        station = line[3]
        coordinate = (float(line[0]), float(line[1]))
        station_data[station] = coordinate

    return station_data


print(get_station_data("stations1.csv"))
