import csv

def _input():
    mode = input('Какой режим будем использовать: 1 = Поиск по фамилии, 2 = Запись нового контакта ==> ')
    if mode == '1':
        find = input('Введите фамилию: ')
        return find
    elif mode == '2':
        name = input("Введите имя: ")
        surname = input('Введите Фамилию: ')
        phone = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        data = [{
            'Name': name,
            'Surname': surname,
            'Phone number': phone,
            'Comment': comment,
        }]
        return data
    else:
        print('Введен не верный режим!')