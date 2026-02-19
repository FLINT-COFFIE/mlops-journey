# Copy here code of line function from previous exercise and use it in your solution


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


def triangle(size, char):
    start = 1
    while start <= size:
        # You should call function line here with proper parameters
        line(start, char)
        start += 1


def square(size, character, row):
    limit = size
    while limit > 0:
        # You should call function line here with proper parameters
        line(row, character)
        limit -= 1


def shape(sizet, chart, sizer, charr):
    triangle(sizet, chart)
    square(sizer, charr, sizet)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
