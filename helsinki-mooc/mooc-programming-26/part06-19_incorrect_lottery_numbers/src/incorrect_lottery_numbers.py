# Write your solution here
# read and return dictionary
def read():
    lottery = {}
    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")

            week = parts[0]
            lottery_numbers = parts[1]
            lottery[week] = lottery_numbers
    return lottery


# filter the data
def filter_weeks(lottery: dict):

    keys = []
    values = []

    correct = {}

    for key, value in lottery.items():
        keys.append(key)
        values.append(value)

    for key in keys:
        parts = key.split(" ")
        key_num = parts[1]

        try:
            key_num = int(key_num)
            correct[key] = value
        except ValueError:
            continue
    return correct


print(filter_weeks(read()))
