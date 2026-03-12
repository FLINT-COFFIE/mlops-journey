# Write your solution here
def new_person(name: str, age: int):
    try:
        name = str(name)
        age = int(age)

    except:
        raise ValueError

    if 2 <= len(name) <= 40 and 0 < age <= 150:
        return name, age

    else:
        raise ValueError


print(new_person("Flint Coffie", 10))
