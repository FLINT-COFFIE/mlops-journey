# Write your solution here

my_list = []

items = int(input("How many items: "))

count = 1
while count <= items:
    item = int(input(f"Item {count}: "))
    my_list.append(item)
    count += 1
print(my_list)
