'''На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет
их так, чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся
идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.'''

# string = input().split()
# str_list = []
# for i in range(len(string)):
#     cnt = string[:i+1].count(string[i])
#     if cnt >= 2:
#         str_list.append(f'{string[i]}_{cnt - 1}')
#     else:
#         str_list.append(string[i])
#
# print(*str_list)

'''На вход программе подается строка текста. Напишите программу, которая выводит слово, которое
встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое
меньше в лексикографическом порядке.'''
# text = [el.lower().strip(' .,!?:;-') for el in input().split()]
# res_dict = {}
# for i in range(len(text)):
#      if text[i] not in res_dict.values():
#          res_dict.setdefault(text[i], text.count(text[i]))
# mn_count = 999
# for v in res_dict.values():
#     mn_count = min(mn_count, v)
# res = []
# for k,v in res_dict.items():
#     if v ==mn_count:
#         res.append(k)
# print(min(res))


'''task'''
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for i in range(len(pets)):
#     if (pets[i][1],pets[i][2],pets[i][3]) not in result:
#         result.setdefault((pets[i][1],pets[i][2],pets[i][3]), [pets[i][0]])
#     else:
#         result[(pets[i][1],pets[i][2],pets[i][3])].append(pets[i][0])
#
# print(result)

'''Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s.
Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.'''
# text = '''orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana
# orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry
# apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon
# pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple
# barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana
# quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'''
# text_list = text.split()
# result = {}
# for i in range(len(text_list)):
#     if text_list[i] not in result.values():
#         result.setdefault(text_list[i], text.count(text_list[i]))
# mx = 0
# for v in result.values():
#     mx = max(v, mx)
# res_list = []
# for k,v in result.items():
#     if result[k] == mx:
#         res_list.append(k)
#
# print(min(res_list))


'''Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки
text будет подсчитано количество его вхождений.'''
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for i in range(len(text)):
#     if text[i] not in result.values():
#         result.setdefault(text[i], text.count(text[i]))
# print(result)

'''Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2: если ключ есть в обоих словарях,
добавьте его в результирующий словарь со значением, равным сумме соответствующих значений из первого и второго словаря;
если ключ есть только в одном из словарей, добавьте его в результирующий словарь с его текущим значением.
Результирующий словарь необходимо присвоить переменной result.'''

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
# result.update(dict2)
# for k in dict1:
#     if k  not in dict2.keys():
#         result.setdefault(k, dict1[k])
#     else:
#         result[k] = dict1[k]+dict2[k]

'''task'''
# n = 16
# result = {}
# for k in range(1,n):
#     result.setdefault(k, k**2)
# print(result)

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

