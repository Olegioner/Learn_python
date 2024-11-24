'''Task4'''
# import sys
# from functools import reduce
# height_list = sorted([int(el.strip()) for el in sys.stdin])
# if len(height_list) == 0:
#     print('нет учеников')
# else:
#     average_height = reduce(lambda x, y: x + y, height_list) / len(height_list)
#     print(f'Рост самого низкого ученика: {height_list[0]}')
#     print(f'Рост самого высокого ученика: {height_list[-1]}')
#     print(f'Средний рост: {average_height}')
'''Task3'''
# import sys
# step_list = [int(el) for el in sys.stdin]
# win = []
# for i in range(len(step_list)):
#     if i % 2 == 0:
#         win.append('Анри')
#     else:
#         win.append('Дима')
# if step_list[-1] % 2 == 0:
#     print(win[-1])
# else:
#     print(win[-2])


'''Task2'''
# import sys
# from datetime import datetime
#
# date_list = [datetime.strptime(el.strip(), '%Y-%m-%d') for el in sys.stdin]
#
# date_list = sorted(date_list)
# count_day = (date_list[-1] - date_list[0]).days
# print(count_day)




'''Task1'''
# import sys
# a = [el.strip() for el in sys.stdin]
# for el in a:
#     print(el[::-1])