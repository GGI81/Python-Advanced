"""
We can use * to unpack the list so that
all elements of it can be passed as different parameters

And we can use ** to unpack a dictionary,
 so all of its elements are passed as keyworded arguments
"""

# Unpacking Lists

# Note that the length of the list , that you unpack, must be the same as the number of parameters in the function


def print_nums(a, b, c):
    return a + b + c


nums = (1, 2, 3)

# unpack as positional arguments
print(print_nums(*nums))

print()
print()

numbers_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# unpacks named arguments
print(print_nums(**numbers_dict))