'''Task 26'''
'''Дни рождения в ближайшие 7 дней'''
# from datetime import datetime, timedelta
#
# p = '%d.%m.%Y'
# today = datetime.strptime(input(), p)
# today_list = [(today + timedelta(days=i)).strftime('%d.%m') for i in range(1,8)]
# employer_dict = {}
# for _ in range(int(input())):
#     fn, ln, date = input().split()
#     employer_dict[f'{fn} {ln}'] = datetime.strptime(date, p)
# birthday_list = list(filter(lambda x: employer_dict[x].strftime('%d.%m') in today_list, employer_dict))
# young = sorted(birthday_list, key=lambda x: employer_dict[x])
# print(young[-1]) if len(young) > 0 else print('Дни рождения не планируются')

'''Task 25'''
'''Одинаковые даты'''
# from datetime import datetime
# p = '%d.%m.%Y'
# date_dict = {}
# for _ in range(int(input())):
#     fn, ln, date = input().split()
#     date_dict[datetime.strptime(date, p)] = date_dict.get(datetime.strptime(date, p), 0) + 1
# list_more_date = sorted(list(filter(lambda x: date_dict[x] > 1, date_dict)))
# if len(list_more_date) == 0:
#     list_more_date =  sorted(date_dict.keys())
# for el in list_more_date:
#     print(el.strftime(p))

'''Task 24'''
'''Самые старые сотрудники'''
# from datetime import datetime
#
# employer_dict = {}
# for _ in range(int(input())):
#     fn, ln, date = input().split()
#     employer_dict[f'{fn} {ln}'] = datetime.strptime(date, '%d.%m.%Y')
# mn = min(employer_dict, key=lambda x: employer_dict[x])
# old_list = list(filter(lambda x: employer_dict[x] == employer_dict[mn], employer_dict))
# if len(old_list) > 1:
#     print(employer_dict[mn].strftime('%d.%m.%Y'), len(old_list))
# else:
#     print(employer_dict[mn].strftime('%d.%m.%Y'), mn)

'''Task 23'''
# from datetime import datetime, timedelta
# p = '%d.%m.%Y'
# start = datetime.strptime(input(), p)
# end = datetime.strptime(input(), p)
# date_list = []
#
# while start < end :
#     if (start.day + start.month) % 2 != 0:
#         break
#     start += timedelta(days=1)
#
#
# while start <= end:
#     if (start.weekday() != 0) and (start.weekday() != 3):
#         date_list.append(start)
#     start += timedelta(days=3)
#
# for d in date_list:
#     print(d.strftime(p))


'''Task 22'''
# from datetime import datetime, timedelta
#
# dict_work = {'01234' : [9, 21], '56' :  [10, 18]}
# cur_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# time_list = []
# for k in dict_work.keys():
#     if str(cur_date.weekday()) in k:
#         time_list += dict_work[k]
# if time_list[0] <= cur_date.hour < time_list[1]:
#     m = timedelta(hours=time_list[1]) - timedelta(hours=cur_date.hour, minutes=cur_date.minute)
#     print(int(m.total_seconds() // 60))
# else:
#     print('Магазин не работает')

'''Task 21'''
# from datetime import datetime, timedelta
#
# start = datetime(1, 1,13)
# stop = datetime(9999,12,31)
# dict_13 = {}
# for i in range(1, 10000):
#     for j in range(1, 13):
#         dict_13[datetime(i,j,13).isoweekday()] = dict_13.get(datetime(i,j,13).isoweekday(), 0) + 1
#
# for k in sorted(dict_13.keys()):
#     print(dict_13[k])
'''Task 20'''
# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
# p = "%H:%M"
# sum_minutes = timedelta(seconds=0)
# for el in data:
#     n = datetime.strptime(el[0], p)
#     k = datetime.strptime(el[1], p)
#     sum_minutes += k - n
# print(sum_minutes.seconds // 60)
'''Task 19'''

# from datetime import timedelta, datetime
# start = datetime.strptime(input(), "%H:%M")
# stop = datetime.strptime(input(), "%H:%M")
# while stop > start:
#     cur = start + timedelta(minutes=45)
#     if cur > stop:
#         break
#     print(f'{start.strftime("%H:%M")} - {cur.strftime("%H:%M")}')
#     start = cur + timedelta(minutes=10)

'''Task 18'''
# from datetime import datetime, timedelta
# def fill_up_missing_dates(dates):
#     dates_list= sorted(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates))
#     dates_sets = set()
#     for i in range(1, len(dates_list)):
#         cnt_day = (dates_list[i] - dates_list[i-1]).days
#         dates_sets.add(dates_list[i-1])
#         for d in range(1, cnt_day+1):
#             dates_sets.add(dates_list[i-1] + timedelta(days=d))
#     return  sorted(map(lambda x: x.strftime('%d.%m.%Y'), dates_sets))

# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
# print(fill_up_missing_dates(dates))

#Вывод['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']
'''Task 17'''
# from datetime import datetime, timedelta
# date_list = [datetime.strptime(el, '%d.%m.%Y') for el in input().split()]
# days_list = []
# for i in range(1,len(date_list)):
#     days_list.append(abs(date_list[i-1] - date_list[i]).days)
# print(days_list)
'''Task 16'''
# from datetime import datetime, timedelta
# cur_date = datetime.strptime(input(), '%d.%m.%Y')
# print(cur_date.strftime('%d.%m.%Y'))
# for i in range(10):
#     day_task = cur_date + timedelta(days=i+2)
#     cur_date = day_task
#     print(day_task.strftime('%d.%m.%Y'))

'''Task 15'''
# from datetime import timedelta, datetime
# def num_of_sundays(year):
#     first_day = datetime(year, 1,1).toordinal()
#     last_day = datetime(year, 12, 31).toordinal()
#     cnt = 0
#     for i in range(first_day, last_day+1):
#         if datetime.fromordinal(i).weekday() == 6:
#             cnt += 1
#     return cnt

'''Task 14'''
# from datetime import timedelta, time
#
# td = [int(el) for el in input().split(':')]
# cur_time = timedelta(hours=td[0], minutes=td[1], seconds=td[-1])
# after_timer = cur_time + timedelta(seconds=int(input()))
# seconds = after_timer.seconds
# a = time(seconds % 86400 // 3600, seconds % 3600 // 60, seconds % 60 // 1)
# print(a)


'''Task 13'''
# from datetime import datetime
#
# cur_date = datetime.strptime(input(), '%d.%m.%Y').toordinal()
# print((datetime.fromordinal(cur_date - 1)).strftime('%d.%m.%Y'))
# print((datetime.fromordinal(cur_date + 1)).strftime('%d.%m.%Y'))

'''Task 12'''
# from datetime import datetime
#
# def is_available_date(booked_dates, date_for_booking):
#     date_b = []
#     if len(date_for_booking) == 10:
#         date_b.append((datetime.strptime(date_for_booking, '%d.%m.%Y')).toordinal())
#     else:
#         d1, d2 = date_for_booking.split('-')
#         d1 = datetime.strptime(d1, '%d.%m.%Y').toordinal()
#         d2 = datetime.strptime(d2, '%d.%m.%Y').toordinal()
#         for i in range(d1, d2+1):
#             date_b.append(i)
#     date_block = []
#     for el in booked_dates:
#         if len(el) == 10:
#             date_block.append((datetime.strptime(el, '%d.%m.%Y')).toordinal())
#         else:
#             d1, d2 = el.split('-')
#             d1 = datetime.strptime(d1, '%d.%m.%Y').toordinal()
#             d2 = datetime.strptime(d2, '%d.%m.%Y').toordinal()
#             for i in range(d1, d2+1):
#                 date_block.append(i)
#     return all(map(lambda x: 0 if x in date_block else 1, date_b))
#
#
#
# # TEST
# assert is_available_date(['04.11.2021', '05.11.2021-09.11.2021'], '01.11.2021') == True
# assert is_available_date(['04.11.2021', '05.11.2021-09.11.2021'], '01.11.2021-04.11.2021') == False
# assert is_available_date(['04.11.2021', '05.11.2021-09.11.2021'], '06.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '12.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '09.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '15.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '17.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '22.11.2021-25.11.2021') == True
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '01.11.2021-04.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '02.11.2021-05.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '10.11.2021-14.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '03.11.2021-05.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '09.11.2021-10.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '06.11.2021-08.11.2021') == False
# assert is_available_date(['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021'], '14.11.2021-22.11.2021') == False
# assert is_available_date(['14.09.2022-14.10.2022'], '20.09.2022') == False
# assert is_available_date(['14.09.2022-14.10.2022'], '14.11.2022') == True
# assert is_available_date(['14.09.2022-14.10.2022'], '15.11.2022-16.11.2022') == True
# assert is_available_date(['14.09.2022-14.10.2022'], '14.09.2022-22.09.2022') == False
# assert is_available_date(['02.11.2021', '05.11.2021-09.11.2021'], '04.11.2021') == True
# print('TESTS_OK')

'''Task 11'''
# from datetime import datetime
# with open('C:/new/diary.txt', 'r', encoding='utf-8') as file:
#     diary = [el.strip() for el in file.readlines()]
#
# dict_diary = {}
# key = 0
# for el in diary:
#     if el == '':
#         continue
#     if el[0].isdigit():
#         key = datetime.strptime(el, '%d.%m.%Y; %H:%M')
#         dict_diary[key] = []
#         continue
#     dict_diary[key].append(el)
#
#
#
# for k,v in sorted(dict_diary.items()):
#     print(k.strftime('%d.%m.%Y; %H:%M'))
#     print(*v, sep='\n')
#     print()

'''Task 10'''
# from datetime import datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
# data_res = {}
# for k in data.keys():
#     data_res[k] = datetime.timestamp(datetime.strptime(data[k][1], '%d.%m.%Y %H:%M:%S')) - datetime.timestamp(datetime.strptime(data[k][0], '%d.%m.%Y %H:%M:%S'))
#
# key = [k for k,v in data_res.items() if v == min(data_res.values())]
# print(*key)
'''Task 9'''
# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
# date_time = [datetime.combine(d, t) for d, t in zip(dates, times)]
# print(*sorted(date_time, key=lambda x: x.second), sep='\n')
'''Task 8'''
# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
# count = len(times_of_purchases)
# for el in times_of_purchases:
#     if el.hour >= 12:
#         count -= 1
# print('До полудня') if len(times_of_purchases)/2 < count else print('После полудня')

'''Task 7'''
# from datetime import date
# def is_correct(day, month, year):
#     try:
#         cur_date = date(year, month, day)
#         return True
#     except:
#         return False
# cnt = 0
# dates = input()
# while dates != 'end':
#     day, month, year = dates.split('.')
#     if is_correct(int(day), int(month), int(year)):
#         print('Корректная')
#         cnt += 1
#     else:
#         print('Некорректная')
#     dates = input()
# print(cnt)

'''Task5'''
# from datetime import date
# def print_good_dates(dates):
#     for el in sorted(dates):
#         if el.year == 1992 and el.month + el.day == 29:
#             print(el.strftime('%B %d, %Y'))

'''Task4'''
# from datetime import date
# dates = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
# for el in dates:
#     print(el.strftime('%d/%m/%Y'))

'''Task3'''
# from datetime import date
# dates = [date.fromisoformat(input()) for _ in range(2)]
# print(min(dates).strftime('%d-%m (%Y)'))


'''Task2'''
# from datetime import date
#
# birthday = date(1992, 10, 6)
#
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%w'))



'''Task1'''
# from datetime import date, timedelta
#
# def saturdays_between_two_dates(start, end):
#     if start > end:
#         start, end = end, start
#     dates = [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end)+1)]
#     return sum(map(lambda x: 1 if x.weekday() == 5 else 0, dates))
#
#
# date1 = date(2020, 7, 26)
# date2 = date(2020, 7, 2)
#
# print(saturdays_between_two_dates(date1, date2))