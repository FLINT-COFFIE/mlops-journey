# Write your solution here
def transpose(matrix: list):
    T = []
    for row in range(len(matrix)):
        trans = []
        for col in range(len(matrix)):
            trans.append(matrix[col][row])
        T.append(trans)
    matrix[:] = T


if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(transpose(mat))
