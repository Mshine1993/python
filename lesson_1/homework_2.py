seconds = int(input('Введите количество секунд от 1 до 86400: '))
hour = (seconds // 3600)
time_sec = (seconds % 60)
min = ((seconds - (hour*3600)) // 60)

time = (hour, min, time_sec)

print (time)