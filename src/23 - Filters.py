grades = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'A']


def removeBad(arr):
    return arr != 'F'


# print(list(filter(removeBad,grades)))

filter_grades = []
for grade in grades:
    if grade != "F":
        filter_grades.append(grade)
print(filter_grades)


# comprehension method
print([grade for grade in grades if grade != "A"])
