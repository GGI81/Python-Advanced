size = int(input())

matrix = []

for i in range(size):
    numbers = ([int(i) for i in input().split(", ")])
    matrix.append([int(i) for i in numbers if i % 2 == 0])

print(matrix)