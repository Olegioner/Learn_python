'''На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
а затем все положительные числа, каждое на отдельной строке.
Числа должны быть выведены в том же порядке, в котором они были введены.'''

# Это тупо, но работает
''' n = int(input())
list_num = []
list_1 = []
list_2 = []
list_0 = []
list_result = []
for _ in range(n):
    list_num.append(int(input()))
for e in list_num:
    if e > 0:
        list_2.append(e)
    elif e == 0:
        list_0.append(e)
    elif e < 0:
        list_1.append(e)
list_result = list_1 + list_0 + list_2
print(*list_result, sep='\n')'''






'''На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем
k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки,
в которых встречаются одновременно все поисковые запросы.'''

'''n = int(input())
list_string = []
list_query = []
flag = 'YES'
for _ in range(n):
    list_string.append(input())
k = int(input())
for _ in range(k):
    list_query.append(input())
for i in range(n):
    for j in range(k):
        if list_query[j].lower() in list_string[i].lower():
            flag = 'YES'
        else:
            flag = 'NO'
            break
    if flag == 'YES':
        print(list_string[i])'''





'''На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.'''
'''
n = int(input())
list_string = []
for _ in range(n):
    list_string.append(input())
query = input().lower()
for i in range(n):
    if query in list_string[i].lower():
        print(list_string[i])
    else:
        continue'''



'''На вход программе подается натуральное число n, а затем n строк.
 Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.'''

'''n = int(input())
list_string = []
for _ in range(n):
    text = input()
    if text in list_string:
        continue
    else:
        list_string.append(text)
print(*list_string, sep = '\n')'''



'''При анализе данных, собранных в рамках научного эксперимента,
бывает полезно удалить самое большое и самое маленькое значение.'''

'''n = int(input())
list_num = []
for _ in range(n):
    list_num.append(int(input()))
del list_num[list_num.index(max(list_num))]
del list_num[list_num.index(min(list_num))]
print(*list_num, sep='\n')'''


'''На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая для каждого введенного числа x выводит значение функции
f(x)=x**+2x+1, каждое на отдельной строке.'''
'''n = int(input())
list_cur = []
list_result = []
for _ in range(n):
    x =int(input())
    list_cur.append(x)
    list_result.append((x**2) + 2 * x +1)
print(*list_cur, sep='\n')
print()
print(*list_result, sep='\n')'''




'''На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая создает список из символов всех строк, а затем выводит его.'''

'''n = int(input())
list_char = []
for _ in range(n):
    list_char.extend(input())
print(list_char)'''



'''На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
k-ую букву из введенных строк на одной строке без пробелов.'''
'''n = int(input())
list_string = []
for _ in range(n):
    list_string.append(input())
k = int(input())
for i in range(n):
    if len(list_string[i]) >= k:
        print((list_string[i])[k-1], end='')
    else:
        continue'''



'''На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам,
а затем выводит полученный список.'''

'''n = int(input())
list_even = []
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        list_even.append(num)
print(list_even)'''



'''На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел.
Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел '''
'''n = int(input())
num1 = int(input())
list_sum = []
for i in range(n-1):
    num2 =int(input())
    list_sum.append(num1 + num2)
    num1 = num2
print(list_sum)'''


'''На вход программе подается натуральное число n.
Напишите программу, которая создает список, состоящий из делителей введенного числа.'''

'''n = int(input())
list_div = []
for i in range(1, n+1):
    if n % i == 0:
        list_div.append(i)
    else:
        continue
print(list_div)'''
'''На вход программе подается натуральное число n, а затем
n целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.'''
'''n = int(input())
list_quad = []
for _ in range(n):
    num = int(input())
    list_quad.append(num**3)
print(list_quad)'''

'''Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]'''
'''alphabet = []
for i in range(1,27):
    alphabet.append((chr(96+i))*i)
print(alphabet)'''

'''На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая создает из указанных строк список и выводит его.'''
'''n = int(input())
list_n = []
for _ in range(n):
    text = input()
    list_n.append(text)
print(list_n)'''