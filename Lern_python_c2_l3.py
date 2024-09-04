'''На шахматной доске 8×8 стоит конь.
Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьёт конь.
Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые бьёт конь, отметьте символами *,
остальные клетки заполните точками.'''
desk = [['.' for el in range(8)] for _ in range(8)]
alpha = [chr(el) for el in range(97,105)]
start = list(input())
ind_start =[alpha.index(start[0])]
ind_start.append(8-int(start[1]))
for i in range(len(desk)):
    for j in range(len(desk)):
        if i == ind_start[1] and j == ind_start[0]:
            desk[i][j] = 'N'
            print(desk[i][j], end=' ')
        else:
            print(desk[i][j], end=' ')
    print()

print(ind_start)

'''Напишите программу, которая поворачивает квадратную матрицу чисел на 90 по часовой стрелке.'''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for j in range(n):
#     for i in range(n):
#         print(matrix[n-1-i][j], end=' ')
#     print()


'''Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает
её элементы относительно горизонтальной оси симметрии.'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         print(matrix[n-i-1][j], end=' ')
#     print()

'''зеркально по вертикали'''
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][n-j-1], end=' ')
#     print()
'''Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и
побочной диагонали, при этом каждый элемент должен остаться в том же столбце
(то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     matrix[i][i], matrix[n-1-i][i] = matrix[n-1-i][i], matrix[i][i]
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()


'''Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# matrix_t = [[matrix[j][i] for j in range(n)] for i in range(n)]
# if matrix == matrix_t:
#     print('YES')
# else:
#     print('NO')





'''Напишите программу, которая меняет местами столбцы в матрице.'''
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# text = input().split()
# a, b = int(text[0]), int(text[1])
#
# for i in range(len(matrix)):
#     matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
#
# for row in matrix:
#     print(*row)


'''На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице, затем
n строк по m целых чисел в каждой, отделенных символом пробела.
Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.'''
# n, m = int(input()),int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# ind_i, ind_j = 0, 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > matrix[ind_i][ind_j]:
#             ind_i, ind_j = i, j
# print(ind_i, ind_j)


'''На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице. Создайте матрицу
n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.'''

# n, m = int(input()),int(input())
# matrix = [[i * j for j in range(m)] for i in range(n)]
# for string in matrix:
#     for el in string:
#         print(str(el).ljust(3), end=' ')
#     print()

'''Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.'''
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# matrix_int = [[int(matrix[i][j]) for j in range(n)] for i in range(n)]
# sm_up, sm_right, sm_left, sm_down = 0, 0, 0, 0,
# for i in range(n):
#     for j in range(n):
#         if i < j and i < n - 1 - j:
#             sm_up += matrix_int[i][j]
#         if i < j and i > n - 1 - j:
#             sm_right += matrix_int[i][j]
#         if i > j and i > n - 1 - j:
#             sm_down += matrix_int[i][j]
#         if i > j and i < n - 1 - j:
#             sm_left += matrix_int[i][j]
#
# print('Верхняя четверть:', sm_up)
# print('Правая четверть:', sm_right)
# print('Нижняя четверть:', sm_down)
# print('Левая четверть:',sm_left)


'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''
'''n = int(input())
matrix = [input().split() for _ in range(n)]
matrix_int = [[int(matrix[i][j]) for j in range(n)] for i in range(n)]
maximum = matrix_int[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j):
            if matrix_int[i][j] > maximum:
                maximum = matrix_int[i][j]
print(maximum)'''

'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# matrix_int = [[int(matrix[i][j]) for j in range(n)] for i in range(n)]
# maximum = matrix_int[0][0]
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             continue
#         elif i >= j and matrix_int[i][j] > maximum:
#             maximum = matrix_int[i][j]
# print(maximum)

'''Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки.'''

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# matrix_int = [[int(matrix[i][j]) for j in range(n)] for i in range(n)]
# for i in range(n):
#     count = 0
#     average = sum(matrix_int[i]) / len(matrix_int[i])
#     for j in range(n):
#         if average < matrix_int[i][j]:
#             count +=1
#     print(count)

'''Следом квадратной матрицы называется сумма элементов главной диагонали.
Напишите программу, которая выводит след заданной квадратной матрицы.'''
# n = int(input())
# sm = 0
# matrix = [input().split() for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             sm += int(matrix[i][j])
# print(sm)


'''На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице.
Далее вводятся сами элементы матрицы —
слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.
Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы,
выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.'''
'''n_row, n_el = int(input()),int(input())
matrix = []
for row in range(n_row):
    temp = [input() for el in range(n_el)]
    matrix.append(temp)
    print(*temp)
print()
for i in range(n_el):
    for j in range(n_row):
        print(matrix[j][i], end=' ')
    print()'''







'''text = input().split()
res = [[]]

for i in range(len(text)):
    for j in range(0,len(text)-i):
        res.append(text[j:j+i+1])

print(res)
'''


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
