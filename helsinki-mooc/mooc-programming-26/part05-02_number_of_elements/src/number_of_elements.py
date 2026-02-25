# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    # store count
    count = 0
    # loop through row
    for row in my_matrix:
        # loop through column
        for column in row:
            if column == element:
                # increase count
                count += 1
    return count


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
