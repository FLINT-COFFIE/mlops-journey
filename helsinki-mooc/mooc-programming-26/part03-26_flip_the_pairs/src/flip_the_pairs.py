# Write your solution here
# take input
num = int(input("Enter a number: "))
# assign a variable ""
count = 1

while count <= num:
    if count + 1 <= num:
        print(count + 1)
        print(count)

    else:
        print(count)

    count += 2
