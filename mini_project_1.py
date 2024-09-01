'''На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.
Гарантируется, что между различными словами присутствует один пробел.'''
text = input().split()
alphabet = [[chr(el) for el in range(65, 91)],[chr(el) for el in range(97, 123)]]
encrypt_text = ''
n = 26
# Задаём ключ для каждого слова
encrypt_key = []
for i in range(len(text)):
    count = 0
    for j in range(len(text[i])):
        if text[i][j] not in ' ,.-:;!?"=)(+-*/':
            count += 1
    encrypt_key.append(count)
# Шифруем текст
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] in alphabet[0]:
            symbol = alphabet[0].index(text[i][j])
            encrypt_text += alphabet[0][(symbol + encrypt_key[i]) % n]
        if text[i][j] in alphabet[1]:
            symbol = alphabet[1].index(text[i][j])
            encrypt_text += alphabet[1][(symbol + encrypt_key[i]) % n]
        if text[i][j] in ',.-:;!?"=)(+-*/':
            encrypt_text += text[i][j]
        if text[i][j] in '0123456789':
            encrypt_text += text[i][j]
    encrypt_text += ' '

print(encrypt_text)




'''Простая угадайка
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
'''




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



