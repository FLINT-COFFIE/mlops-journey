# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as words:
        words = words.read()
        words = words.replace(".", "").replace(",","")
        words = words.split()
        return{word : words.count(word) for word in words if words.count(word) >= lower_limit}