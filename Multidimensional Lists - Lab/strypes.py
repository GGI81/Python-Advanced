matrix = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

total = 0


for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        a = matrix[r][c]
        if matrix[r][c] != 2 and r != c:
            total += matrix[r][c]


"""
r    c     total      matrix[r][c]
0    0       0               1
"""