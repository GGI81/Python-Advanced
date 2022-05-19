def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size

size = int(input())

matrix = []

bunny_row, bunny_col = 0, 0

for r in range(size):
    elements = input().split()
    matrix.append(elements)
    for c in range(size):
        element = elements[c]
        if element == "B":
            bunny_row, bunny_col = r, c

directions = {
    "right": lambda row, col: (row, col + 1),
    "left": lambda row, col: (row, col - 1),
    "up": lambda row, col: (row - 1, col),
    "down": lambda row, col: (row + 1, col),
}

max_eggs = float("-inf")
best_direction = ""
best_path = []

for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    eggs = 0
    path = []
    while True:
        current_row, current_col = step(current_row, current_col)
        if not is_inside(current_row, current_col, size):
            break
        if matrix[current_row][current_col] == "X":
            break
        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])
    if eggs > max_eggs:
        max_eggs = eggs
        best_direction = direction
        best_path = path

print(best_direction)
for i in best_path:
    print(i)
print(max_eggs)