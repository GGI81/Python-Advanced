# First using a Ready MODULE

# from itertools import combinations
#
# result = list(combinations(input().split(", "), int(input())))
# for x, y in result:
#     print(x, y, sep=", ")

# We have a module for combinations


"""
Doncho's solution
def generate_combinations(values, index,  count, combination):
    if len(combination) == count:
        print(", ".join(combination))
        return

    for i in range(index, len(values)):
        combination.append(values[i])
        generate_combinations(values, i+1, count, combination)
        combination.pop()

string = input().split(", ")
count = int(input())
generate_combinations(string, 0, count, [])
"""

def combinations(names, count, current_names=[]):
    if len(current_names) == count:
        print(", ".join(current_names))
        return

    for i in range(len(names)):
        current_names.append(names[i])
        combinations(names[i+1:], count, current_names)
        current_names.pop()





names = input().split(", ")
n = int(input())
combinations(names, n)