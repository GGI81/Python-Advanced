file = open("main.py", "r")

print(file.readlines())

file = open("d/__init__.py", "r")

print(file.readlines())

# if the file does not exist returns ERROR
# FileNotFoundError

# r = read
# w = write
# x = create new file and open it for writing
# a = open for writing, appending to the end of the file if it exists
# t = text mode
# b = binary mode
# + = open a disk file for updating (reading and writing)
