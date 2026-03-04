# write your solution here'

# open file
with open("fruits.csv") as f:
    # create a dictonary
    fruits = {}
    # loop through
    for line in f:
        # replace newline with nothing
        line = line.replace("\n", "")
        parts = line.split(";")

        fruit = parts[0]
        # append key values and float values
        fruits[fruit] = parts[1:]

    print(fruits)
