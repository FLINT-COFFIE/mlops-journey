# Write your solution here
# importing json
import json


# writing the function
def print_persons(filename: str):
    with open(filename) as file:
        profiles = file.read()

    for profile in profiles:
        name = profile[name]
        age = profile[age]
        hobbies = profile[hobbies]

        print(f"{name} {age} years ({hobbies})")


filename = "file1.json"  # input("Filename: ")

print_persons(filename)
