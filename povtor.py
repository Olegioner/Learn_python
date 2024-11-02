'''Task11'''
# def get_biggest(numbers):
#     if len(numbers) == 0:
#         return -1
#     else:
#         num = [str(el) for el in numbers]
#         num_max = len(max(num, key=lambda x: len(x)))
#         num_s = sorted(num, key=lambda x: x*num_max, reverse=True)
#         return int(''.join(num_s))

'''Task10'''
# def choose_plural(amount, declensions):
#     num = amount % 100
#     num_last = int(str(num)[-1])
#     if num == 11 or num == 12:
#         return f'{amount} {declensions[2]}'
#     elif num == 1 or num_last == 1:
#         return f'{amount} {declensions[0]}'
#     elif 2<= num < 5 or 2<= num_last < 5:
#         return f'{amount} {declensions[1]}'
#     else:
#         return f'{amount} {declensions[2]}'

'''Task9'''
# def spell(*args):
#     dict_letter = {}
#     for k in args:
#         if k[0].lower() in dict_letter.keys():
#             if dict_letter[k[0].lower()] < len(k):
#                 dict_letter[k[0].lower()] = len(k)
#             else:
#                 continue
#         else:
#             dict_letter[k[0].lower()] = len(k)
#     return dict_letter

'''Task8'''
# def index_of_nearest(numbers, number):
#     if len(numbers) == 0:
#         return -1
#     num = sorted(numbers, key=lambda x: abs(x - number))
#     return numbers.index(num[0])

'''Task7'''
# def likes(names):
#     if len(names) == 0:
#         return 'Никто не оценил данную запись'
#     elif len(names) == 1:
#         return f'{names[0]} оценил(а) данную запись'
#     elif len(names) == 2:
#         return f'{names[0]}, {names[1]} оценили данную запись'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
#     elif len(names) > 3:
#         return f'{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись'

'''Task6'''
# def filter_anagrams(word, words):
#     if len(words) == 0:
#         return words
#     else:
#         ws_res = list(map(lambda x: x if sorted(list(x)) == sorted(list(word)) else '', words))
#         ws_res_clean = (' '.join(ws_res)).split()
#     return ws_res_clean
#
#
# print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
# print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
# print(filter_anagrams('стекло', []))
'''Task5'''
# def convert(string):
#     count_l = 0
#     need_string = ''.join(map(lambda x: x if x.isalpha() else '', string))
#     for el in need_string:
#         if el.lower() == el:
#             count_l += 1
#     if count_l >= len(need_string) // 2:
#         return string.lower()
#     else:
#         return  string.upper()
#
# print(convert('BEEgeek'))
# print(convert('pyTHON'))
# print(convert('pi31415!'))
# print(convert('PI31415!'))
'''Task4'''
# def print_given(*args, **kwargs):
#     for el in args:
#         print(el, type(el))
#     for k,v in sorted(kwargs.items()):
#         print(k, v, type(v))

'''Task3'''
# def is_valid(string):
#     return True if 4 <= len(string) <= 6 and string.isdigit() else False
'''Task2'''
# def same_parity(numbers):
#     num_list = []
#     if len(numbers) == 0:
#        return num_list
#     elif numbers[0] % 2 == 0:
#         for el in numbers:
#             if el % 2 == 0:
#                 num_list.append(el)
#     else:
#         for el in numbers:
#             if el % 2 != 0:
#                 num_list.append(el)
#     return num_list


'''Task1'''
# def hide_card(card_number):
#     card_n = ''.join(card_number.split())
#     return 12 * '*' + card_n[12:]
