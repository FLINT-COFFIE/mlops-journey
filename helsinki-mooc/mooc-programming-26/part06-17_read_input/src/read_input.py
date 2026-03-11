# Write your solution here
def read_input(text: str, bound1: int, bound2: int):

    while True:
        try:
            number = int(input(text))  # (input("Enter a number: "))

        except ValueError:
            print(f"You must type in a number between {bound1} and {bound2}\n")

        if bound1 < number < bound2:
            return number


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
