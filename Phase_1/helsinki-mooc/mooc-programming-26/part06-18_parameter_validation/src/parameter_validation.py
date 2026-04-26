# Write your solution here
def new_person(name: str, age: int):

    if " " not in name:
        raise ValueError

    if age > 150 or age < 2:
        raise ValueError

    if 2 <= len(name) <= 40:
        if 0 < age <= 150:
            return name, age

    else:
        raise ValueError


if __name__ == "__main__":
    print(new_person("Flint Coffie", 10))
