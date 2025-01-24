'''Task 4.6.15'''
# import pickle
#
# filename = input()
# n = int(input())
#
# with open(filename, 'rb') as file:
#     data = pickle.load(file)
#
# if type(data) == dict:
#     cur = sum(list(filter(lambda x: type(x) == int, data.keys())))
# elif type(data) == list:
#     sort_list = list(filter(lambda x: type(x) == int, data))
#     if sort_list != []:
#         cur = min(sort_list) * max(sort_list)
#     else:
#         cur = 0
#
# if n == cur:
#     print('Контрольные суммы совпадают')
# else:
#     print('Контрольные суммы не совпадают')


'''Task 4.6.14'''
# import pickle
#
# def filter_dump(filename, objects, typename):
#     sort_obj = list(filter(lambda x:type(x) == typename, objects))
#     with open(filename, 'wb') as file:
#         pickle.dump(sort_obj, file)
#
# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)

'''Task 4.6.13'''
# import pickle
# import sys
# def func(*args):
#     return ' '.join(args)
# with open('C:/new/func.pkl', 'wb') as file:
#     pickle.dump(func, file)
#
# with open('C:/new/func.pkl', mode='rb') as file:
#     fu = pickle.load(file)
#     arg = [el for el in sys.stdin]
#     print(fu(*arg))