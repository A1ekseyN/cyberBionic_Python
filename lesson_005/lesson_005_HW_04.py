# Ready
from collections import namedtuple

subject = ('Algebra', 'Geometry', 'History', 'Computer science', 'Geography')
grades = []
marks = namedtuple('Marks', 'Geometry History Computer science Geography ')

for _ in range(len(subject)):
    i = input('Введите оценку для студента: ')
    grades.append(i)

print()
for s in subject:
    mark = ''
    for j in grades:
        mark = j
    print(f"Предмет - {s}, оценка: {mark}.")
