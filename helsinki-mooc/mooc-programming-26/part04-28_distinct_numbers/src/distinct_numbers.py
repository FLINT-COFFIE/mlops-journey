# Write your solution here
def distinct_numbers(list1):
    new_list = []
    for i in list1:
        if i in new_list:
            continue
        new_list.append(i)
    return sorted(new_list)


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]
