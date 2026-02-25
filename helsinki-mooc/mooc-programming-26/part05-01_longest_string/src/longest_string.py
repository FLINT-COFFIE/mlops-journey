# Write your solution here
def longest(strings: list):
    long = 0
    for word in strings:
        if len(word) > long:
            long = len(word)
    for word in strings:
        if len(word) == long:
            return word


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
