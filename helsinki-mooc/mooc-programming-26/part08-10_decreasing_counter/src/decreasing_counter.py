# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.initial_value >= 1:
            self.initial_value -= 1

    def set_to_zero(self):
        self.initial_value = 0

    # Write the rest of the methods here!
