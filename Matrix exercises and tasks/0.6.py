# Symbol in Matrix

def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append(list(input()))

    return matrx


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

searched_symbol = input()
is_found = False
symbol_row, symbol_col = 0, 0

for r in range(n):
    for c in range(m):
        if matrix[r][c] == searched_symbol:
            symbol_row = r
            symbol_col = c
            is_found = True
            break

if is_found == True:
    print((symbol_row, symbol_col))
else:
    print(f"{searched_symbol} does not occur in the matrix")

