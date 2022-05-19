# 1.	Negative vs Positive

def function(nums):
    total_negative = 0
    total_positive = 0
    for i in nums:
        if i > 0:
            total_positive += i
        else:
            total_negative += i
    print(total_negative)
    print(total_positive)
    if abs(total_positive) < abs(total_negative):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
function(numbers)