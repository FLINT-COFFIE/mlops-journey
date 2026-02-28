# Write your solution here
def times_ten(start_index: int, end_index: int):
    # use a for loop to append keys to the dict
    by_ten = {}
    for key in range(start_index, end_index + 1):
        by_ten[key] = key * 10

    return by_ten


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
