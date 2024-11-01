'''На вход программе подается строка текста с именем существующего текстового файла,
в котором необходимо заменить запрещенные слова звездочками.'''
# file = 'C:/new/data (1).txt'
# with open('C:/new/forbidden_words.txt', 'r', encoding='utf-8') as forbidden:
#     bad_words = [el.strip() for el in forbidden.read().split()]
#
# with open(file, 'r', encoding='utf-8') as text:
#     text_this = text.read()
# text_low = text_this.lower()
# for el in bad_words:
#     text_low = text_low.replace(el, len(el)*'*')
#
# res_test = ''
# for i in range(len(text_this)):
#     if text_this[i].lower() != text_low[i]:
#         res_test += text_low[i]
#     else:
#         res_test += text_this[i]
#
# print(res_test)

'''Все функции без комментов'''
# file = 'C:/new/func.txt'
# with open(file, 'r', encoding='utf-8') as code:
#     code_list = [[el.strip() for el in row.split()] for row in code.readlines()]
# code_list_clean = []
# for el in code_list:
#     if el != []:
#         code_list_clean.append(el)
# count = 0
# for i in range(len(code_list_clean)):
#     if code_list_clean[i][0] == 'def' and code_list_clean[i-1][0] != '#':
#         print(code_list_clean[i][1][:code_list_clean[i][1].index('(')])
#         count += 1
# if count == 0:
#     print('Best Programming Team')


'''Транслитерация '''
# d = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
#     }
# d.update({k.upper(): v.capitalize() for k, v in d.items()})
# translator = str.maketrans(d)
# with open('C:/new/cyrillic.txt', 'r', encoding='utf-8') as text_cyrill:
#     words = text_cyrill.read()
#     transliterated_text = words.translate(translator)
# with open('C:/new/transliteration.txt', 'w', encoding='utf-8') as tran_text:
#     print(transliterated_text, file=tran_text)



'''На вход программе подается строка текста с именем текстового файла. Напишите программу,
выводящую на экран последние 10 строк данного файла.'''
#
# with open(input(), 'r', encoding='utf-8') as text:
#     text_list = [el.strip() for el in text.readlines()]
#     if len(text_list) > 10:
#         print(*text_list[-10:], sep='\n')
#     else:
#         print(*text_list, sep='\n')



'''Вам доступен текстовый файл words.txt со словами, разделенными пробелом.
Напишите программу, которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования'''

# with open('C:/new/words.txt', 'r', encoding='utf-8') as words:
#     words_list = [el.strip() for el in words.read().split()]
# sort_words_list = sorted(words_list, key=lambda x: len(x))
# for el in words_list:
#     if len(el) == len(sort_words_list[-1]):
#         print(el)

'''Напишите программу для подсчета количества студентов, сдавших все три теста.
Тест считается сданным, если количество баллов по нему не меньше 65.'''
# with open('C:/new/grades.txt', 'r', encoding='utf-8') as grades:
#     grades_list = [[(int(el)) if el.isdigit() else el for el in row.split()] for row in grades.readlines()]
# res = 0
# for el in grades_list:
#     count = 0
#     for i in range(1, len(el)):
#         if el[i] >= 65:
#             count += 1
#     if count == 3:
#         res += 1
# print(res)



'''Напишите программу для подсчета суммарной месячной выручки фирмы. '''
# with open('C:/new/ledger.txt', 'r', encoding='utf-8') as ledger:
#     ledger_list = [int(el.strip('$')) for el in ledger.read().split()]
#     sm = 0
#     for el in ledger_list:
#         sm+= el
#     print(f'{sm}$')

'''Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей
(не меняя порядка следования), которые были в сети не менее часа'''

# with open('C:/new/logfile.txt', 'r', encoding='utf-8') as logfile:
#     log_list = [[el.strip() for el in row.split(',')] for row in logfile.readlines()]
# list_user = []
# for el in log_list:
#     if ((int(el[2][:2]) * 60 + int(el[2][3:])) - (int(el[1][:2]) * 60 + int(el[1][3:]))) >= 60:
#         list_user.append(el[0])
#
# with open('C:/new/output.txt', 'w', encoding='utf-8') as output:
#     print(*list_user, sep='\n', file=output)

'''На вход программе подается натуральное число n и n строк с названиями файлов.
Напишите программу, которая создает файл output.txt и выводит в него содержимое всех файлов, не меняя их порядка'''
# count_file = int(input())
# file_list = [input() for _ in range(count_file)]
# content_from_files = ''
# for i in range(count_file):
#     content_from_files += open(file_list[i], 'r', encoding='utf-8').read()
# with open('C:/new/output.txt', 'w', encoding='utf-8') as output:
#     print(content_from_files, file=output)


'''Напишите программу создания файла answer.txt и вывода в него списка козлов,
которые удовлетворяют условию загадки от Жака Фреско.'''

# with open('C:/new/goats.txt', 'r', encoding='utf-8') as goats:
#     goats_list = [row for row in goats.read().split('\n')]
# ind_goats = goats_list.index('GOATS')
# color_goats = goats_list[1:ind_goats]
# count_goats = goats_list[ind_goats+1:]
# dict_goats = {}
# for el in color_goats:
#     dict_goats[el] = 0
# for el in count_goats:
#     dict_goats[el] += 1
# sm_goats = 0
# for v in dict_goats.values():
#     sm_goats += v
# fresko_answer = []
# for k,v in dict_goats.items():
#     if v/sm_goats> 0.07:
#         fresko_answer.append(k)
# with open('C:/new/answer.txt', 'w', encoding='utf-8') as answer:
#     print(*fresko_answer, sep='\n', file=answer)

'''Напишите программу для добавления 5 баллов к каждому результату теста
и вывода фамилий и новых результатов тестов в файл new_scores.txt.'''

# with open('C:/new/class_scores.txt', 'r', encoding='utf-8') as class_scores, open('C:/new/new_scores.txt', 'w', encoding='utf-8') as new_scores:
#     old_scores = [[int(el) if el.isdigit() else el for el in row.split()] for row in class_scores.readlines()]
#     class_scores_new = list(map(lambda x: [x[0], x[1] + 5] if x[1] + 5 < 100 else [x[0], 100], old_scores))
#     for el in class_scores_new:
#         print(*el, file=new_scores)

'''Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка,
где перед каждой строкой стоит ее номер, символ) и пробел. Нумерация строк должна начинаться с 1.'''
# with open('C:/new/input.txt', 'r', encoding='utf-8') as input_file, open('C:/new/output.txt', 'w', encoding='utf-8') as output:
#     input_data = input_file.readlines()
#     for i in range(len(input_data)):
#         print(f'{i+1})', input_data[i], end='', file = output)

'''Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне
от 111 до 777 (включительно), каждое с новой строки.'''
# from random import randint
# with open('random.txt', 'w', encoding='utf-8') as random:
#     for i in range(25):
#         print(randint(111, 777), file = random)

'''Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из этого файла.
Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей'''
# def read_csv():
#     with open('C:/new/data.csv', 'r', encoding='utf-8') as data:
#         data_keys = [el.strip() for el in data.readline().split(',')]
#         data_value = [el.strip().split(',') for el in data.readlines()]
#     dict_list = []
#     for i in range(len(data_value)):
#         dict_list.append(dict(zip(data_keys, data_value[i])))
#     return dict_list
# print(read_csv())

'''Напишите программу выводящую все страны, название которых начинается с буквы 'G',
численность населения которых больше чем 500000 человек, не меняя их порядок.'''

# with open('C:/new/population.txt', 'r', encoding='utf-8') as country:
#     country_list = [[el.strip() for el in row.split('\t')] for row in country.read().split('\n')]
# country_list_res = list(map(lambda x: list(map(lambda el: int(el) if el.isdigit() else el, x)), country_list))
# for i in range(len(country_list_res)):
#     if country_list_res[i][0].startswith('G') and country_list_res[i][1] > 500000:
#         print(country_list_res[i][0])


'''Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
Напишите программу, которая c помощью модуля random создает
3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.'''
# from random import randrange
# with open('C:/new/first_names.txt') as f_name, open('C:/new/last_names.txt') as l_name:
#     first_names = [el.strip() for el in f_name.readlines()]
#     last_names = [el.strip() for el in l_name.readlines()]
# for i in range(3):
#     print(first_names[randrange(len(first_names))], last_names[randrange(len(last_names))])

'''Напишите программу, которая выводит количество букв латинского алфавита, слов и строк'''
# with open('C:/new/file.txt', 'r', encoding='utf-8') as file:
#     content_file = file.read()
#     file.seek(0)
#     content_list = file.readlines()
# letter = [el.strip() for el in list(content_file)]
# letter_clean = []
# for el in letter:
#     if el not in ' .,!?0123456789"':
#         letter_clean.append(el)
# words = [el for el in content_file.split()]
# print('Input file contains:', f'{len(letter_clean)} letters', f'{len(words)} words', f'{len(content_list)} lines', sep='\n')

'''Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.'''

# with open('C:/new/nums(1).txt', 'r', encoding='utf-8') as numbers:
#     num = numbers.read()
#     only_num = ''
#     for el in num:
#         if el.isalnum():
#             if el.isalpha():
#                 only_num+= ' '
#             elif el.isdigit():
#                 only_num+= el
#         else:
#             only_num += ' '
#     # print(num)
#     # print(only_num)
#     only_num_list = [int(el) for el in only_num.split()]
#     print(sum(only_num_list))

'''Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран
(для каждой строки выводится сумма чисел в этой строке).'''
# with open('C:/new/numbers (1).txt', 'r', encoding='utf-8') as numbers:
#     num = [[int(el) for el in row.split()]for row in numbers.readlines()]
#     for el in num:
#         print(sum(el))


'''Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.'''
# with open('C:/new/lines.txt', 'r', encoding='utf-8') as file:
#     lines = [el.strip() for el in file.readlines()]
#     lines_sort = sorted(lines, key=lambda x: len(x))
#     for el in lines:
#         if len(el) == len(lines_sort[-1]):
#             print(el)

'''Обратный порядок вывода'''
# with open('C:/new/data.txt', 'r', encoding='utf-8') as file:
#     file_list = [el.strip() for el in file.readlines()]
#     print(*file_list[::-1], sep='\n')

'''Строка в обратном порядке'''
# with open('C:/new/text.txt', 'r', encoding='utf-8') as file:
#     print(file.readline()[::-1])

'''Сумма всех товаров'''
# file = open(f'C:/new/prices.txt', 'r', encoding='utf-8')
# price = [[el for el in row.split()] for row in file.readlines()]
# file.close()
# sm = 0
# for el in price:
#     sm += int(el[1]) * int(el[2])
# print(sm)
'''Случайная стройка из файла'''
# from random import randrange
# name_file = open('lines.txt', 'r', encoding='utf-8')
# list_text = name_file.readlines()
# print(list_text[randrange(len(list_text))])
# name_file.close()
'''Сумма двух чисел'''
# from functools import reduce
# file = open('numbers.txt', 'r', encoding='utf-8')
# list_num = [int(el) for el in file.readlines()]
# print(reduce(lambda x,y: x + y, list_num, 0))
# file.close()