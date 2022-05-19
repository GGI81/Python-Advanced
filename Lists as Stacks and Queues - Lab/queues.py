from collections import deque

q = deque()
q_list = []
stack = []

for i in range(1, 6):
    q.append(i)
    stack.append(i)
    q_list.append(i)

print("Queue")
while q:
    print(q.popleft())

    # Queue
    # 1
    # 2
    # 3
    # 4
    # 5

print("Queue wihtl ist")
while q_list:
    print(q_list.pop(0))

print("Stack")
while stack:
    print(stack.pop())

    # Stack
    # 5
    # 4
    # 3
    # 2
    # 1