matrix = [
    [7, 1, 3, 3, 2, 1],
    [1, 3, 9, 8, 5, 6],
    [4, 6, 7, 9, 1, 0],
]

print(matrix[1])
ll = matrix[1]
print(ll[3])

print()

print(matrix[1][3])
print(matrix[2][2])
print(matrix[-1])
#  --> Last row
print(matrix[-1][-1])

print()

print(matrix[1][5])
print(matrix[1][-1])

print()

# Example with 3-dimensional list
matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(matrix[0][1][1])  # 4

cube = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ],
    [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9],
    ]
]

print(cube[1][1][1])
# -5

print()
print()
print()

# Using loops to traverse multidimensional list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row_index in range(len(matrix)):  # [1, 2, 3]
    for column_index in range(len(matrix[row_index])):  # (first iteration) -> 1 2 3 (second iteration) -> 4 5 6 (third iteration) -> 7 8 9
        print(matrix[row_index][column_index], end=" ")  # Result -> 1 2 3 4 5 6 7 8 9
