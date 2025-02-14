'''Task 6.10.15'''
#
# from collections import ChainMap
#
# def get_value(chainmap, key, from_left=True):
#     chainmap.setdefault(key, None)
#     if from_left:
#         return chainmap[key]
#     else:
#         chainmap.maps.reverse()
#         return chainmap[key]
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
#
# print(get_value(chainmap, 'name'))

'''Task 6.10.14'''
# from collections import ChainMap
#
# def deep_update(chainmap, key, value):
#     for el in chainmap.maps:
#         if key in el:
#             el[key] = value
#     if key not in chainmap.keys():
#         chainmap.maps[0].update({key:value})
#
#
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'age', 20)
#
# print(chainmap)


'''Task 6.10.13'''
# from collections import ChainMap
#
# def get_all_values(chainmap, key):
#     key_set = set()
#     for el in chainmap.maps:
#         if key in el:
#             key_set.add(el[key])
#     return key_set
#
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'age')
#
# print(result)


'''Task 6.9.23'''
# from collections import ChainMap, Counter
#
# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
#
# products = ChainMap(bread, meat, sauce, vegetables, toppings)
#
# purchases = Counter([el for el in input().split(',')])
# max_len = len(max(purchases.keys(), key=lambda x: len(x)))
#
# sum_price = 0
# max_len_str = 0
# for product, count in sorted(purchases.items(), key=lambda x: x[0]):
#     sum_price += products[product] * count
#     str = f'{product}{(max_len - len(product)) * " "} x {count}'
#     if max_len_str < len(str):
#         max_len_str = len(str)
#     print(str)
# result = f'ИТОГ: {sum_price}р'
# print('-' * max(len(result), max_len_str))
# print(result)


'''Task 6.9.22'''
# from collections import ChainMap
# import json
#
# with open('C:/new/zoo.json', 'r', encoding='utf-8') as file:
#     zoo = json.load(file)
# zoo_dict = ChainMap(*zoo)
# print(sum(zoo_dict.values()))