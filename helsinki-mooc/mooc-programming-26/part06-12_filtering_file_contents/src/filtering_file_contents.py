# Write your solution here

# open and pass correct and incorrect files

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

    for profile in problem_sets:
        name = profile[0]
        target = int(profile[2])
        operation = profile[1]

        first_number = ""
        second_number = ""
        # define operation
        for i in operation:
            first_number += i
            operand = operation[len(first_number)]
            second_number += operation[len(first_number) + 2 :]

        first_number = int(first_number)
        second_number = int(second_number)

        if operand == "+":
            result = first_number + second_number

        elif operand == "-":
            result = first_number - second_number

        if result == target:
            with open("correct.csv", "a") as f:
                f.write(f"{name};{operation};{result}")

        else:
            with open("incorrect.csv", "a") as f:
                f.write(f"{name};{operation};{result}")
