"""
number = int(input())

my_list = []

for i in range(number):
    name = input()
    my_list.append(name)

print("\n".join(set(my_list)))
"""

n = int(input())
names = {input() for i in range(n)}
for name in names:
    print(name)