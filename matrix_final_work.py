'''На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 0;
на двух диагоналях, прилегающих к главной, – число 1;
на следующих двух диагоналях – число 2, и т.д.'''

n = int(input())
matrix = [[abs(i - j) for j in range(n) if abs(i - j) == abs(j - i)] for i in range(n)]
for row in matrix:
     for el in row:
         print(el, end=' ')
     print()




'''На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните точками.'''

# desk = [['.' for el in range(8)] for _ in range(8)]
# alpha = [chr(el) for el in range(97,105)]
# start = list(input())
# ind_start =[alpha.index(start[0])]
# ind_start.append(8-int(start[1]))
# for i in range(len(desk)):
#     for j in range(len(desk)):
#         if i == ind_start[1] and j == ind_start[0]:
#             desk[i][j] = 'Q'
#             print(desk[i][j], end=' ')
#         elif (ind_start[1] + ind_start[0]) == (i + j):
#             print('*', end=' ')
#         elif (ind_start[1] - ind_start[0]) == (i - j):
#             print('*', end=' ')
#         elif ((ind_start[1] == i) and (ind_start[0] != j)) or ((ind_start[1] != i) and (ind_start[0] == j)):
#             print('*', end=' ')
#         else:
#             print('.', end=' ')
#     print()

'''Латинским квадратом порядка n называется квадратная матрица размером n×n,
каждая строка и каждый столбец которой содержат все числа от 1 до n.
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.'''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# flag = 'YES'
# sm_n = int((n*(n + 1))/2)
# for i in range(n):
#     sm = 0
#     for j in range(n):
#         sm += matrix[i][j]
#     if sm > sm_n or sm < sm_n:
#         flag = 'NO'
#         break
# for j in range(n):
#     sm = 0
#     for i in range(n):
#         sm += matrix[i][j]
#     if sm > sm_n or sm < sm_n:
#         flag = 'NO'
#         break
#
# print(flag)


'''Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.'''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# flag = 'YES'
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[n-j-1][n-i-1]:
#             flag = 'NO'
#             break
# print(flag)

'''На вход программе подается нечетное натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив её символами . .
Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
Выведите полученную матрицу на экран, разделяя элементы пробелами.'''
# n = int(input())
# matrix = [['.' for _ in range(n)] for _ in range(n)]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == j or i == n - 1 -j or j == n // 2 or i == n // 2:
#             matrix[i][j] = '*'
#             print(matrix[i][j], end=' ')
#         else:
#             print(matrix[i][j], end=' ')
#     print()

'''Напишите программу, которая транспонирует квадратную матрицу.'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for j in range(len(matrix)):
#     for i in range(len(matrix)):
#         print(matrix[i][j], end=' ')
#     print()

'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# mx = 0
# if n == 1:
#     mx = matrix[0]
#     print(*mx)
# else:
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if (i <= j and i >= n - 1 - j) or (i >= j and i >= n - 1 - j):
#                 mx = max(matrix[i][j], mx)
#     print(mx)




'''На вход программе подается строка текста, содержащая символы и число n. Из данной строки формируется список.
Напишите программу, которая разделяет список на вложенные подсписки так, что n последовательных элементов принадлежат разным подспискам.'''

# text = input().split()
# n = int(input())
# matrix = [[text[i] for i in range(k,len(text),n)] for k in range(n)]
# print(matrix)
