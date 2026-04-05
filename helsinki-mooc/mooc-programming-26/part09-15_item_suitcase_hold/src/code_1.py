# Write your solution here:
# first class
class Item:
    # constructor
    def __init__(self, name, weight):
        # hidden attributes(encapsulated)
        self.__name = name
        self.__weight = weight


# second class
class Suitcase:
    def __init__(self, maximum_weight):
        self.__maximum_weight = maximum_weight
        self.__current_weight = 0
        self.__items = []

    def add_item(self, item: Item):
        if item.__weight + self.__current_weight <= 5:
            self.__current_weight += item.__weight
            self.__items.append(item)

    def __str__(self):
        return f"{len(self.__items)}"
