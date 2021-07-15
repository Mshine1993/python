a = input('Введите число больше 0: ')
m = int(a) % 10
a = int(a) // 10

while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10

print('Наиболоьшая цифра', m)

