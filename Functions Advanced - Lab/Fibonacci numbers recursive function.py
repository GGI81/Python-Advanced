# Fibonacci numbers
# f(n) = f(n - 1)+ f(n - 2)
# f(0) = 0
# f(1) = 1

print()


# Имаме раздвояване и първо ще изчисли f(n - 1), a после ще изчисли f(n - 2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

counts = {
    "x": 0
}

def fibonacci(n):
    counts["x"] += 1
    if n == 1:
        return 1
    if n == 0:
        return 0

    result = fibonacci(n - 1) + fibonacci(n - 2)

    return result

print(fibonacci(5))