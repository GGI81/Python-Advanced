from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacity = [int(x) for x in input().split(", ")]

total_pizzas = 0

while True:
    if len(pizza_orders) == 0 or len(employees_capacity) == 0:
        if len(pizza_orders) > 0:
            print(f"Not all orders are completed.")
            print(f"Orders left: {', '.join(map(str, pizza_orders))}")
            break
        elif len(employees_capacity) > 0:
            print(f"All orders are successfully completed!")
            print(f"Total pizzas made: {total_pizzas}")
            print(f"Employees: {', '.join(map(str, employees_capacity))}")
            break
    current_order = pizza_orders.popleft()
    if current_order > 0:
        current_employee = employees_capacity.pop()
        if current_order > 10:
            employees_capacity.append(current_employee)
        else:
            if current_order <= current_employee:
                total_pizzas += current_order
            else:
                total_pizzas += current_employee
                current_order -= current_employee
                while current_order:
                    if len(employees_capacity) > 1:
                        next_employee = employees_capacity.pop()
                        if next_employee > current_order:
                            total_pizzas += current_order
                            break
                        else:
                            current_order -= next_employee
                            total_pizzas += next_employee
                    else:
                        break
