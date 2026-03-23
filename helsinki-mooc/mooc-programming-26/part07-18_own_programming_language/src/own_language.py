# Write your solution here
# imports
import string


# defining the function
def run(program):
    # A-Z
    variables = {char: 0 for char in string.ascii_uppercase}
    results = []

    # whic lines contains commands with :
    labels = {}
    for index, line in enumerate(program):
        if line.endswith(":"):
            labels[line[:-1]] = index

    # Function to check existing value or return an int
    def get_value(x):
        if x in variables:
            return variables[x]
        return int(x)
