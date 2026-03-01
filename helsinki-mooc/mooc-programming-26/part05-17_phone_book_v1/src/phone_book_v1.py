# Write your solution here
# dictionary to hold all
phonebook = {}

# while loop to take commands
while True:
    # take input
    command = int(input("command (1 search, 2 add, 3 quit): "))
    # command :int
    if command not in range(1, 4):  # <= 0 or command > 3:
        continue

    elif command == 3:
        print("quitting...")
        break
    # name :
    name = input("name: ")

    if command == 2:
        # number:
        number = input("number: ")
        phonebook[name] = number
        print("ok!")

    elif command == 1:
        if name in phonebook:
            print(phonebook[name])

        else:
            print("no number")
