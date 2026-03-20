# Write your solution here
# imports
from datetime import *

# asking for inputs
# filename = input("Filename: ")
start_date = input("Starting date: ")
no_of_days = int(input("How many days: "))

# calculated reformatting
timedelta_days = timedelta(days=no_of_days)

# reformatting data types
# no_of_days = timedelta(days=no_of_days)
start_date = datetime.strptime(start_date, "%d.%m.%Y")
end_date = datetime.strptime((start_date + timedelta_days), "%d.%m.%Y")

# difference
difference = end_date - start_date

# printing screen time input
print("Please type in screen time in minutes on each day (TV computer mobile):\n")

# writing to file
with open("late_june.txt", "w") as file:
    file.write(f"Time period: {start_date}-{end_date}\n")
    file.write(f"Total minutes: {difference.min}\n")
    file.write(f"How many days: {no_of_days}\n")
    file.write(
        "Please type in screen time in minutes on each day (TV computer mobile):\n"
    )


# looping through days
for day in range(no_of_days):
    day = timedelta(days=day)
    screen_time = input(f"Screen time {(start_date + day).strftime('%d.%m.%Y')}: ")
    print(screen_time)

    # appending to file
    # write("Data stored in file late_june.txt")
