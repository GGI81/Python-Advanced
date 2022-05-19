# 4.	Concatenate

def concatenate(*args):
    string = ""
    for i in args:
        string += i

    return string


print(concatenate("Soft", "Uni", "Is", "Great", "!"))  # SoftUniIsGreat!
print(concatenate("I", " ", "Love", " ", "Python"))	 # I Love Python
