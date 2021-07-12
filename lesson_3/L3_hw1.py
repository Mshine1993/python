# def my_sum(a, b):
#     c = a/b
#     return c
#
# a = int(input('Введите число больше нуля: '))
# b = int(input('Введите число больше нуля: '))
# while b == 0:
#     print('Ошибка')
#     b = int(input('Введите число больше нуля: '))
# result = my_sum(a, b)
# print(result)

def my_sum(a, b):
    while b == 0:
        print('Ошибка')
        b = int(input('Введите число больше нуля: '))
    c = a / b
    return c


print(my_sum(int(input('Введите число больше нуля: ')), (int(input('Введите число больше нуля: ')))))
