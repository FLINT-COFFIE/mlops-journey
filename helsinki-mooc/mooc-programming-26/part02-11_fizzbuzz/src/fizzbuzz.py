# Write your solution here

# input
num = int(input("Number: "))

# conditionals
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")
