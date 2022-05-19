n = int(input())

stack = []

for i in range(n):
    command = input().split()
    if int(command[0]) == 1:
        x = int(command[1])
        stack.append(x)
    elif int(command[0]) == 2:
        if len(stack) > 0:
            stack.pop()
    elif int(command[0]) == 3:
        if len(stack) > 0:
            print(max(stack))
    elif int(command[0]) == 4:
        if len(stack) > 0:
            print(min(stack))


print(", ".join(map(str, stack[::-1])))