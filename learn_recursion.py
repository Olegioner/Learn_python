'''task 8.2.13'''

# def print_digits(number):
#     number = list(str(number))
#     def res(digit):
#         if len(digit) > 0:
#             print(digit.pop(0))
#             res(digit)
#     res(number)
#
# print_digits(8)

'''Task 8.2.12'''

# def print_digits(arr):
#     if arr > 0:
#         print(arr % 10)
#         arr //= 10
#         print_digits(arr)
'''Task 8.2.11'''

# def hourglass(n):
#
#     if n < 4:
#         print((str(n) * (20 - n * 4)).center(16))
#         hourglass(n + 1)
#     print((str(n) * (20 - n * 4)).center(16))
#
# hourglass(1)

'''Task 8.2.10'''
# def triangle(h):
#     def res(n):
#         if n <= h:
#             print('*' * n)
#             res(n + 1)
#     res(1)
# triangle(5)

'''Task 8.2.9'''
# def triangle(h):
#     if h >= 1:
#         print('*' * h)
#         triangle(h - 1)
#
# triangle(5)сто

'''Task 8.2.8'''
# def func():
#     num = int(input())
#     if num:
#         func()
#     print(num)
#
# func()

'''Task 8.2.7'''
# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841,
#            -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195,
#            792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96,
#            533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166,
#            -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
#            984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916,
#            802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249,
#            190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
#
# def out_index(arr):
#     def res(index):
#         if index < len(arr):
#             print(f'Элемент {index}: {arr[index]}')
#             res(index + 1)
#     res(0)
#
# out_index(numbers)