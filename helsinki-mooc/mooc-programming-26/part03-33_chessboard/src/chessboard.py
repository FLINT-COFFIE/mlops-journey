# Write your solution here
def chessboard(limit):
    row = 0

    while row < limit:
        line = ""
        column = 0
        while column < limit:
            if (row + column) % 2 == 0:
                line += "1"

            else:
                line += "0"

            column += 1

        print(line)
        row += 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
