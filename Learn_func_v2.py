'''Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает
именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>,
при этом имена аргументов следуют в алфавитном порядке (по возрастанию).'''
# def info_kwargs(**kwargs):
#     for k in sorted(kwargs.keys()):
#         print(f'{k}: {kwargs[k]}')
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

'''Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов
(любая непустая строка) по образцу: <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы).
Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.'''

# def print_products(*args):
#     cnt = 0
#     for el in args:
#         if isinstance(el, str) and  el !='':
#             cnt += 1
#             print(f'{cnt}) {el}')
#     if cnt == 0:
#         print('Нет продуктов')
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')

'''Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и возвращает приветствие'''

# def greet(name, *args):
#     res = 'Hello, ' + name
#     for el in args:
#         res +=' and ' + el
#     res += '!'
#     return res
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))


'''Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое
переданных в нее числовых (int или float) аргументов.'''

# def mean(*args):
#     sm, cnt = 0, 0
#     for el in args:
#         if (isinstance(el, int) or isinstance(el, float)) and isinstance(el, bool) != True:
#             sm += el
#             cnt += 1
#     if cnt == 0:
#         return float(cnt)
#     else:
#         return sm / cnt
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

'''Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. '''
# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     return [[value for _ in range(n)] for _ in range(n)]



