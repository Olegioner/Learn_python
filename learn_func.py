'''Панграмма – это фраза, содержащая в себе все буквы алфавита.
Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.
Напишите функцию is_pangram(text), которая принимает в качестве аргумента строку текста на английском языке
и возвращает значение True, если текст является панграммой, или значение False в противном случае.'''

'''def is_pangram(text):
    text = text.lower()
    alphabet = [chr(el) for el in range(97, 123)]
    count = 0
    for el in alphabet:
        if el in text:
           count += 1
        else:
            return False
    if count >= 26:
        return True

print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))'''

'''Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.
Напишите функцию is_magic(date),
которая принимает в качестве аргумента строковое представление корректной даты и возвращает значение True,
если дата является магической и False - в противном случае.'''
'''def is_magic(date):
    date = date.split('.')
    if date[1][0] == '0':
        if int(date[0]) * int(date[1][1]) == int(date[2][2:]):
            return True
        else:
            return False
    elif int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
    else:
        return False

print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))'''




'''Напишите функцию get_month(language, number),
которая принимает на вход два аргумента language – язык ru или en и number – номер месяца (от 1 до 12)
и возвращает название месяца на русском или английском языке.'''
'''def get_month(language, number):
    month_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    month_eng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return month_ru[number - 1]
    if language == 'en':
        return month_eng[number - 1]'''



'''Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и
возвращает его словесное описание на русском языке.
Считайте, что число 1≤num≤99'''
'''def number_to_words(num):
    list_digit = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
                  'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_number = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num <= 19:
        return list_digit[num-1]
    if num > 19 and (num % 10 != 0):
        return list_number[(num // 10) - 2 ] + ' ' + list_digit[(num % 10) - 1]
    else:
        return list_number[(num // 10) - 2 ]

print(number_to_words(31))'''
'''Интернет-магазин осуществляет экспресс доставку для своих товаров по цене 1000 рублей за первый товар и
120 рублей за каждый последующий товар. Напишите функцию get_shipping_cost(quantity),
которая принимает в качестве аргумента натуральное число quantity – количество товаров в заказе –
и возвращает стоимость доставки.'''

'''def get_shipping_cost(quantity):
    return 1000 + (120 * (quantity - 1))'''



'''Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой равными
15 и 8 соответственно:'''

'''def draw_triangle(base, height):
    for i in range(height):
        print((' ' * (height - i -1)) + ('*' * (base - (base-(i + i + 1)))))



draw_triangle(15,8)'''

'''Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения
и возвращает его корни в порядке возрастания.'''
'''import math
def solve(a,b,c):
    d = (b**2) - 4 * a * c
    if d < 0.0:
        return print('Нет корней')
    elif d == 0.0:
        x1 = -(b / (2 * a))
        return x1, x1
    elif d > 0.0:
        x1 = (-b - math.sqrt(math.pow(b,2) - 4 * a * c))/ (2 * a)
        x2 = (-b + math.sqrt(math.pow(b,2) - 4 * a * c))/ (2 * a)
        return min(x1,x2), max(x1,x2)'''


'''Напишите функцию get_circle(radius),
которая принимает в качестве аргумента радиус окружности и возвращает
два значения: длину окружности и площадь круга, ограниченного данной окружностью.'''
'''import math
def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * (radius ** 2)
    return c, s'''





'''Напишите функцию convert_to_python_case(text),
которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».'''

'''def convert_to_python_case(text):
    text = list(text)
    text_python = []
    text_python.append(text[0].lower())
    for i in range(1,len(text)):
        if text[i].isupper():
            text_python.append('_')
            text_python.append(text[i].lower())
        else:
            text_python.append(text[i])
    return ''.join(text_python)'''



'''Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
состоящую из символов ( и ) и возвращает значение True, если поступившая на вход строка является правильной
скобочной последовательностью, или значение False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов
( и ), где каждой открывающей скобке найдётся парная закрывающая скобка (при этом каждая открывающая
скобка должна быть левее соответствующей ей закрывающей скобки).'''

'''def is_correct_bracket(text):
    text = list(text)
    if text[0] == ')' or text[-1] == '(' or len(text) % 2 != 0:
        return False
    count_s = 0
    for el in text:
        if el == '(':
            count_s += 1
        elif el == ')':
            count_s -= 1
            if count_s < 0:
                return False
    if count_s != 0:
        return False
    else:
        return True'''


'''BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение
пароля password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка,
или False в противном случае.'''
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
def is_valid_password(password):
    password = password.split(':')
    if len(password) > 3:
        return False
    flag = 'YES'
    if password[0] == password[0][::-1]:
        flag = 'YES'
    else:
        return False
    if is_prime(int(password[1])):
        flag = 'YES'
    else:
        return False
    if int(password[2]) % 2 == 0:
        flag = 'YES'
    else:
        return False
    return flag == 'YES'''


'''Напишите функцию is_palindrome(text),
которая принимает в качестве аргумента строку text и возвращает значение
True если указанный текст является палиндромом и False в противном случае.'''

'''def is_palindrome(text):
    text = text.lower().replace(' ', '')
    text_clear = ''
    for i in range(len(text)):
        if text[i] not in '!?.,-':
            text_clear += text[i]
    return text_clear == text_clear[::-1]'''


'''Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2
и возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе,
или значение False в противном случае.'''

'''def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count_sym = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count_sym += 1
    if count_sym == 1:
        return True
    else:
        return False'''


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

