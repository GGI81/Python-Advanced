def say_smth(times):
    if times == 0:
        return
    print("I am saying")
    say_smth(times - 1)

say_smth(5)

# What is Recursion?
# The process in which a function calls itself is called recursion
# The function that is calling itself is called a recursive function
#
# A recursive function has the following structure
#   - A base case
#   - A recursive case
