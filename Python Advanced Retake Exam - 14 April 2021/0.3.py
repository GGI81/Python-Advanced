def flights(*args):
    destination_list = {}
    for a in range(len(args)):
        if args[a] == "Finish":
            break
        if a % 2 == 0:
            destination = args[a]
        else:
            passenger = args[a]

            if destination not in destination_list:
                destination_list[destination] = []

            destination_list[destination].append(passenger)
    for destination, passenger in destination_list.items():
        destination_list[destination] = sum(passenger)
    return destination_list

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
