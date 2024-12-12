# module_2_4 - for loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    for j in numbers:
        if j == 1:
            continue
        elif i == j:
            primes.append(i)
            break
        elif i % j == 0:
            not_primes.append(i)
            break

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
