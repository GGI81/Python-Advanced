# There can be more than one additional dimension to list
# Multi-dimensional lists are the lists within lists

# Examples:
#   1. A grid is a basic example of two-dimensional list
#   2. A cube is a basic example ot three-dimensional list

# USAGE
#   1. When dealing with graphics (pixels on the screen are in
#       a grid formation)
#   2. When working with tabular data
#   3. Game development
#   4. Other cases when you want each item of your list to be
#       another list (Example: list of students, each of which has
#       many tests

ll = [1, 2, 3, 4, 5]
matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
]
print(f"Matrix")
print(matrix)

print()

# Using loops
print("Making Matrix using a loop")
matrix = []

rows_count = 3
columns_count = 2

for row_index in range(rows_count):
    row = []
    for column_index in range(columns_count):
        row.append(0)
    matrix.append(row)
print(matrix)

print()

# Using comprehension  !!!(Don't use comprehension)!!!
print("Making Matrix using a comprehension")
matrix = [[0 for j in range(2)] for i in range(3)]

print(matrix)

print()
print()
print()


# Taking numbers from matrix
matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5]
]

print("Returns the whole matrix")
print(matrix)   # Returns the whole matrix
print()

print("Returns the list on its index")
print(matrix[1])    # Returns the list on its index
print()

print("Returns the specific number from the inside list")
print(matrix[1][2])     # Returns the specific number from the inside list -> 4
print()
