def read_matrix():
    rows, cols = [int(x) for x in input().split(", ")]
    matrx = []
    for i in range(rows):
        matrx.append([int(x) for x in input().split(", ")])

    return matrx


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

numbers = []
total = 0

for r in range(n - 1):
    for c in range(m - 1):
        square = matrix[r][c] + matrix[r][c + 1] + \
                 matrix[r + 1][c] + matrix[r + 1][c + 1]
        if total < square:
            total = square
            if len(numbers) == 0:
                numbers.append(matrix[r][c])
                numbers.append(matrix[r][c + 1])
                numbers.append(matrix[r + 1][c])
                numbers.append(matrix[r + 1][c + 1])
            else:
                numbers = []
                numbers.append(matrix[r][c])
                numbers.append(matrix[r][c + 1])
                numbers.append(matrix[r + 1][c])
                numbers.append(matrix[r + 1][c + 1])


counter = 0
for i in numbers:
    counter += 1
    if counter % 2 != 0:
        print(i, end=" ")
    else:
        print(i, end="\n")

print(total)