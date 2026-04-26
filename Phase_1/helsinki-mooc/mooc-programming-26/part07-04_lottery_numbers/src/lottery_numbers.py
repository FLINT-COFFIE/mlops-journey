# Write your solution here
# importing random
from random import *

# defining the function


def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper + 1))
    draw = sample(number_pool, amount)
    return sorted(draw)


if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
