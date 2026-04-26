# Write your solution here

# fuction to read the files and return dictionary
def read():
    problem_sets = []
    filename = "solutions.csv"
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.split(";")
            problem_sets.append(line)
    return problem_sets


# use the function accessor to assess the operation
def accessor(problem_sets: list):
    # open and pass correct and incorrect files
    with open("correct.csv", "w") as f:
        pass
    # incorrect
    with open("incorrect.csv", "w") as f:
        pass

    # loopint through problem sets
    for profile in problem_sets:
        name = profile[0]
        target = int(profile[2])
        operation = profile[1]

        # define operation
        if "+" in operation:
            parts = operation.split("+")
            first_number = int(parts[0])
            second_number = int(parts[1])
            result = first_number + second_number

        # subtracting
        if "-" in operation:
            parts = operation.split("-")
            first_number = int(parts[0])
            second_number = int(parts[1])
            result = first_number - second_number

        # writing to files
        if result == target:
            with open("correct.csv", "a") as f:
                f.write(f"{name};{operation};{result}\n")

        elif result != target:
            with open("incorrect.csv", "a") as f:
                f.write(f"{name};{operation};{target}\n")


def filter_solutions():
    accessor(read())


if __name__ == "__main__":
    filter_solutions()
