"""
✅
Лабораторная работа № 3 - АиСД
С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D	Е
С	В
Каждая из матриц B, C, D, E имеет вид:
     4
  3     1
     2

Вариант 2:
Формируется матрица F следующим образом:
если в С количество положительных элементов в четных столбцах в области 2 больше,
чем количество отрицательных элементов в нечетных столбцах в области 4,
то поменять в С симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется.
После чего вычисляется выражение: (F+A)*AT – K * F.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random
import os
print("--- Начало работы --- ")
count_positive_elements = 0  # Кол-во положительных элементов
count_negative_elements = 0  # кол-во отрицательных элементов

def multiply_matrix(m1, m2):
    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]

def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print("{:10d}".format(arr[i][j]), end="")
        print()

while True:
    try:
        # Выборы вариантов работы
        print("--- Выбор варианта работы --- ")
        print("[0] - Если вы хотите использовать целенаправленное заполнение матрицы")
        print("[1] - Если вы хотите использовать случайное заполнение матрицы")
        print("[2] - Выход из программы")
        choice = int(input("Введите номер варианта: "))
        if choice == 0:
            # Целенаправленное заполнение матрицы
            print("--- Целенаправленное заполнение матрицы --- ")
            print("Пример матрицы 10x10")
            N = 10
            A = [[2, -7, 4, 3, -4, 10, 1, 0, 2, 7], 
                 [-9, 9, -9, 2, -2, -9, 5, 10, 4, -4], 
                 [-7, 2, 3, 6, 6, 4, 0, 6, 4, -1], 
                 [3, 2, 9, 1, -5, -4, 5, 5, -9, 7], 
                 [-3, -2, -4, 5, -7, -5, 10, -10, 6, 5], 
                 [8, 6, 2, -6, 1, 1, 0, 1, 0, 5], 
                 [-3, 5, -1, 10, 10, 4, -9, -5, 2, -6], 
                 [8, -4, 5, 10, -2, 8, 8, -5, -5, -3], 
                 [2, 8, -10, 7, -1, -7, -6, -3, 3, -6], 
                 [1, -10, 5, -1, 1, -9, -8, 9, -6, 8]]
        elif choice == 1:
            # Случайное заполнение матрицы
            print("--- Случайное заполнение матрицы --- ")
            N = int(input("Введите число N: "))
        elif choice == 2:
            print("--- Выход из программы --- ")
            os._exit(0)
        else:
            print("--- Неизвестная команда! Перезапустите программу --- ")
            os._exit(0)
        K = int(input("Введите число K: "))
        # Примечание! Т.к в ЛР, матрица состоит из 4-х равных по размерам под матриц следует что N % 2 == 0 и N >= 6
        middle_line = N // 2  # Размерность под матрицы D, E, C, B и средняя линия
        if N % 2 == 0 and N >= 6:
            # Создаем матрицу A NxN и заполняем ее вручную
            print("Матрица A:")
            A = [[0 for i in range(N)] for j in range(N)]
            for i in range(N):
                for j in range(N):
                    A[i][j] = random.randint(-10, 10)
                    print("{:5d}".format(A[i][j]), end="")
                print()
            break
        else:
            print("Т.к матрица состоит из 4-х равных по размерам под матриц следует что N % 2 == 0 и N >= 6")
    except:
        raise ValueError
        print("Некорректный запрос! Повторите попытку.")


D = [[A[i][j] for j in range(N // 2)] for i in range(N//2)]
E = [[A[i][j] for j in range(N // 2, N)] for i in range(0, N//2)]
C = [[A[i][j] for j in range(N // 2)] for i in range(N//2, N)]
B = [[A[i][j] for j in range(N // 2, N)] for i in range(N//2, N)]

F = [[A[i][j] for j in range(N)] for i in range(N)] # Матрица F, при этом матрица А не меняется
# Работаем с C - область 2
# если в С количество положительных элементов в четных столбцах в области 2 больше
for i in range((middle_line // 2) + 1, middle_line): #3 4
    for j in range(middle_line-i, i): # 1 3
        # print(i,j) # индексы
        if j % 2 != 0 and C[i][j] > 0:
            count_positive_elements += 1
print("Кол-во положительных элементов в чётных столбцах: ", count_positive_elements)


# чем количество отрицательных  элементов в нечетных столбцах в области 4
for i in range(0, middle_line // 2): #0 3
    for j in range(i+1, (middle_line - i)-1): # 6 12
        # print(i,j) # индексы
        if j % 2 == 0 and E[i][j] < 0:
            count_negative_elements += 1
print("Кол-во отрицательных элементов в нечётных столбцах: ", count_negative_elements)


# Выполняется условие
print("-"*50)
if count_positive_elements > count_negative_elements:
    print("Количество положительных элементов в четных столбцах в области 2 больше, чем количество отрицательных  элементов в нечетных столбцах в области 4")
    # то поменять в С симметрично области 1 и 3 местами
    for i in range(0, middle_line+1):
        for j in range(i+1, (middle_line - i)-1):
            # print(j,i) # Индексы области 3
            # print(j, middle_line-i-1) # Индексы области 1
            C[j][i], C[j][middle_line-i-1] = C[j][middle_line-i-1], C[j][i]
else:
    # иначе С и Е поменять местами несимметрично
    print("Количество положительных элементов в четных столбцах в области 2 меньше, чем количество отрицательных  элементов в нечетных столбцах в области 4")
    C, E = E, C

# Формируем матрицу F
# Собираю матрицу F из D C E B

print()
for i in range(N // 2):
    for j in range(N // 2):
        F[i][j] = D[i][j]  # D

for i in range(N // 2):
    for j in range(N // 2, N):
        F[i][j] = E[i][j - (N // 2)]  # E

for i in range(N // 2, N):
    for j in range(N // 2):
        F[i][j] = C[i - N // 2][j]  # C

for i in range(N // 2, N):
    for j in range(N // 2, N):
        F[i][j] = B[i - N // 2][j - N // 2]  # B

# При этом матрица А не меняется.
print("Матрица A:")
print_matrix(A) # Матрица A остаётся неизменной

# Выводятся по мере формирования А, F и все матричные операции последовательно.
# После чего вычисляется выражение: (F+A)*AT – K * F. 
# 1) AT (транспанирование)
# 2) K * F
# 3) F+A
# 4) (F+A)*AT
# 5) (F+A)*AT – K * F

# Операции
# 1) AT (транспанирование)
# Ручное транспонирование
transposed_A = [[0] * N for _ in range(N)]  # Создаем пустую матрицу для транспонирования

for i in range(N):
    for j in range(N):
        transposed_A[j][i] = A[i][j]  # Меняем местами индексы

print()
print("Матрица AT:")
print_matrix(transposed_A)
print()
# Проверка матриц
# 2) K * F
KF = [[K * F[i][j] for j in range(N)] for i in range(N)] # Матрица F
print("Матрица F:")
print_matrix(F)
print()
print("Матрица KF:")
print_matrix(KF)
# 3) F+A
F_A = [[F[i][j] + A[i][j] for j in range(N)] for i in range(N)]
print()
print("Матрица F_A:")
print_matrix(F_A)
# 4) (F+A)*AT
F_A_AT = multiply_matrix(F_A, transposed_A)
print()
print("Матрица F_A_AT:")
print_matrix(F_A_AT)
# 5) (F+A)*AT – K * F
F_A_AT_KF = [[F_A_AT[i][j] - KF[i][j] for j in range(N)] for i in range(N)]
print()
print("Матрица F_A_AT_KF:")
print_matrix(F_A_AT_KF)
print()
print("--- Конец работы --- ")