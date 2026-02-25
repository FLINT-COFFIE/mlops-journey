# Write your solution here
def who_won(game_board: list):
    # define individual counts
    zero = []
    one = []
    two = []

    # loop through and increase each counts using for then if statements.
    for odd in game_board:
        # count the numbers uniquely
        zeros = odd.count(0)
        ones = odd.count(1)
        twos = odd.count(2)

        zero.append(zeros)
        one.append(ones)
        two.append(twos)

    # returning a value
    if sum(one) > sum(two):
        return 1

    elif sum(two) > sum(one):
        return 2

    else:
        return 0


if __name__ == "__main__":
    who_won([[1, 2, 1], [0, 0, 1], [2, 1, 0]])
