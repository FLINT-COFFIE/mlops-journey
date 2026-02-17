# Write your solution here
while True:
    num = int(input("Enter a number: "))

    if num <= 0:
        print("Thanks and bye!")
        break

    else:
        multiply = 1
        factorial = 1
        while factorial <= num:
            multiply *= factorial
            factorial += 1
        print(f"The factorial of the number {num} is {multiply}")
