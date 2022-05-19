from collections import deque
from io import StringIO
import sys

test_input1 = """5, 25, 25, 115
5, 15, 25, 35
"""

test_input2 = """30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10
"""

sys.stdin = StringIO(test_input2)

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs_dict = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}

bombs_count = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while True:
    if len(bomb_effects) == 0 or len(bomb_casings) == 0:
        if bombs_count["Datura Bombs"] >= 3 and bombs_count["Cherry Bombs"] >= 3 and bombs_count["Smoke Decoy Bombs"] >= 3:
            print("Bene! You have successfully filled the bomb pouch!")
            if len(bomb_effects) > 0:
                print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
            else:
                print("Bomb Effects: empty")
            if len(bomb_casings) > 0:
                print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
            else:
                print("Bomb Casings: empty")
            for key, value in sorted(bombs_count.items(), key=lambda x: x[0]):
                print(f"{key}: {value}")
            break
        else:
            print("You don't have enough materials to fill the bomb pouch.")
            if len(bomb_effects) > 0:
                print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
            else:
                print("Bomb Effects: empty")
            if len(bomb_casings) > 0:
                print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
            else:
                print("Bomb Casings: empty")
            for key, value in sorted(bombs_count.items(), key=lambda x: x[0]):
                print(f"{key}: {value}")
            break
    if bombs_count["Datura Bombs"] >= 3 and bombs_count["Cherry Bombs"] >= 3 and bombs_count["Smoke Decoy Bombs"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        if len(bomb_effects) > 0:
            print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
        else:
            print("Bomb Effects: empty")
        if len(bomb_casings) > 0:
            print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
        else:
            print("Bomb Casings: empty")
        for key, value in sorted(bombs_count.items(), key=lambda x: x[0]):
            print(f"{key}: {value}")
        break
    current_effects = bomb_effects.popleft()
    current_casings = bomb_casings.pop()
    total = current_casings + current_effects
    if total == bombs_dict["Datura Bombs"]:
        bombs_count["Datura Bombs"] += 1
    elif total == bombs_dict["Cherry Bombs"]:
        bombs_count["Cherry Bombs"] += 1
    elif total == bombs_dict["Smoke Decoy Bombs"]:
        bombs_count["Smoke Decoy Bombs"] += 1
    else:
        current_casings -= 5
        bomb_casings.append(current_casings)
        bomb_effects.appendleft(current_effects)
