# write your solution here
# initialise a list of correct words
words = []
# open the file
with open("wordlist.txt") as newfile:
    for word in newfile:
        # strip and split
        word = word.strip()
        word = word.split(";")
        # add it to a list
        words.append(word[0])

# take user input
text = input("Write text: ")
char = text.split(" ")
# print(char)
for string in char:
    if string.lower() not in words:
        print(f"*{string}*", end=" ")
    else:
        print(f"{string}", end=" ")
# print(words)
print()
# return the string
# use end = " " then add the reset
