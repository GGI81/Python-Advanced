from collections import deque

players = input().split()
toss = int(input())

queue = deque(players)

counter = 0
while len(queue) > 1:
    counter += 1
    current_player = queue.popleft()
    if counter == toss:
        counter = 0
        print(f"Removed {current_player}")
    else:
        queue.append(current_player)

for i in queue:
    print(f"Last is {i}")