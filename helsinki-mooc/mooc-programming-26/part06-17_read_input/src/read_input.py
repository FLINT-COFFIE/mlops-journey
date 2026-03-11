# Write your solution here
def read_input(text: str, bound1: int, bound2: int):

    while True:
        number = int(input("Enter a number: "))
        if bound1 < number < bound2:
            return number
