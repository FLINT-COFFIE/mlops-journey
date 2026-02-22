# Write your solution here
def sum_of_positives(list1):
    pos = []
    for i in list1:
        if i > 0:
            pos.append(i)
    return sum(pos)


if __name__ == "__main__":
    print("The result is", sum_of_positives([1, -2, 3, -4, 5]))
