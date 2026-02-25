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


# call the function

if __name__ == "__main__":
    sudoku = [
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

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
