#Моя версия шифра Цезаря
print('Добро пожаловать!')
ans = input('Шифруем или дешифруем? (1 - шифруем/2 - дешифруем)',)
lang = input('С каким языком работаем? (1 - ru/2 - eng)',)
alphabet_ru_up = [chr(el) for el in range(1040, 1072)]
alphabet_ru_low = [chr(el) for el in range(1072, 1104)]
alphabet_eng_up = [chr(el) for el in range(65, 91)]
alphabet_eng_low = [chr(el) for el in range(97, 123)]
def it_encrypt(lang, text, key):
    alphabet = [[],[]]
    if lang == '1':
        alphabet[0] = alphabet_ru_up
        alphabet[1] = alphabet_ru_low
        n = 33
    else:
        alphabet[0] = alphabet_eng_up
        alphabet[1] = alphabet_eng_low
        n = 26
    encrypt_text = ''
    for el in text:
        if el in alphabet[0]:
            symbol = alphabet[0].index(el)
            encrypt_text += alphabet[0][(symbol + key) % n]
        elif el in alphabet[1]:
            symbol = alphabet[1].index(el)
            encrypt_text += alphabet[1][(symbol + key) % n]
        elif el in ' ,.-:;!?':
            encrypt_text += el
    return encrypt_text

def it_decrypt(lang, text, key):
    alphabet = [[],[]]
    if lang == '1':
        alphabet[0] = alphabet_ru_up
        alphabet[1] = alphabet_ru_low
        n = 32
    else:
        alphabet[0] = alphabet_eng_up
        alphabet[1] = alphabet_eng_low
        n = 26
    encrypt_text = ''
    for el in text:
        if el in alphabet[0]:
            symbol = alphabet[0].index(el)
            encrypt_text += alphabet[0][(symbol - key) % n]
        elif el in alphabet[1]:
            symbol = alphabet[1].index(el)
            encrypt_text += alphabet[1][(symbol - key) % n]
        elif el in ' ,.-:;!?':
            encrypt_text += el
    return encrypt_text
key = int(input('Введите размер сдвига(ключ):',))

if ans == '1':
    print('Введите строку для шифрования')
    string = input()
    print('Результат:', it_encrypt(lang, string, key))
if ans == '2':
    print('Введите строку для дешифрования')
    string = input()
    print('Результат:', it_decrypt(lang, string, key))



