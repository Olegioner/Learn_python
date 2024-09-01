ans = input('Перевод в десятичную или из десятичной? (1 - в десятичную/ 2 - из десятичной)',)
list_num = ['A', 'B', 'C', 'D', 'E','F']
if ans == '1':
    n = int(input('Введите систему исчислений из какой переводим:'))
    print('Введите число')
    digit = list(input())
    digit.reverse()
    result = 0
    if n != 16:
        for i in range(len(digit) ):
            result += int(digit[i]) * n**i
    elif n == 16:
        for i in range(len(digit)):
            if digit[i] in list_num:
                digit_in_list = (int(list_num.index(digit[i])) + 10)
                result += digit_in_list * n**i
            else:
                result += int(digit[i]) * n**i
    print(result)
elif ans == '2':
    n = int(input('Введите систему исчислений в какую переводим:'))
    print('Введите число')
    digit = int(input())
    res = ''
    if n != 16:
        while digit > 0:
            res = str(digit % n) + res
            digit = digit // n
    elif n == 16:
        while digit > 0:
            if 10 <= digit % n <= 15:
                res = list_num[digit % n - 10] + res
                digit = digit // n
            else:
                res = str(digit % n) + res
                digit = digit // n
    print(res)



