# WRITE YOUR SOLUTION HERE:
def lengths(strings: list):
    return {word : len(word) for word in strings}


#testing
word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)