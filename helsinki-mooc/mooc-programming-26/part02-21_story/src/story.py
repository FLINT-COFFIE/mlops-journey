# Write your solution here
codes = ""
last = ""

while True:
    code = input("Please type in a word: ")

    if code == "end":
        print(codes)
        break

    if code == last:
        print(codes)
        break

    codes += code + " "
    last = code
