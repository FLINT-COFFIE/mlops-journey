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

    def print_items(self):
        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)")

    def heaviest_item(self):
        # heaviest = []
        heaviest = None
        # for item in self.__items:
        #    heaviest.append(item.weight())
        # max_weight = max(heaviest)
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item  # f"{item.name()} ({item.weight()} kg)"
        return heaviest

    def __str__(self):
        if len(self.__items) == 1:
            return f"1 item ({self.weight()} kg)"
        return f"{len(self.__items)} items ({self.weight()} kg)"


class CargoHold:
    def __init__(self, maximum_weight):
        self.__maximum_weight = maximum_weight
        self.__cargo = []

    def current_weight(self):
        weight = 0
        for suitcase in self.__cargo:
            weight += suitcase.weight()
        return weight

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.current_weight() <= self.__maximum_weight:
            self.__cargo.append(suitcase)

    def __str__(self):
        if len(self.__cargo) == 1:
            return f"1 suitcase, space for {self.__maximum_weight - self.current_weight()} kg"
        return f"{len(self.__cargo)} suitcases, space for {self.__maximum_weight - self.current_weight()} kg"

    def print_items(self):
        for suitcase in self.__cargo:
            suitcase.print_items()


# testing
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()
