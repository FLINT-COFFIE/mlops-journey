# Write your solution here
# importing json
import json


# writing the function
def print_persons(filename: str):
    with open(filename) as file:
        profiles = file.read()
