from collections import deque

day_quantity = int(input())
customers = [int(x) for x in input().split()]

queue = deque(customers)

print(max(queue))

for i in customers:
    current_order = queue.popleft()
    if day_quantity - current_order >= 0:
        day_quantity -= current_order
    else:
        queue.appendleft(current_order)
        break

if len(queue) == 0:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, queue))}")