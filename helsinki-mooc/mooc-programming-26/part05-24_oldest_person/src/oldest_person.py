# Write your solution here
def oldest_person(people: list):
    oldest = []
    for person in people:
        oldest.append(person[1])
    old = min(oldest)

    for person in people:
        if old in person:
            return person[0]


if __name__ == "__main__":
    people_list = [("Arthur", 1977), ("Emily", 2014)]
    print(oldest_person(people_list))
