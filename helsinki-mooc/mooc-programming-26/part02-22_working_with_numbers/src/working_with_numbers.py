# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
# variables
count = 0
add = 0
positive = 0
negative = 0
# conditional
while True:
    num = int(input("Number: "))

    if num > 0:
        positive += 1
    if num < 0:
        negative += 1

    if num == 0:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {add}")
        print(f"The mean of the numbers is {mean}")
        print(f"Positive numbers {positive}")
        print(f"Negative numbers {negative}")
        break
    count += 1
    add += num
    mean = add / count
