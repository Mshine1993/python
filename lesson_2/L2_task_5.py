rate = [9, 8, 7, 6, 5, 4, 3, 2, 1]
number = int(input('Введите число (от 1 до 9): '))
i = 0
for n in rate:
    if number <= n:
        i += 1
rate.insert(i, (number))
print(rate)