# Sum Matrix Columns


def read_matrix():
    rows, cols = [int(x) for x in input().split(", ")]
    matrix = []
    for i in range(rows):
        matrix.append([int(x) for x in input().split()])

    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
columns = [0] * m

for r in range(n):
    for c in range(m):
        value = matrix[r][c]
        columns[c] += value

for i in columns:
    print(i, end="\n")