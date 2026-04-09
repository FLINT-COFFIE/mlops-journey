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


# if __name__ == "__main__":
e1 = Money(4, 10)
e2 = Money(2, 5)

print(e1 != e2)
print(e1 < e2)
print(e1 > e2)
