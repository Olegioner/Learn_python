'''Task 7'''
# n = int(input())
# z1,z2 = complex(input()), complex(input())
# res = z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n + 1)
# print(res)

'''Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число
с наибольшим модулем и сам модуль числа на отдельных строках.'''
# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# dict_num = {abs(el) : el for el in numbers}
# m = max(dict_num)
# print(dict_num[m])
# print(m)
'''Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их сумму, разность и произведение.'''
# a,b  = complex(input()), complex(input())
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')


'''На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания
все несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.'''
# from fractions import Fraction
# n = int(input())
# set_fraction = set()
# [[set_fraction.add(Fraction(i, j)) for j in range(1, n+1) if 0 < (i / j) < 1] for i in range(1, n+1)]
# for el in sorted(set_fraction):
#     print(el)


'''На вход программе подается натуральное число n. Напишите программу, которая находит наибольшую
правильную несократимую дробь с суммой числителя и знаменателя равной n.'''
# from fractions import Fraction
# n = int(input())
# list_fractions = [[Fraction(i,j) for j in range(1,n+1)] for i in range(1,n+1)]
# list_f = []
# for i in range(len(list_fractions)):
#     for j in range(len(list_fractions[i])):
#         if list_fractions[i][j].numerator + list_fractions[i][j].denominator == n:
#             if list_fractions[i][j].numerator < list_fractions[i][j].denominator:
#                 list_f.append(list_fractions[i][j])
# print(max(list_f))



'''Task 6'''
# from fractions import Fraction
# from math import factorial
# n = int(input())
# sm = 0
# for i in range(1, n+1):
#     sm += Fraction(1, factorial(i))
# print(sm)

'''Task 5'''
# from fractions import Fraction
# n = int(input())
# sm = 0
# for i in range(1, n+1):
#     sm += Fraction(1, i**2)
# print(sm)


'''Task 4'''
# from fractions import Fraction as F
# a = input()
# b = input()
# af = F(a)
# bf = F(b)
# print(f'{a} + {b} = {af + bf}')
# print(f'{a} - {b} = {af - bf}')
# print(f'{a} * {b} = {af * bf}')
# print(f'{a} / {b} = {af / bf}')


'''Task 3'''
# from fractions import Fraction
# print(Fraction(int(input()), int(input())))

'''На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение выражения: '''
# from decimal import Decimal as D
# d = D(input())
# res =  d.exp() + d.ln() + d.log10() + d.sqrt()
# print(res)


'''Task 2'''
# from decimal import *
# num = Decimal(input())
# num_first = [Decimal(el) for el in list(str(abs(num // 1)))]
# print(max(max(num.as_tuple().digits), max(num_first)) + min(min(num.as_tuple().digits), min(num_first)))


'''Task 1'''
# from decimal import Decimal
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
# list_s = [Decimal(el) for el in s.split()]
#
# sm = sum(list_s)
# set_max = set()
# while len(set_max) != 5:
#     mx = max(list_s)
#     ind = list_s.index(mx)
#     set_max.add(list_s.pop(ind))
#
# print(sm)
# print(*sorted(set_max, reverse= True))

# from decimal import *
#
# num = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
#
# if num == 0:
#     print('YES')
# else:
#     print('NO')
# print(num)