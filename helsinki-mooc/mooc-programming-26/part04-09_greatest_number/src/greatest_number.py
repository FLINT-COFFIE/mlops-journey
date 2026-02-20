# Write your solution here
def greatest_number(a, b, c):
    highest = -10000
    if a > highest:
        highest = a

        if highest < b:
            highest = b

            if highest < c:
                highest = c
    return highest


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
