'''Все книги в домашней библиотеке Душнилы, друга Сэма, должны быть обязательно отсортированы по возрастанию:
сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям.
Напишите программу, которая проверяет, верно ли отсортированы книги.'''

n = int(input())
book_one = input()
flag = 'YES'
for i in range(n-1):
    book = input()
    book = book[:book.find(' ')] + ' ' + book[book.find('«'):]
    book_one = book_one[:book_one.find(' ')] + ' ' + book_one[book_one.find('«'):]
    if book > book_one:
        flag = 'YES'
    else:
        flag = "NO"
        break
    book_one = book
print(flag)

'''На вход программе подаются 3 различных слова.
Вам необходимо отсортировать эти слова по возрастанию в лексикографическом порядке и
вывести их на одной строке, разделяя символом пробела.'''

'''a = input()
b = input()
c = input()
mx_string = max(a,b,c)
mn_string = min(a,b,c)
if mn_string < a < mx_string:
    average_string = a
elif mn_string < b < mx_string:
    average_string = b
elif mn_string < c < mx_string:
    average_string = c
print(mn_string, average_string, mx_string)'''


'''На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно,
не учитывая регистр и игнорируя все небуквенные символы.
Программа должна вывести «YES», если строки окажутся равны в результате такой проверки,
или «NO» в противном случае.
text_one = input().lower()
text_two = input().lower()
text_one_new, text_two_new = '', ''
for e in text_one:
    if e.isalpha() == True:
        text_one_new += e
for e in text_two:
    if e.isalpha() == True:
        text_two_new += e
result = 'YES'
for i in range(len(text_one_new)):
    if len(text_two_new) == len(text_one_new):
        if text_one_new[i] == text_two_new[i]:
            result = 'YES'
        else:
            result = 'NO'
    else:
        result = 'NO'
print(result)'''

'''Напишите программу, которая принимает натуральное число n, а далее n названий классов,
каждое на новой строке. Для каждого названия класса ваша программа должна выводить на отдельной
строке «YES» (без кавычек), если название класса корректное, или «NO» (без кавычек) в противном случае

n = int(input())
for _ in range(n):
    num_class = input()
    if len(num_class) == 2:
        if num_class[0] in '0123456789' and num_class[1] in 'АБВГДЕЖЗИЙКЛМНОП':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')'''

'''В некотором наборе слов Сэм находит "волшебное" число по следующему алгоритму:
берет самую "маленькую" и самую "большую" строки, перемножает Unicode-коды последних
символов этих строк и возводит полученное число в квадрат. Результатом и является "волшебное" число.

На вход программе подаются 4 слова. Найдите "волшебное" число в этом наборе слов.

mx_string = ''
mn_string = 'яяя'
i = 4
while i > 0:
    text = input()
    mx_string = max(mx_string, text)
    mn_string = min(mn_string, text)
    i-=1
mx_string_last_letter = ord(mx_string[len(mx_string) - 1])
mn_string_last_letter = ord(mn_string[len(mn_string) - 1])
print((mx_string_last_letter * mn_string_last_letter)**2)'''




'''Напишите программу, которая находит в данной последовательности максимальную и минимальную строки
(в лексикографическом порядке) и выводит их в следующем формате:

Минимальная строка ⬇️: <минимальная строка>
Максимальная строка ⬆️: <максимальная строка>


mx_string = ''
min_string = 'яяяяяя'
text = input()
while text != 'КОНЕЦ':
    mx_string = max(text, mx_string)
    min_string = min(text, min_string)
    text = input()
print(f'Минимальная строка ⬇️: {min_string}')
print(f'Максимальная строка ⬆️: {mx_string}')
'''



