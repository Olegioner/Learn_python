'''Task 6.8.22'''
# from collections import Counter
#
# dict_books = Counter(input().split())
# total_profit = 0
#
# for i in range(int(input())):
#     book, price = input().split()
#     if dict_books[book] > 0:
#         total_profit += int(price)
#         dict_books.subtract({book:1})
#     else:
#         continue
#
# print(total_profit)

'''Task 6.8.21'''
# from collections import Counter
# import json
# import csv
#
# all_products = Counter()
# for i in range(1, 5):
#     with open('C:/new/prices/quarter' + str(i) + '.csv', 'r', encoding='utf-8') as file:
#         quarter = csv.reader(file, delimiter=',')
#         next(quarter)
#         for el in quarter:
#             k, *count = el
#             count = sum(list(map(lambda x: int(x), count)))
#             all_products[k] += count
# with open('C:/new/prices/prices.json', 'r', encoding='utf-8') as file:
#     prices = json.load(file)
#
# for k,v in prices.items():
#     all_products[k] = all_products[k] * v
#
# print(all_products.total())

'''Task 6.8.20'''
# from collections import Counter
#
# def print_bar_chart(data, mark):
#     data_counter = Counter(data)
#     max_len = len(max(data_counter.keys(), key=lambda x: len(x)))
#     for k,v in data_counter.most_common():
#         print(f'{k}{" " * (max_len - len(k))} |{mark * v}')


'''Task 6.8.19'''
# from collections import Counter
#
# def scrabble(symbols, word):
#     if Counter(symbols.lower()) > Counter(word.lower()):
#         return True
#     else:
#         return False
#
# print(scrabble('begk', 'beegeek'))
'''Task 6.8.18'''
# import csv
# from collections import Counter
#
# with open('C:/new/name_log.csv', 'r', encoding='utf-8') as file:
#     log = csv.DictReader(file, delimiter=',' )
#     count_change_name = Counter()
#     for user in log:
#         count_change_name[user['email']] += 1
# for k,v in sorted(count_change_name.items(), key=lambda x: x[0]):
#     print(f'{k}: {v}')
'''Task 6.8.17'''

# from collections import Counter
#
# data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
# data.min_values = lambda: list(filter(lambda x: x[1] == data.most_common()[-1][1], data.items()))
# data.max_values = lambda: list(filter(lambda x: x[1] == data.most_common()[0][1], data.items()))
#
# print(data.max_values())
# print(data.min_values())

'''Task 6.8.16'''
# import sys
# from collections import Counter
#
# student = Counter()
# for el in sys.stdin:
#     for k,v in el.split():
#         student[k] = int(v)
#
# print(student.most_common()[-2][0])

'''Task 6.8.15'''
# from collections import Counter
#
# words = Counter([len(el) for el in input().split()])
#
# for key, value in sorted(words.items(), key=lambda x: x[1]):
#     print(f'Слов длины {key}: {value}')

'''Task 6.8.14'''
# from collections import Counter
#
# words = Counter(el.lower() for el in input().split())
# max_count = words.most_common(1)[0][1]
# print(sorted(filter(lambda x: words[x]==max_count, words))[-1])

'''Task 6.8.13'''
# from collections import Counter
#
# count_words = Counter(input().lower().split())
# min_count = []
# for word in count_words:
#     if count_words[word] == min(count_words.values()):
#         min_count.append(word)
# print(', '.join(sorted(min_count)))
'''Task 6.8.12'''
# from collections import Counter
#
# count_words = Counter([el.lower() for el in input().split()])
# print(count_words.most_common(1)[0][0])
'''Task 6.7.19'''
# from collections import Counter
#
# with open('C:/new/pythonzen.txt', 'r', encoding='utf-8') as file:
#     text = Counter(el.lower() for el in list(file.read()) if el.isalpha())
# for k,v in sorted(text.items()):
#     print(f'{k}: {v}')


'''Task 6.7.18'''
# from collections import Counter
#
# products = Counter(input().split(','))
# max_len = len(max(products.keys(), key=lambda x: len(''.join(x.split()))))
#
# for prod, count in sorted(products.items()):
#     price_prod = 0
#     for char in prod:
#         if char == ' ':
#             continue
#         else:
#             price_prod += ord(char)
#     print(f'{prod}{(max_len - len(prod)) * " "}: {price_prod} UC x {count} = {price_prod*count} UC')


'''Task 6.7.17'''
# from collections import Counter
#
# products = Counter(input().split(','))
# for prod, count in sorted(products.items()):
#     print(f'{prod}: {count}')


'''Task 6.7.16'''
# from collections import Counter
#
# def count_occurences(word, words):
#     count_words = Counter([el.lower() for el in words.split()])
#     return count_words[word.lower()]


'''Task 6.7.15'''
# from collections import Counter
#
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
#
# count_extension = Counter([el[el.index('.'):] for el in files])
#
# for ext, count in sorted(count_extension.items(), key=lambda x: x[0]):
#     print(f'{ext[1:]}: {count}')
