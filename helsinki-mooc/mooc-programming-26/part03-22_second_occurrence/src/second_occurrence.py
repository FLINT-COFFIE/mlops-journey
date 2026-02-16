# Write your solution here
word = input("Enter a word: ")
sub = input("please type in substring: ")

# execute if true
if sub in word:
    index = word.find(sub)
    # length of substring
    addlen = len(sub)
    # new word
    update_word = word[index + addlen :]
    new_index = update_word.find(sub)

    difference = len(word) - len(update_word)

    if new_index == -1:
        print("The substring does not occur twice in the string.")

    else:
        print(
            f"The second occurrence of the substring is at index {new_index + difference}."
        )

else:
    print("The substring does not occur twice in the string.")
