string = input()

stack = []

for i in string:
    stack.append(i)

result = ""

while stack:
    result += stack.pop()

print(result)
