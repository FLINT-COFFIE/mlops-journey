# Write your solution here
# imports
import datetime
import csv


# defining functions
def cheaters():
    with open("start_time.csv") as startfile:
        for line in csv.reader(startfile, delimiter=";"):
            print(line)


# testing
cheaters()
