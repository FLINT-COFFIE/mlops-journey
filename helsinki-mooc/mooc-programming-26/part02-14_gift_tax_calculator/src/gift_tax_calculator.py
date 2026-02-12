# Write your solution here
value = float(input("Value of gift: "))

if value < 5000:
    print("No tax!")

if 5000 <= value < 25000:
    tax = 100 + (value - 5000) * 0.08
    print(f"Amount of tax: {tax} euros")

if 25000 <= value < 55000:
    tax = 1700 + (value - 25000) * 0.10
    print(f"Amount of tax: {tax} euros")

if 55000 <= value < 200000:
    tax = 4700 + (value - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")

if 200000 <= value < 1000000:
    tax = 22100 + (value - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")

if value >= 1000000:
    tax = 142100 + (value - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")
