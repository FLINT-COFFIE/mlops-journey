# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        self.balance -= 2.60

    def eat_special(self):
        self.balance -= 4.60

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros."


# testing
card = LunchCard(50)
print(card)

card.eat_lunch()
print(card)

card.eat_special()
card.eat_lunch()
print(card)
