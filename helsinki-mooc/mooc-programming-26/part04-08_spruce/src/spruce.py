# Write your solution here


def spruce(num):
    # print the string
    print("a spruce!")

    # print row of all stars
    row = 0

    while row < num:
        # max space
        space = " " * (num - row - 1)
        stars = "*" * (2 * row + 1)
        print(f"{space}{stars}")
        row += 1

    print(" " * (num - 1) + "*")


# You can test your function by calling it within the following block
# if __name__ == "__main__":
# spruce(5)

spruce(5)
