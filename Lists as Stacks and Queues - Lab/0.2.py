expression = input()

stack = []

for index, ch in enumerate(expression):
    if ch == "(":
        stack.append(index)
    elif ch == ")":
        closing_index = index
        opening_index = stack.pop()
        print(expression[opening_index:closing_index + 1])
