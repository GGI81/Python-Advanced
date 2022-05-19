size_square = int(input())

matrix = []

for i in range(size_square):
    matrix.append([int(x) for x in input().split()])

print(sum([matrix[i][i] for i in range(size_square)]))

