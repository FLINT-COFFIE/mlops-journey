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


def triangle(size):
    start = 1
    while start <= size:
        # You should call function line here with proper parameters
        line(start, "#")
        start += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
