from random import randint

question = randint(1,100)
print('Добро пожаловать в числовую угадайку')
answer = input()
def is_valid(n):
    return n.isdigit() and (1 <= int(n) <= 100)

while is_valid(answer) == False:
    print('А может быть все-таки введем целое число от 1 до 100?')
    answer = input()
answer = int(answer)

while answer != 200:
    if answer > question:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif answer < question:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break



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



