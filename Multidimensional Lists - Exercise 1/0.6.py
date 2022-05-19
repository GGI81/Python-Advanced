def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrx = []
    for i in range(rows):
        matrx.append(input().split())

    return matrx


def is_index_valid(r1, c1, r2, c2, mat):
    size = len(mat)
    if 0 > r1 or 0 > r2 or 0 > c1 or 0 > c2 or r1 > size or r2 > size or c1 > size or c2 > size:
        return False
    return True


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

while True:
    my_command = input()
    if my_command == "END":
        break
    args = my_command.split()
    command = args[0]
    if command == "swap":
        if len(args[1:]) == 4:
            row1 = int(args[1])
            col1 = int(args[2])
            row2 = int(args[3])
            col2 = int(args[4])
            if is_index_valid(row1, col1, row2, col2, matrix):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for i in matrix:
                    print(' '.join(i))
            else:
                print(f"Invalid input!")
        else:
            print(f"Invalid input!")
    else:
        print(f"Invalid input!")