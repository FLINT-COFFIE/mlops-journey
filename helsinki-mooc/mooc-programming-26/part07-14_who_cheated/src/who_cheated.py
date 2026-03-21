# Write your solution here
# imports
from datetime import datetime
import csv


# defining functions
def cheaters():
    ##reading starttimes
    with open("start_times.csv") as startfile:
        start_time_info = {}
        for line in csv.reader(startfile, delimiter=";"):
            name = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")

            # populating start_time_info
            start_time_info[name] = start_time

        print(start_time_info)


# testing
cheaters()
