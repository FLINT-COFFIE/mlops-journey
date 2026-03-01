# Write your solution here
def dict_of_numbers():
    # hard code the building blocks
    ones = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero",
    }

    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eithteen",
        19: "nineteen",
    }

    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    # empty dict
    number = {}
    # using a for loop to add the keys
    for num in range(0, 20):
        # break num down and get the word in one variable
        if num < 10:
            number[num] = ones[num]
        elif num < 20:
            number[num] = teens[num]

    return number


numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
