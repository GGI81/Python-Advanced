numbers = [float(x) for x in input().split()]

numbers_counts = {}

for number in numbers:
    if number not in numbers_counts:
        numbers_counts[number] = 0
    numbers_counts[number] += 1


for key, value in numbers_counts.items():
    print(f"{key} - {value} times")