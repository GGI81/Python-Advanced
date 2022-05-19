# To return all lines from a file you can loop over it
# More memory efficient and fas manner
#   Simple and easy to read

file = open("Looping over a file object.py", "r")

for line in file:
    print(line, end="")
    # Prints every line in a new line

print()

# if you want to take a special line:

def read_nth_line(file_path, n):
    file = open(file_path, "r")
    for i in range(n - 1):
        file.readline()
    return file.readline()

nth_line = 3
result = read_nth_line("Looping over a file object.py", nth_line)
print(result)  # Takes the third line




