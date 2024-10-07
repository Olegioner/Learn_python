
'''Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием
от начала координат (точки (0;0)). Программа должна вывести отсортированный список.'''
# from math import sqrt
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2),
#           (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def distance(point):
#     return sqrt(point[0]**2 + point[1]**2)
#
# print(sorted(points, key=distance))



'''Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max()
 выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое
 значение элементов.'''
# def average(num_tuple):
#     return sum(num_tuple) / len(num_tuple)
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# print(min(numbers, key=average))
# print(max(numbers, key=average))



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



