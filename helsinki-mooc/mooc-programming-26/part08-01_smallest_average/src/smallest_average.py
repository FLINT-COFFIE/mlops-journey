# Write your solution here
# helper function
def average(person: dict):
    # helper variable
    sum = 0
    # loop through dict
    for key, value in person.items():
        if key == "name":
            continue
        sum += value
    # defining average
    average = sum / len(person)

    # returning average
    return average


# defining function
def smallest_average(person1: dict, person2: dict, person3: dict):
    averages = [average(person1), average(person2), average(person3)]
    return min(averages)
