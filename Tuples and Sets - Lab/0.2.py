def avg(values):
    return sum(values) / len(values)


number_students = int(input())

my_dict = {}

for i in range(number_students):
    name, grade_String = input().split()
    grade = float(grade_String)
    if name not in my_dict:
        my_dict[name] = []
    my_dict[name].append(grade)

for key, value in my_dict.items():
    average_grade = avg(value)
    value_str = " ".join(str(f"{x:.2f}") for x in value)
    print(f"{key} -> {value_str} (avg: {average_grade:.2f})")