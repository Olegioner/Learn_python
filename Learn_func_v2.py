'''Программа должна вывести одно число — значение указанного многочлена при заданном значении x.'''
# from functools import reduce
#
# def evaluate(coefficients, x):
#     new_cf = map(lambda el, i: el * x**i, coefficients, range(len(coefficients)-1, -1, -1))
#     return reduce(lambda a,b: a + b, new_cf, 0)
#
#
# coefficients = [int(el) for el in input().split()]
# x = int(input())
#
# print(evaluate(coefficients, x))

'''Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета. '''

# print(*list(map(lambda x: 255 - x, [int(el) for el in input().split()])))


'''Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки
по неубыванию значений элементов, при этом числа должны следовать до строк.
Элементы отсортированного списка выведите на одной строке, разделив символом пробела.'''

# mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
# print(*(sorted(filter(lambda x: isinstance(x, int), mixed_list)) + sorted(filter(lambda x: isinstance(x, str), mixed_list))))


'''Список mixed_list содержит целочисленные и строковые значения. Напишите программу,
которая с помощью встроенной функции max() находит и выводит наибольшее числовое
значение в указанном списке.'''
# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory',
#               'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919,
#               2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle',
#               'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665,
#               'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106,
#               242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772,
#               'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105,
#               'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068,
#               'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant',
#               2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698,
#               'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound',
#               1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
#
# print(max(mixed_list, key=lambda x: (isinstance(x, int), x)))
'''Список data содержит слова на русском языке. Напишите программу, которая сортирует этот список по
возрастанию длины слов. В случае, если длины каких-то слов совпадают, – отсортировать эти слова в
лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом пробела.'''
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука',
#         'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз',
#         'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова',
#         'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город',
#         'отношение', 'женщина', 'деньги']
#
# print(*sorted(sorted(data), key=lambda x: len(x)))

'''Task'''
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'),
#         (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'),
#         (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'),
#         (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# print(*list(map(lambda data: f'{data[1]}: {data[0]}', sorted(data, reverse=True, key=lambda x: x[1][-1]))), sep='\n')

'''Task'''
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100,
#            36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93,
#            36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27,
#            57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6,
#            4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49,
#            5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# print(*list(map(lambda num: num // 2 if num % 2 == 0 else num, (filter(lambda num: '' if num % 2 != 0 and num > 47 else num, numbers)))))

'''Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words,
имеющие длину ровно 6 символов. Слова следует вывести в алфавитном порядке на одной
строке, разделив символом пробела.'''
#
# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid',
#          'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides',
#          'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard',
#          'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent',
#          'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday',
#          'accessory', 'absorb']
# print(*sorted(filter(lambda text: len(text) == 6, words)))

'''Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и
возвращает значение True, если переданный аргумент начинается и заканчивается на английскую букву a
(регистр буквы неважен) и False в противном случае.'''

# func = lambda text: True if text[0].lower() == 'a' and text[-1].lower() == 'a' else False

'''Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает строковый аргумент
и возвращает значение True, если переданный аргумент является неотрицательным числом (целым или вещественным),
или False в противном случае.'''

# is_non_negative_num = lambda num: True if ((num.replace('.','',1)).isdigit() and num.count('.') <= 1) and float(num) >= 0 else False
# is_num = lambda q: ((q.replace('.', '', 1)).lstrip('-')).isdigit() and q[1:].count('-') == 0


'''Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент
 и возвращает значение True, если он делится без остатка на 19 или на 13 и False в противном случае.'''
# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False

'''TASK'''
# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
#
# big_city = sorted(map(lambda el: el[0], filter(lambda x:x if x[2] == 'primary' and x[1] > 10**7 else '', data)))
# big_city_output = reduce(lambda x, y: x + y + ', ' if y != big_city[-1] else x + y, big_city , 'Cities: ')
# print(big_city_output)


'''Task'''
# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: name if name == name[::-1] and len(name) > 4 else '', words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
'''Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трёхзначные числа,
дающие при делении на 5 остаток 2, и выводит их кубы, каждый в отдельной строке.'''
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def f1(el):
#    return (99 < el <= 999) and (el % 5 == 2)
#
# def f2(el):
#     return print(el**3)
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374,
#            1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98,
#            530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926,
#            175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274,
#            387, 120, 340, 963, 832, 1127]
#
# map(f2, filter(f1, numbers))


'''Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков,
а затем выводит их, каждый на отдельной строке.'''
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# def round_num(el):
#     return print(round(el, 2))
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# map(round_num, numbers)

'''На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.'''
# list_num = sorted([int(el) for el in input().split()])
# def sort_sum(el):
#     return sum([int(i) for i in str(el)])
# print(*sorted(list_num, key=sort_sum))


'''Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.
Список возможных функций:
квадрат: функция принимает число и возвращает его квадрат;
куб: функция принимает число и возвращает его куб;
корень: функция принимает число и возвращает корень квадратный из этого числа;
модуль: функция принимает число и возвращает его модуль;
синус: функция принимает число (в радианах) и возвращает синус этого числа.'''
# from math import sqrt, sin
# def square(num):
#     return num**2
# def cube(num):
#     return num**3
# def sqrt_n(num):
#     return sqrt(num)
# def module(num):
#     return abs(num)
# def sinus(num):
#     return sin(num)
# dict_math = {'квадрат':square, 'куб': cube, 'корень':sqrt_n, 'модуль':module, 'синус':sinus}
#
# n = int(input())
# key = input()
#
# print(dict_math[key](n))

'''Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
Напишите программу сортировки списка спортсменов по указанному полю:
1: по имени;
2: по возрасту;
3: по росту;
4: по весу.'''
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
#             ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
#             ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# def sort_name(tuple_athletes):
#     return tuple_athletes[0]
#
# def sort_age(tuple_athletes):
#     return tuple_athletes[1]
#
# def sort_height(tuple_athletes):
#     return tuple_athletes[2]
#
# def sort_weight(tuple_athletes):
#     return tuple_athletes[3]
#
# dict_func = {1:sort_name, 2:sort_age, 3:sort_height, 4:sort_weight}
#
# n = int(input())
# a1 = sorted(athletes, key=dict_func[n])
# for el in a1:
#     print(*el)



'''Дан список numbers, содержащий кортежи чисел. Напишите программу, которая сортирует и выводит список numbers в
соответствии с суммой минимального и максимального элемента кортежа.'''

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100),
#            (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def sm_tuple(num_tuple):
#     return max(num_tuple) + min(num_tuple)
#
# print(sorted(numbers, key=sm_tuple))


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



