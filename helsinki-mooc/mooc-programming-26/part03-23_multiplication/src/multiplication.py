# Write your solution here
num = int(input("Please type in a number: "))
first = 0

while first < num:
    first += 1
    second = 0

    while second < num:
        second += 1
        print(f"{first} x {second} = {first * second}")
