numbers = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for i in range(numbers[0]):
    n = int(input())
    first_set.add(n)

for i in range(numbers[1]):
    m = int(input())
    second_set.add(m)

[print(x) for x in (first_set & second_set)]
