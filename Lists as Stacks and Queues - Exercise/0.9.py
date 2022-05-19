from collections import deque

price_for_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = [int(x) for x in input().split()]
value_of_intelligence = int(input())

locks_queue = deque(locks)
bullets_stack = []

for i in bullets:
    bullets_stack.append(i)

counter = 0
bullet_Counter = 0
while True:
    if counter == size_of_gun_barrel:
        counter = 0
        if len(bullets_stack) > 0:
            print("Reloading!")
    if len(bullets_stack) == 0 and len(locks_queue) > 0:
        print(f"Couldn't get through. Locks left: {len(locks_queue)}")
        break
    elif len(locks_queue) == 0 and len(bullets_stack) >= 0:
        total = price_for_bullet * bullet_Counter
        earned = value_of_intelligence - total
        print(f"{len(bullets_stack)} bullets left. Earned ${earned}")
        break
    current_lock = locks_queue.popleft()
    current_bullet = bullets_stack.pop()
    if current_bullet > current_lock:
        print(f"Ping!")
        locks_queue.appendleft(current_lock)
        bullet_Counter += 1
    elif current_bullet <= current_lock:
        print(f"Bang!")
        bullet_Counter += 1
    counter += 1