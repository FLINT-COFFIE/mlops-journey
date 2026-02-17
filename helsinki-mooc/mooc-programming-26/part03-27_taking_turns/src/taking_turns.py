# Write your solution here
# take input
num = int(input("Enter a number: "))

first = 1
second = num

while first <= second:
    if first == second:
        print(first)
        break
    print(first)
    print(second)

    first += 1
    second -= 1
