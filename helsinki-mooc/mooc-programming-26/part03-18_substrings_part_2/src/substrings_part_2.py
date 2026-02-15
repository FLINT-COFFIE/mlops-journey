# Write your solution here
word = input("Please type in a string: ")

end = -len(word)
inc = -1
while inc >= end:
    print(word[inc:])
    # debug print(inc)
    inc -= 1
