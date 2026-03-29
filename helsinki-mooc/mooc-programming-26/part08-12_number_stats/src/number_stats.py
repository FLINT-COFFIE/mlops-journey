# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number: int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers

    def average(self):
        return self.numbers / self.count


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
