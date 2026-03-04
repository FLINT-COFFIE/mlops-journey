# write your solution here'
def read_fruits():
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
            price = float(parts[1:][0])
            # append key values and float values
            fruits[fruit] = price

        return fruits


if __name__ == "__main__":
    read_fruits()
