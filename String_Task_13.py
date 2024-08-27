'''На вход программе подается строка текста. Расшифруйте текст, заменив все конструкции
[u-<номер символа в таблице Unicode>]
на соответствующие буквы русского алфавита, и выведите его.'''
message = input()
i = 0
while i < len(message):
    if message[i] == '[':
        cur_letter = chr(int(message[i + 3:i + 7]))
        print(cur_letter, end='')
        i += 8
    else:
        print(message[i],end='')
        i += 1




