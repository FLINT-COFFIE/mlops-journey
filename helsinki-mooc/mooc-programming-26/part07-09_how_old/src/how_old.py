# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date_of_birth = datetime(year, month, day)
millenium = datetime(1999, 12, 31)

age = millenium - date_of_birth

if age.days > 0:
    print(f"You were {age.days} days old on the eve of the new millennium.")

else:
    print("You weren't born yet on the eve of the new millennium.")
