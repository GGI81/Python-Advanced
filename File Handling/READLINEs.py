file = open("READLINEs.py", "r")

# print(file.readlines())

i = 1
for line in file.readlines():
    print(f"{i}: { line}")
    i += 1

