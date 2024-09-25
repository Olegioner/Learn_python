'''Task'''
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
#           (10, 11, 12), (13, 14, 15), (16, 17, 18),
#           (19, 20, 21), (22, 23, 24), (25, 26, 27),
#           (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {el[0]:el[1:] for el in tuples}
# print(result)


'''Task'''
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70),
#             'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87),
#             'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120),
#             'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100),
#             'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {k:v for k,v in students.items() if v[0] > 167 and v[1] < 75 }
# print(result)


"""Task"""
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
#            11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
#            21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {k:v for k,v in letters.items() if k not in remove_keys}
# print(result)

'''Task'''

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {words[i]:[ord(words[i][j]) for j in range(len(words[i]))]for i in range(len(words))}
# print(result)


'''Task'''
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {numbers[i] : [j for j in range(1, numbers[i]+1) if numbers[i] % j == 0] for i in range(len(numbers))}
# print(result)

'''Task'''
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# s = s.split()
# s = [s[i].split(':') for i in range(len(s))]
#
# result = {int(s[i][0]):s[i][1] for i in range(len(s))}
# 2 решение: result = {int(i.split(":")[0]): i.split(":")[1] for i in s.split()}
# 3 решение: result = {int(k):v for k, v in [l.split(':') for l in s.split()]}


'''В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре.
В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.'''

# code_list = list(input())
#
# m = int(input())
# dict_letter = {}
# for _ in range(m):
#     k,v = input().split(': ')
#     dict_letter[k] = int(v)
# result = ''
# for el in code_list:
#     for k,v in dict_letter.items():
#         if code_list.count(el) == dict_letter[k]:
#             result += k
#
# print(result)

'''Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.
У каждого из друзей Тимура может быть один или более телефонных номеров.
Напишите программу, которая поможет Тимуру находить все номера определённого друга.'''
# n = int(input())
# dict_contacts = {}
# for _ in range(n):
#     tel, name = input().lower().split()
#     if name in dict_contacts:
#         dict_contacts[name] += ' ' + tel
#     else:
#         dict_contacts[name] = tel
#
# m = int(input())
# for _ in range(m):
#     print(dict_contacts.get(input().lower(), 'абонент не найден'))


'''Программа получает на вход количество стран n. Далее идет n строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число m, далее идут m запросов — названия каких-то
m городов, из перечисленных выше.'''
# n = int(input())
# dict_country = {}
# for _ in range(n):
#     country, *city = input().split()
#     dict_country[country] = city
# m = int(input())
# list_city = [input() for _ in range(m)]
# for el in list_city:
#     for key in dict_country.keys():
#         if el in dict_country[key]:
#             print(key)

'''Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу,
которая для одного данного слова определяет его синоним.'''
# n = int(input())
# dict_synonyms ={}
# for _ in range(n):
#     key, value = input().split()
#     dict_synonyms[key] = value
# word = input()
# for key,value in dict_synonyms.items():
#     if key == word:
#         print(value)
#     elif value == word:
#         print(key)


'''На вход программе подаются два предложения. Напишите программу, которая определяет,
являются они анаграммами или нет. Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.'''
# ТРЭШ
# first_text = ''.join(sorted([el for el in  list(input().lower()) if el not in ' .,!?:;-']))
# second_text = ''.join(sorted([el for el in  list(input().lower()) if el not in ' .,!?:;-']))
# first_dict = {i:first_text[i] for i in range(len(first_text))}
# second_dict = {i:second_text[i] for i in range(len(second_text))}
# print('YES') if first_dict == second_dict else print('NO')


'''На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.'''
# dict_anagrams = {input():input()}
# for key, value in dict_anagrams.items():
#     if sorted(key) == sorted(value):
#         print('YES')
#     else:
#         print('NO')

'''В первой строке задано одно целое число n — количество слов в словаре. В следующих n строках записаны слова
и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число m — количество
поисковых слов, чье определение нужно вывести. В следующих m строках записаны сами слова, по одному на строке.'''
# slang_list = [input().split(': ') for _ in range(int(input()))]
# slang_dict = {}
# for i in range(len(slang_list)):
#     for j in range(len(slang_list[i])):
#         slang_list[i][0] = slang_list[i][0].lower()
#     slang_dict.setdefault(slang_list[i][0],slang_list[i][1])
#
# for i in range(int(input())):
#     print(slang_dict.get(input().lower(), 'Не найдено'))

# Решение лучше_____________________________

# slang_dict = {}
# for _ in range(int(input())):
#     key, value = input().split(': ')
#     slang_dict.setdefault(key.lower(), value)
#
# for _ in range(int(input())):
#     print(slang_dict.get(input().lower(), 'Не найдено'))







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

