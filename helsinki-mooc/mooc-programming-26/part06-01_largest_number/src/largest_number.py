# write your solution here
def largest():
    with open("numbers.txt") as n:
        max = 0
        for num in n:
            num = num.replace("\n", "")
            num = int(num)
            if num > max:
                max = num
    return max


if __name__ == "__main__":
    print(largest())
