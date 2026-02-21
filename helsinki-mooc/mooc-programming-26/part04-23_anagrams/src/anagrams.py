# Write your solution here
def anagrams(str1, str2):
    list1 = sorted(str1.lower())
    list2 = sorted(str2.lower())

    if list1 == list2:
        return True
    return False


if __name__ == "__main__":
    anagrams(str1, str2)
