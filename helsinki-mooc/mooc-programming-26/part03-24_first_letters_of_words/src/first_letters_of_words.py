# Write your solution here
# take input
word = input("Please type in a sentence: ")

# print out first letter
print(word[0])

# find " " character
while True:
    space = word.find(" ")
    if space == -1:
        # print out first letter
        break

    # set new word to " " plus 1

    word = word[space + 1 :]
    # print out first letter
    print(word[0])


# repeat
