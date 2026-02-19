# Copy here code of line function from previous exercise
# Write your solution here
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


def box_of_hashes(height):
    limit = height
    while limit > 0:
        # You should call function line here with proper parameters
        line(10, "#")
        limit -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
