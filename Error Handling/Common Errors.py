"""
Syntax Error

A certain statement is not in accordance with the
prescribed usage

It is the most common reason of an error in a Python program

# >>> print "Hello"
SyntaxError: Missing parentheses in call to "print".
"""


# Index error

# ll = [1]
# print(ll[0])  # IndexError: list index out of range


# Key exception
# Solution: Check whether key is in dict
"""
if "k3" in dd:
    print(dd["k3"])
"""
# dd = {
#     "k1": "v1",
#     "k2": "v2",
# }
# print(dd["k3"])  # KeyError: 'k3'


# Type error
# Solution: (", ".join(str(x) for x in [1, 2, 3]))
# print(", ".join([1, 2, 3]))
# expected str instance, int found


# # Value Error
# print(int("1"))  # 1
# print(int(1))  # 1
# print(int("3.14"))  # 3
# print(int("x"))  # Value Error
