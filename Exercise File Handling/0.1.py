symbols = {"-", ",", ".", "!", "?"}

with open("text_ex1.txt", "r") as file:
    idx = 0
    while True:
        line = file.readline().strip()
        if not line:
            break
        if idx % 2 != 0:
            idx += 1
            continue
        else:
            for symbol in symbols:
                line = line.replace(symbol, "@")
            line = " ".join(line.split()[::-1])
            print(line)
            idx += 1
