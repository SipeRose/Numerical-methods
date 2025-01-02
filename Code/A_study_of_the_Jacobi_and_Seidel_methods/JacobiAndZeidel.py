import random
import numpy as np
import math


Xlabel = np.zeros(201)
Ylabel1 = np.zeros(201)
Ylabel2 = np.zeros(201)

for i in range(201):
    Xlabel[i] = -1 + 0.01 * i
    Ylabel1[i] = -1 * Xlabel[i] ** 2 + 1
    Ylabel2[i] = abs(Xlabel[i]) - 1

x = np.zeros(100000)
y = np.zeros(100000)
areas = [math.pi * 1 ** 2 for i in range(100000)]

for w in range(2, 6):  # Размеры матриц 2х2, 3х3, 4х4, 5х5

    JJ = 0
    JS = 0
    AJAS = 0
    NJNS = 0
    summa1 = 0  # Количество удачных случаев для метода Якоби
    summa2 = 0  # Количество удачных случаев для метода Зейделя
    
    for i in range(1, 100001):  # Проверка для 100000 матриц одной размерности

        A = np.random.rand(w, w) * 100

        for qer in range(0, w):
            for j in range(0, w):
                A[qer, j] = random.randrange(-10, 10)
                if A[qer, j] == 0:
                    A[qer, j] = A[qer, j] + random.randrange(1, 10)

        if w == 3:
            p = -1 * (A[0, 2] * A[1, 1] * A[2, 0] + A[1, 2] * A[0, 0] * A[2, 1] + A[0, 1] * A[2, 2] * A[1, 0]) / (A[0, 0] * A[1, 1] * A[2, 2])
            q = (A[0, 2] * A[2, 1] * A[1, 0] + A[0, 1] * A[1, 2] * A[2, 0]) / (A[0, 0] * A[1, 1] * A[2, 2])
            a1 = A[0, 0] * A[1, 1] * A[2, 2]
            b1 = A[0, 1] * A[1, 2] * A[2, 0]

        # Метод Якоби
        L = np.random.rand(w, w)  # Нижнетреугольная матрица
        for a in range(0, w):
            for b in range(0, w):
                if a > b:
                    L[a, b] = A[a, b]
                else:
                    L[a, b] = 0

        D = np.random.rand(w, w)  # Диагональная матрица
        for a in range(0, w):
            for b in range(0, w):
                if a == b:
                    D[a, b] = A[a, b]
                else:
                    D[a, b] = 0

        R = np.random.rand(w, w)  # Верхнетреугольная матрица
        for a in range(0, w):
            for b in range(0, w):
                if a < b:
                    R[a, b] = A[a, b]
                else:
                    R[a, b] = 0

        # Ход метода Якоби
        L = L + R
        D = np.linalg.inv(D)
        B = D.dot(L)
        B = -1 * B
        eigenvalues = np.linalg.eig(B)  # Собственные значения матрицы -invD*(L+R)
        eigenvalues1 = eigenvalues[0]

        kJac = 0
        kZei = 0

        # Проверка модулей собственных значений для матриц разного размера и подсчет подходящих вариантов:
        if w == 2:

            if abs(eigenvalues1[0]) < 1 and abs(eigenvalues1[1]) < 1:
                summa1 += 1
                kJac = 1

        elif w == 3:

            if abs(eigenvalues1[0]) < 1 and abs(eigenvalues1[1]) < 1 and abs(eigenvalues1[2]) < 1:
                summa1 += 1
                kJac = 1

        elif w == 4:

            if abs(eigenvalues1[0]) < 1 and abs(eigenvalues1[1]) < 1 and abs(eigenvalues1[2]) < 1 and \
                    abs(eigenvalues1[3]) \
                    < 1:
                summa1 += 1
                kJac = 1

        elif w == 5:

            if abs(eigenvalues1[0]) < 1 and abs(eigenvalues1[1]) < 1 and abs(eigenvalues1[2]) < 1 and \
                    abs(eigenvalues1[3])\
                    < 1 and abs(eigenvalues1[4]) < 1:
                summa1 += 1
                kJac = 1

        # Метод Зейделя
        L = np.random.rand(w, w)  # Нижнетреугольная матрица
        for a in range(0, w):
            for b in range(0, w):
                if a > b:
                    L[a, b] = A[a, b]
                else:
                    L[a, b] = 0

        D = np.random.rand(w, w)  # Диагональная матрица
        for a in range(0, w):
            for b in range(0, w):
                if a == b:
                    D[a, b] = A[a, b]
                else:
                    D[a, b] = 0

        R = np.random.rand(w, w)  # Верхнетреугольная матрица
        for a in range(0, w):
            for b in range(0, w):
                if a < b:
                    R[a, b] = A[a, b]
                else:
                    R[a, b] = 0

        # Ход метода Зейделя
        L = L + D
        L = np.linalg.inv(L)
        B = L.dot(R)
        B = -1 * B
        eigenvalues = np.linalg.eig(B)  # Собственный значения матрицы -inv(L+D)*R
        eigenvalues2 = eigenvalues[0]

        # Проверка модулей собственных значений для матриц разного размера и подсчет подходящих вариантов:
        if w == 2:

            if abs(eigenvalues2[0]) < 1 and abs(eigenvalues2[1]) < 1:
                summa2 += 1
                kZei = 1

        elif w == 3:

            if abs(eigenvalues2[0]) < 1 and abs(eigenvalues2[1]) < 1 and abs(eigenvalues2[2]) < 1:
                summa2 += 1
                kZei = 1

        elif w == 4:

            if abs(eigenvalues2[0]) < 1 and abs(eigenvalues2[1]) < 1 and abs(eigenvalues2[2]) < 1 and \
                    abs(eigenvalues2[3])\
                    < 1:
                summa2 += 1
                kZei = 1

        elif w == 5:

            if abs(eigenvalues2[0]) < 1 and abs(eigenvalues2[1]) < 1 and abs(eigenvalues2[2]) < 1 and \
                    abs(eigenvalues2[3])\
                    < 1 and abs(eigenvalues2[4]) < 1:
                summa2 += 1
                kZei = 1

        if kJac == 1 and kZei == 0:

            # print(i, w, 'МЕТОД Якоби СХОДИТСЯ, А ЗЕЙДЕЛЯ НЕ СХОДИТСЯ ДЛЯ МАТРИЦЫ')
            # print(A)
            # print(eigenvalues1)
            # print(eigenvalues2)

            JJ += 1

        if kJac == 0 and kZei == 1:

            # print(i, w, 'Метод ЗЕЙДЕЛЯ сходится, а метод Якоби не сходится')
            # print(A)
            # print(eigenvalues1)
            # print(eigenvalues2)

            JS += 1

        if kJac == 1 and kZei == 1:

            # print(i, w, 'Сходится для обоих методов матрица')
            # print(A)
            # print(eigenvalues1)
            # print(eigenvalues2)

            AJAS += 1

        if kJac == 0 and kZei == 0:

            # print(i, w, 'РАСХОДЯТСЯ оба метода')
            # print(A)
            # print(eigenvalues1)
            # print(eigenvalues2)

            NJNS += 1

    print('Случай матрица', w, 'x', w)
    print('Якоби сходится:', summa1)
    print('Зейдель сходится:', summa2)
    print('Сходятся только для Якоби:', JJ)
    print('Сходятся только для Зейделя:', JS)
    print('Сходится и для Якоби, и для Зейделя:', AJAS)
    print('Не сходится ни для Якоби, ни для Зейделя:', NJNS)
    print('')
