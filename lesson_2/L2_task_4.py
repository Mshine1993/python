words = input('Введите несколько слов, разделяя их пробелами: ').split()
for i, word in enumerate(words, 1):
    print (f'{i}) {word[:10]}')
