# Write your solution here
word = input("Word: ")

spacing = 28 - len(word)

print("*" * 30)

if spacing % 2 == 0:
    space = (spacing // 2) * " "
    print(f"*{space}{word}{space}*")

elif spacing % 2 != 0:
    left = spacing // 2
    right = spacing - left
    print(f"*{left * ' '}{word}{right * ' '}*")

print("*" * 30)
