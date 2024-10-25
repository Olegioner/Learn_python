
'''Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.'''
# from functools import reduce
# def pretty_print(data, side='-',delimiter='|'):
#     output = reduce(lambda x,y : x + y, map(lambda x:' ' + str(x) + ' ' + delimiter, data), delimiter)
#     print(reduce(lambda x, y: x+y, side*(len(output)-2), ' '))
#     print(output)
#     print(reduce(lambda x, y: x+y, side*(len(output)-2), ' '))
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

'''Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в соответствии
с десятичным представлением.'''

# list_ip = [input() for _ in range(int(input()))]
#
# def sort_ip(ip_zip):
#     ip = [int(el) for el in ip_zip.split('.')]
#     res = 0
#     for i in range(len(ip)):
#         res += ip[i] * 256**(len(ip) - 1 - i)
#     return res
#
#
# print(*sorted(list_ip, key=sort_ip), sep='\n')



'''Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке)
в порядке возрастания их гематрии. Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке.'''

# list_words = sorted([input() for _ in range(int(input()))])
#
# def gematria(text):
#     res = 0
#     for i in range(len(text)):
#         res += (ord(text.upper()[i]) - ord('A'))
#     return res
# print(*sorted(list_words, key=gematria), sep='\n')


'''Дана строка из разделенных пробелами слов в разных регистрах. Напишите программу, которая отсортирует
слова независимо от регистра, а затем выведет их. Отсортированные слова должны выводиться
на печать в исходном регистре, в каком переданы программе на вход.'''

# print(*sorted(input().split(), key=lambda x: x.lower()))


'''Дан список numbers, состоящий из кортежей. Допишите пропущенную часть программы,
чтобы список sorted_numbers был упорядочен по убыванию среднего арифметического элементов кортежей списка numbers.'''

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32),
#            (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23),
#            (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)
#
# print(sorted_numbers)

'''Дан список целых чисел numbers. Допишите код после оператора распаковки (*),
для удаления из списка всех чисел-палиндромов и печати результата на одной строке через пробел.'''

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))


'''Дан список слов words. Допишите код после оператора распаковки (*),
который оборачивает в двойные кавычки все элементы списка words,
а затем печатает результат на одной строке через пробел.'''
# words = 'the world is mine take a look what you have started'.split()
#
# print(*list(map(lambda x: f'"{x}"', words)))

'''Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce()'''
# from functools import reduce
# def product_of_odds(data):
#     return reduce(lambda x,y: x * y, filter(lambda x: x % 2 == 1, data), 1)

'''Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую
их в одну строку через разделитель (sep). Если разделитель не задан, им служит пробел.'''
# def concat(*args, sep=' '):
#     args_str = []
#     for el in args:
#         args_str.append(str(el))
#     return sep.join(args_str)
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
