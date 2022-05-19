"""
p, g, a
p
  g
  a
g a
"""
# Combinations
# NO ORDER

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

