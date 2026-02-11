# Write your solution here
# input
fah = int(input("Enter temperature in degrees fahrenheit: "))

cel = (5 / 9) * (fah - 32)

print(f"{fah} degrees Fahrenheit equals {cel} degrees Celsius")

if cel < 0:
    print("Brr! It's cold in here!")
