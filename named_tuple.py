'''Task 6.4.12'''
# from collections import namedtuple
# from datetime import datetime
# import csv
#
# with open('C:/new/meetings.csv',  'r', encoding='utf-8') as file:
#     persons = list(csv.reader(file, delimiter=','))
#     headers = persons.pop(0)
#     Friends = namedtuple('Friends', headers)
#     all_friends = []
#     for el in persons:
#         all_friends.append(Friends(*el))
#
# all_friends = sorted(all_friends, key=lambda x:datetime.strptime(f'{x.meeting_date} {x.meeting_time}', '%d.%m.%Y %H:%M'))
# for el in all_friends:
#     print(el.surname, el.name)

'''Task 6.4.11'''
# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
#
# plans = ['Gold', 'Silver', 'Bronze', 'Basic' ]
#
# for el in sorted(sorted(users, key=lambda x: x.email), key=lambda x: plans.index(x.plan)):
#     print(el.name, el.surname)
#     print(f'  Email: {el.email}')
#     print(f'  Plan: {el.plan}')
#     print()


'''Task 6.4.10'''
# import pickle
# from collections import namedtuple
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
#
# with open('C:/new/data.pkl', 'rb') as file:
#     pet = pickle.load(file)
#
# for el in pet:
#     for field, value in zip(Animal._fields, el):
#         print(f'{field}: {value}')
#     print()
