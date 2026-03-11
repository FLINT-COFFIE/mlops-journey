# Write your solution here
print("1 - Add word, 2 - Search, 3 - Quit")

while True:
    # take input
    function = int(input("Function: "))

    # Quitting
    if function == 3:
        print("Bye!")
        break

    # adding
    if function == 1:
        # words
        fin = input("The word in Finnish")
        eng = input("The word in English")

        # add and print dictionary entry added
        with open("dictionary.txt", "a") as file:
            file.write(f"{fin} - {eng}")

        print("Dictionary entry added")

    # searching
    if function == 2:
        search_term = input("Search term: ")
        # read the file
        with open("dictionary.txt") as file:
            for line in file:
                if search_term in line:
                    print(line)
