# Write your solution here
# importing functions
import string
import random


# defining the function
def generate_password(length: int, dig: bool, spe: bool):
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

        if dig:
            found_dig = False
            for char in password:
                if char in digits:
                    found_dig = True

            if found_dig == False:
                valid = False

        if spe:
            found_spe = False
            for char in password:
                if char in special:
                    found_spe = True

            if found_spe == False:
                valid = False

        if valid:
            return password


if __name__ == "__main__":
    # testing
    # for i in range(10):
    print(generate_password(2, False, False))
