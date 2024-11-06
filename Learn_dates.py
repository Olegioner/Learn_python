
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