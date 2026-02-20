# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1 or 0 < index >= len(my_list):
        break

    replace = int(input("New_value: "))
    my_list[index] = replace
    print(my_list)
