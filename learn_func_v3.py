'''Task 9.6.17'''

# def matrix_to_dict(matrix:list[list[int | float]]) -> dict[int, list[int | float]]:
#     return {el[0]: el[1] for el in enumerate(matrix, 1)}

'''Task 9.6.16'''
# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     numbers[:] = [numbers[(el - step) % len(numbers)] for el in range(len(numbers))]


'''Task 9.6.15'''

# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     grades.setdefault('top_grades', max(grades['grades']))
#     del grades['grades']
#     return grades


'''Task 9.6.14'''

# def get_digits(number: int | float) -> list[int]:
#     return [int(el) for el in str(number) if el != '.']

'''Task 9.5.20'''
# def sort_priority(values, group):
#     values.sort()
#     group = list(group)
#     group.sort()
#     for el in group[::-1]:
#         if el in values:
#             values.remove(el)
#             values.insert(0, el)

# как надо было:
# def sort_priority(numbers, group):
#     numbers.sort(key=lambda x: (x not in group, x))

'''Task 9.5.19'''
# import datetime
# from datetime import date
#
#
# def date_formatter(country_code):
#     base_format = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y',
#                    'ca': '%Y-%m-%d', 'br': '%d/%m/%Y',
#                    'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y',}
#     return lambda x: datetime.datetime.strftime(x, base_format[country_code])
#
# date_ru = date_formatter('us')
# today = date(2025, 1, 5)
# print(date_ru(today))
'''Task 9.5.18'''
# def sourcetemplate(url):
#     def agr(**kwarg):
#         res = url
#         if len(kwarg) == 0:
#             return res
#         else:
#             res += '?'
#             for key in sorted(kwarg.keys()):
#                 res += f'{key}={kwarg[key]}&'
#
#         return res[:-1]
#     return agr
#
# url = 'https://stepik.org/lesson/651459/step/14'
# load = sourcetemplate(url)
# print(load(thread='solutions', unit=648165))
'''Task 9.5.17'''
# def generator_square_polynom(a, b, c):
#     return lambda x: a * x**2 + x * b + c
#
# f = generator_square_polynom(26, 83, 22)
# print(f(55))

'''Task 9.5.16'''
# def power(degree):
#     return lambda x: x**degree
#
# result = power(4)(2)
# print(result)
'''Task 9.4.18'''
# def remove_marks(text, marks):
#     remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1
#     return ''.join(filter(lambda x: x not in marks, text))
#
#
# marks = '.,!?'
# text = 'Are you listening? Meet my family! There are my parents, my brother and me.'
#
# for mark in marks:
#     print(remove_marks(text, mark))
#
# print(remove_marks.count)
'''Task 9.4.17'''
# def polynom(x):
#     res = x**2 + 1
#     polynom.__dict__.setdefault('values', set())
#     polynom.values.add(res)
#     return res
#
#
# polynom(1)
# polynom(2)
# polynom(3)
#
# print(*sorted(polynom.values))

'''Task 9.4.12'''
# def change_print(*args, sep=' ', end='\n'):
#     res = list()
#     for el in args:
#         if type(el) == str:
#             res.append(str(el).upper())
#         else:
#             res.append(str(el))
#     old_print(*res, sep = sep.upper(), end = end.upper())
#
# old_print = print
# print  = change_print


'''Task 9.4.11'''
# def numbers_sum(elems):
#     '''Принимает список и возвращает сумму его чисел (int, float),
# игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
#     return sum(filter(lambda x: type(x) in (int, float), elems))
#
# print(numbers_sum.__doc__)
'''Task 9.3.18'''
#import string
#моё:
# def verification(login, password, success, failure):
#     passwd = list(password)
#
#     if any(filter(lambda x: x.isalpha, passwd)):
#         if any(filter(lambda x: x in string.ascii_uppercase, passwd)):
#             if any(filter(lambda x: x in string.ascii_lowercase, passwd)):
#                 if any(filter(lambda x: x.isdigit, passwd)):
#                     success(login)
#                 else:
#                     failure(login, 'в пароле нет ни одной цифры')
#             else:
#                 failure(login, 'в пароле нет ни одной строчной буквы')
#         else:
#             failure(login, 'в пароле нет ни одной заглавной буквы')
#     else:
#         failure(login, 'в пароле нет ни одной буквы')
#
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', '797777777777', success, failure)


# Нормальное:
#
# def verification(login, password, success, failure):
#     vd = {str.isalpha: 'в пароле нет ни одной буквы',
#           str.islower: 'в пароле нет ни одной строчной буквы',
#           str.isupper: 'в пароле нет ни одной заглавной буквы',
#           str.isdigit: 'в пароле нет ни одной цифры'}
#     for f in vd:
#         if not any(f(i) for i in password):
#             return failure(login, vd[f])
#     success(login)


'''Task 9.3.17'''
# def print_operation_table(operation, rows, cols):
#     matrix = [[operation(i,j) for j in range(1, cols + 1)] for i in range(1, rows + 1)]
#     for row in matrix:
#         for el in row:
#             print(str(el).ljust(3), end=' ')
#         print()

'''Task 9.3.16'''
#
# fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
# print(fib(5))


'''Task 9.3.15'''

# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита',
#          'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион',
#          'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей',
#          'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара',
#          'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья',
#          'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор',
#          'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина',
#          'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия',
#          'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана',
#          'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон',
#          'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
#
# print(*sorted(map(str.capitalize, (filter(lambda x: x[0].upper() in ('А', 'М') and len(x) > 4, names)))))


'''Task 9.3.14'''
# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223,
#            4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217,
#            -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299,
#            3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225,
#            -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741,
#            -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304,
#            4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62,
#            -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512,
#            756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]
#
#
# print(sum(map(lambda x: x**2, filter(lambda x: x < 100 and x % 9 == 0 and x > -100, numbers))))




'''Task 9.3.13'''
# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454,
#         -765, (3, 4), -105.10718000213546, 976, -308.96857946288094,
#         458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve',
#         112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3],
#         -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek',
#         -224, 431, 170.6353248658936, -343.0016746052049, 'number',
#         104.17133679352878, [], -353.5964777099863, 'zero', -113, 288,
#         None, -708.3036176571618]
#
# data_sort = filter(lambda x: type(x) == int or type(x) == float, data)
# data_sort_part2 = list(map(lambda x: int(x) if type(x) == float else x, data_sort))
# for el in data_sort_part2:
#     print(el)
#
#
# Вот как надо
# print(*map(int, filter(lambda x: type(x) in (int,float),data)), sep='\n')

'''Task 9.2.22'''

# new_func = input()
# a,b = map(int, input().split())
# res = [eval(new_func) for x in range(a, b+1)]
# print(f'Минимальное значение функции {new_func} на отрезке [{a}; {b}] равно {min(res)}')
# print(f'Максимальное значение функции {new_func} на отрезке [{a}; {b}] равно {max(res)}')


'''Task 9.2.21'''
# import sys
# print(max([eval(el) for el in sys.stdin]))

'''Task 9.2.20'''
# n = eval(input())
# print(eval({list: 'n[-1]', tuple: 'n[0]', set: 'len(n)'}[type(n)]))


# n = input()
# new_object = eval(n)
#
# if isinstance(new_object, list):
#     print(new_object[-1])
# elif isinstance(new_object, tuple):
#     print(new_object[0])
# else:
#     print(len(new_object))


'''Task 9.2.8'''
# def hash_as_key(objects):
#     dict_hash = dict()
#     for el in objects:
#         if hash(el) not in dict_hash:
#             dict_hash[hash(el)] = el
#         elif hash(el) in dict_hash and type(dict_hash[hash(el)]) != list:
#             dict_hash[hash(el)] = [dict_hash[hash(el)]]
#             dict_hash[hash(el)].append(el)
#         else:
#             dict_hash[hash(el)].append(el)
#     return dict_hash
#
# data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]
#
# print(hash_as_key(data))

'''Task 9.1.16'''
# n = sorted(input())
#
# a = list(filter(lambda x: x.islower(), n))
# b = list(filter(lambda x: x.isupper(), n))
# c = list(filter(lambda x: x if int(x) % 2 != 0 else 0, filter(lambda x: x.isdigit(), n)))
# d = list(filter(lambda x: x if int(x) % 2 == 0 else 0, filter(lambda x: x.isdigit(), n)))
# print(''.join(a) + ''.join(b) + ''.join(c) + ''.join(d))

'''Task 9.1.15'''

# def zip_longest(*args, fill=None):
#
#     res = []
#     max_len = max(map(len, args))
#     for el in args:
#         if len(el) != max_len:
#             el.extend([fill] * (max_len - len(el)))
#
#     for i in zip(*args):
#         res.append(i)
#     return res

'''Task 9.1.14'''
# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
#
# for el in sorted(zip(names, budgets, box_offices), key=lambda x: x[0]):
#     print(f'{el[0]}: {el[2] - el[1]}$')
#

'''Task 9.1.13'''
# def my_pow(number):
#     return sum(map(lambda x: int(x[1])**x[0], enumerate(list(str(number)), 1)))

'''Task 9.1.12'''
# numbers = [-7724, 5023, 3197, -102, -4129, -880,
#            5857, -2866, -8913, 1195, 9809, 5347,
#            -8071, 903, 3030, -4347, -3354, 1024,
#            8670, 4210, -5228, 8900, 4823, -2002,
#            4900, 9520, -3658, 1104, -9554, 3064,
#            9632, -8701, 3384, 4370, 2034, 7822,
#            -9694, 3347, 7440, -8459, 3238, -5193,
#            -3381, 5281, 9022, 5559, 7593, -6540,
#            -6204, -2483, 8729, 5810, -8254, -9846,
#            -1801, 4882, 3838, -3140, 7609, -3325,
#            6026, 2994, -1677, 1266, -1893, -4408,
#            -5722, -2841, 9812, 5837, -7474, 4624,
#            -664, 6998, 7888, -971, 8810, 3812,
#            -5396, 2593, 512, -4634, 9735, -3062,
#            9031, -9300, 3657, 6332, 7552, 8125,
#            -725, 4392, 1727, 8194, -2828, -4314,
#            -8967, -7912, -1363, -5957]
#
# print(max(list(enumerate(numbers)),key=lambda x: x[1])[0])
'''Task 9.1.11'''
# def custom_isinstance(objects, typeinfo):
#     return sum(map(lambda x: 1 if isinstance(x, typeinfo) else 0, objects))

'''Task 9.1.10'''
# def is_greater(lists, number):
#     return any(map(lambda x: True if sum(x) > number else False, lists))

'''Task 9.1.9'''
# def non_negative_even(numbers):
#     return all(map(lambda x: True if x >= 0 and x % 2 == 0 else False, numbers))
#
#
# print(non_negative_even([0, 2, 4, 8, 16]))
# print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
# print(non_negative_even([0, 0, 0, 0, 0]))
'''Task 9.1.8'''

# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
#
# res = min(films, key=lambda x: sum(films[x].values()))
# print(res)

'''Task 9.1.5'''
# def convert(number):
#     func_list = [str(bin(number)), str(oct(number)), str(hex(number)).upper()]
#     res = []
#     for el in func_list:
#         if el[0] == '-':
#             res.append(el[0] + el[3:])
#         else:
#             res.append(el[2:])
#     return tuple(res)

'''Task 9.1.4'''
# import string
# for el in string.ascii_lowercase:
#     print(el)