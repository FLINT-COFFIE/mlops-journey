# Write your solution here
def everything_reversed(list1):
    inverse = list1[::-1]
    for i in range(len(inverse)):
        inverse[i] = inverse[i][::-1]

    return inverse


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
