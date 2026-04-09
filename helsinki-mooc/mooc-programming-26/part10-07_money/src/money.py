# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        fig = f"{self.euros}.{self.cents}"
        fig = float(fig)
        if self.cents < 10:
            return f"{self.euros}.0{self.cents} eur"
        return f"{fig:.2f} eur"

    # equality between objects
    def __eq__(self, another):
        return self == another


if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)
