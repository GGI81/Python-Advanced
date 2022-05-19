import os


def traverse_directories(dir_path, result):
    for x in os.listdir(dir_path):
        file_with_path = os.path.join(dir_path, x)
        if os.path.isfile(os.path.join(dir_path, x)):
            ext = x.split(",")[-1]
            if ext not in result:
                result[ext] = []
            result[ext].append(file_with_path)
        elif os.path.isdir(file_with_path):

            traverse_directories(os.path.join(dir_path, x), result)

result = {}
traverse_directories(os.getcwd(), result)

for ext, files in sorted(result.items()):
    print(f".{ext}")
    for file in sorted(files):
        print(f"--- {file}")