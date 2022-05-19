def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([int(x) for x in input().split(", ")])

    return matrx


matrix = read_matrix()
n = len(matrix)
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
