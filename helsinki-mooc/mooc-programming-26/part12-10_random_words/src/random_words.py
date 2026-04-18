# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
    return (characters[i : length] for i in range(amount))