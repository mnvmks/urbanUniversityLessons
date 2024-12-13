# module_2_6 - additional task

result = ''

n = int(input("Введите число для первого поля: "))

for i in range(1, n):
    for j in range(i + 1, n + 1):
        if n % (i + j) == 0:
            result += str(i) + str(j)

print(result)
