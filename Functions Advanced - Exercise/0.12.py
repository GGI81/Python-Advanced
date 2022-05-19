from collections import deque

def math_operations(*args, **kwargs):
    dictionary = {
        "a": 0,
        "s": 0,
        "d": 0,
        "m": 0
    }
    args_list = deque([])
    for i in args:
        args_list.append(i)
    for key, value in kwargs.items():
        if key in dictionary:
            dictionary[key] = value
    counter = 1
    if len(args_list) > 0:
        while True:
            if len(args_list) <= 0:
                return dictionary
            current_element = int(args_list.popleft())
            if counter == 1:
                dictionary["a"] += current_element
            elif counter == 2:
                dictionary["s"] -= current_element
            elif counter == 3:
                if current_element != 0:
                    dictionary["d"] /= current_element
            elif counter == 4:
                dictionary["m"] *= current_element
                counter = 0
            counter += 1

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))