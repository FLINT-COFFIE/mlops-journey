# Write your solution here


def same_chars(word, int1, int2):
    if int1 >= len(word) or int2 >= len(word) or int1 < 0 or int2 < 0:
        return False
    return word[int1] == word[int2]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("aaaa", 1, 2))
