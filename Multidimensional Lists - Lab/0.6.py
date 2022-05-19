def read_matrix():
    number = int(input())
    matrx = []
    for i in range(number):
        words = input().split()
        matrx.append(words)

    return matrx


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
searched_symbol = input()
is_found = False
my_list = []
for r in range(n):
    if is_found:
        break
    for c in range(m):
        for index, char in enumerate(matrix[r][c]):
            if char == searched_symbol:
                my_list.append(r)
                my_list.append(index)
                is_found = True
                break

if is_found == False:
    print(f"{searched_symbol} does not occur in the matrix")
else:
    print(f"({', '.join(map(str, my_list))})")