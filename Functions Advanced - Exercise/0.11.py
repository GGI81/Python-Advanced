from collections import deque

def fill_the_box(height, length, width, *args):
    total = deque([])
    box_size = height * length * width
    for i in args:
        if i == "Finish":
            break
        else:
            total.append(i)
    while True:
        if len(total) == 0 and box_size > 0:
            return f"There is free space in the box. You could put {box_size} more cubes."
        else:
            current_value = total.popleft()
            if box_size - current_value > 0:
                box_size -= current_value
            else:
                left_thing = current_value - box_size
                return f"No more free space! You have {left_thing + sum(total)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
