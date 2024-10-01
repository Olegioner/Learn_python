






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