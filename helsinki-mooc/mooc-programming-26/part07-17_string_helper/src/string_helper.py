# Write your solution here
# imports
import string
# writing my first module


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


change_case
