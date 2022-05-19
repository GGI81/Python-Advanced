# Tuples are part of the standard language
# Tuples are immutable* objects
# but the objects, inside the tuples, are mutable
# Tuples are sequences, just like lists
# Tuples cannot be changed unlike lists
# Tuples are parentheses, whereas lists ues square brackets

ll = [1, 2, 3]
tt = (1, 2, 3)

ll.append(3)
print(ll)

print(tt)

tt = 5
print(tt)

# methods
# count
# index

# count
tt = (1, 2, 3, 4, 5, 1, 6, 1, 7)
print(tt.count(1))
# 3
print(tt.count(6))
# 1

# index
print(tt.index(3))
# 2
print(tt.index(1))
# 0
print(tt.index(1, 1))  # Returns the first specific element after the first tuple element
# 5

# len command
print(len(tt))

print()
print()
print()

# Adding tuples
tt1 = (1, 2, 3, 4, 5, 1, 6, 7)
tt2 = (-11, 1024)

tt_result = tt1 + tt2
print(f"{tt1} + {tt2} = {tt_result}")
# (1, 2, 3, 4, 5, 1, 6, 7) + (-11, 1024) = (1, 2, 3, 4, 5, 1, 6, 7, -11, 1024)

print()
print()
print()

# Tuples Unpacking
tt = (1, 2, 3)
x = tt[0]
y = tt[1]
z = tt[2]
print(x, y, z)

a, b, c = tt
print(a, b, c)

i, *j = tt  # First in i the others in j
print(i, j)

print()
print()
print()

# .items in dictionaries are returning list with TUPLES

dd = {
    "name": "Gosho",
    "age": 17,
}

print(dd.items())
# dict_items([('name', 'Gosho'), ('age', 17)])

print()
print()

for key, value in dd.items():
    print(key)
    print(value)
