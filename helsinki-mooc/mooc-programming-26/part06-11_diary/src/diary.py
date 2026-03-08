# Write your solution here
while True:
    # displaying requirements
    print("1 - add an entry, 2 - read entries, 0 - quit")

    # ask for function
    function = int(input("Function: "))

    # exit if zero
    if function == 0:
        print("Bye now!")
        break

    # reading the file
    elif function == 2:
        print("Entries: ")
        with open("diary.txt") as f:
            for line in f:
                line = line.strip()
                print(line)

    # adding entries
    elif function == 1:
        entry = input("diary entry: ")
        print("diary saved")

        # open and read the file
        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
