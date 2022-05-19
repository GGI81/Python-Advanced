from collections import deque

START_COMMAND = "Start"
END_COMMAND = "End"

liters_water = int(input())

people_queue = deque()

while True:
    name = input()
    if name == START_COMMAND:
        break
    else:
        people_queue.append(name)

command = input().split()

while True:
    if command[0] == END_COMMAND:
        break
    if command[0].isdigit():
        if liters_water - int(command[0]) >= 0:
            liters_water -= int(command[0])
            print(f"{people_queue.popleft()} got water")
        else:
            print(f"{people_queue.popleft()} must wait")
    elif command[0] == "refill":
        liters = int(command[1])
        liters_water += liters
    command = input().split()

print(f"{liters_water} liters left")