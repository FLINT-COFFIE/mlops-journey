# Write your solution here
def histogram(word: str):
    collection = {}
    for char in word:
        if char not in collection:
            collection[char] = "*"
        else:
            collection[char] += "*"

    for key, value in collection.items():
        print(f"{key} {value}")


if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")
