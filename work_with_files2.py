'''Task16'''
# import csv
# with open('C:/new/titanic.csv', 'r', encoding='utf') as file:
#     passengers = csv.reader(file, delimiter=';')
#     next(passengers)
#     survivors_list = sorted(filter(lambda x: x[0] == '1', passengers), key=lambda x: x[2], reverse=True)
#     young_survivors = filter(lambda x: float(x[-1]) < 18, survivors_list)
#     for el in young_survivors:
#         print(el[1])

'''Task15'''
# import csv
# with open('C:/new/wifi.csv', 'r', encoding='utf-8') as file:
#     wifi = csv.reader(file, delimiter=';')
#     next(wifi)
#     dict_wifi = {}
#     for el in wifi:
#         if dict_wifi.get(el[1]):
#             dict_wifi[el[1]] += int(el[-1])
#         else:
#             dict_wifi[el[1]] = int(el[-1])
#     dict_wifi = sorted(sorted(dict_wifi.items()), key = lambda x: x[1], reverse=True)
#     for el in dict_wifi:
#         print(f'{el[0]}: {el[1]}')
'''Task14'''
# import csv
# with open('C:/new/data.csv', 'r', encoding='utf-8') as file:
#     emails = csv.DictReader(file, delimiter=',')
#     email_list = []
#     for el in emails:
#         for k in el.keys():
#             if k == 'email':
#                 email_list.append(el[k])
#     dict_email = {}
#     for el in email_list:
#         dict_email[el[el.index('@')+1:]] = dict_email.get(el[el.index('@')+1:], 0) + 1
#     dict_email = sorted(sorted(dict_email.items()), key = lambda x: x[1])
# with open('C:/new/domain_usage.csv', 'w', encoding = 'utf-8') as output:
#     email_output = csv.DictWriter(output, fieldnames = ['domain', 'count'])
#     email_output.writeheader()
#     for k,v in dict_email:
#         email_output.writerow({'domain':k,'count':v})


'''Task13'''
# import csv
# def csv_columns(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = csv.DictReader(file, delimiter=',')
#         dict_data = {}
#         for el in data:
#             for k,v in el.items():
#                 if dict_data.get(k):
#                     dict_data[k].append(v)
#                 else:
#                     dict_data[k] = [v]
#
#     return dict_data
#
# print(csv_columns('C:/new/deniro.csv'))
'''Task12'''
# import csv
# n = int(input())
# with open('C:/new/deniro.csv', 'r', encoding='utf-8') as file:
#     columns = csv.reader(file, delimiter=',')
#     for el in sorted(columns, key=lambda x: int(x[n-1]) if x[n-1].isdigit() else x[n-1]):
#         print(','.join(el))

'''Task11'''
# import csv
#
# with open('C:/new/salary_data.csv', 'r', encoding='utf-8') as file:
#     fork = csv.reader(file,delimiter=';')
#     next(fork)
#     dict_company = {}
#
#     for k, v in fork:
#         if dict_company.get(k):
#             dict_company[k].append(int(v))
#         else:
#             dict_company[k] = [int(v)]
#
# for k in dict_company.keys():
#     dict_company[k] = round(sum(dict_company[k]) / len(dict_company[k]), 0)
#
# for el in sorted(sorted(dict_company.items()), key=lambda x: x[1]):
#     print(el[0])

'''Task10'''
#import csv
#
# with open('C:/new/sales.csv', 'r', encoding='utf-8') as file:
#     sale = csv.DictReader(file, delimiter=';')
#     for row in sale:
#         if int(row['old_price']) > int(row['new_price']):
#             print(row['name'])
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