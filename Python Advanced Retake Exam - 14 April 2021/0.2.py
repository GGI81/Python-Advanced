def read_matrix():
    size = 7
    matrx = []
    for i in range(size):
        matrx.append(input().split())

    return matrx


def is_index_valid(r, c, mat_size):
    if 0 <= r < mat_size and 0 <= c < mat_size:
        return True
    return False


PLAYER1, PLAYER2 = input().split(", ")
matrix = read_matrix()
n = len(matrix)

player1_points = 501
player2_points = 501

player_one_throws = 0
player_two_throws = 0

players_turn = 1
while True:
    command = input()
    row, col = eval(command)
    if players_turn % 2 != 0:
        player_one_throws += 1
        players_turn += 1
        if is_index_valid(row, col, n):
            if matrix[row][col] == "D":
                total = 0
                total += int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])
                player1_points -= total * 2
                if player1_points <= 0:
                    print(f"{PLAYER1} won the game with {player_one_throws} throws!")
                    break
            elif matrix[row][col] == "T":
                total = 0
                total += int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])
                player1_points -= total * 3
            if player1_points <= 0:
                print(f"{PLAYER1} won the game with {player_one_throws} throws!")
                break
            elif matrix[row][col] == "B":
                print(f"{PLAYER1} won the game with {player_one_throws} throws!")
                break
            elif matrix[row][col].isdigit():
                player1_points -= int(matrix[row][col])
                if player1_points <= 0:
                    print(f"{PLAYER1} won the game with {player_one_throws} throws!")
                    break
    elif players_turn % 2 == 0:
        player_two_throws += 1
        players_turn += 1
        if is_index_valid(row, col, n):
            if matrix[row][col] == "D":
                total = 0
                total += int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])
                player2_points -= total * 2
                if player2_points <= 0:
                    print(f"{PLAYER2} won the game with {player_two_throws} throws!")
                    break
            elif matrix[row][col] == "T":
                total = 0
                total += int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])
                player2_points -= total * 3
            if player2_points <= 0:
                print(f"{PLAYER2} won the game with {player_two_throws} throws!")
                break
            elif matrix[row][col] == "B":
                print(f"{PLAYER2} won the game with {player_two_throws} throws!")
                break
            elif matrix[row][col].isdigit():
                player2_points -= int(matrix[row][col])
                if player2_points <= 0:
                    print(f"{PLAYER2} won the game with {player_two_throws} throws!")
                    break
