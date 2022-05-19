def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([int(x) for x in input().split()])

    return matrx


matrix = read_matrix()
n = len(matrix)

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
