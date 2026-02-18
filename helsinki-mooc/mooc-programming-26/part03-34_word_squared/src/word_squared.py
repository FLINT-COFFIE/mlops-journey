# Write your solution here
def squared(word, num):
    # define variables
    row = 0
    index = 0
    # conditionals
    while row < num:
        # line to print
        line = ""
        col = 0
        while col < num:
            char = word[index % len(word)]
            line += char
            col += 1
            index += 1
        row += 1
        print(line)
