from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while True:
    if len(males) == 0 or len(females) == 0:
        break
    current_man = males.pop()
    current_woman = females.popleft()
    if current_man > 0 and current_woman > 0:
        if current_woman % 25 == 0 or current_man % 25 == 0:
            if current_woman % 25 == 0:
                females.popleft()
            if current_man % 25 == 0:
                males.pop()
        elif current_man == current_woman:
            matches += 1
        elif current_man != current_woman:
            males.append(current_man - 2)
    else:
        if current_woman > 0:
            females.appendleft(current_woman)
        elif current_man > 0:
            males.append(current_man)


print(f"Matches: {matches}")
if len(males) > 0:
    males = males[::-1]
    print(f"Males left: {', '.join(map(str, males))}")
else:
    print("Males left: none")


if len(females) > 0:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")