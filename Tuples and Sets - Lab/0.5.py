n = int(input())
guest_list = {input() for i in range(n)}

while True:
    command = input()
    if command == "END":
        break
    guest_list.remove(command)


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([g for g in guest_list if is_vip(g)])
regular_guests = sorted([g for g in guest_list if not is_vip(g)])

print(len(vip_guests) + len(regular_guests))
[print(i) for i in vip_guests]
[print(i) for i in regular_guests]
