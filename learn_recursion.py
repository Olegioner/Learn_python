'''Task 8.4.7'''
def get_all_values(nested_dict, key):
    res = set()
    if key in nested_dict:
        return nested_dict[key]
    for v in nested_dict.values():
        if type(v) == dict:
            value = get_all_values(v, key)
            if value is not None:
                print(value)
                res.add(value)
    return res

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')
#print(result)
print(*sorted(result))

'''Task 8.4.6'''
# def get_value(nested_dict, key):
#     if key in nested_dict:
#         return nested_dict[key]
#     for v in nested_dict.values():
#         if type(v) == dict:
#             value = get_value(v, key)
#             if value is not None:
#                 return value


'''Task 8.4.5'''
# def linear(nested_lists):
#     total = []
#     if len(nested_lists) == 0:
#          return 0
#     for el in nested_lists:
#         if type(el) == int:
#             total.append(el)
#         elif type(el) == list:
#             total.extend(linear(el))
#     return total

'''Task 8.4.4'''
# def recursive_sum(nested_lists):
#     total = 0
#     if len(nested_lists) == 0:
#         return 0
#     for el in nested_lists:
#         if type(el) == int:
#             total += el
#         elif type(el) == list:
#             total += recursive_sum(el)
#     return total


'''Task 8.3.17'''
# def minus_five(n):
#     print(n)
#     if n - 5 < 0:
#         print(n - 5)
#     else:
#         minus_five(n - 5)
#     print(n)
#
#
# n = int(input())
# minus_five(n)
'''Task 8.3.16'''
# def to_binary(number):
#     if number <= 1:
#         return number
#     else:
#         return str(to_binary(number // 2)) + str(number % 2)

'''Task 8.3.15'''
# def is_palindrome(string):
#     if len(string) == 0 or len(string) == 1:
#         return True
#     elif string[0] != string[-1]:
#         return False
#     else:
#         return is_palindrome(string[1:-1])

'''Task 8.3.14'''

# def tribonacci(n):
#     cache = {1: 1, 2: 1, 3: 1}
#
#     def tribonacci_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = tribonacci_rec(n - 3) + tribonacci_rec(n - 2) + tribonacci_rec(n - 1)
#             cache[n] = result
#         return result
#
#     return tribonacci_rec(n)

'''Task 8.3.13'''
# def is_power(number):
#     if number == 1:
#         return True
#     elif number >= 2:
#         return is_power(number / 2)
#     else:
#         return False


'''Task 8.3.12'''
# def recursive_sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return 1 + recursive_sum(a, b - 1)
#
# print(recursive_sum(0, 0))

'''Task 8.3.11'''
# def get_fast_pow(a, n):
#    if n == 0:
#        return 1
#    elif n % 2 == 0:
#        return get_fast_pow(a * a, n // 2)
#    else:
#        return a * get_fast_pow(a, n - 1)


'''Task 8.3.10'''
# def get_pow(a, n):
#     if n == 1:
#         return a
#     elif n == 0:
#         a = 1
#         return a
#     else:
#         return a * get_pow(a, n - 1)
'''Task 8.3.9'''
# def range_sum(numbers, start, end):
#     if start == end:
#         return numbers[start]
#     else:
#         return numbers[start] + range_sum(numbers, start + 1 , end)
'''Task 8.3.8'''

# def number_of_frogs(year):
#     if year <= 1:
#         return 77
#     else:
#         return 3 * (number_of_frogs(year - 1) - 30)

'''Task 8.3.7'''

# def sum_num(num):
#     if num < 10:
#         return num
#     else:
#          return num % 10 + sum_num(num // 10)
#
# print(sum_num(int(input())))

'''Task 8.3.6'''
# def count(num):
#     if num < 9:
#         return 1
#     else:
#         return 1 + count(num // 10)
#
# print(count(int(input())))



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