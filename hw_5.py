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