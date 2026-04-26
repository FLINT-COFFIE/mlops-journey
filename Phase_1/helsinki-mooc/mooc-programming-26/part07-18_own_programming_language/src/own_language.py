# Write your solution here
# imports
import string


# defining the function
def run(program):
    # A-Z
    variables = {char: 0 for char in string.ascii_uppercase}
    results = []

    # whic lines contains commands with :
    labels = {}
    for index, line in enumerate(program):
        if line.endswith(":"):
            labels[line[:-1]] = index

    # Function to check existing value or return an int
    def get_value(x):
        if x in variables:
            return variables[x]
        return int(x)

    # moving through
    i = 0
    while i < len(program):
        parts = program[i].split()
        command = parts[0]

        # Calculations and output
        if command == "PRINT":
            results.append(get_value(parts[1]))
        elif command == "MOV":
            variables[parts[1]] = get_value(parts[2])
        elif command == "ADD":
            variables[parts[1]] += get_value(parts[2])
        elif command == "SUB":
            variables[parts[1]] -= get_value(parts[2])
        elif command == "MUL":
            variables[parts[1]] *= get_value(parts[2])

        elif command == "JUMP":
            i = labels[parts[1]]
            continue

        elif command == "IF":
            value1 = get_value(parts[1])
            operator = parts[2]
            value2 = get_value(parts[3])
            target = parts[5]

            condition_met = False
            if operator == "==":
                condition_met = value1 == value2
            elif operator == "!=":
                condition_met = value1 != value2
            elif operator == "<=":
                condition_met = value1 <= value2
            elif operator == ">=":
                condition_met = value1 >= value2
            elif operator == "<":
                condition_met = value1 < value2
            elif operator == ">":
                condition_met = value1 > value2

            if condition_met:
                i = labels[target]
                continue

        elif command == "END":
            break

        i += 1

    return results


if __name__ == "__main__":
    ##
    program = "PRINT [value]"
    run(program)
