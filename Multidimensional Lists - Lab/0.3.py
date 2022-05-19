def read_matrix():
    rows = int(input())
    matrx = []
    for i in range(rows):
        matrx.append([int(x) for x in input().split(", ")])

    return matrx


matrix = read_matrix()
ll = []
for i in matrix:
    ll += i

print(ll)
