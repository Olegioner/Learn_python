
'''Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого покупателя — двоеточие,
затем список названий всех приобретенных им товаров в лексикографическом порядке, после названия каждого товара — количество
единиц товара. Информация о каждом товаре выводится на отдельной строке.'''

# dict_buy = {}
# for _ in range(int(input())):
#     k, v, count = input().split()
#     if k not in dict_buy:
#         dict_buy.setdefault(k, {v: int(count)})
#     elif v not in dict_buy[k]:
#         dict_buy[k].update({v: int(count)})
#     else:
#         dict_buy[k][v] += int(count)
#
# for name in sorted(dict_buy):
#     print(name + ':')
#     for key, value in sorted(dict_buy[name].items()):
#         print(key, value)


'''Программа получает на вход количество файлов n, содержащихся в файловой системе компьютера. Далее идет
n строк, на каждой имя файла и допустимые с ним операции, разделенные символом пробела. В следующей строке записано число
m — количество запросов к файлам, и затем m строк с запросами вида операция файл. Одному и тому же файлу может
быть адресовано любое количество запросов.'''
# s = {'write': 'W', 'read': 'R','execute': 'X'}
# dict_access = {}
# for _ in range(int(input())):
#     k, *v = input().split()
#     dict_access[k] = v
#
# list_request = [[el for el in input().split()] for _ in range(int(input()))]
# for i in range(len(list_request)):
#     if list_request[i][1] in dict_access:
#         if s[list_request[i][0]] in dict_access[list_request[i][1]]:
#             print('OK')
#         else:
#             print('Access denied')
#     else:
#         print('Access denied')


'''Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и
возвращать словарь, каждый ключ которого содержит множество (тип данных set)
уникальных значений собранных из всех словарей переданного списка.'''

# def merge(list_dict):
#     result = {}
#     for i in range(len(list_dict)):
#         for k,v in list_dict[i].items():
#             result.setdefault(k, set()).add(v)
#     return result
#
# lst = [{'a': 1, 'b': 2},
# {'b': 10, 'c': 100},
# {'a': 1, 'b': 17, 'c': 50},
# {'a': 5, 'd': 777}]
#
# print(merge(lst))


'''Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения.
Она начинается после вопросительного знака и идет до конца адреса. Если параметров в строке запроса несколько,
то они отделяются символом амперсанда &. Напишите функцию build_query_string(),
которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров.'''
#
# def build_query_string(dict_parameters):
#     return '&'.join(sorted([str(k) + '=' + str(v) for k,v in dict_parameters.items()]))
#
# print(build_query_string({'name': 'timur', 'age': 28}))


'''В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв.
Чем реже буква встречается, тем больше она ценится. Напишите программу подсчета итоговой стоимости введенного слова.'''
# dict_letter = { 1: "AEILNORSTU",
#                 2: "DG",
#                 3: "BCMP",
#                 4: "FHVWY",
#                 5: "K",
#                 8: "JX",
#                 10: "QZ"}
# word = input()
# sm = 0
# for el in word:
#     for k, v in dict_letter.items():
#         if el in v:
#             sm += k
# print(sm)


'''Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв,
слова разделены одним пробелом или несколькими. Напишите программу, определяющую для каждого слова порядковый номер
его вхождения в текст именно в этой форме, с учетом регистра. Для первого вхождения слова программа выведет 1,
для второго вхождения того же слова — 2 и т. д.'''

# text = input().split()
# result = {}
# for word in text:
#     result[word] = result.get(word, 0) + 1
#     print(result[word], end=' ')


'''Как известно из курса биологии, ДНК и РНК – последовательности нуклеотидов. Напишите программу, переводящую цепь ДНК в цепь РНК.'''

# dict_dna_rna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
# dna = list(input())
# for el in dna:
#     print(dict_dna_rna[el], end='')


'''Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену.
Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке,
каждый на отдельной строке, в формате username@domain.'''
# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# list_emails = sorted((' '.join(([' '.join([v[i] + '@' + k for i in range(len(v))]) for k,v in emails.items()]))).split())
# for el in list_emails:
#     print(el)



'''Дополните приведенный код, чтобы в списках значений элементов словаря my_dict не было чисел, больших
20. При этом порядок оставшихся элементов меняться не должен.'''
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12],
#            'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19],
#            'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48],
#            'C9': [2, 7, 18, 28, 18, 28]}
# my_dict = {k : [v[i] for i in range(len(v)) if v[i] <= 20] for k,v in my_dict.items()}
# print(my_dict)