# Write your solution here
def create_tuple(x: int, y: int, z: int):
    word = [x, y, z]
    first = min(word)
    second = max(word)
    third = x + y + z

    return (first, second, third)


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
