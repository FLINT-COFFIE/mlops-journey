# Write your solution here
# importing datetime
from datetime import datetime


# define func
def is_it_valid(pic: str):
    # only change this if invalid
    valid = True
    century_markers = ["+", "-", "A"]
    control_characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    # early gate keeping
    if len(pic) < 11 or pic[6] not in century_markers:
        return False

    try:
        # control marker check
        control_num_str = f"{pic[:6]}{pic[7:10]}"
        control_number = int(control_num_str)

        # control number check
        control_index = control_number % 31

        # control character
        control_char = control_characters[control_index]

        # control char gatekeeping
        if pic[-1] != control_char:
            return False

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

        # date of birth filter
        date_of_birth = datetime(year, month, day)

    except:
        valid = False

    # return bool
    if valid:
        return True

    else:
        return False


# testing
print(is_it_valid("230827-906F"))
