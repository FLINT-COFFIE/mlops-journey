# Write your solution here
# importing functions
import string
import random


# defining the function
def generate_password(length: int):
    alphabet = string.ascii_lowercase

    password_list = []
    for i in range(length):
        char = random.choice(alphabet)
        password_list.append(char)
    password = "".join(password_list)
    return password


if __name__ == "__main__":
    # testing
    for i in range(10):
        print(generate_password(8))
