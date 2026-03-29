# Write your solution here:
class Person:
    def __init__(self, name):
        self.name = name

    def return_first_name(self):
        parts = self.name.split()
        first_name = parts[0]
        return first_name

    def return_second_name(self):
        parts = self.name.split()
        second_name = parts[1]
        return second_name


# testing
