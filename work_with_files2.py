'''Task9'''
# import sys
# num_list = [int(i) for i in sys.stdin]
# arf = set()
# geom = set()
# for i in range(1, len(num_list)):
#     arf.add(num_list[i] - num_list[i-1])
#     geom.add(num_list[i] / num_list[i - 1])
# if len(arf) == 1:
#     print('Арифметическая прогрессия')
# elif len(geom) == 1:
#     print('Геометрическая прогрессия')
# else:
#     print('Не прогрессия')


'''Task8'''
# import sys
# from datetime import datetime
# list_date = [datetime.strptime(el.strip(), '%d.%m.%Y') for el in sys.stdin]
# dates = set(list_date)
# sort = sorted(dates)
# sort_reverse = sorted(dates, reverse=True)
#if list_date == sort:
#    print('ASC')
#elif list_date == sort_reverse:
#    print('DESC')
#else:
#    print('MIX')

'''Task7'''
# import sys
# list_news = [[el.strip() for el in row.split(' / ')]for row in sys.stdin]
# tag = ''.join(list_news.pop(-1))
# news = list(filter(lambda x: x[1] == tag, list_news))
# s_news = sorted(sorted(news, key=lambda x: x[0][0]), key=lambda x: float(x[2]))
# for el in s_news:
#     print(el[0])
'''Task6'''
# import sys
# list_command = [el for el in sys.stdin]
# list_comm = list(map(lambda x: '' if x.strip().startswith("#") else x, list_command))
# for el in list_comm:
#     print(el, end='')

'''Task5'''
# import sys
# list_command = [el.strip() for el in sys.stdin]
# list_comm = list(filter(lambda x: x[0] == '#', list_command))
# print(len(list_comm))

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