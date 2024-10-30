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