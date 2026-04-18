# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
    return (characters[i : i + 3] for i in range(amount))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)