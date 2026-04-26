# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people = []
        self.sum_height = 0

    def add(self, person: Person):
        self.people.append(person)
        self.sum_height += person.height

    def is_empty(self):
        if len(self.people) == 0:
            return True
        return False

    def print_contents(self):
        print(
            f"There are {len(self.people)} persons in the room, and their combined height is {self.sum_height} cm"
        )
        for person in self.people:
            print(f"{person} ({person.height} cm)")

    def shortest(self):
        if len(self.people) == 0:
            return None

        short_person = self.people[0]
        for person in self.people:
            if person.height < short_person.height:
                short_person = person
        return short_person

    def remove_shortest(self):
        if len(self.people) == 0:
            return None

        short = self.shortest()
        self.sum_height -= short.height
        self.people.remove(short)
        if short is not None:
            return short


if __name__ == "__main__":
    # testing
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
