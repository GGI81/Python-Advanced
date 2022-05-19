import sys
from io import StringIO

test_input1 = """Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right
"""

test_input2 = """Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left
"""

test_input3 = """test
3
--P
---
---
1
up
"""

sys.stdin = StringIO(test_input1)


def read_matrix():
    num = int(input())
    matrx = []
    for _ in range(num):
        matrx.append(list(input()))

    return matrx


def is_index_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False

string = ""
WORD = input().split()
for i in WORD:
    string += i
matrix = read_matrix()
n = len(matrix)

player_row, player_col = 0, 0
for r in range(n):
    for c in range(n):
        if matrix[r][c] == "P":
            player_row = r
            player_col = c
            break

found_letters = []

number_command = int(input())
for i in range(number_command):
    command = input()
    if command == "up":
        if is_index_valid(player_row - 1, player_col, n):
            if matrix[player_row - 1][player_col] == "-":
                matrix[player_row][player_col] = "-"
                player_row -= 1
                matrix[player_row][player_col] = "P"
            elif matrix[player_row - 1][player_col].isalpha():
                matrix[player_row][player_col] = "-"
                player_row -= 1
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = "P"
        else:
            if len(string) > 0:
                string = string[:-1]
                break
    elif command == "down":
        if is_index_valid(player_row + 1, player_col, n):
            if matrix[player_row + 1][player_col] == "-":
                matrix[player_row][player_col] = "-"
                player_row += 1
                matrix[player_row][player_col] = "P"
            elif matrix[player_row + 1][player_col].isalpha():
                matrix[player_row][player_col] = "-"
                player_row += 1
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = "P"
        else:
            if len(string) > 0:
                string = string[:-1]
                break
    elif command == "left":
        if is_index_valid(player_row, player_col - 1, n):
            if matrix[player_row][player_col - 1] == "-":
                matrix[player_row][player_col] = "-"
                player_col -= 1
                matrix[player_row][player_col] = "P"
            elif matrix[player_row][player_col - 1].isalpha():
                matrix[player_row][player_col] = "-"
                player_col -= 1
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = "P"
        else:
            if len(string) > 0:
                string = string[:-1]
                break
    elif command == "right":
        if is_index_valid(player_row, player_col + 1, n):
            if matrix[player_row][player_col + 1] == "-":
                matrix[player_row][player_col] = "-"
                player_col += 1
                matrix[player_row][player_col] = "P"
            elif matrix[player_row][player_col + 1].isalpha():
                matrix[player_row][player_col] = "-"
                player_col += 1
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = "P"
        else:
            if len(string) > 0:
                string = string[:-1]
                break

print(string)
for i in matrix:
    print("".join(i))