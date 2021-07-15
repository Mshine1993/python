from random import randint

my_list = [randint(0, 25) for _ in range(25)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Начальный спиок - {my_list}')
print(f'Список без повторений - {uniq_list}')

