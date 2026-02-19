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


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
