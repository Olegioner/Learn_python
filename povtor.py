'''Task20'''
# with open('C:/new/file.txt', 'r', encoding='utf-8') as file:
#     file_list = [[el.strip() for el in row.split()] for row in file.readlines()]
# file_list = list(map(lambda x: list(map(lambda el: int(el) if el.isdigit() else el, x)), file_list))
#
# file_list = sorted(file_list, key=lambda x: x[0])
#
# dict_file = {}
# for el in file_list:
#     if dict_file.get(el[0][el[0].index('.'):], False):
#         dict_file[el[0][el[0].index('.'):]].append(el)
#     else:
#         dict_file[el[0][el[0].index('.'):]] = [el]
# dict_file = dict(sorted(dict_file.items()))
#
# for v in dict_file.values():
#     sm = 0
#     for el in v:
#         if el[2] == 'B':
#             sm += el[1]/1024/1024/1024
#         if el[2] == 'KB':
#             sm += el[1]/1024/1024
#         if el[2] == 'MB':
#             sm += el[1]/1024
#         if el[2] == 'GB':
#             sm += el[1]
#         print(el[0])
#     cnt = 0
#     while sm < 1:
#         sm *= 1024
#         cnt += 1
#     ed = 'GB'
#     if cnt == 1:
#         ed = 'MB'
#     if cnt == 2:
#         ed = 'KB'
#     if cnt == 3:
#         ed = 'B'
#
#     print('----------')
#     print(f'Summary: {round(sm)} {ed}')
#     print()


'''Task19'''
# digits, names = '0123456789', []
#
# for _ in range(int(input())):
#     name, _ = input().split('@')
#     names.append(name)
# for _ in range(int(input())):
#     name = input()
#     counter = 1
#     while name in names:
#         name = name.rstrip(digits) + str(counter)
#         counter += 1
#     names.append(name)
#     print(names)
#     print(f'{name}@beegeek.bzz')

'''Task18'''
# letter_vow = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
#
# word = [el for el in list(input())]
# words = [[el for el in list(input())] for _ in range(int(input()))]
#
# word_vow = []
# for i in range(len(word)):
#     if word[i] in letter_vow:
#         word_vow.append(i)
#
# for el in words:
#     words_vow = []
#     for i in range(len(el)):
#         if el[i] in letter_vow:
#             words_vow.append(i)
#     if words_vow == word_vow:
#         print(''.join(el))

'''Task17'''
# list_language = [[el for el in input().split(', ')] for _ in range(int(input()))]
# need_language = []
# count = 1
# for el in list_language[0]:
#     for i in list_language[1:]:
#         if el in i:
#             count += 1
#     if count == len(list_language):
#         need_language.append(el)
#     count = 1
# print(', '.join(sorted(need_language))) if len(need_language) != 0 else print('Сериал снять не удастся')
'''Task16'''
# nums = [int(el)  for el in range(1, int(input())+1)]
# dict_nums = {}
# for el in nums:
#     res = sum([int(i) for i in list(str(el))])
#     if dict_nums.get(res, False):
#         dict_nums[res].append(el)
#     else:
#         dict_nums[res] = [el]
#
# print(len(max(dict_nums.values(), key=lambda x: len(x))))
'''Task15'''
# num = [int(el) for el in input().split()]
# num_res = set()
# for el in num:
#     if num.count(el) > 1:
#         num_res.add(el)
#
# print(*sorted(num_res))
'''Task14'''
# n, x, y, a, b = input().split()
# n, x, y, a, b = int(n), int(x)-1, int(y)-1, int(a)-1, int(b)-1
# nums = [el for el in range(1, n+1)]
# nums = nums[:x] + nums[x:y+1][::-1] + nums[y+1:]
# nums = nums[:a] + nums[a:b+1][::-1] + nums[b+1:]
# print(*nums)

'''Task13'''
# en = 'AaBCcEeHKMOoPpTXxy'
# ru = 'АаВСсЕеНКМОоРрТХху'
# letter_list = list(map(lambda x: 'ru' if x in ru else 'en',[input() for _ in range(3)]))
# set_list = set(el for el in letter_list)
# print(*set_list) if len(set_list) == 1 else print('mix')

'''Task12'''
# m1, m2, step_between_m = int(input()),int(input()),int(input())
# res = 0
# short_step = min(m1, m2)
# long_step = max(m1, m2)
# # Пришел в первый магаз
# res+= short_step
# # Идем во второй магаз
# if step_between_m > short_step + long_step:
#     res += short_step + long_step
# else:
#     res += step_between_m
# # Идем домой
# if step_between_m + short_step < long_step:
#     res += step_between_m + short_step
# else:
#     res += long_step
# print(res)


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
