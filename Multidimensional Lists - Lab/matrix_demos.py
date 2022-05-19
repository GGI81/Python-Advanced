ll = [1, 2, 3, 4]

print(ll[2])


strings = [
    "Doncho",
    "Pesho",
    "Gosho"
]

print()

list_of_lists = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
]

print(strings[2])
print(list_of_lists[2])

print()
print()

# Creating
"""
[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
"""

n = 5  # rows
m = 4  # columns count

matrix_of_zeros = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(0)
    matrix_of_zeros.append(row)

print(matrix_of_zeros)


