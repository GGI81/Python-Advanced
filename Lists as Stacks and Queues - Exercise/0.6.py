expression = input()

stack = []
balanced = True
for i in expression:
    if i in "[{(":
        stack.append(i)
    else:
        if len(stack) == 0:
            balanced = False
        current_bracket = stack.pop()
        if current_bracket + i in "[]{}()":
            balanced = True
        else:
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")