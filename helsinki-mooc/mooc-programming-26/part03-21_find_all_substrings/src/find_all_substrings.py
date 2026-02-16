# Write your solution here
word = input("Word: ")
char = input("Enter character: ")
# taking inputs

"""while True:
    output = word.find(char)

    if output == -1:
        break

    elif len(word) >= output + 3:
        print(word[output : output + 3])
    word = word[output + 1 :]"""

while True:
    index = word.find(char)

    if index == -1:
        break

    if len(word) >= index + 3:
        print(word[index : index + 3])

    word = word[index + 1 :]
