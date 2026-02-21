# Write your solution here
def palindromes(word):
    list1 = []
    list2 = []
    for char in word:
        list1.append(char)
    list2 = list1[::-1]

    if list2 == list1:
        return True
    return False


while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
