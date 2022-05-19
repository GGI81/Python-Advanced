def write_to_file(file_path, mode, text):
    file = open(file_path, mode)
    file.write(text)
    file.close()

write_to_file("d/numbers.txt", "w", """1
2
3
4
5
""")

write_to_file("d/numbers.txt", "w", """New
TEXT
""")

# Difference between w and a
# w deletes everything and ads the new
# a APPENDS the text to te file

