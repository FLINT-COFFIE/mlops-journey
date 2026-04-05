# Write your solution here:
# first class
class Item:
    # constructor
    def __init__(self, name, weight):
        # hidden attributes(encapsulated)
        self.__name = name
        self.__weight = weight

    def weight(self):
        return self.__weight

    def name(self):
        return self.__name


# second class
class Suitcase:
    def __init__(self, maximum_weight):
        self.__maximum_weight = maximum_weight
        self.__items = []

    def weight(self):
        current_weight = 0
        for item in self.__items:
            current_weight += item.weight()
        return current_weight

    def add_item(self, item: Item):
        total_weight = self.weight()
        if item.weight() + total_weight <= self.__maximum_weight:
            total_weight += item.weight()
            self.__items.append(item)

    def __str__(self):
        if len(self.__items) == 1:
            return f"1 item ({self.weight} kg)"
        return f"{len(self.__items)} items ({self.weight} kg)"

    def print_items(self):
        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)")

    def heaviest_item(self):
        heaviest = []
        heavy = None
        for item in self.__items:
            heaviest.append(item.weight())
        max_weight = max(heaviest)
        for item in self.__items:
            if item.weight == max_weight:
                heavy = item
        return heavy


# testing
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(10)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

heaviest = suitcase.heaviest_item()
print(f"The heaviest item: {heaviest}")
