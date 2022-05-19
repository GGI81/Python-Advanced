# 2.	Odd or Even

def odd_even(cmd, nums):
    if cmd == "Odd":
        total = 0
        for i in nums:
            if i % 2 != 0:
                total += i
        print(total * len(nums))
    elif cmd == "Even":
        total = 0
        for i in nums:
            if i % 2 == 0:
                total += i
        print(total * len(nums))


command = input()
numbers = [int(x) for x in input().split()]
odd_even(command, numbers)

"""
Odd
1 3 5 34 7 9 12 11 13 10

Even
1 3 5 7 9 13
"""