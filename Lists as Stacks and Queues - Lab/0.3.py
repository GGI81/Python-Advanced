from collections import deque

PAID_COMMAND = "Paid"
END_COMMAND = "End"

name = input()

queue = deque()

while True:
    if name != PAID_COMMAND and name != END_COMMAND:
        queue.append(name)
    elif name == PAID_COMMAND:
        while queue:
            print(queue.popleft())
    if name == END_COMMAND:
        print(f"{len(queue)} people remaining.")
        break
    name = input()
