# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    # equality between objects
    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents

    # other comparison operators
    def __lt__(self, another):
        if self._euros < another._euros:
            return True
        elif self._euros == another._euros and self._cents < another._cents:
            return True
        return False

    def __gt__(self, another):
        if self._euros > another._euros:
            return True
        elif self._euros == another._euros and self._cents > another._cents:
            return True
        return False

    def __ne__(self, another):
        return self._euros != another._euros or self._cents != another._cents

    # addition and subtraction
    def __add__(self, another):
        new_total = (self._euros * 100 + self._cents) + (
            another._euros * 100 + another._cents
        )
        new_euros = new_total // 100
        new_cents = new_total % 100
        return Money(new_euros, new_cents)

    def __sub__(self, another):
        new_total = (self._euros * 100 + self._cents) - (
            another._euros * 100 + another._cents
        )
        if new_total < 0:
            raise ValueError("a negative result is not allowed")
        else:
            new_euros = new_total // 100
            new_cents = new_total % 100
            return Money(new_euros, new_cents)


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    print(e1)
    e1.euros = 1000
    print(e1)
