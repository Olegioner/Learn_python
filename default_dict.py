'''Task 6.5.24'''
# from collections import defaultdict
#
# def best_sender(messages, senders):
#     senders_dict = defaultdict(int)
#     for mes, send in zip(messages, senders):
#         senders_dict[send] += len(mes.split())
#     count_mes = max(senders_dict.values())
#     best = max(dict(filter(lambda x: x[1] == count_mes, senders_dict.items())), key=lambda x: x[0])
#     return best
#
#
#
# messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree']
# senders = ['Alice', 'userTwo', 'userThree', 'Alice']
# print(best_sender(messages, senders))

'''Task 6.5.23'''
# from collections import defaultdict
#
# def flip_dict(dict_of_list):
#     dict_flip = defaultdict(list)
#
#     for k, v in dict_of_list.items():
#         for el in v:
#             dict_flip[el].append(k)
#     return dict_flip
#
# data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}
#
# for key, values in flip_dict(data).items():
#     print(f'{key}: {", ".join(values)}')

'''Task 6.5.22'''
# from collections import defaultdict
#
# def wins(pairs):
#     dict_wins = defaultdict(set)
#     for win, loser in pairs:
#         dict_wins[win].add(loser)
#     return dict_wins
#
# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))

'''Task 6.5.21'''
# from collections import defaultdict
#
# staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
#                 ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
#                 ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
#                 ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
#                 ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
#                 ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
#                 ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
#                 ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
#                 ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
#                 ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
#                 ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
#                 ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
#                 ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
#                 ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
#                 ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
#                 ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
#                 ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
#                 ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
#                 ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
#                 ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
#                 ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
#                 ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
#                 ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
#                 ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
#                 ('Accounting', 'Dale Houston')]
#
# staff_dict = defaultdict(set)
#
# for el in staff_broken:
#     staff_dict[el[0]].add(el[1])
#
# for k,v in sorted(staff_dict.items()):
#     print(f'{k}: {", ".join(sorted(v))}')




'''Task 6.5.20'''
# from collections import defaultdict
#
# staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'),
#          ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
#          ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'),
#          ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
#          ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'),
#          ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
#          ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'),
#          ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
#          ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'),
#          ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
#          ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'),
#          ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
#          ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'),
#          ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
#          ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'),
#          ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
#          ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
#
# staff_dict = defaultdict(int)
#
# for el in staff:
#     staff_dict[el[0]] += 1
#
# for k,v in sorted(staff_dict.items()):
#     print(f'{k}: {v}')


'''Task 6.5.19'''
# from collections import defaultdict
#
# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966),
#         ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964),
#         ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
#         ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951),
#         ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
#
# data_dict  = defaultdict(int)
#
# for el in data:
#     data_dict[el[0]] += el[1]
#
# for k, v in sorted(data_dict.items()):
#     print(f'{k}: ${v}')