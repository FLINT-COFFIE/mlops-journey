# Write your solution here
# importing json
import json


# writing the function
def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    # loading the json into profiles
    profiles = json.loads(data)

    # looping through profiles
    for profile in profiles:
        name = profile["name"]
        age = profile["age"]
        hobbies = ", ".join(profile["hobbies"])

        print(f"{name} {age} years ({hobbies})")


if __name__ == "__main__":
    filename = "file1.json"  # input("Filename: ")

    print_persons(filename)
