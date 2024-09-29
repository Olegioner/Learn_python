'''Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа π.'''

from random import uniform
s0 = 4
k = 0
n = 10**6
for _ in range(n):
    x, y = uniform(-1, 1), uniform(-1, 1)
    if x**2 + y**2 <= 1:
        k += 1
print((k/n)*s0)



'''Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств'''

# from random import uniform
# s0 = 16
# k = 0
# n = 10**6
# for _ in range(n):
#     x, y = uniform(-2, 2), uniform(-2, 2)
#     if x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <=2:
#         k+= 1
# print((k/n)*s0)


'''Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой'''
# import string
# from random import sample,shuffle,choice
# n, m = int(input()), int(input())
# list_up_letter = [el for el in list(string.ascii_uppercase) if el not in 'IO']
# list_low_letter = [el for el in list(string.ascii_lowercase) if el not in 'lo']
# list_digit = [el for el in list(string.digits) if el not in '10']
# list_all = [el for el in list(string.ascii_letters + string.digits) if el not in 'Il1oO0']
# shuffle(list_all)
#
# for i in range(n):
#     passwd = [choice(i) for i in (list_up_letter, list_low_letter, list_digit)] + [choice(list_all) for _ in range(3, m)]
#     shuffle(passwd)
#     print(''.join(passwd))


'''Напишите программу, которая случайным образом назначает каждому ученику его тайного друга,
который будет вместе с ним решать задачи по программированию.'''
# from random import choice,shuffle
# n = int(input())
# dict_students = {i : input() for i in range(n)}
# list_ind = [i for i in range(n)]
# list_friends = list_ind.copy()
# for i in range(n):
#     ind = choice(list_ind[:i]+list_ind[i+1:])
#     print(f'{dict_students[i]} - {dict_students[ind]}')
#     list_ind.pop(list_ind.index(ind))






'''Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.'''
# from random import randint, choice
# # Получаем множество из 25 уникальных чисел
# set_num = set()
# while len(set_num) != 25:
#     set_num.add(randint(1,75))
# # Строим матрицу на основе ранее созданного множества
# matrix_list = list(set_num)
# matrix = [[matrix_list.pop(matrix_list.index(choice(matrix_list))) for _ in range(5)] for _ in range(5)]
# matrix[2][2] = 0
# # Выводим карточку для бинго
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(str(matrix[i][j]).ljust(3), end= '')
#     print()


'''Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.'''
# from random import shuffle
# word = list(input())
# shuffle(word)
# anagram = ''.join(word)
#
# print(anagram)

'''Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит
их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 7 цифр;
все 100 лотерейных билетов должны быть различными.'''

# from random import randrange
# set_tickets = set()
# while len(set_tickets) != 100:
#     ticket = str(randrange(1,10))
#     for _ in range(6):
#         ticket += str(randrange(10))
#     set_tickets.add(ticket)
# for el in set_tickets:
#     print(el)



'''Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).'''
# from random import shuffle
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# for el in matrix:
#     shuffle(el)
# print(matrix)


'''Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.'''
# def generate_index():
#     import string
#     from random import choice,randrange
#     return f'{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{randrange(100)}_{randrange(100)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}'
# print(generate_index())


'''Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.'''

# def generate_ip():
#     from random import randrange
#     return f'{randrange(256)}.{randrange(256)}.{randrange(256)}.{randrange(256)}'

'''Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.'''
# from random import randrange
# set_num = set()
# while len(set_num) != 7:
#     set_num.add(randrange(1,50))
# print(*sorted(set_num))


'''Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину
пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).'''

# from random import randrange
# passwd = ''
# i = int(input())
# while i != 0:
#     p = randrange(65, 123)
#     if chr(p).isalpha():
#         passwd += chr(p)
#         i -= 1
#     else:
#         continue
# print(passwd)

'''Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 6 гранями.
Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано
на грани кубика (каждое на отдельной строке).'''
# from random import randrange
# for _ in range(int(input())):
#     print(randrange(1,7))
