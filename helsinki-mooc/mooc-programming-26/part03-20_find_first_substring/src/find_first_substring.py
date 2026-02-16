# Write your solution
word = input("Please type in a word: ")
char = input("Please type in a character: ")

start = word.find(char)

output = word[start : start + 3]

if len(output) > 2:
    print(output)
