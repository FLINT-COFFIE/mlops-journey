# Write your solution here
# imports
import string
# writing my first module


# First function
def change_case(orig_string: str):
    # what it does
    """creates and returns a new version of the parameter string. The lowercase letters in the original will be uppercase, and uppercase letters will be lowercase."""
    replaced_str = ""
    for char in orig_string:
        if char.islower():
            replaced_str += char.upper()
        elif char.isupper():
            replaced_str += char.lower()
    return replaced_str


# Second Function
def split_in_half(orig_string: str):
    """splits the parameter string in half, and returns the results in a tuple."""  # splitting
    first_index = len(orig_string) // 2
    # second_index = len(orig_string) - first_index
    first_half = orig_string[:first_index]
    second_half = orig_string[first_index:]

    return first_half, second_half


# testing
print(change_case("fLINT"))
print(split_in_half("fLINT"))
