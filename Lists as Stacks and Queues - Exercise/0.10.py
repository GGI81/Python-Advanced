from collections import deque

cups_capacity = [int(x) for x in input().split()]
filled_bottles = [int(x) for x in input().split()]

queue = deque(cups_capacity)
stack = []

wasted_liters_of_water = 0

for i in filled_bottles:
    stack.append(i)

while True:
    if len(stack) == 0 or len(queue) == 0:
        if len(stack) > 0:
            print(f"Bottles: {' '.join(map(str, stack))}")
            print(f"Wasted litters of water: {wasted_liters_of_water}")
            break
        elif len(queue) > 0:
            print(f"Cups: {' '.join(map(str, queue))}")
            print(f"Wasted litters of water: {wasted_liters_of_water}")
            break
    current_cup = queue.popleft()
    current_bottle = stack.pop()
    if current_bottle - current_cup >= 0:
        wasted_liters_of_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        queue.appendleft(current_cup)
