sublist = input().split("|")

result = []

for idx in range(len(sublist) - 1, -1, -1):
    element = sublist[idx].split()
    result += element

print(" ".join(result))