import sys
from io import StringIO

test_input1 = """2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
"""

test_input2 = """1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
"""

sys.stdin = StringIO(test_input1)

def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrx = []
    for i in range(rows):
        matrx.append(input().split())

    return matrx


END_COMMAND = "END"

matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

command = input().split()
while True:
    if command[0] == END_COMMAND:
        break
    if command[0] == "swap":
        if len(command[1:]) == 4:
            row1 = int(command[1])
            col1 = int(command[2])
            row2 = int(command[3])
            col2 = int(command[4])
            if row1 <= n and col1 <= m and row2 <= n and col2 <= m:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for i in matrix:
                    print(' '.join(map(str, i)))
            else:
                print(f"Invalid input!")
        else:
            print(f"Invalid input!")
    else:
        print(f"Invalid input!")
    command = input().split()