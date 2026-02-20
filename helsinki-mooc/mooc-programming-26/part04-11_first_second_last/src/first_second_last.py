# Write your solution here
def first_word(sentence):
    first = ""
    start = 0
    while start < len(sentence):
        if sentence[start] == " ":
            break
        first += sentence[start]
        start += 1
    return first


# Second word
def second_word(sentence):
    second = ""
    index = sentence.find(" ")
    start = index + 1
    while start < len(sentence):
        if sentence[start] == " ":
            break
        second += sentence[start]
        start += 1
    return second


# third word

# didn't read it well i had to do last not third.
# def third_word(sentence):
#    third = ""
#    second = second_word(sentence)
#    second_end = len(second)
#    index = sentence.find(second) + second_end
#    start = index + 1
#    while start < len(sentence):
#        if sentence[start] == " ":
#            break
#        third += sentence[start]
#        start += 1
#    return(third)"""


# last word
def last_word(sentence):
    word = ""
    index = len(sentence) - 1

    while index >= 0:
        if sentence[index] == " ":
            break

        word = sentence[index] + word
        index -= 1
    return word


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
#    return first_word(sentence)
#    return second_word(sentence)
#    return last_word(sentence)
