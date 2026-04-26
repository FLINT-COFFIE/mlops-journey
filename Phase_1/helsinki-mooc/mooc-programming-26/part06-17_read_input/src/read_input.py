# Write your solution here
def read_input(text: str, bound1: int, bound2: int):

    while True:
        try:
            number = input(text)  # (input("Enter a number: "))
            number = int(number)

            if bound1 <= number <= bound2:
                return number
            else:
                print(f"You must type in an integer between {bound1} and {bound2}")

        except ValueError:
            print(f"You must type in an integer between {bound1} and {bound2}")


if __name__ == "__main__":
    number = read_input("Give a number", 95, 105)
    print("You typed in:", number)
