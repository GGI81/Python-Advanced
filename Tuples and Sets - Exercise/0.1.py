number = int(input())
unique_names = {input() for i in range(number)}
[print(name) for name in unique_names]
