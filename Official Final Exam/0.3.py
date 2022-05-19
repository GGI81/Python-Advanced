def shopping_list(budget: int, **kwargs):
    basket = []
    if budget >= 100:
        money = budget
        ll = []
        for key, value in kwargs.items():
            if len(basket) != 5:
                if key not in basket:
                    basket.append(key)
                b = [*value]
                total = b[0] * b[1]
                if total <= money:
                    ll.append(f"You bought {key} for {total:.2f} leva.")
                    money -= total
            else:
                return "\n".join(ll)
        return "\n".join(ll)
    else:
        return "You do not have enough budget."


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))
print(shopping_list(20, jeans=(19.99, 1), ))
print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5), tomatoes=(4.20, 1),
                    milk=(2.50, 2), juice=(2, 3), eggs=(3, 1), ))
