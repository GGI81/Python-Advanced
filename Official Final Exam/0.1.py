from collections import deque

materials_for_wedding = [int(x) for x in input().split()]
genie_magic_level = deque([int(x) for x in input().split()])


total_gifts1 = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
}

total_gifts2 = {
    "Gold": 0,
    "Diamond Jewellery": 0,
}

ALL_gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while True:
    if len(materials_for_wedding) == 0 or len(genie_magic_level) == 0:
        if total_gifts1["Gemstone"] > 0 and total_gifts1["Porcelain Sculpture"] > 0:
            print("The wedding presents are made!")
            if len(materials_for_wedding) > 0:
                print(f"Materials left: {', '.join(map(str, materials_for_wedding))}")
            if len(genie_magic_level) > 0:
                print(f"Magic left: {', '.join(map(str, genie_magic_level))}")
            for key, value in sorted(total_gifts1.items(), key=lambda x: x[0]):
                if value > 0:
                    print(f"{key}: {value}")
            break
        elif total_gifts2["Gold"] > 0 and total_gifts2["Diamond Jewellery"] > 0:
            print("The wedding presents are made!")
            if len(materials_for_wedding) > 0:
                print(f"Materials left: {', '.join(map(str, materials_for_wedding))}")
            if len(genie_magic_level) > 0:
                print(f"Magic left: {', '.join(map(str, genie_magic_level))}")
            for key, value in sorted(total_gifts2.items(), key=lambda x: x[0]):
                if value > 0:
                    print(f"{key}: {value}")
            break
        else:
            print("Aladdin does not have enough wedding presents.")
            if len(materials_for_wedding) > 0:
                print(f"Materials left: {', '.join(map(str, materials_for_wedding))}")
            if len(genie_magic_level) > 0:
                print(f"Magic left: {', '.join(map(str, genie_magic_level))}")
            for key, value in sorted(ALL_gifts.items(), key=lambda x: x[0]):
                if value > 0:
                    print(f"{key}: {value}")
            break
    current_material = materials_for_wedding.pop()
    current_magic_level = genie_magic_level.popleft()
    total = current_material + current_magic_level
    if total < 100:
        if total % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
            total = current_material + current_magic_level
        else:
            total *= 2
    if total >= 500:
        total /= 2
    if 100 <= total < 200:
        total_gifts1["Gemstone"] += 1
        ALL_gifts["Gemstone"] += 1
    elif 200 <= total < 300:
        total_gifts1["Porcelain Sculpture"] += 1
        ALL_gifts["Porcelain Sculpture"] += 1
    elif 300 <= total < 400:
        total_gifts2["Gold"] += 1
        ALL_gifts["Gold"] += 1
    elif 400 <= total < 500:
        total_gifts2["Diamond Jewellery"] += 1
        ALL_gifts["Diamond Jewellery"] += 1

