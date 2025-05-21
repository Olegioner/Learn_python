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