# Square Matrix
# Chess

def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        letters = input()
        matrx.append(list(letters))

    return matrx


def is_knight_placed(board, row, col):
    size = len(board)
    if row < 0 or col < 0 or row >= size or col >= size:
        return False
    return board[row][col] == "K"


def count_affected_knights(board, row, col):
    result = 0
    if is_knight_placed(board, row - 2, col - 1):
        result += 1
    if is_knight_placed(board, row - 2, col + 1):
        result += 1
    if is_knight_placed(board, row + 2, col - 1):
        result += 1
    if is_knight_placed(board, row + 2, col + 1):
        result += 1
    if is_knight_placed(board, row - 1, col - 2):
        result += 1
    if is_knight_placed(board, row - 1, col + 2):
        result += 1
    if is_knight_placed(board, row + 1, col - 2):
        result += 1
    if is_knight_placed(board, row + 1, col + 2):
        result += 1
    return result


matrix = read_matrix()
n = len(matrix)

removed_knights = 0

while True:
    max_count = 0
    knight_row = 0
    knight_col = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == "0":
                continue
            else:
                count = count_affected_knights(matrix, r, c)
                if count > max_count:
                    max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)