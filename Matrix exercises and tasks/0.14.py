def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([int(x) for x in input().split()])

    return matrx


def is_index_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


matrix = read_matrix()
n = len(matrix)

command = input().split()
while True:
    if command[0] == "END":
        for i in matrix:
            print(" ".join(map(str, i)))
        break
    if command[0] == "Add":
        row, col, value = int(command[1]), int(command[2]), int(command[3])
        if is_index_valid(row, col, n):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        row, col, value = int(command[1]), int(command[2]), int(command[3])
        if is_index_valid(row, col, n):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    command = input().split()