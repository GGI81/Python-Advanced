# Set is an unordered collection of items
# Every element of a set is unique
# Sets are mutable, so we can add or remove items from it
# Sets can be used to preform mathematical set operation (union, intersection, symmetric difference, etc.)

ss = set()
ll = []

ss.add(1)
ss.add(2)
ss.add(3)
ss.add(1)
ss.add(2)

print(ss)
# {1, 2, 3}

for i in range(10):
    ss.add(1)
    ll.append(1)

print(ss)
# {1, 2, 3}
print(ll)
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1)
print(s2)

print()

# together
print(s1 | s2)
# {1, 2, 3, 4, 5, 6}

print()

# section (сечение)
print(s1 & s2)
# {3, 4} (Returning the elements which are participating in both of our sets)
# If there aren't any, it will return -> set()

s3 = {1, 2, 3, 4}
s4 = {3, 4, 5, 6}
print(s3 & s4)
# set()

print()

# OPERATORS
# | & < <= - ^
# We can check if a set is subset on a another set
# It will return a bool (True/False)
# Subset means all the elements from s3 to be in s4
print(s3 < s4)
# False
print({3, 4} < s4)
# True
print(s3 < s3)
# False
print(s3 <= s3)
# True
print(s3 - s4)
# {1, 2}
print(s4 - s3)
# {5, 6}
print(s3 ^ s4)
# {1, 2, 5, 6} (Returns the different elements from both of our sets)

print()
print()
print()

# SET COMPREHENSION

print(
    {x for x in range(1, 16)}
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
)

print(
    {x % 5 for x in range(15)}
    # {0, 1, 2, 3, 4}
)

print(
    set(
        [x % 5 for x in range(15)]
    )
    # {0, 1, 2, 3, 4}
)