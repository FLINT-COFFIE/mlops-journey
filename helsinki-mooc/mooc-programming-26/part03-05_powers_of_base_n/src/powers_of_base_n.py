# Write your solution here
lim = int(input("Upper limit: "))
base = int(input("Base: "))

power = 1
start = 1

while power <= lim:
    print(power)
    power = base**start
    start += 1
