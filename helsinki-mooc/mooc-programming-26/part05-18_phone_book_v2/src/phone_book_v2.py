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

    if command == 2:
        # name :
        name = input("name: ")

        # number:
        number = input("number: ")

        if name not in phonebook:
            phonebook[name] = []

        phonebook[name].append(number)
        print("ok!")

    elif command == 1:
        # name :
        name = input("name: ")

        if name in phonebook:
            for digit in phonebook[name]:
                print(digit)

        else:
            print("no number")
