def read_matrix():
    rows, cols = [int(x) for x in input().split(", ")]
    matrx = []
    for i in range(rows):
        matrx.append([int(i) for i in input().split(", ")])

    return matrx


matrix = read_matrix()
total = 0
for i in matrix:
    total += sum(i)

print(total)
print(matrix)