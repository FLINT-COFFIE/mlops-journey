# Write your solution here

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    # take input
    function = int(input("Function: "))

    # Quitting
    if function == 3:
        print("Bye!")
        break

    # adding
    elif function == 1:
        # words
        fin = input("The word in Finnish: ")
        eng = input("The word in English: ")

        # add and print dictionary entry added
        with open("dictionary.txt", "a") as file:
            file.write(f"{fin} - {eng}\n")

        print("Dictionary entry added")

    # searching
    elif function == 2:
        search_term = input("Search term: ")
        # read the file
        with open("dictionary.txt") as file:
            for line in file:
                line = line.strip()
                if search_term in line:
                    print(line)
