'''Простая угадайка'''
from random import randint

question = randint(1,100)
print('Добро пожаловать в числовую угадайку')
# Проверка введенного числа на соответствие условию
def is_valid():
    n = input()
    while n != -999:
        if n.isdigit() and (1 <= int(n) <= 100):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            return is_valid()
# тело игры
i = 0
count = 0
while i == 0:
    answer = is_valid()
    if  answer > question:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
    elif answer < question:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
    else:
        print('Вы угадали, поздравляем!')
        print('Всего попыток -', count)
        break





'''Поиск минимального количества попыток угадать загаданное число'''
'''from random import randint
from math import log2, ceil
n = int(input())
question = randint(1,n)
print(ceil(log2(n + 1)))'''




'''from random import randint
n = int(input())
question = randint(1,n)
left = 1
right = n
middle = (left + right) // 2
count = 0
while middle != 999:
    if middle == question:
        count +=1
        break
    elif middle < question:
        left = middle + 1
        count +=1
    elif middle > question:
        right = middle - 1
        count += 1
    middle = (left + right) // 2
print(middle)'''



