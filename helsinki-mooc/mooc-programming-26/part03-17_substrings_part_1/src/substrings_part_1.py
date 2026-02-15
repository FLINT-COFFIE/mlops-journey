# Write your solution here
word = input("Please type in a string: ")

end = len(word)
start = 1

while end >= start:
    print(word[0:start])
    start += 1
