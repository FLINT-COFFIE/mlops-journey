# Write your solution here
# import random in order to use choice
import random


# define the roll function
def roll(die: str):
    # assigning values to the dies
    die_A = [3, 3, 3, 3, 3, 6]
    die_B = [2, 2, 2, 5, 5, 5]
    die_C = [1, 4, 4, 4, 4, 4]

    # condition for each die
    if die == "A":
        result = random.choice(die_A)

    if die == "B":
        result = random.choice(die_B)

    if die == "C":
        result = random.choice(die_C)

    return result


# play die function
def play(die1: str, die2: str, times: int):

    # assign both results to an empty list
    result_1 = []
    result_2 = []

    # get results and populate lists
    for i in range(times):
        result_1.append(roll(die1))
        result_2.append(roll(die2))

    # count for each
    count_1 = 0
    count_2 = 0
    count_tie = 0

    # compare_each
    for i in range(times):
        # three if statements
        if result_1[i] > result_2[i]:
            count_1 += 1
        elif result_2[i] > result_1[i]:
            count_2 += 1
        elif result_1[i] == result_2[i]:
            count_tie += 1

    return count_1, count_2, count_tie


if __name__ == "__main__":
    # testing
    result = play("A", "C", 1000)
    print(result)
