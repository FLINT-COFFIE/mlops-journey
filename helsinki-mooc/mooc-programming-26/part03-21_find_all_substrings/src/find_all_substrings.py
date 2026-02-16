# Write your solution here
word = input("Word: ")
char = input("Enter character: ")
# taking inputs

# conditional
while True:
    index = word.find(char)

    if index == -1:
        break

    if len(word) >= index + 3:
        print(word[index : index + 3])

    word = word[index + 1 :]
