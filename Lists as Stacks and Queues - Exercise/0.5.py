from collections import deque

number = int(input())

queue = deque()

for i in range(number):
    gas_station_info = [int(i) for i in input().split()]
    queue.append(gas_station_info)

for index in range(number):
    total_gas = 0
    completed = True
    for pump in queue:
        gas = pump[0]
        distance = pump[1]
        total_gas += gas
        if total_gas - distance < 0:
            completed = False
            break
        else:
            total_gas -= distance
    if completed:
        print(index)
        break
    else:
        queue.append(queue.popleft())
