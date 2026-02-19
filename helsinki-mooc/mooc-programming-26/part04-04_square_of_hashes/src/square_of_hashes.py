# Copy here code of line function from previous exercise
def line(num, char):
    if len(char) < 1:
        char = "*"

    elif len(char) > 1:
        char = char[0]
    start = ""
    while num > 0:
        start += char
        num -= 1
    print(start)


def square_of_hashes(size):
    count = size
    while count > 0:
        # You should call function line here with proper parameters
        line(size, "#")
        count -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
