# Write your solution here
def invert(dictionary: dict):
    inverted = {}
    for key, value in dictionary.items():
        inverted[value] = key
    return inverted


s = {1: "first", 2: "second", 3: "third", 4: "fourth"}

print(s)
print(invert(s))
