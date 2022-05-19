# Flattening Matrix

def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([int(i) for i in input().split(", ")])

    return matrx


matrix = read_matrix()
ll = []
for i in matrix:
    ll += i

print(ll)