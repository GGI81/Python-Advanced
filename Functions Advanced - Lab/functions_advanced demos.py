# Packing and Unpacking

# Normal function
"""
def add(x, y, z):
    return x + y + z

# The order matters if are positional
print(add(1, 2, 3))

# the orders doesn't matters if its named:
print(add(x=1, y=2, z=3))

print(add(y=1, x=2, z=3))


# x and y are positional, and z is names
print(add(1, 2, z=5))

print()
print()
"""


# PACKING

def add_with_list(numbers):
    return sum(numbers)


def add(x, y, *numbers):  # x and y will take the first two values of them below
    return sum(numbers)


print(add_with_list([1, 2, 3, 4]))
print(add(1, 2, 3, 4))

# If we have *args with x and y for parameters we cannot print the function without arguments
# while if we have only *args we can

print(" --- = *ARGS = --- ")

def add2(*args):
    return sum(args)


print(add2())  # everything is ok

print()
print()
print()


def some_func(*args):
    print(args)


some_func(1, 2, 3)
some_func("Peter", "George")
some_func(True, False)
some_func()


print()
print()
print()

print(" --- = **KWARGS = --- ")

# **kwargs returns a dictionary


def add(*args, **kwargs):
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    return (f"sum args = {sum(args)}, sum kwargs = {kwargs.values()}")


print("      -- Positional -- ")
print(add(1, 2, 3))
# args = (1, 2, 3) --> tuple
# kwargs returns -- > empty dictionary, because the arguments are positional, not named

print()

print("      -- Named --")
print(add(x=1, y=2, z=3))
# args returns (), because there is no positional
# kwargs returns {'x': 1, 'y': 2, 'z': 3}
# and sum(args) returns 0

print()

print(add(y=1, x=5, z=4))

print()

# args = (1, 2, 3)
print(add(1, 2, 3))
# kwargs = {}

print()

# args = (1, 2)
print(add(1, 2, x=1))
# kwargs = {x: 1}

print()
print()
print()


def add_x(x, *args, **kwargs):
    print(f"x={x}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")
    return sum(args) + sum(kwargs.values())


# args -= x  args = (2, 3)
# kwargs -= x  kwargs = {}
print(add_x(1, 2, 3))

print()

print(f"x, 1, z=5")
print(add_x(1, 2, z=5))
# x = 1
# args = (2,)
# kwargs = {"z": 5}
