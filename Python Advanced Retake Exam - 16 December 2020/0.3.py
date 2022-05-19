def get_magic_triangle(n, count=0):
    matrix = []
    matrix.append([int(1)])
    matrix.append([int(1) for _ in range(2)])
    if count == n:
        print(matrix)
        return

    return get_magic_triangle(n, count+1)


get_magic_triangle(5)