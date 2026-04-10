# WRITE YOUR SOLUTION HERE:
# simple date comparison
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, another: "SimpleDate"):
        if self.year < another.year:
            return True
        elif self.year == another.year and self.month < another.month:
            return True
        elif (
            self.year == another.year
            and self.month < another.month
            and self.day < another.day
        ):
            return True
        else:
            return False

    def __gt__(self, another: "SimpleDate"):
        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif (
            self.year == another.year
            and self.month > another.month
            and self.day > another.day
        ):
            return True
        else:
            return False

    def __eq__(self, another: "SimpleDate"):
        return (
            self.year == another.year
            and self.month == another.month
            and self.day == another.day
        )


# testing
d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)
d3 = SimpleDate(28, 12, 1985)

print(d1 == d3)
print(d1 < d2)
print(d1 > d2)
