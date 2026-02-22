# Write your solution here
def no_vowels(word):
    new_word = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in word:
        if char.lower() in vowels:
            continue
        new_word += char
    return new_word


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
