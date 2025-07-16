'''Task 10.4.12'''
class DictItemsIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) == 0:
            raise StopIteration


'''Task 10.4.11'''

# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.start = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         return self.number ** self.start

'''Task 10.4.10'''

# class Fibonacci:
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a

'''Task 10.4.9'''

# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.step = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.step += 1
#         if self.step > self.n:
#             raise StopIteration
#         return self.step ** 2
#
# squares = Square(1)
#
# print(list(squares))

'''Task 10.4.8'''
# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         if self.count > self.times:
#             raise StopIteration
#         return self.obj
#
# geek = BoundedRepeater('geek', 1)
#
# print(next(geek))
#
#
# try:
#     print(next(geek))
# except StopIteration:
#     print('Error')


'''Task 10.4.7'''
# class Repeater:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.obj


'''Task 10.3.16'''
# from random import randint
# def random_numbers(left, right):
#     return iter(lambda: randint(left, right), -1)

'''Task 10.3.15'''
# def is_iterator(obj):
#     try:
#         if obj == iter(obj):
#             return True
#         else:
#             return False
#     except TypeError:
#         return False

'''Task 10.3.14'''
# def is_iterable(obj):
#     try:
#         iter(obj)
#         return True
#     except TypeError:
#         return False


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





