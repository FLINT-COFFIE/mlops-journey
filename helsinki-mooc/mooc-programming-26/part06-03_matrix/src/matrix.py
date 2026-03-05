# write your solution here
def read():
    # reading the file
    with open("matrix.txt") as f:
        matrix = []
        for line in f:
            line = line.replace("\n", "")
            line = line.split(",")
            for num in line:
                matrix.append(int(num))
        return matrix


def matrix_sum():
    matrix = read()
    return sum(matrix)


def matrix_max():
    matrix = read()
    return max(matrix)


def row_sums():
    # reading the file
    with open("matrix.txt") as f:
        matrix = {}
        add = []
        sum_num = []

        for line in f:
            line = line.replace("\n", "")
            line = line.split(",")
            add.append(line)

        for row in add:
            addition = 0
            for i in range(len(row)):
                number = int(row[i])
                addition += number
            sum_num.append(addition)
        return sum_num


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
