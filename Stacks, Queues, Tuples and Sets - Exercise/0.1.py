def is_subset(set1: set, set2: set):
    if set1.issubset(set2) or set2.issubset(set1):
        return "True"
    else:
        return "False"


integers1 = [int(x) for x in input().split()]
integers2 = [int(x) for x in input().split()]

integers1_set = set(integers1)
integers2_set = set(integers2)

n = int(input())

for i in range(n):
    command = input().split()
    first_part = command[:2]
    if first_part[0] == "Add":
        if first_part[1] == "First":
            second_part = command[2:]
            for j in second_part:
                integers1_set.add(int(j))
        elif first_part[1] == "Second":
            second_part = command[2:]
            for j in second_part:
                integers2_set.add(int(j))
    elif first_part[0] == "Remove":
        if first_part[1] == "First":
            second_part = command[2:]
            for j in second_part:
                if len(integers1_set) > 0:
                    if int(j) in integers1_set:
                        integers1_set.remove(int(j))
        elif first_part[1] == "Second":
            second_part = command[2:]
            for j in second_part:
                if len(integers2_set) > 0:
                    if int(j) in integers2_set:
                        integers2_set.remove(int(j))
    elif first_part[0] == "Check":
        print(is_subset(integers1_set, integers2_set))


# first_set = ", ".join([str(i) for i in integers1_set])
# print(first_set)
#
# second_set = ", ".join([str(i) for i in integers2_set])
# print(second_set)

list1 = []
if len(integers1_set) > 0:
    for i in sorted(integers1_set):
        list1.append(i)

list2 = []
if len(integers2_set) > 0:
    for i in sorted(integers2_set):
        list2.append(i)


print(", ".join(map(str, list1)))
print(", ".join(map(str, list2)))
