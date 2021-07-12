def my_sum():
    s = 0
    while True:
        in_list = input('Введите числа через пробел или Q для выхода: ').split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print('Чтобы выйти из программы нажмите "q"- ')

        print(f'Сумма чисел = {s}')

print(my_sum())
