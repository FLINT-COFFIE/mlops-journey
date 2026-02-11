# Write your solution here
# words
word1 = input("word: ")
word2 = input("word: ")

# conditionals
if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
elif word1 == word2:
    print("You gave the same word twice")
