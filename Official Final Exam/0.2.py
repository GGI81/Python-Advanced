def read_matrix():
    rows, cols = 6, 6
    matrx = []
    for _ in range(rows):
        matrx.append(list(input().split()))

    return matrx


def is_index_valid(r, c, ):
    if 0 <= r < 6 and 0 <= c < 6:
        return True
    return False

matrix = read_matrix()
n = 6
m = 6

TOTAL_POINTS = 0


hit_buckets = []

for i in range(3):
    row, col = eval(input())
    if is_index_valid(row, col):
        if matrix[row][col] == "B":
            if row not in hit_buckets and col not in hit_buckets:
                hit_buckets.append([row, col])
                for j in range(m):
                    if matrix[j][col] != "B":
                        TOTAL_POINTS += int(matrix[j][col])

if 100 <= TOTAL_POINTS < 200:
    print(f"Good job! You scored {TOTAL_POINTS} points, and you've won Football.")
elif TOTAL_POINTS < 100:
    print(f"Sorry! You need {100 - TOTAL_POINTS} points more to win a prize.")
if 200 <= TOTAL_POINTS < 300:
    print(f"Good job! You scored {TOTAL_POINTS} points, and you've won Teddy Bear.")
if TOTAL_POINTS >= 300:
    print(f"Good job! You scored {TOTAL_POINTS} points, and you've won Lego Construction Set.")
