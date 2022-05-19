string = input()

dd = {}

for i in string:
    if i not in dd:
        dd[i] = 0
    dd[i] += 1

for key, value in sorted(dd.items(), key=lambda x: x[0]):
    print(f"{key}: {value} time/s")
