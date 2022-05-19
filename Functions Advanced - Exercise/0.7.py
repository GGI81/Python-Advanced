# 7.	Keyword Arguments Length

def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))  # 2

dictionary = {}
print(kwargs_length(**dictionary))  # 0
