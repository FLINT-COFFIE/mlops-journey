# Write your solution here
limit = int(input("Limit: "))
sum = 0
add = 1
text = "1"

while sum < limit:
    sum += add
    if add > 1:
        text += " + " + str(add)
    add += 1

print(f"The consecutive sum: {text} = {sum}")
