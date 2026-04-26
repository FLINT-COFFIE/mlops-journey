# Write your solution here
# importing string module
import string


# define the function
def separate_characters(my_string: str):
    ascii_chars = ""
    punctuation = ""
    other_chars = ""

    for char in my_string:
        if char in string.ascii_letters:
            ascii_chars += char
        elif char in string.punctuation:
            punctuation += char
        else:
            other_chars += char

    return (ascii_chars, punctuation, other_chars)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
