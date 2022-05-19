# ADS
# Peek
# Pop
# Push
# Lifo structures
# Last in first out

s = []

s.append(1)
s.append(-1)
s.append(55)
s.append(3)

while s:
    print(s.pop())


class Stack:
    def __init__(self):
        self.internal_stack = []

    def push(self, value):
        self.internal_stack.append(value)

    def pop(self):
        return self.internal_stack.pop()

    def peek(self):
        return self.internal_stack[-1]


s2 = Stack()
