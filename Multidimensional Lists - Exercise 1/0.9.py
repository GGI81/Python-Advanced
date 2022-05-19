def read_square_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([int(i) for i in input().split()])

    return matrx


def is_explosion_valid(rows, cols, mat):
    damage = mat[rows][cols]
    if mat[rows][cols] > 0 and rows < len(mat) and cols < len(mat):
        mat[rows][cols] -= damage

    if mat[rows][cols + 1] > 0 and rows < len(mat) and cols + 1 < len(mat):
        mat[rows][cols + 1] -= damage

    if mat[rows][cols - 1] > 0 and rows < len(mat) and cols - 1 < len(mat):
        mat[rows][cols - 1] -= damage

    if mat[rows + 1][cols] > 0 and rows < len(mat) and cols < len(mat):
        mat[rows + 1][cols] -= damage

    if mat[rows + 1][cols + 1] > 0 and rows < len(mat) and cols + 1 < len(mat):
        mat[rows + 1][cols + 1] -= damage

    if mat[rows + 1][cols - 1] > 0 and rows < len(mat) and cols - 1 < len(mat):
        mat[rows + 1][cols - 1] -= damage

    if mat[rows - 1][cols] > 0 and rows < len(mat) and cols < len(mat):
        mat[rows - 1][cols] -= damage

    if mat[rows - 1][cols + 1] > 0 and rows < len(mat) and cols + 1 < len(mat):
        mat[rows - 1][cols + 1] -= damage

    if mat[rows - 1][cols - 1] > 0 and rows < len(mat) and cols - 1 < len(mat):
        mat[rows - 1][cols - 1] -= damage


matrix = read_square_matrix()
n = len(matrix)
m = len(matrix[0])

command = input().split()

for i in command:
    args = i.split(",")
    row = int(args[0])
    col = int(args[1])
    is_explosion_valid(row, col, matrix)

