# Write your solution here
import string


# define the function
def separate_characters(my_string: str):
    ascii_chars = ""
    punctuation = ""
    other_chars = ""

    for char in my_string:
        if char.ascii_letters:
            ascii_chars += char

    return ascii_chars


parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
