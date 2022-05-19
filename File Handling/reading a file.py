x = 5
file = open("reading a file.py", "r")

# print(file.read())  -> reads all

while True:
    text = file.read(12)
    print(text)
    print(" --------- ")
    if not text:
        break

# print(file.read(2))  # Takes only the first two symbols
# print(file.read(3))  # Takes the next three
# print(file.read(3))
"""
7GB = 7 * 1000MB = 7 * 1000 * 1000KB = 7 * 1000 * 1000 * 1000B
7GB text file => RAM

10000B ~= 10 KB
"""

