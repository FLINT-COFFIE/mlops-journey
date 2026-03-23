# Write your solution here
def row_sums(my_matrix: list):
    # looping through my_matrix
    for row in my_matrix:
        # adding sum to each row
        row.append(sum(row))
