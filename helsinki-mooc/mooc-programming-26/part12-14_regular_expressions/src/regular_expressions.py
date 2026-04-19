# Write your solution here
import re

def is_dotw(my_string: str):
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(expression, my_string):
        return True
    return False


#testing
print(is_dotw("Mon"))
print(is_dotw("Fri"))
print(is_dotw("Tui"))