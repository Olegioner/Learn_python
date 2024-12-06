'''Task4.4.16'''
# import json
# with open('C:/new/food_services.json', 'r', encoding='utf-8') as file:
#     food_services = json.load(file)
#     dist_rest = {}
#
#     rest_list = sorted(food_services, key=lambda x: x['SeatsCount'])
#     for el in rest_list:
#         dist_rest.setdefault(el['TypeObject'], {})
#         dist_rest[el['TypeObject']][el['Name']] = el['SeatsCount']
#
#     dist_rest = dict(sorted(dist_rest.items(), key=lambda x: x[0]))
#
#     for key, value in dist_rest.items():
#         v = sorted(value.items(), key=lambda x: x[1])[-1]
#         print(f'{key}: {v[0]}, {v[1]}')
'''Task4.4.15'''
# import json
# with open('C:/new/food_services.json', 'r', encoding='utf-8') as file:
#     food_services = json.load(file)
#     dict_district = {}
#     dict_restaurant = {}
#     for el in food_services:
#         dict_district[el['District']] = dict_district.get(el['District'], 0) + 1
#         dict_restaurant[el['OperatingCompany']] = dict_restaurant.get(el['OperatingCompany'], 0) + 1
#     max_distr = (sorted(dict_district.items(), key=lambda x: x[1]))[-1]
#     max_rest = (sorted(dict_restaurant.items(), key=lambda x: x[1]))[-2]
#     print(f'{max_distr[0]}: {max_distr[1]}')
#     print(f'{max_rest[0]}: {max_rest[1]}')
'''Task4.4.14'''
# import csv
# import json
# from datetime import datetime
# with open('C:/new/exam_results.csv' , 'r', encoding='utf-8') as file:
#     students_score = csv.DictReader(file, delimiter=',')
#     header_list = []
#     for stud in students_score:
#         for key in stud.keys():
#             if key == 'score':
#                 key = 'best_score'
#             header_list.append(key)
#         break
#     stud_list = sorted(students_score, key=lambda x:datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S'))
# stud_list = sorted(stud_list, key=lambda x: int(x['score']))
# dict_stud = {}
# for el in stud_list:
#     el['score'] = int(el['score'])
#     dict_stud[f"{el['surname']} {el['name']}"] = dict(zip(header_list, el.values()))
#
# sort_dict_stud = sorted(dict_stud.values(), key=lambda x: x['email'])
#
# with open('C:/new/best_scores.json', 'w', encoding='utf-8') as output:
#     json.dump(sort_dict_stud, output, indent=3)

'''Task4.4.13'''
# import json
# with open('C:/new/pools.json', 'r', encoding='utf-8') as file:
#     pools = json.load(file)
#     sort_pools = []
#     for el in pools:
#         start = int(el['WorkingHoursSummer']['Понедельник'][:2])
#         stop = int(el['WorkingHoursSummer']['Понедельник'][6:8])
#         length_pool = el['DimensionsSummer']['Length']
#         width_pool = el['DimensionsSummer']['Width']
#         if start <= 10 and stop >= 12:
#             sort_pools.append([el['Address'], length_pool, width_pool])
# sort_pools = sorted(sorted(sort_pools, key=lambda x: x[2]), key=lambda x: x[1])
# print(f'{sort_pools[-1][1]}x{sort_pools[-1][2]}')
# print(sort_pools[-1][0])

'''Task4.4.12'''
# import json
# import csv
# with open('C:/new/students.json', 'r', encoding='utf-8') as file:
#     students = json.load(file)
#     sorted_students = []
#     for student in students:
#         if student['age'] >= 18 and student['progress'] >= 75:
#             sorted_students.append([student['name'], student['phone']])
#     sorted_students = sorted(sorted_students, key=lambda x: x[0])
#     header_list = ['name', 'phone']
# with open('C:/new/data.csv', 'w', encoding='utf-8') as output:
#     sort_stud = csv.DictWriter(output, delimiter=',', fieldnames=header_list)
#     sort_stud.writeheader()
#     for name in sorted_students:
#         sort_stud.writerow(dict(zip(header_list, name)))


'''Task4.4.11'''
# import json
# import csv
# with (open('C:/new/playgrounds.csv', 'r', encoding='utf-8') as file):
#     playgrounds = csv.DictReader(file, delimiter=';')
#     dict_adm_area = {}
#     for area in playgrounds:
#         dict_adm_area.setdefault(area['AdmArea'], {}).setdefault(area['District'],[]).append(area['Address'])
# with open('C:/new/addresses.json', 'w', encoding='utf-8') as output:
#     json.dump(dict_adm_area, output, indent=3, ensure_ascii=False)


'''Task4.4.10'''
# import json
# with open('C:/new/countries.json', 'r', encoding='utf-8') as file:
#     countries = json.load(file)
#     religions_dict = {}
#     for country in countries:
#         key = country['religion']
#         value = country['country']
#         if religions_dict.get(key):
#             religions_dict[key].append(value)
#         else:
#             religions_dict[key] = [value]
# with open('C:/new/religion.json', 'w', encoding='utf-8') as output:
#     json.dump(religions_dict, output)

'''Task24'''
# import json
# with open('C:/new/people.json', 'r', encoding='utf-8') as file:
#     people = json.load(file)
#     key_list = []
#     for person in people:
#         for key in person.keys():
#             if key not in key_list:
#                 key_list.append(key)
#     for person in people:
#         for key in key_list:
#             if key not in person:
#                 person.setdefault(key, None)
# with open('C:/new/updated_people.json', 'w', encoding='utf-8') as output:
#     json.dump(people, output)


'''Task23'''
# import json
# with (open('C:/new/data1.json', 'r', encoding='utf-8') as data1,
#       open('C:/new/data2.json', 'r', encoding='utf-8') as data2):
#     data_dict = json.load(data1)
#     data_dict.update(json.load(data2))
# with open('C:/new/data_merge.json', 'w', encoding='utf-8') as output:
#     json.dump(data_dict, output)

'''Task22'''
# import json
# with open('C:/new/data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
# list_data = []
# for el in data:
#     if type(el) == str:
#         list_data.append(el + '!')
#     if type(el) == int:
#         list_data.append(el + 1)
#     if type(el) == bool:
#         list_data.append(not el)
#     if type(el) == list:
#         list_data.append(el + el)
#     if type(el) == dict:
#         el.setdefault("newkey", None)
#         list_data.append(el)
# with open('C:/new/updated_data.json', 'w', encoding='utf-8') as output:
#     json.dump(list_data, output)


'''Task21'''
# import sys
# import json
#
# json_list = ''.join([el for el in sys.stdin])
# json_dict = json.loads(json_list)
# for key, value in json_dict.items():
#     if type(value) == list:
#         print(f'{key}: {", ".join(str(el) for el in value])}')
#     else:
#         print(f'{key}: {value}')


'''Task20'''
# import csv
# with open('C:/new/prices.csv', 'r', encoding='utf-8') as file:
#     prices = csv.DictReader(file, delimiter=';')
#     dict_low_prices = {}
#     for el in prices:
#         dict_low_prices[el['Магазин']] = min(el.items(), key = lambda x: int(x[1]) if x[1].isdigit() else 999)
#     low_price = (min(dict_low_prices.values(), key = lambda x: int(x[1])))[1]
#
#     list_low_price = {}
#     for key, value in dict_low_prices.items():
#         if value[1] == low_price:
#             list_low_price[key] = value[0]
#
#     list_low_price = sorted(sorted(list_low_price.items(), key = lambda x: x[1]), key = lambda x: x[0])
#     print(f'{list_low_price[-1][1]}: {list_low_price[-1][0]}')


'''Task19'''
# import csv
# with (open('C:/new/student_counts.csv', 'r', encoding='utf-8') as file,
#       open('C:/new/sorted_student_counts.csv', 'w') as output):
#     stud = csv.DictReader(file, delimiter=',')
#     year_list = []
#     for el in stud:
#         el = dict(sorted(el.items(), key=lambda x: x[0][-1]))
#         el = dict(sorted(el.items(), key=lambda x: int(x[0][:x[0].index('-')]) if x[0] != 'year' else 1))
#         year_list.append(el)
#
#     stud_writer = csv.DictWriter(output, delimiter=',', fieldnames=year_list[0].keys())
#     stud_writer.writeheader()
#     for el in year_list:
#         stud_writer.writerow(el)

'''Task18'''
# import csv
#
# def condense_csv(filename, id_name):
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = [[el.strip() for el in row.split(',')] for row in file.readlines()]
#     dict_data = {}
#     header_list = []
#     for el in data:
#         obj, key, value = el
#         if obj not in dict_data:
#             dict_data[obj] = {id_name: obj}
#         dict_data[obj][key] = value
#     for el in dict_data.values():
#        header_list.extend(el)
#        break
#
#     with open('C:/new/condensed.csv', 'w', encoding='utf-8') as output:
#         writer = csv.DictWriter(output, delimiter=',', fieldnames=header_list)
#         writer.writeheader()
#         for el in dict_data.values():
#             writer.writerow(el)


'''Task17'''
# import csv
# from datetime import datetime
#
# with open('C:/new/name_log.csv', 'r', encoding='utf-8') as file:
#     log = list(csv.reader(file, delimiter=','))
#     head_names = log.pop(0)
#     sorted_log = sorted(log, key=lambda x: datetime.strptime(x[-1], '%d/%m/%Y %H:%M'))
#
# dict_log = {el[1] : el for el in sorted_log}
# new_log = sorted(dict_log.values(), key=lambda x: x[1])
#
# with open('C:/new/new_name_log.csv' , 'w', encoding='utf-8') as output:
#     log_output = csv.DictWriter(output, fieldnames=head_names)
#     log_output.writeheader()
#     for el in new_log:
#         log_output.writerow(dict(zip(head_names, el)))

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