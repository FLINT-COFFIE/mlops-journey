# Write your solution here
# importing datetime
from datetime import datetime


# define func
def is_it_valid(pic: str):
    # only change this if invalid
    valid = True

    # splitting into dates and other parts
    day = int(pic[:2])
    month = int(pic[2:4])

    # incomplete year
    year = int(pic[4:6])

    if "-" in pic:
        year += 1900

    elif "+" in pic:
        year += 1800

    elif "A" in pic:
        year += 2000

    # return bool
    if valid:
        return True

    else:
        return False
