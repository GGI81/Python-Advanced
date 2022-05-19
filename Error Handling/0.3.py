try:
    text = input()
    times = int(input())
    print(text * times)
except ValueError:
    print("Variables times must be integers")

