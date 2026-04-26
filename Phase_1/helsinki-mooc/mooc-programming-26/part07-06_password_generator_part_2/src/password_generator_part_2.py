# Write your solution here
# importing functions
import string
import random


# defining the function
def generate_strong_password(length: int, dig: bool, spe: bool):
    alphabet = string.ascii_lowercase
    digits = string.digits
    special = "!?=+-()#"

    if dig:
        alphabet += string.digits

    if spe:
        alphabet += special

    while True:
        password_list = []

        for i in range(length):
            password_list.append(random.choice(alphabet))

        password = "".join(password_list)

        valid = True

        found_lower = False

        for char in password:
            if char in string.ascii_lowercase:
                found_lower = True
        if not found_lower:
            valid = False

        if dig:
            found_dig = False
            for char in password:
                if char in digits:
                    found_dig = True

            if not found_dig:
                valid = False

        if spe:
            found_spe = False
            for char in password:
                if char in special:
                    found_spe = True

            if not found_spe:
                valid = False

        if valid:
            return password


if __name__ == "__main__":
    # testing
    # for i in range(10):
    print(generate_strong_password(2, False, False))
