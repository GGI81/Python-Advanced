# raise IndexError("My Index is out of range")

# Custom exception are exception made by us

class ValueTooSmallError(Exception):
    def __init__(self, min_value):
        super().__init__(f"The value must be greater or equal to {min_value}")

raise ValueTooSmallError("The value is to small")

