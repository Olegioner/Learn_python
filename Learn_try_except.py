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
