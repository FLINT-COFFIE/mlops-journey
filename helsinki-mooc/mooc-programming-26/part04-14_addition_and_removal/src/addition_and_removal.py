# Write your solution here
# it is reset if in the while loop
my_list = []
print("The list is now []")
while True:
    # take input
    choice = input("Add or Remove: ")

    # break if x
    if choice.lower() == "x":
        print("Bye!")
        break

    elif choice.lower() == "r":
        if len(my_list) == 0:
            continue
        else:
            my_list.pop(-1)

    # add one if d
    elif choice.lower() == "d":
        if len(my_list) == 0:
            my_list.append(1)
        else:
            my_list.append(my_list[-1] + 1)
    print("The list is now", my_list)
