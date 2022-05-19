def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrx = []
    for i in range(rows):
        matrx.append([int(x) for x in input().split()])

    return matrx


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

best_row = 0
best_col = 0

total = 0
best_numbers_matrix = []

for r in range(n - 2):
    for c in range(m - 2):
        current_3x3 = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + \
                        matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] + \
                        matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if total < current_3x3:
            total = current_3x3
            best_row = r
            best_col = c

print(f"Sum = {total}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}")
