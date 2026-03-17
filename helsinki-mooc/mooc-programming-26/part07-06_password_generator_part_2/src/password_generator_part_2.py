# Write your solution here
# importing functions
import string
import random


# defining the function
def generate_password(length: int, dig: bool, spe: bool):
    alphabet = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

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
            for char in password:
                if char in digits:
                    valid = True
                else:
                    valid = False

        if spe:
            for char in password:
                if char in special:
                    valid = True
                else:
                    valid = False

        if valid:
            return password


if __name__ == "__main__":
    # testing
    for i in range(10):
        print(generate_password(2, False, False))
