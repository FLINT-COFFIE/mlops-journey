# Write your solution here
limit = int(input("Limit: "))
sum = 0
add = 1

while sum < limit:
    sum += add
    add += 1
print(sum)
