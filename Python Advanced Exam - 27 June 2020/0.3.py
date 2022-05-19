from collections import deque

def list_manipulator(numbers: list, command, position, *args):
    numbers = deque(numbers)
    if command == "add":
        if position == "beginning":
            for i in args[::-1]:
                numbers.appendleft(i)
            return list(numbers)
        elif position == "end":
            for i in args:
                numbers.append(i)
            return list(numbers)
    elif command == "remove":
        if position == "beginning":
            if len(args) > 0:
                ll = []
                for i in args:
                    ll.append(i)
                for _ in range(ll[0]):
                    numbers.popleft()
                return list(numbers)
            else:
                numbers.popleft()
                return list(numbers)
        elif position == "end":
            if len(args) > 0:
                ll = []
                for i in args:
                    ll.append(i)
                for _ in range(ll[0]):
                    numbers.pop()
                return list(numbers)
            else:
                numbers.pop()
                return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
