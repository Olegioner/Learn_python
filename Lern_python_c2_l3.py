text = ['1', '2', '3','4']
res = []

for i in range(len(text)):
    for j in range(len(text)):
        res.append(text[j:j+i])


print(res)



'''На вход программе подаются две строки: на одной – символы, на другой – число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков (кусков) указанной длины.'''

'''def chunked(text, num):
    text = text.split()
    res = []
    while len(text) > 0:
        res.append(text[:num])
        text = text[num:]
    return res

string = '1 2 3 4 5 6 7 8 9'
n = 1

print(chunked(string, n))'''




'''На вход программе подается строка текста, содержащая символы.
Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.'''
'''s = input().split()
seq = [[s.pop(0)]]

for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])

print(seq)
'''

'''Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов,
имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы.
Каждое число равно сумме двух расположенных над ним чисел.'''
'''from math import factorial

n = int(input())
for i in range(n):
    print(*[round(factorial(i) / (factorial(el) * factorial(i - el))) for el in range(i+1)])'''
