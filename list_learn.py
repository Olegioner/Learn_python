




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