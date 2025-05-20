'''Task 9.1.10'''
# def is_greater(lists, number):
#     return any(map(lambda x: True if sum(x) > number else False, lists))

'''Task 9.1.9'''
# def non_negative_even(numbers):
#     return all(map(lambda x: True if x >= 0 and x % 2 == 0 else False, numbers))
#
#
# print(non_negative_even([0, 2, 4, 8, 16]))
# print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
# print(non_negative_even([0, 0, 0, 0, 0]))
'''Task 9.1.8'''

# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
#
# res = min(films, key=lambda x: sum(films[x].values()))
# print(res)

'''Task 9.1.5'''
# def convert(number):
#     func_list = [str(bin(number)), str(oct(number)), str(hex(number)).upper()]
#     res = []
#     for el in func_list:
#         if el[0] == '-':
#             res.append(el[0] + el[3:])
#         else:
#             res.append(el[2:])
#     return tuple(res)

'''Task 9.1.4'''
# import string
# for el in string.ascii_lowercase:
#     print(el)