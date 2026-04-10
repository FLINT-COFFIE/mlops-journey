# WRITE YOUR SOLUTION HERE:
# simple date comparison
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, another: "SimpleDate"):
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
            return True
