# Write your solution here
# imports
from datetime import *

# asking for inputs
filename = "late_june.txt"  # input("Filename: ")
str_date = "24.06.2020"  # input("Starting date: ")
no_of_days = 5  # int(input("How many days: "))

# calculated reformatting
timedelta_days = timedelta(days=no_of_days - 1)

# reformatting data types
start_date = datetime.strptime(str_date, "%d.%m.%Y")
end_date = start_date + timedelta_days
str_end_date = end_date.strftime("%d.%m.%Y")
end_date = datetime.strptime(str_end_date, "%d.%m.%Y")

# difference
difference = end_date - start_date
# total_minutes = no_of_days * 24 * 60

# printing screen time input
print("Please type in screen time in minutes on each day (TV computer mobile):\n")


# writing to file
with open(filename, "w") as file:
    file.write(f"Time period: {str_date}-{str_end_date}\n")

    mins = []
    keys = {}
    # looping through days
    for day in range(no_of_days):
        day = timedelta(days=day)
        screen_time = input(f"Screen time {(start_date + day).strftime('%d.%m.%Y')}: ")

        parts = screen_time.split(" ")
        for part in parts:
            mins.append(int(part))

        key = (start_date + day).strftime("%d.%m.%Y")
        keys[key] = screen_time
        # split screen_time

    total_minutes = sum(mins)
    avarage = total_minutes / len(mins)

    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {avarage}\n")

    for dates, minutes in keys.items():
        minutes = minutes.replace(" ", "/")
        file.write(f"{dates}: {minutes}\n")


# print final line
print("Data stored in file late_june.txt")
