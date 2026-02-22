# Write your solution here
def most_common_character(word):
    common = 0
    freq = ""
    for char in word:
        count = word.count(char)
        if count >= common:
            common = count

        if word.count(char) == common:
            freq = char
    return freq


if __name__ == "__main__":
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
