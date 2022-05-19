# Even Matrix

def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([x for x in [int(x) for x in input().split(", ")] if x % 2 == 0])

    return matrx

matrix = read_matrix()
print(matrix)
