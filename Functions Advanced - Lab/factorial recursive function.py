# f(n) = f(n - 1) * n
# f(1) = 1
# f(0) = 1

def factorial(n):
    if n == 1 or n == 0:
        return 1

    result = factorial(n-1) * n

    return result
print(factorial(3))
