def raise_exception():
    x = {}["asd"]  # Key Error
    x = [1][1]     # IndexError
    pass

# Try -> except

try:
    raise_exception()
    print("No Exception")
except IndexError:
    print("Index Exception Handled")
except KeyError:
    print(f"Key Exception Handled")
print("End")

# Except is catching all the errors

# LookupError is higher level of IndexError and KeyError
# We can write the same thing with only one -> LookupError
