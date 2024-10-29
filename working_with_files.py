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