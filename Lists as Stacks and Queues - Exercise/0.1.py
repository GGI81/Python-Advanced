numbers = input().split()

stack = []

for i in numbers:
    stack.append(int(i))

stack_2 = []

for i in numbers:
    stack_2.append(stack.pop())

for i in stack_2:
    print(i, end=" ")