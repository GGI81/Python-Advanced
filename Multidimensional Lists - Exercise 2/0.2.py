def read_matrix():
    size = int(input())
    matrx = []
    for i in range(size):
        matrx.append([int(x) for x in input().split()])

    return matrx


def is_index_valid(r, c, mat):
    if 0 > r or 0 > c or r >= len(mat) or c >= len(mat):
        return False
    return True


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

while True:
    my_command = input()
    if my_command == "END":
        for i in matrix:
            print(" ".join(map(str, i)))
        break
    args = my_command.split()
    if args[0] == "Add":
        row = int(args[1])
        col = int(args[2])
        value = int(args[3])
        if is_index_valid(row, col, matrix):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif args[0] == "Subtract":
        row = int(args[1])
        col = int(args[2])
        value = int(args[3])
        if is_index_valid(row, col, matrix):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")