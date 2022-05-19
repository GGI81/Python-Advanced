# Primary Diagonal

def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([int(x) for x in input().split()])

    return matrx


matrix = read_matrix()
n = len(matrix)
print(sum([matrix[i][i] for i in range(n)]))