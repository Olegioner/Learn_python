
'''Код Морзе для представления цифр и букв использует тире и точки.
Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.'''
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
#          '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
#          '....-', '.....', '-....', '--...', '---..', '----.']
# text = input().upper()
# dict_morse = dict(zip(letters, morse))
# for i in range(len(text)):
#     for k, v in dict_morse.items():
#         if text[i] == k:
#             print(v, end=' ')

'''На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры.
Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш.
При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши.
Нажатие цифры 2,3,4 или 5 раз генерирует второй, третий, четвертый или пятый символ клавиши.'''
# d = {
#     '1': ".,?!:",
#     '2': "ABC",
#     '3': "DEF",
#     '4': "GHI",
#     '5': "JKL",
#     '6': "MNO",
#     '7': "PQRS",
#     '8': "TUV",
#     '9': "WXYZ",
#     '0': " " }
# result = ''
# text = input().upper()
# for i in range(len(text)):
#     for k, v in d.items():
#         if text[i] in v:
#             result += k * (v.index(text[i]) + 1)
# print(result)

'''Напишите программу, которая по номеру курса выводит информацию о данном курсе. '''
# dict_course = {'CS101':	'3004, Хайнс, 8:00',
#                'CS102':	'4501, Альварадо, 9:00',
#                'CS103': '6755, Рич, 10:00',
#                'NT110': '1244, Берк, 11:00',
#                'CM241': '1411, Ли, 13:00'}
# num = input()
# print(f'{num}: {dict_course[num]}')

'''Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:'''
# num = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
# n = list(input())
# for el in n:
#     print(num[el], end=' ')

'''Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), у которых нет информации об электронной почте.'''
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# list_email_empty = []
# for i in range(len(users)):
#     if 'email' in users[i]:
#         if users[i]['email'] == '':
#             list_email_empty.append(users[i]['name'])
#     else:
#         list_email_empty.append(users[i]['name'])
# print(*sorted(list_email_empty))


'''Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 8.'''
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# list_user = []
# for i in range(len(users)):
#     if users[i]['phone'][-1] == '8':
#         list_user.append(users[i]['name'])
# print(*sorted(list_user))

