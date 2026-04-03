# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self, people: list):
        self.people = people
        
    def add(self, person: Person):
        self.people += person
        
    def is_empty(self):
        if len(self.people) == 0:
            return True
        return False
    
    def print_contents(self):
        for person in self.people:
            print person
            
            
#testing
room = Room()
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 155))
print("Is the room empty?", room.is_empty())
room.print_contents()