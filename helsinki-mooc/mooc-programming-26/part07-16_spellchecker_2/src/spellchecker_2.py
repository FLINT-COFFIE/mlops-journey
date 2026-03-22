# Write your solution here
#imports
from difflib import get_close_matches

##Part 1
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

close_matches = {}
wrong_words = []

for string in char:
    if string.lower() not in words:
        wrong_words.append(string)
        print(f"*{string}*", end=" ")
        
for wor
# print(words)
print()
# return the string
# use end = " " then add the reset


##Part 2
