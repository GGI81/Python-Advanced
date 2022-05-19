n = int(input())

my_set = set()

for i in range(n):
    elements = input().split()
    for j in elements:
        my_set.add(j)

[print(x) for x in my_set]
