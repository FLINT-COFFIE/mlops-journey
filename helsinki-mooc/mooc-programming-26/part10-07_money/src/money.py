# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros}.{self.cents:02d} eur"

    # equality between objects
    def __eq__(self, another):
        return self.euros == another.euros and self.cents == another.cents

    # other comparison operators
    def __lt__(self, another):
        if self.euros < another.euros:
            return True
        elif self.euros == another.euros and self.cents < another.cents:
            return True
        return False

    def __gt__(self, another):
        if self.euros > another.euros:
            return True
        elif self.euros == another.euros and self.cents > another.cents:
            return True
        return False

    def __ne__(self, another):
        return self.euros != another.euros or self.cents != another.cents

    # addition and subtraction
    def __add__(self, another):
        new_total = (self.euros * 100 + self.cents) + (
            another.euros * 100 + another.cents
        )
        new_euros = new_total // 100
        new_cents = new_total % 100
        return Money(new_euros, new_cents)

    def __sub__(self, another):
        new_total = (self.euros * 100 + self.cents) - (
            another.euros * 100 + another.cents
        )
        if new_total < 0:
            raise ValueError("a negative result is not allowed")
        else:
            new_euros = new_total // 100
            new_cents = new_total % 100
            return Money(new_euros, new_cents)


# if __name__ == "__main__":
e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2 - e1
