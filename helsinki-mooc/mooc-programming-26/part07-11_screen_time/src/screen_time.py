# Write your solution here
# imports
from datetime import *

# asking for inputs
filename = input("Filename: ")
start_date = input("Starting date: ")
no_of_days = float(input("How many days: "))

# reformatting data types
# no_of_days = timedelta(days=no_of_days)
start_date = start_date.strftime("%d.%m.%Y")

# printing screen time input
print("Please type in screen time in minutes on each day (TV computer mobile):\n")

# looping through days
for day in range(no_of_days):
    day = timedelta(days=day)
    screen_time = input(f"Screen time {start_date + day}: ")
    print(screen_time)

# print("Data stored in file late_june.txt")
