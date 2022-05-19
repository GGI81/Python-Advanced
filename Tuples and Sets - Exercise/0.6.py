n = int(input())

even_set = set()
odd_set = set()

ascii_total = 0
rows = 0
for i in range(n):
    rows += 1
    names = input()
    for j in names:
        ascii_total += ord(j)
    ascii_total //= rows
    if ascii_total % 2 == 0:
        even_set.add(ascii_total)
        ascii_total = 0
    else:
        odd_set.add(ascii_total)
        ascii_total = 0

even_sum = sum(even_set)
odd_sum = sum(odd_set)
result = set()
if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(", ".join([str(x) for x in result]))