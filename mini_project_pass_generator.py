import random
from random import randint

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
symbol_amb_list = 'il1Lo0O'
chars = ''
count_pass = input('Введите необходимое количество генерируемых паролей:',)
len_pass = input('Введите длину пароля:')
digit = input('Включать ли цифры (да/нет)')
let_low = input('Включать ли прописные буквы (да/нет)')
let_up = input('Включать ли строчные буквы (да/нет)')
symbol = input('Включать ли символы (да/нет)')
amb_symbol = input('Исключать ли неоднозначные символы - il1Lo0O (да/нет)')

if digit in ('д', 'да', 'yes', 'y'):
    chars += digits
if let_low in ('д', 'да', 'yes', 'y'):
    chars += lowercase_letters
if let_up in ('д', 'да', 'yes', 'y'):
    chars += uppercase_letters
if symbol in ('д', 'да', 'yes', 'y'):
    chars += punctuation
if amb_symbol in ('д', 'да', 'yes', 'y'):
    chars += symbol_amb_list
chars = list(chars)


def generate_password(length, chars):
    pass_word = ''
    for _ in range(length):
        n = randint(0, len(chars))
        pass_word += chars[n]
    return pass_word


for _ in range(int(count_pass)):
    print(generate_password(int(len_pass), chars))

