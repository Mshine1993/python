# Task 1
a = 10
b = 5
c = a + b
print(c)
name = input('Ведите имя ')
surname = input('Введите фамилию ')
print('Вас зовут: ', name, surname)
age = int(input('Введите ваш возраст: '))
retire = 65
print('До выхода на пенсию осталось: ', retire - age, 'лет')

# Task2
seconds = int(input('Введите количество секунд от 1 до 86400: '))
hour = (seconds // 3600)
time_sec = (seconds % 60)
min = ((seconds - (hour*3600)) // 60)
time = (hour, min, time_sec)
print(time)

# Task 3
n = input('Введите число: ')
sum = (int(n)) + (int(n+n)) + (int(n+n+n))
print(sum)

# Task 4
a = input('Введите число больше 0: ')
m = int(a) % 10
a = int(a) // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print('Наиболоьшая цифра', m)

# Task 5
income = int(input('Введите прибыль организации в рублях: '))
loss = int(input('Введите затраты организации в рублях: '))
if income > loss:
    money = income - loss
    print('Поздравляем, Ваша организация заработала: ', money, 'рублей')
    people = int(input('Введите количество сотрудников: '))
    average = money // people
    print('Каждый сотрудник заработал: ', average, 'рублей')
elif income == loss:
    print('Вы ничего не заработали')
else:
    print('Вы понесли убытки')

# Task 6
a = int(input('Текущая дистанция, км: '))
b = int(input('Целевая дистанция, км: '))
n = 0
while a < b:
    c = a * 0.1
    a = a + c
    print(a)
    n = n + 1
print(n)
