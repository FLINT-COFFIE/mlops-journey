# Write your solution here
def prime_numbers():
    x = 2
    for i in range(2, x):
        if x / i != 1:
            continue
    else:
        yield x
    x += 1