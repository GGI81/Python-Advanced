from collections import deque

"""
def stock_availability(products: list, command, *args):
    if command == "delivery":
        for i in args:
            products.append(i)
    elif command == "sell":
        products = deque(products)
        if len(args) == 0:
            products.popleft()
        else:
            for i in args:
                if i in products:
                    while i in products:
                        products.remove(i)
                else:
                    for j in range(i):
                        products.popleft()
    return list(products)
"""

def stock_availability(inventory, command, *args):
    if command == "delivery":
        return inventory + list(args)
    if not args:
        return inventory[1:]
    if isinstance(args[0], int):
        count = int(args[0])
        return inventory[count:]

    sold_items = set(args)

    return [item for item in inventory if item not in sold_items]


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
