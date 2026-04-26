# Write your solution here
# imports
from difflib import get_close_matches

##Part 1
# initialise a list of correct words
words = []
# open the file
with open("wordlist.txt") as newfile:
    for word in newfile:
        # strip and split
        word = word.strip()
        # word = word.split(";")
        # add it to a list
        words.append(word)

# take user input
text = input("Write text: ")
char = text.split(" ")
# print(char)

close_matches = {}
wrong_words = []

for string in char:
    if string.lower() not in words:
        wrong_words.append(string)
        print(f"*{string}*", end=" ")
    else:
        print(f"{string}", end=" ")

for word in wrong_words:
    close_matches[word] = get_close_matches(word, words)

print()
print("suggestions:")

# print(words)
for key, values in close_matches.items():
    print(f"{key}: {', '.join(values)}")
# return the string
# use end = " " then add the reset


##Part 2
