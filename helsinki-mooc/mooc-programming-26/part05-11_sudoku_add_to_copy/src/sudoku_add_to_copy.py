# Write your solution here
def print_sudoku(sudoku: list):
    row_count = 0
    for row in sudoku:
        if row_count != 0 and row_count % 3 == 0:
            print()
        count = 0
        for col in row:
            if count != 0 and count % 3 == 0:
                print(" ", end="")

            if col == 0:
                print("_", end=" ")
            else:
                print(col, end=" ")
            count += 1
        row_count += 1
        print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_grid = []
    for row in sudoku:
        new_grid.append(row[:])
    new_grid[row_no][column_no] = number

    return new_grid


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
