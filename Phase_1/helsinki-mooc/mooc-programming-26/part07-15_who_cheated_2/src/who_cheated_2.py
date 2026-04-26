# Write your solution here
# imports
from datetime import datetime, timedelta
import csv


# defining functions
def final_points():
    ##reading starttimes
    with open("start_times.csv") as startfile:
        # name : starttime
        start_time_info = {}
        for line in csv.reader(startfile, delimiter=";"):
            name = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")

            # populating start_time_info
            start_time_info[name] = start_time

    # reading submissions
    with open("submissions.csv") as end_file:
        # end file info
        points_info = {}

        for line in csv.reader(end_file, delimiter=";"):
            # assigning values
            name = line[0]
            task = line[1]
            point = int(line[2])
            end_time = datetime.strptime(line[3], "%H:%M")

            starting = start_time_info[name]

            # 3 hour
            if end_time - starting > timedelta(hours=3):
                continue

            # initialize dict with dict
            if name not in points_info:
                points_info[name] = {}

            # update if better score
            if task not in points_info[name] or point > points_info[name][task]:
                points_info[name][task] = point

        result = {}

        for name, tasks in points_info.items():
            result[name] = sum(tasks.values())

        # print(cheater)
        return result


if __name__ == "__main__":
    # testing
    print(final_points())
