'''Task 7.5.8 and 7.5.9'''
# import sys
#
#
# class PasswordError(Exception):
#     pass
#
# class LengthError(PasswordError):
#     pass
#
# class LetterError(PasswordError):
#     pass
#
# class DigitError(PasswordError):
#     pass
#
#
# def is_good_password(string):
#     try:
#         if len(string) < 9:
#             raise LengthError('LengthError')
#         elif string.isdigit()or (string.lower() == string or string.upper() == string):
#             raise LetterError('LetterError')
#         elif string.isalpha():
#             raise DigitError('DigitError')
#         else:
#             return True
#     except LengthError as l:
#         print(l)
#     except LetterError as let:
#         print(let)
#     except DigitError as d:
#         print(d)
#
#
#
# for el in sys.stdin:
#     if is_good_password(el.strip()):
#         print('Success!')
#         break




'''Task 7.5.7'''
# def is_good_password(string):
#     if all(
#         (len(string) >= 9,
#          any(char.islower() for char in string),
#          any(char.isupper() for char in string),
#          any(char.isdigit() for char in string))
#             ):
#         return True
#     else:
#         return False

'''Task 7.4.20'''
# import json
#
# try:
#     with open(input(), 'r', encoding='utf-8') as file:
#         try:
#             json_file = json.load(file)
#             print(json_file)
#         except json.JSONDecodeError:
#             print('Ошибка при десериализации')
# except FileNotFoundError:
#     print('Файл не найден')

'''Task 7.4.19'''

# def get_id(names, name):
#     if type(name) == str:
#         if name.isalpha() and name.istitle():
#             names.append(name)
#             return len(names)
#         else:
#             raise ValueError('Имя не является корректным')
#     else:
#         raise TypeError('Имя не является строкой')

'''Task 7.4.18'''
# def get_weekday(number):
#     week_days = {1: 'Понедельник', 2: 'Вторник',
#                  3: 'Среда', 4: 'Четверг',
#                  5: 'Пятница', 6: 'Суббота',
#                  7: 'Воскресенье'}
#     if type(number) != int:
#         raise TypeError('Аргумент не является целым числом')
#     elif number not in week_days.keys():
#         raise ValueError('Аргумент не принадлежит требуемому диапазону')
#     else:
#         return week_days[number]

'''Task 7.3.22'''
# try:
#     with open(input(), 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('Файл не найден')

'''Task 7.3.21'''

# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key].append(element)
#     except KeyError:
#         data.setdefault(key, [element])

'''Task 7.3.20'''
# months_name = {1: 'January', 2: 'February', 3: 'March',
#                4: 'April', 5: 'May', 6: 'June',
#                7: 'July', 8: 'August', 9: 'September',
#                10: 'October', 11: 'November', 12: 'December'}
# try:
#     months_num = int(input())
#     try:
#         print(months_name[months_num])
#     except:
#         print('Введено число из недопустимого диапазона')
# except:
#     print('Введено некорректное значение')
'''Task 7.2.23'''
# import sys
#
# list_values = [el.strip() for el in sys.stdin]
# list_num = []
# list_str = []
# for value in list_values:
#     try:
#         if value.isdigit():
#             list_num.append(int(value))
#         else:
#             list_num.append(float(value))
#     except:
#         list_str.append(value)
#
#
# print(sum(list_num))
# print(len(list_str))
