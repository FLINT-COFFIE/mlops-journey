# Write your solution here
word = input("Please type in a string: ")
limit = 20
fill = 20 - len(word)

if fill > 0:
    print(f"{'*' * fill}{word}")

else:
    print(word)
