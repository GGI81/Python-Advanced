def read_matrix():
    rows, cols = [int(x) for x in input().split(", ")]
    matrx = []
    for i in range(rows):
        matrx.append([int(x) for x in input().split()])

    return matrx


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

columns_total = [0] * m

for r in range(n):
    for c in range(m):
        value = matrix[r][c]
        columns_total[c] += value

for i in columns_total:
    print(i, end="\n")