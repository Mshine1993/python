def information(name, surname, age, birthday, city, phone, email):
    return f'Name - {name}, Surname - {surname}, Age - {age}, Birthday - {birthday} City - {city}, Phone - {phone},' \
           f' Email - {email}'


Name = input('Введите ваше имя: ')
Surname = input('Введите вашу фаимлию: ')
Age = input('Введите ваш возраст: ')
Birthday = input('Введите вашу дату рождения: ')
City = input('Введите ваш город: ')
Phone = input('Введите ваш номер телефона: ')
Email = input('Введите ваш email: ')

print(information(name=Name, surname=Surname, age=Age, birthday=Birthday, city=City, phone=Phone, email=Email))

