def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrx = []
    for i in range(rows):
        matrx.append(list(input().split()))

    return matrx


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

counter = 0
for r in range(n - 1):
    for c in range(m - 1):
        if matrix[r][c] == matrix[r][c + 1] == \
                matrix[r + 1][c] == matrix[r + 1][c + 1]:
            counter += 1

print(counter)
