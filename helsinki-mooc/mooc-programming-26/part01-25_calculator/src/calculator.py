# Write your solution here
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
operation = input("Operation: ")

# OPERATORS
if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")

if operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")

if operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
