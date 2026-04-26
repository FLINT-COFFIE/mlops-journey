# Write your solution here
def prime_numbers():
    try:
        x = 2
        while True:
            for i in range(2, x):
                if x % i == 0:
                    break
                   
            else:
                yield x
            x += 1
    
    except StopIteration:
        print("ran out of numbers")
        

if __name__ == "__main__":
    #testing
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))