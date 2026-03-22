# Write your solution here
# imports
from datetime import datetime
import csv


# defining functions
def cheaters():
    ##reading starttimes
    with open("start_times.csv") as startfile:
        # name : starttime
        start_time_info = {}
        for line in csv.reader(startfile, delimiter=";"):
            name = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")

            # populating start_time_info
            start_time_info[name] = start_time

    with open("submissions.csv") as end_file:
        # end file info
        end_file_info = {}

        for line in csv.reader(end_file, delimiter=";"):
            # assigning values
            name = line[0]
            # task = line[1]
            # points = line[2]
            end_time = datetime.strptime(line[3], "%H:%M")

            # condition to add name to endfile info
            if name not in end_file_info or end_time > end_file_info[name]:
                end_file_info[name] = end_time

        print(end_file_info)


# testing
cheaters()
