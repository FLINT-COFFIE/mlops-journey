# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros."

    def deposit_money(self, amount: int):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        else:
            self.balance += amount


# testing
card = LunchCard(10)
card.deposit_money(-10)
