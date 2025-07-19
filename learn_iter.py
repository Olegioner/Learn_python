'''Task 10.5.26'''
# class Iterator:
#     def __init__(self):
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         return self.count
#
#
# infinity_num = Iterator()
#
#
#
# def palindromes():
#     yield from filter(lambda x: str(x) == str(x)[::-1], infinity_num)


# generator = palindromes()
# numbers = [next(generator) for _ in range(30)]
#
# print(*numbers)


generator = palindromes()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))



'''Task 10.5.25'''

# def matrix_by_elem(matrix):
#     for row in matrix:
#         yield from row
#
#
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(*matrix_by_elem(matrix))
# '''Task 10.5.20'''

# def card_deck(suit):
#     num = ['2', '3', '4', '5', '6', '7', '8', '9',
#            '10', 'валет', 'дама', 'король', 'туз']
#     suits = ['пик', 'треф', 'бубен', 'червей']
#     suits.remove(suit)
#     while True:
#         for s in suits:
#             for n in num:
#                 yield f'{n} {s}'
#
#
# generator = card_deck('треф')
# cards = [next(generator) for _ in range(40)]
#
# print(*cards)
'''Task 10.5.19'''
# from datetime import timedelta, date
#
# def dates(start, count=None):
#     step = 0
#     try:
#         while step != count:
#             yield start
#             start += timedelta(days=1)
#             step += 1
#     except OverflowError:
#         return


'''Task 10.5.18'''
# def reverse(sequence):
#     for el in sequence[::-1]:
#         yield el


'''Task 10.5.17'''
# def primes(left, right):
#     for i in range(left, right + 1):
#         count = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             yield i
#
# generator = primes(6, 36)
#
# print(next(generator))
# print(next(generator))

'''Task 10.5.16'''
# def alternating_sequence(count=None):
#     num = 0
#     while num != count:
#         num += 1
#         if num % 2 == 0:
#             yield num * (-1)
#         else:
#             yield num


'''Task 10.5.15'''

# def simple_sequence():
#     num = 1
#     while True:
#         for n in range(num):
#             yield num
#         num += 1


'''Task 10.4.17'''

# class Xrange:
#     def __init__(self, start, end, step=1):
#         self.start = start - step
#         self.end = end
#         self.step = step
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += self.step
#         if self.step < 0:
#             if self.end >= self.start:
#                 raise StopIteration
#         elif self.step > 0:
#             if self.start >= self.end:
#                 raise StopIteration
#
#         return self.start

'''Task 10.4.16'''

# class Alphabet:
#     def __init__(self, language):
#         self.language = language
#         self.alphabet = {'ru': [chr(el) for el in range(1072, 1104)],
#                          'en':[chr(el) for el in range(97, 123)]}
#         self.step = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.step += 1
#         if self.step == len(self.alphabet[self.language]):
#             self.step = 0
#         return self.alphabet[self.language][self.step]


'''Task 10.4.15'''
# from random import randint
#
# class RandomNumbers:
#     def __init__(self, left, right, n):
#         self.left = left
#         self.right = right
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.n -= 1
#         if self.n < 0:
#             raise StopIteration
#         return randint(self.left, self.right)
#
#
# iterator = RandomNumbers(-1000, -900, 4)
#
# print(next(iterator) in range(-1000, -899))
# print(next(iterator) in range(-1000, -899))
# print(next(iterator) in range(-1000, -899))
# print(next(iterator) in range(-1000, -899))
#
# try:
#     next(iterator)
# except StopIteration:
#     print('Error')


'''Task 10.4.14'''
# class Cycle:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.step = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.step += 1
#         if self.step == len(self.iterable):
#             self.step = 0
#         return self.iterable[self.step]
#
#
#
#
# cycle = Cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# for _ in range(100):
#     print(next(cycle))
'''Task 10.4.13'''
# class CardDeck:
#     def __init__(self):
#         self.num = ['2', '3', '4', '5', '6', '7', '8', '9',
#                     '10', 'валет', 'дама', 'король', 'туз']
#         self.suits = ['пик', 'треф', 'бубен', 'червей']
#         self.step = -1
#         self.step_num = -1
#         self.step_suits = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.step += 1
#         self.step_num += 1
#         if self.step_num > 12:
#             self.step_suits += 1
#             self.step_num = 0
#         if self.step == 52:
#             raise StopIteration
#         return f'{self.num[self.step_num]} {self.suits[self.step_suits]}'
#
#
#
# cards1 = list(CardDeck())
# cards2 = tuple(CardDeck())
# cards3 = list(CardDeck())
#
# print(cards1)
# print(cards2)
# print(cards3)

'''Task 10.4.12'''
# class DictItemsIterator:
#     def __init__(self, data):
#         self.data = data
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if len(self.data) == 0:
#             raise StopIteration
#         for el in self.data:
#             return el, self.data.pop(el)
#
#
# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
#
# pairs = DictItemsIterator(data)
#
# print(tuple(pairs))
#
#
# try:
#     print(next(pairs))
# except StopIteration:
#     print('Error')



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





