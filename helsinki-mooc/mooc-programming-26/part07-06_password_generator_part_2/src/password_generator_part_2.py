# Write your solution here
# importing functions
import string
import random


# defining the function
def generate_password(length: int, val: bool, val2: bool):
    alphabet = string.ascii_lowercase
    digits = string.digits
    if val:
        alphabet += string.digits

    password_list = []
    for i in range(length):
        char = random.choice(alphabet)
        password_list.append(char)
    password = "".join(password_list)

    if val:
        for i in digits:
            if i in password:
                return password
    return password


if __name__ == "__main__":
    # testing
    for i in range(10):
        print(generate_password(8, True, False))
