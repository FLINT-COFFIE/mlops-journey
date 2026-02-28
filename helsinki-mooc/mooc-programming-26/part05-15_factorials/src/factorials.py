# Write your solution here
def factorials(n: int):
    fact = {}
    # use a for loop and range n
    for key in range(n, 0, -1):
        multiply = 1
        for value in range(key, 0, -1):
            multiply *= value
        fact[key] = multiply
    return fact


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
