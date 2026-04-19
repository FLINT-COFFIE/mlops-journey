# Write your solution here
import re

def is_dotw(my_string: str):
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(expression, my_string):
        return True
    return False


def all_vowels(my_string: str):
    expression = "^[aeiou]*$"
    if re.search(expression, my_string):
        return True
    return False



#testing
print(all_vowels("eioueioieoieou"))
print(all_vowels("autoooo"))