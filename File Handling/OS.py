import os
from os import path
# os.remove("sample.txt")
# How to delete files
# Returns error if the file doesn't exist
print(path.exists("sample.txt"))
# Returns boolean
# False

if path.exists("sample-a.txt"):
    os.remove("sample-a.txt")

[print(x) for x in os.listdir(".")]
# Returns the files with . (all)

ss = [os.getcwd()]
while ss:
    current_dir = ss.pop()
    if path.isfile(current_dir):
        continue

    for file_path in os.listdir(current_dir):
        absolute_path = path.join(
            current_dir,
            file_path
        )
        ss.append(absolute_path)

# for file_name in os.listdir():
#     full_path = path.join(
#         os.getcwd(),
#         file_name
#     )
#    print(full_path)

