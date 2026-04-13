# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as words:
        words = words.split()
        return{word: word.count() for word in words if word.count >= lower_limit}