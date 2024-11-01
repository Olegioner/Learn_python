'''Task2'''
def same_parity(numbers):
    num_list = []
    if numbers == []:
       return num_list
    elif numbers[0] % 2 == 0:
        num_list = list(filter(lambda x: x if x % 2 == 0 else '', numbers))
    else:
        num_list = list(filter(lambda x: x if x % 2 != 0 else '', numbers))
    return num_list


# print(same_parity([]))
print(same_parity([6, 0, 67, -7, 10, -20]))
# print(same_parity([-7, 0, 67, -9, 70, -29, 90]))




'''Task1'''
# def hide_card(card_number):
#     card_n = ''.join(card_number.split())
#     return 12 * '*' + card_n[12:]
