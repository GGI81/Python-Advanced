file = open("reading a file.py", "r")

# print(file.readline())  -> whole line by line

# while True:
#     text = file.readline()
#     print(text)
#     print(" ------- ")
#     if not text:
#         break


while True:
    # reads at most 7 characters on the line
    text = file.readline(7)
    print(text)
    print(" ------- ")
    if not text:
        break

# file.readline(7) read the first 7 symbols from the first line

