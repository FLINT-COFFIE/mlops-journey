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

    # adding entries
    elif function == 1:
        entry = input("Dairy entry: ")

        # open and read the file
        with open("dairy.txt", "a") as file:
            file.write(entry + "\n")
