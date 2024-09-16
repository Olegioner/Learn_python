'''На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.'''
# n = int(input())
# my_set = set(list(input()))
# for _ in range(n-1):
#     my_set.intersection_update(set(list(input())))
# set_sort = sorted(my_set)
# print(*set_sort)


'''На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа
в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.'''

# my_set, my_set2  = (set(int(el) for el in input().split())), (set(int(el) for el in input().split()))
# my_list = list(my_set - my_set2)
# my_list.sort()
# print(*my_list)

'''На вход программе подаются две строки текста, содержащие числа. Напишите программу,
которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.'''
# my_set, my_set2  = (set(int(el) for el in input().split())), (set(int(el) for el in input().split()))
# my_list = list(my_set & my_set2)
# my_list.sort()
# print(*my_list)




'''На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая определяет
количество чисел, которые есть как в первой строке, так и во второй.'''
# my_set = set(input().split())
# my_set2 = set(input().split())
#
# print(len(my_set & my_set2))



'''У каждой задачи на Stepik есть виджет с процентом верных решений и общим количеством решений. В последнее время
у Stepik барахлит алгоритм, обновляющий этот виджет. Помогите Stepik и напишите программу, которая будет подсчитывать,
сколько учеников решили задачу и сколько верных попыток составляет от общего числа попыток.'''
# from math import floor, ceil
#
# n = int(input())
# list_result = [input() for _ in range(n)]
# set_list = set()
# [set_list.add(el) for el in list_result]
# cnt_c = 0
# cnt_c_all = 0
# for el in set_list:
#     if 'Correct' in el:
#         cnt_c += 1
# for el in list_result:
#     if 'Correct' in el:
#         cnt_c_all += 1
# if cnt_c == 0 or n == 0:
#     print('Вы можете стать первым, кто решит эту задачу')
# else:
#     per = (cnt_c_all * 100) / n
#     if per % 1 >= 0.5:
#         per = ceil(per)
#     else:
#         per = floor(per)
#     print(f'Верно решили {cnt_c} учащихся')
#     print(f'Из всех попыток {per}% верных')





'''На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO, если не встречалось.'''
# n = [int(el) for el in input().split()]
# for i in range(len(n)):
#     if n[i] in n[:i]:
#         print('YES')
#     else:
#         print('NO')


'''Напишите программу для определения общего количества различных слов в строке текста
Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.'''

# n = input()
# my_list = [el.lower().strip('.,;:-?!') for el in n.split()]
# my_set = set()
# for el in my_list:
#     my_set.add(el)
# print(len(my_set))


'''Напишите программу для вывода общего количества уникальных
символов во всех считанных словах без учета регистра.'''
# n = int(input())
# my_list = [list(input().lower()) for el in range(n)]
# my_set = set()
# [[my_set.add(my_list[i][j]) for j in range(len(my_list[i]))] for i in range(len(my_list))]
#
# print(len(my_set))


'''Напишите программу для вывода количества уникальных
символов каждого считанного слова без учета регистра.'''
# n = int(input())
# my_set = [set(input().lower()) for el in range(n)]
# for el in my_set:
#     print(len(el))




'''На вход программе подается строка, состоящая из трех слов.
Верно ли, что для записи всех трех слов был использован один и тот же набор букв?'''
# n = input().split()
# set_1 = set(n[0])
# set_2 = set(n[1])
# set_3 = set(n[2])
#
# if set_1 == set_2 and set_2 == set_3:
#     print('YES')
# else:
#     print('NO')



'''На вход программе подаются две строки, состоящие из цифр.
Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?'''
# n = list(input())
# m = list(input())
# set_n = set(n)
# set_m = set(m)
# if set_m == set_n:
#     print('YES')
# else:
#     print('NO')


'''На вход программе подаются две строки, состоящие из цифр.
Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?'''
# n = list(input())
# m = list(input())
# my_set = set(n + m)
#
# if len(my_set) == 10:
#     print('YES')
# else:
#     print('NO')



'''На вход программе подается строка, состоящая из цифр. Необходимо определить,
верно ли, что в ее записи ни одна из цифр не повторяется?'''
# n = input()
# my_set = set(n)
# if len(n) == len(my_set):
#     print('YES')
# else:
#     print('NO')




'''На вход программе подается строка текста. Напишите программу, которая определяет количество различных символов в строке.'''
# n = input()
# my_set = set(n)
# print(len(my_set))



'''Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке,
отсортированные по убыванию (в обратном лексикографическом порядке).'''
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# fruits_sort = sorted(fruits, reverse=True)
# print(*fruits_sort, sep='\n')




'''Дополните приведенный код, чтобы он вывел сумму квадратов элементов множества numbers.'''

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# sm = 0
# for el in numbers:
#     sm += el**2
# print(sm)


'''task2'''
# n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
#
# a_b = -1 * (x - n - m)
# b_c = -1 * (y - m - k)
# c_a = -1 * (z - n - k)
# only_a_b = a_b - t
# only_b_c = b_c - t
# only_c_a = c_a - t
# one_a = n - t - only_c_a - only_a_b
# one_b = m - t - only_b_c - only_a_b
# one_c = k - t - only_b_c - only_c_a
#
# print(one_a + one_b + one_c)
#
# print(only_a_b + only_b_c + only_c_a)
#
# print(a - t - (one_a + one_b + one_c) - (only_a_b + only_b_c + only_c_a))





'''task1'''
# n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# sm = x + y + z + ((n - 0 -x) + (m - x - y) + (k - y - 0))
# print(sm)