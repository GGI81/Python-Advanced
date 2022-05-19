punctuation_marks_set = {",", ".", "?", "'", "-", "!", ";", ":", "_", '"', }

with open("text_ex2.txt", "r") as file, open("output.txt", "w") as result:
    index = 1
    for line in file:
        letters_count = 0
        punctuation_marks = 0
        for ch in line:
            if ch in punctuation_marks_set:
                punctuation_marks += 1
            elif ch.isalpha():
                letters_count += 1
        print(f"Line {index}: {line.strip()} ({letters_count})({punctuation_marks})")
        index += 1