# --- DIAGONALS ---

# index  0  1  2  3  4

#   0    1  2  3  4  5
#   1    6  7  8  9  10
#   2    11 12 13 14 15
#   3    16 17 18 19 20
#   4    21 22 23 24 25


# 1 7 13 19 25  -> Primary Diagonal for this matrix  (TOP LEFT - BOTTOM RIGHT)
# -- >>  the ROW is equal to the column
#  row = col


# 5 9 13  17 21  -> Secondary Diagonal for this matrix  (TOP RIGHT - BOTTOM LEFT)
# -- >>  the ROW is equal to the columns count -1
#  row = columns count - col - 1


# Below PRIMARY Diagonal
# Taking values ONLY UNDER THE PRIMARY DIAGONAL
# 6 11 12 16 17 18 21 22 23 24
# row = 0.. n
# col = 0.. row


# Below PRIMARY Diagonal WITH THE DIAGONAL
# Taking the Primary diagonal with all numbers bellow it
# row = 0.. n
# col = 0.. row + 1

# Above Primary Diagonal
# Taking values ONLY ABOVE THE PRIMARY DIAGONAL
# row = 0.. n
# col = row + 1


# Below secondary diagonal
# row = 0.. n
# col = n - row - 1... n

# Above secondary diagonal
# row = 0.. n
# col = 0.. n - row - 2

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

n = 5

# Primary Diagonal
print(" --- Primary Diagonal --- ")
print(
    sum([matrix[i][i] for i in range(n)])
)

print()

# Secondary Diagonal
print(" --- Secondary Diagonal --- ")
print(
    sum([matrix[i][n - i - 1] for i in range(n)])
)

print()

# Below primary
print(" --- Below primary --- ")

below_primary_diagonal = []
for r in range(n):
    for c in range(r):
        below_primary_diagonal.append(matrix[r][c])
print(", ".join(map(str, below_primary_diagonal)))

print()

# Below primary Diagonal WITH THE PRIMARY DIAGONAL

print(" --- Below primary WITH PRIMARY --- ")

below_primary_diagonal_with_primary = []
for r in range(n):
    for c in range(r + 1):
        below_primary_diagonal_with_primary.append(matrix[r][c])
print(", ".join(map(str, below_primary_diagonal_with_primary)))

print()

print(" --- Above primary --- ")

above_primary = []
for r in range(n):
    for c in range(r + 1):
        above_primary.append(matrix[r][c])
print(", ".join(map(str, above_primary)))

print()

# print(" --- Below Secondary --- ")
#
# below_secondary = []
# for r in range(n):
#     for c in range(n - r - 1):
#         below_secondary.append(matrix[r][c])
# print(", ".join(map(str, below_secondary)))

print()

print(f" --- Above secondary --- ")

above_secondary = []
for r in range(n):
    for c in range(n - r - 1):
        above_secondary.append(matrix[r][c])
print(", ".join(map(str, above_secondary)))