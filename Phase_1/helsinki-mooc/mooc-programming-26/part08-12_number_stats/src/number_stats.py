# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum_even = 0
        self.sum_odd = 0

    def add_number(self, number: int):
        self.numbers += number
        self.count += 1
        # even and odd
        if number % 2 == 0:
            self.sum_even += number
        elif number % 2 == 1:
            self.sum_odd += number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers

    def average(self):
        if self.count == 0:
            return 0
        return self.numbers / self.count

    def even_sum(self):
        return self.sum_even

    def odd_sum(self):
        return self.sum_odd


# Part 3
print("Please type in integer numbers:")
add = NumberStats()

while True:
    num = int(input(""))
    # less than zero
    if num < 0:
        break

    # adding number
    add.add_number(num)

# final result
print(f"Sum of numbers: {add.get_sum()}")
print(f"Mean of numbers: {add.average()}")
print(f"Sum of even numbers: {add.even_sum()}")
print(f"Sum of odd numbers: {add.odd_sum()}")
