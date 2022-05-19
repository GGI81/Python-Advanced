import sys
from io import StringIO

test_input1 = """6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left
"""

test_input2 = """7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down
"""


sys.stdin = StringIO(test_input1)


def read_matrix():  # Square matrix
    size = int(input())
    matrx = []
    for _ in range(size):
        matrx.append(list(input()))

    return matrx


def is_index_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


matrix = read_matrix()
n = len(matrix)

snake_row, snake_col = 0, 0

b_row, b_col = None, None

for r in range(n):
    for c in range(n):
        if matrix[r][c] == "S":
            snake_row = r
            snake_col = c

food_eaten = 0

while True:
    if food_eaten >= 10:
        print("You won! You fed the snake.")
        print(f"Food eaten: {food_eaten}")
        for i in matrix:
            print("".join(i))
        break
    command = input()
    if command == "left":
        if is_index_valid(snake_row, snake_col - 1, n):
            if matrix[snake_row][snake_col - 1] == "-":
                matrix[snake_row][snake_col] = "."
                snake_col -= 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row][snake_col - 1] == "*":
                matrix[snake_row][snake_col] = "."
                snake_col -= 1
                food_eaten += 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row][snake_col - 1] == "B":
                matrix[snake_row][snake_col] = "."
                snake_col -= 1
                matrix[snake_row][snake_col] = "."
                for r in range(n):
                    for c in range(n):
                        if matrix[r][c] == "B":
                            b_row = r
                            b_col = c
                snake_row, snake_col = b_row, b_col
                matrix[snake_row][snake_col] = "S"
        else:
            matrix[snake_row][snake_col] = "."
            print("Game over!")
            print(f"Food eaten: {food_eaten}")
            for i in matrix:
                print("".join(i))
            break
    elif command == "down":
        if is_index_valid(snake_row + 1, snake_col, n):
            if matrix[snake_row + 1][snake_col] == "-":
                matrix[snake_row][snake_col] = "."
                snake_row += 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row + 1][snake_col] == "*":
                matrix[snake_row][snake_col] = "."
                snake_row += 1
                food_eaten += 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row + 1][snake_col] == "B":
                matrix[snake_row][snake_col] = "."
                snake_row += 1
                matrix[snake_row][snake_col] = "."
                for r in range(n):
                    for c in range(n):
                        if matrix[r][c] == "B":
                            b_row = r
                            b_col = c
                snake_row, snake_col = b_row, b_col
                matrix[snake_row][snake_col] = "S"
        else:
            matrix[snake_row][snake_col] = "."
            print("Game over!")
            print(f"Food eaten: {food_eaten}")
            for i in matrix:
                print("".join(i))
            break
    elif command == "up":
        if is_index_valid(snake_row - 1, snake_col, n):
            if matrix[snake_row - 1][snake_col] == "-":
                matrix[snake_row][snake_col] = "."
                snake_row -= 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row - 1][snake_col] == "*":
                matrix[snake_row][snake_col] = "."
                snake_row -= 1
                food_eaten += 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row - 1][snake_col] == "B":
                matrix[snake_row][snake_col] = "."
                snake_row -= 1
                matrix[snake_row][snake_col] = "."
                for r in range(n):
                    for c in range(n):
                        if matrix[r][c] == "B":
                            b_row = r
                            b_col = c
                snake_row, snake_col = b_row, b_col
                matrix[snake_row][snake_col] = "S"
        else:
            matrix[snake_row][snake_col] = "."
            print("Game over!")
            print(f"Food eaten: {food_eaten}")
            for i in matrix:
                print("".join(i))
            break
    elif command == "right":
        if is_index_valid(snake_row, snake_col + 1, n):
            if matrix[snake_row][snake_col + 1] == "-":
                matrix[snake_row][snake_col] = "."
                snake_col += 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row][snake_col + 1] == "*":
                matrix[snake_row][snake_col] = "."
                snake_col += 1
                food_eaten += 1
                matrix[snake_row][snake_col] = "S"
            elif matrix[snake_row][snake_col + 1] == "B":
                matrix[snake_row][snake_col] = "."
                snake_col += 1
                matrix[snake_row][snake_col] = "."
                for r in range(n):
                    for c in range(n):
                        if matrix[r][c] == "B":
                            b_row = r
                            b_col = c
                snake_row, snake_col = b_row, b_col
                matrix[snake_row][snake_col] = "S"
        else:
            matrix[snake_row][snake_col] = "."
            print("Game over!")
            print(f"Food eaten: {food_eaten}")
            for i in matrix:
                print("".join(i))
            break
# 100 / 100