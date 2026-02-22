# Write your solution here
def all_the_longest(str_list):
    longest = ""
    long_list = []
    for word in str_list:
        if len(word) > len(longest):
            longest = word
    for word in str_list:
        if len(longest) == len(word):
            long_list.append(word)
    return long_list


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)
