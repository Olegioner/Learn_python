'''Task 10.2.24'''

# def get_min_max(iterable):
#     try:
#         if iterable != iter(iterable):
#             iterable = iter(iterable)
#         max_n = next(iterable)
#         min_n = max_n
#         for el in iterable:
#             if el > max_n:
#                 max_n = el
#             elif el < min_n:
#                 min_n = el
#         return min_n, max_n
#     except:
#         return None
#
#
# iterable = [6, 4, 2, 33, 19, 1]
#
# print(get_min_max(iterable))
#
# data = iter(iter(range(100_000_000)))
#
# print(get_min_max(data))
#
# iterable = iter([])
#
# print(get_min_max(iterable))

'''Task 10.2.23'''
# def starmap(func, iterable):
#
#     return map(func, *zip(*iterable))
#
# pairs = [(1, 3), (2, 5), (6, 4)]
#
# print(*starmap(lambda a, b: a + b, pairs))
'''Task 10.2.22'''
# def get_min_max(data):
#
#     if len(data) == 0:
#         return None
#     return data.index(min(data)), data.index(max(data))
#
# data = [9]
#
# print(get_min_max(data))

'''Task 10.2.21'''
# def transpose(matrix):
#     trans = []
#     for row in zip(*matrix):
#         trans.append(list(row))
#     return trans
#
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# for row in transpose(matrix):
#     print(row)
'''Task 10.2.20'''
# def filterfalse(predicate, iterable):
#     if predicate == None:
#         predicate = bool
#     return filter(lambda x: predicate(x) == False, iterable)
#
# objects = [0, 1, True, False, 17, []]
#
# print(*filterfalse(None, objects))
#
# numbers = (1, 2, 3, 4, 5)
#
# print(*filterfalse(lambda x: x % 2 == 0, numbers))

'''Task'''
# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62,
#            64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
#
# num = iter(numbers)
#
# while True:
#     try:
#         last = next(num)
#     except:
#         print(last)
#         break





