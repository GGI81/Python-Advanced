file = open("numbers.txt")

# Variant 1
total = 0
for line in file:
    total += int(line)

print(total)

# Variant 2
print(sum([int(line) for line in file]))
