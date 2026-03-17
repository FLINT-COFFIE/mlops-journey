# Write your solution here
# import random in order to use choice
import random


# define the roll function
def roll(die: str):
    # assigning values to the dies
    die_A = [3, 3, 3, 3, 3, 6]
    die_B = [2, 2, 2, 5, 5, 5]
    die_C = [1, 4, 4, 4, 4, 4]

    if die == "A":
        result = random.choice(die_A)

    if die == "B":
        result = random.choice(die_B)

    if die == "C":
        result = random.choice(die_C)

    return result


# testing
for i in range(20):
    print(roll("A"), " ", end="")
