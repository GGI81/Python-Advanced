file_name = "text.txt"

try:
    open(file_name, "r")  # Exception
    print(f"File found")
except:
    print("File Not found")

