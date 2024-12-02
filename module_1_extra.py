# module 1: extra homework

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
mid_grades = dict()

students = sorted(list(students))

for i, name in enumerate(students):
    mid_grades[name] = sum(grades[i]) / len(grades[i])

print(mid_grades)