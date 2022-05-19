# RECURSION
# Function Calling Itself

# The process in which a function calls itself is called recursion
# The function that is calling itself is called a recursive function
# A recursive function has the following structure
#   A base case
#   A recursive case


# Base case and Recursive case
# The base case in a recursion returns a value without making any other recursive calls
#   It is the condition for the recursion to stop
#
# The recursive case is the central part of the recursive function
#   It is the solution to the bigger problem expressed in terms of smaller problems


def loop(index, max_index):
    print(f" -- loop({index}, {max_index}) -- ")
    if index == max_index:
        print(f" -- ending loop({index}, {max_index}) -- ")
        return  # base case, exit condition

    print(index)
    loop(index=index + 1, max_index=max_index)  # recursive call

    print(f" -- ending loop({index}, {max_index}) -- ")

loop(0, 10)
