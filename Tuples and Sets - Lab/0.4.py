car_number = int(input())

my_set = set()

for i in range(car_number):
    command = input().split(", ")
    if command[0] == "IN":
        car_number = command[1]
        my_set.add(car_number)
    elif command[0] == "OUT":
        car_number = command[1]
        my_set.remove(car_number)

if len(my_set) > 0:
    for i in my_set:
        print(i, end="\n")
else:
    print("Parking Lot is Empty")