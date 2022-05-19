box_clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())

stack = []

for i in box_clothes:
    stack.append(i)

counter = 1
total = 0
while stack:
    current_piece_of_clothing = stack.pop()
    total += current_piece_of_clothing
    if total > capacity_of_rack:
        total = 0
        counter += 1
        stack.append(current_piece_of_clothing)

print(counter)