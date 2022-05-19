def raise_exception():
    raise TypeError


try:
    print(" -- Try: start")
    raise_exception()
    print(f" -- Try: end")
except TypeError:
    print(" -- Except")
finally:  # Finally is ALWAYS WORKING
    print(" -- Finally")


# try:
#     pass
# finally:
#     pass