from collections import deque

materials_for_toys = [int(x) for x in input().split()]
magic_level = [int(x) for x in input().split()]

present_magic = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

number_crafted_toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

stack_material = []
queue_magic_levels = deque(magic_level)

for i in materials_for_toys:
    stack_material.append(i)

while True:
    if len(queue_magic_levels) == 0 or len(stack_material) == 0:
        break
    current_material = stack_material.pop()
    current_magic_level = queue_magic_levels.popleft()
    multiplication = current_material * current_magic_level
    if multiplication == present_magic["Doll"]:
        number_crafted_toys["Doll"] += 1
    elif multiplication == present_magic["Wooden train"]:
        number_crafted_toys["Wooden train"] += 1
    elif multiplication == present_magic["Teddy bear"]:
        number_crafted_toys["Teddy bear"] += 1
    elif multiplication == present_magic["Bicycle"]:
        number_crafted_toys["Bicycle"] += 1

    if multiplication < 0:
        total = current_material + current_magic_level
        stack_material.append(total)
    elif multiplication > 0 and (multiplication != present_magic["Doll"] and
                                 multiplication != present_magic["Wooden train"] and
                                 multiplication != present_magic["Teddy bear"] and
                                 multiplication != present_magic["Bicycle"]):
        current_material += 15
        stack_material.append(current_material)
    elif current_material == 0 or current_magic_level == 0:
        if current_material > 0:
            stack_material.append(current_material)
        elif current_magic_level > 0:
            queue_magic_levels.appendleft(current_magic_level)

if number_crafted_toys["Doll"] and number_crafted_toys["Wooden train"] \
        or number_crafted_toys["Teddy bear"] and number_crafted_toys["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if len(stack_material) > 0:
    print(f"Materials left: {', '.join(map(str, stack_material[::-1]))}")

if len(queue_magic_levels) > 0:
    print(f"Magic left: {', '.join(map(str, queue_magic_levels))}")

for key, value in sorted(number_crafted_toys.items(), key=lambda x: x[0]):
    if value > 0:
        print(f"{key}: {value}")
