# WRITE YOUR SOLUTION HERE:
from collections import Counter


class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        unique = Counter(my_list)
        highest = unique.most_common(1)
        return highest[0][0]

    @classmethod
    def doubles(cls, my_list: list):
        unique = Counter(my_list)
        doubles = []
        for num, counts in unique.items():
            if counts >= 2:
                doubles.append(num)
        return doubles


# testing
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
