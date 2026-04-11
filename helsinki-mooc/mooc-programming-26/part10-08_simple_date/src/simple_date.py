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

    def __ne__(self, another: "SimpleDate"):
        return (
            self.year != another.year
            or self.month != another.month
            or self.day != another.day
        )

    def total_days(self):
        return self.day + self.month * 30 + self.year * 360

    def __add__(self, days: int):
        total_days = self.total_days() + days

        new_year = total_days // 360
        remaining_days = total_days % 360

        new_days = remaining_days % 30
        new_month = remaining_days // 30

        if new_month == 0:
            new_month = 12
            new_year -= 1

        if new_days == 0:
            new_days = 30
            new_month -= 1

        return SimpleDate(new_days, new_month, new_year)

    def __sub__(self, other):
        return abs(self.total_days() - other.total_days())

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


# testing
d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(2, 11, 2020)
d3 = SimpleDate(28, 12, 1985)

print(d2 - d1)
print(d1 - d2)
print(d1 - d3)
