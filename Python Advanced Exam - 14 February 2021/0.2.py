from math import floor
import sys
from io import StringIO

test_input1 = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
right
right
up
up
left
down
"""


test_input2 = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
left
"""

sys.stdin = StringIO(test_input2)

def read_matrix():
    size = int(input())
    matrx = []
    for _ in range(size):
        matrx.append(list(input().split()))

    return matrx


def is_index_valid(row, col, size_matrix):
    if 0 <= row < size_matrix and 0 <= col < size_matrix:
        return True
    return False


matrix = read_matrix()
n = len(matrix)

player_row, player_col = 0, 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] == "P":
            player_row = r
            player_col = c
            break

total_coins = 0
path = []

while True:
    if total_coins >= 100:
        print(f"You won! You've collected {total_coins} coins.")
        print(f"Your path:")
        for i in path:
            print(i)
        break
    command = input()
    if command == "right":
        if is_index_valid(player_row, player_col + 1, n):
            if matrix[player_row][player_col + 1].isnumeric():
                matrix[player_row][player_col] = "0"
                player_col += 1
                path.append([player_row, player_col])
                total_coins += int(matrix[player_row][player_col])
            elif matrix[player_row][player_col + 1] == "X":
                result_coins = floor(total_coins / 2)
                print(f"Game over! You've collected {result_coins} coins.")
                print(f"Your path:")
                for i in path:
                    print(i)
                break
        else:
            result_coins = floor(total_coins / 2)
            print(f"Game over! You've collected {result_coins} coins.")
            print(f"Your path:")
            for i in path:
                print(i)
            break
    elif command == "left":
        if is_index_valid(player_row, player_col - 1, n):
            if matrix[player_row][player_col - 1].isnumeric():
                matrix[player_row][player_col] = "0"
                player_col -= 1
                path.append([player_row, player_col])
                total_coins += int(matrix[player_row][player_col])
            elif matrix[player_row][player_col - 1] == "X":
                result_coins = floor(total_coins / 2)
                print(f"Game over! You've collected {result_coins} coins.")
                print(f"Your path:")
                for i in path:
                    print(i)
                break
        else:
            result_coins = floor(total_coins / 2)
            print(f"Game over! You've collected {result_coins} coins.")
            print(f"Your path:")
            for i in path:
                print(i)
            break
    elif command == "down":
        if is_index_valid(player_row + 1, player_col, n):
            if matrix[player_row + 1][player_col].isnumeric():
                matrix[player_row][player_col] = "0"
                player_row += 1
                path.append([player_row, player_col])
                total_coins += int(matrix[player_row][player_col])
            elif matrix[player_row + 1][player_col] == "X":
                result_coins = floor(total_coins / 2)
                print(f"Game over! You've collected {result_coins} coins.")
                print(f"Your path:")
                for i in path:
                    print(i)
                break
        else:
            result_coins = floor(total_coins / 2)
            print(f"Game over! You've collected {result_coins} coins.")
            print(f"Your path:")
            for i in path:
                print(i)
            break
    elif command == "up":
        if is_index_valid(player_row - 1, player_col, n):
            if matrix[player_row - 1][player_col].isnumeric():
                matrix[player_row][player_col] = "0"
                player_row -= 1
                path.append([player_row, player_col])
                total_coins += int(matrix[player_row][player_col])
            elif matrix[player_row - 1][player_col] == "X":
                result_coins = floor(total_coins / 2)
                print(f"Game over! You've collected {result_coins} coins.")
                print(f"Your path:")
                for i in path:
                    print(i)
                break
        else:
            result_coins = floor(total_coins / 2)
            print(f"Game over! You've collected {result_coins} coins.")
            print(f"Your path:")
            for i in path:
                print(i)
            break
