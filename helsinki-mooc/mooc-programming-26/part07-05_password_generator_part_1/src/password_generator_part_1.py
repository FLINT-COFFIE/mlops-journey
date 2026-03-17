# Write your solution here
# importing functions
from string import *
from random import *

# defining the function


def password_gen(length: int):
    alphabet = string.ascii_lowercase
    password = sample(alphabet, length)
    return password
