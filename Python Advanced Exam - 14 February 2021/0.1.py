from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

dictionary = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while True:
    if dictionary["Palm Fireworks"] >= 3 and dictionary["Willow Fireworks"] >= 3 and dictionary["Crossette Fireworks"] >= 3:
        break
    if len(firework_effects) == 0 or len(explosive_power) == 0:
        break
    current_firework = firework_effects.popleft()
    current_power = explosive_power.pop()
    if current_firework > 0 and current_power > 0:
        total = current_power + current_firework
        if total % 3 == 0 and total % 5 != 0:
            dictionary["Palm Fireworks"] += 1
        elif total % 5 == 0 and total % 3 != 0:
            dictionary["Willow Fireworks"] += 1
        elif total % 3 == 0 and total % 5 == 0:
            dictionary["Crossette Fireworks"] += 1
        else:
            if current_firework - 1 > 0:
                current_firework -= 1
                firework_effects.append(current_firework)
            explosive_power.append(current_power)
    else:
        if current_firework <= 0 < current_power:
            explosive_power.append(current_power)
        elif current_power <= 0 < current_firework:
            firework_effects.appendleft(current_firework)

if dictionary["Palm Fireworks"] >= 3 and dictionary["Willow Fireworks"] >= 3 and dictionary["Crossette Fireworks"] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if len(firework_effects) > 0:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if len(explosive_power) > 0:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for key, value in dictionary.items():
    print(f"{key}: {value}")
