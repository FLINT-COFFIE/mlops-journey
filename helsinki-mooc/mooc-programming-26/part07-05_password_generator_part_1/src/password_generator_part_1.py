# Write your solution here
# importing functions
from string import *
from random import *


# defining the function
def password_gen(length: int):
    alphabet = ascii_lowercase
    password = sample(alphabet, length)
    return password.join()


# testing
for i in range(10):
    print(password_gen(8))
