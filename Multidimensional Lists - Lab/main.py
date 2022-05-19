matrix = []

for i in range(3):
    rows = []
    for j in range(1, 4):
        rows.append(j)
    matrix.append(rows)
print(matrix)

print()
print()
print()

matrix = []

for i in range(3):
    matrix.append([])
    for j in range(2):
        matrix[i].append(0)
print(matrix)

# Indices
#      0          1           2
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# 1 2 3
# 1 2 3   | = Rows
# 1 2 3   - = Columns

