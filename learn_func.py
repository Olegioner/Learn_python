'''Напишите функцию is_password_good(password),
которая принимает в качестве аргумента строковое значение пароля password и возвращает
значение True, если пароль является надежным и False - в противном случае.'''

'''def is_password_good(password):
    count_mn = 0
    count_mx = 0
    count_dig = 0
    if len(password) < 8:
        return False
    for i in range(len(password)):
        if password[i].isupper():
            count_mx += 1
        if password[i].islower():
            count_mn += 1
        if password[i].isdigit():
            count_dig += 1
    if count_mn > 0 and count_mx > 0 and count_dig > 0:
        return True
    else:
        return False'''


'''Напишите функцию get_next_prime(num),
которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.'''
'''def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    i = num + 1
    while is_prime(i) == False:
        is_prime(i)
        i+= 1
    return i'''

'''Напишите функцию is_prime(num),
которая принимает в качестве аргумента натуральное число и
возвращает значение True, если число является простым, или False в противном случае.'''

'''def is_prime(num):
    count_del = 0
    for i in range(1,num+1):
        if num % i == 0:
            count_del += 1
    if num == 1:
        return False
    if count_del > 2:
        return False
    else:
        return True
'''

'''Быстрое слияние трех и более списков'''

'''def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    else:  # иначе прицепляем остаток другого списка
        result += list2[p2:]

    return result

list_num = [input().split() for el in range(int(input()))]
for i in range(len(list_num)):
    for j in range(len(list_num[i])):
        list_num[i][j] = int(list_num[i][j])

list_result = quick_merge(list_num[0],list_num[1])
for i in range(2, len(list_num)):
    list_result = quick_merge(list_result,list_num[i])
print(list_result)'''






'''Напишите функцию с именем find_all(target, symbol),
которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.'''
'''def find_all(target, symbol):
    count = []
    for i in range(len(target)):
        if target[i] == symbol:
            count.append(i)
    return count'''

'''Сумма делителей числа'''
'''def number_of_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])'''

'''Список делителей числа'''
'''def get_factors(num):
    return [i for i in range(1,num+1) if num % i == 0]
print(get_factors(10))
'''

'''Вычисление кол-ва дней в месяце'''
'''def get_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        return 28

num = int(input())
print(get_days(num))'''


#def convert_to_miles(km):
    #return km * 0.6214

