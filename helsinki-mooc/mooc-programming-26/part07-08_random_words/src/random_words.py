# Write your solution here
# imports
import random


# defining the function
def words(n: int, beginning: str):
    # store the words in a list
    words = []
    with open("words.txt") as word_file:
        for line in word_file:
            word = line.strip()

            # condition to fill words
            if word.startswith(beginning):
                words.append(word)
        try:
            passwords = random.sample(words, n)

        except len(passwords) < n:
            raise ValueError

    return passwords


# debugging print
word_list = words(3, "ca")
for word in word_list:
    print(word)
