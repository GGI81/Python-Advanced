# The process in which a function calls itself is called recursion
# The function that is calling itself is called a recursive function

# A recursive function has the following structure
#   A base case
#   A recursive case

n = 10
index = 0
while True:
    if index == n:
        break
    print(index)
    index += 1


n = 3


def f1(index, max_index):
    if index == max_index:
        return  # base case, exit condition
    print(index)
    f1(index=index + 1, max_index=max_index)  # recursive call


f1(index=0, max_index=n)

print()


# Example
# Factorial recursive representation


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)