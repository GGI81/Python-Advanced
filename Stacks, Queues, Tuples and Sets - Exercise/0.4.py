from collections import deque

working_bees = [int(x) for x in input().split()]
nectar = [int(x) for x in input().split()]
symbols = input().split()

queue_bees = deque(working_bees)
stack_nectar = []
queue_symbols = deque(symbols)

for i in nectar:
    stack_nectar.append(i)

total_honey = 0

while True:
    if len(queue_bees) == 0 or len(stack_nectar) == 0:
        break
    current_bee = queue_bees.popleft()
    current_nectar = stack_nectar.pop()
    if current_nectar >= current_bee:
        if len(symbols) > 0:
            current_symbol = queue_symbols.popleft()
            if current_symbol == "+":
                total_honey += abs(current_bee + current_nectar)
            elif current_symbol == "-":
                total_honey += abs(current_bee - current_nectar)
            elif current_symbol == "*":
                total_honey += abs(current_bee * current_nectar)
            elif current_symbol == "/":
                total_honey += abs(current_bee / current_nectar)
    elif current_nectar < current_bee:
        queue_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if len(queue_bees) > 0:
    print(f"Bees left: {', '.join(map(str, queue_bees))}")
elif len(stack_nectar) > 0:
    print(f"Nectar left: {', '.join(map(str, stack_nectar))}")