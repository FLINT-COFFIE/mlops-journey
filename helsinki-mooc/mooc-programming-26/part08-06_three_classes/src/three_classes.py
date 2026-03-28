# Write your solution here
# definig classes
class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries
class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount
        
class Cable: