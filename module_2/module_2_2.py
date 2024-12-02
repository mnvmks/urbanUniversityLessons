# module_2_2 - if, elif, else

first = 0
second = 0
third = 0

for i in range(3):
    if i == 0:
        first = input(f'Введите {i + 1} число: ')
        continue
    if i == 1:
        second = input(f'Введите {i + 1} число: ')
        continue
    if i == 2:
        third = input(f'Введите {i + 1} число: ')

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
