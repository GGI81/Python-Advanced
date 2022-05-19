def recursive_power(number, power, counter=0, result=1):
    if counter == power:
        return result
    result *= number
    return recursive_power(number, power, counter+1, result)

print(recursive_power(2, 10))  # 1024
print(recursive_power(10, 100))
