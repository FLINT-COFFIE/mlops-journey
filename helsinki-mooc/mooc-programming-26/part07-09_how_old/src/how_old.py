# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date_of_birth = datetime(year, month, day)
millenium = datetime(2000, 1, 1)

age = millenium - date_of_birth

if age >= 0:
    print(age)
