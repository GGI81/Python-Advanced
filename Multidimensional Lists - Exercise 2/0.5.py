def get_next_position(direction, r, c):
    if direction == "up":
        return (r - 1, c)
    if direction == "down":
        return (r + 1, c)
    if direction == "right":
        return (r, c + 1)
    if direction == "left":
        return (r, c - 1)


def is_outside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return False
    return True


size = int(input())

matrix = []

alice_row, alice_col = 0, 0
for r in range(size):
    elements = input().split()
    matrix.append(elements)
    for c in range(size):
        if matrix[r][c] == "A":
            alice_row, alice_col = r, c

tea_bags = 0
matrix[alice_row][alice_col] = "*"
while True:
    command = input()
    alice_row, alice_col = get_next_position(command, alice_row, alice_col)
    if is_outside(alice_row, alice_col, size):
        break
    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"
    if cell_value == "R":
        break
    if cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(" ".join(row))
