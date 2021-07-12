a = int(input('Текущая дистанция, км: '))
b = int(input('Целевая дистанция, км: '))
n = 0
while a < b:
    c = a * 0.1
    a = a + c
    print(a)
    n = n + 1

print(n)

