def avg(numbers):
    # Fixes the case with the empty list
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


print(avg([1, 2, 3]))
print(avg([]))  # ZeroDivisionError

# Name Exception
# x = 5
#print(x)  # NameError

# Type Exception
# print(", ".join([1, 2, 3]))
