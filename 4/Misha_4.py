"""
Михаил Айдашкин ИСТбд-23
С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для отладки использовать не случайное заполнение, а целенаправленное.
Вид матрицы А:
Для ИСТд-13
D	Е
С	В

Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графика.
Программа должна использовать функции библиотек numpy  и mathplotlib

Вариант №2.
Формируется матрица F следующим образом:
скопировать в нее А и если в С количество положительных элементов в четных столбцах больше,
чем количество отрицательных элементов в нечетных столбцах,
то поменять местами С и В симметрично,
иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение:
A*AT – K * F*A-1,
иначе вычисляется выражение (К*A-1 +G-FТ) * K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import copy
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt

print("Тестирование: Целенаправленное")
K = int(input("Введите число K:"))
print("Для тестирования будем использовать матрицу 6x6")
N = 6
# M - middle_line средняя линия
M = N // 2

count_of_positive_elements = 0 # кол-во положительных элементов
count_of_negative_elements = 0 # кол-во отрицательных элементов


print("Матрица B :")
b = np.array([[-27,61,39], [88,-63,52], [45,-92,-37]])
print(b, '\n')
print("Матрица C :")
c = np.array([[-67,-39,96], [25,-45,31], [39,60,-40]])
print(c, '\n')
print("Матрица D :")
d = np.array([[43,-52,79], [73,92,-42], [82,28,92]])
print(d, '\n')
print("Матрица E :")
e = np.array([[96,-90,-32], [50,12,67], [-83,82,-73]])
print(e, '\n')

print("Матрица A: ")
a = np.vstack(((np.hstack([d, e])), (np.hstack([c, b]))))
print(a)

# Детерминант
det_A = int(np.linalg.det(a))
# G-нижняя треугольная матрица, полученная из А
g = np.tri(N) * a
# Матрица F
f = copy.deepcopy(a)

# Работаем с C
for i in range(0, len(c)):
    for j in range(0, len(c)):
        print(i,j)
        if j % 2 == 0 and c[i][j] > 0: # нечётные столбцы
            count_of_positive_elements += 1
        elif j % 2 == 1 and c[i][j] < 0: # нечётные столбцы
            count_of_negative_elements += 1

print(count_of_positive_elements, count_of_negative_elements)


if count_of_positive_elements > count_of_negative_elements:
    # меняем C и B симметрично
    f[M:N, M:N] = np.fliplr(c)
    f[M:N, :M] = np.fliplr(b)
else:
    # иначе С и Е поменять местами несимметрично
    f = np.vstack(((np.hstack([d, c])), (np.hstack([e, b]))))

print("Матрица F")
print(f)
# Сумма Диагональных элементов
summ_diagonal_elements = sum(np.diagonal(f))

if det_A > summ_diagonal_elements:
    # A*AT – K * F*A-1
    """
    1) a ** t
    2) a * a ** t
    3) a ** -1
    4) f * a ** -1
    5) k * f * a ** -1
    6) (a * a ** t) - (k * f * a ** -1)
    """
    print("A ** T")
    a_t = np.transpose(a) # 1
    print(a_t)

    print("A * A ** t")
    a_a_t = np.dot(a, a_t) # 2
    print(a_a_t)

    print("A ** -1")
    reverse_a = np.linalg.inv(a) # 3
    print(reverse_a)

    print("F * A ** - 1")
    f_reverse_a = np.dot(f, reverse_a) # 4
    print(f_reverse_a)

    print("K * F * A ** - 1")
    kf_reverse_a = K * f_reverse_a  # 5
    print(kf_reverse_a)

    print("(a * a ** t) - (k * f * a ** -1)")
    result = a_a_t - kf_reverse_a
    print(result)

else:
    # (К*A-1 +G-FТ) * K
    """
    1) a ** -1
    2) k * a ** -1
    3) f ** t
    4) G-FТ
    5) (k * a ** -1) + (G-FТ)
    6) (k * a ** -1 + G-FТ) * K
    """
    print("A ** -1")
    reverse_a = np.linalg.inv(a)  # 1
    print(reverse_a)

    print("K * A ** -1")
    k_reverse_a = K * reverse_a # 2
    print(reverse_a)

    print("F ** T")
    f_t = np.transpose(f)  # 3
    print(f_t)

    print("G - F ** T")
    g_ft = g - f_t   # 4
    print(g_ft)

    print("(K * A ** -1) + (G-FТ)")
    ka_gft = k_reverse_a + g_ft  # 5
    print(ka_gft)

    print("((K * A ** -1) + (G-FТ) ) * K")
    result = ka_gft * K
    print(result)

# Графики (визуализация)
column_index = 0
data = f[:, column_index]

# Создание графиков
plt.figure(figsize=(12, 10))

# 1. Точечный график
plt.subplot(2, 2, 1)  # 2 строки, 2 колонки, 1-й график
plt.scatter(np.arange(len(data)), data, color='blue', label='Scatter Plot')
plt.title('Scatter Plot of Column 1')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.grid()
plt.legend()

# 2. Стеблевый график
plt.subplot(2, 2, 2)  # 2 строки, 2 колонки, 2-й график
plt.stem(np.arange(len(data)), data, basefmt=" ")
plt.title('Stem Plot of Column 1')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.grid()

# 3. Линейный график
plt.subplot(2, 2, 3)  # 2 строки, 2 колонки, 3-й график
plt.plot(np.arange(len(data)), data, marker='o', label='Line Plot', color='orange')
plt.title('Line Plot of Column 1')
plt.xlabel('Row Index')
plt.ylabel('Value')
plt.grid()
plt.legend()

# 4. Гистограмма
plt.subplot(2, 2, 4)  # 2 строки, 2 колонки, 4-й график
plt.hist(data, bins=10, alpha=0.7, label='Histogram', color='green')
plt.title('Histogram of Column 1')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()