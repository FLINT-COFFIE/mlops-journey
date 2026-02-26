# Write your solution here
# define the function
def row_correct(sudoku: list, row_no: int):
    # loop through row
    for column in sudoku[row_no]:
        if column == 0:
            continue
        count = sudoku[row_no].count(column)
        # check if number occurs at most once
        if count > 1:
            return False

        # return true if yes and false if no
    return True


def column_correct(sudoku: list, column_no: int):
    columns = []
    # loop through row
    for row in sudoku:
        if row[column_no] == 0:
            continue
        elif row[column_no] > 0:
            columns.append(row[column_no])

    # check for counts
    count = 1
    for i in columns:
        total = columns.count(i)

        if total > count:
            return False

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    found = []
    for row_number in range(row_no, row_no + 3):
        for column_number in range(column_no, column_no + 3):
            number = sudoku[row_number][column_number]

            if number != 0:
                if number in found:
                    return False
                else:
                    found.append(number)
    return True


# define the function
def sudoku_grid_correct(sudoku: list):

    for row in range(9):
        if row_correct(sudoku, row) == False:
            return False

    for col in range(9):
        if column_correct(sudoku, col) == False:
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if block_correct(sudoku, row, col) == False:
                return False

    return True


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(sudoku_grid_correct(sudoku2))
    sudoku_grid_correct
