# Write your solution here
def length_of_longest(str_list):
    longest = ""
    for word in str_list:
        if len(word) > len(longest):
            longest = word
    return len(longest)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
