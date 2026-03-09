# Write your solution here
def store_personal_data(person: tuple):
    name, age, height = person
    with open("people.csv", "a") as file:
        file.write(f"{name};{age};{height}\n")


# ask for input
people = "(Paul Paulson; 37; 175.5)"
# input("input person: ")
person = people.strip("()")
person = tuple(person.split(";"))
