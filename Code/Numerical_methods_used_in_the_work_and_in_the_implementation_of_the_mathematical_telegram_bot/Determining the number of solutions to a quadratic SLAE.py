# Определение количества решений СЛАУ с квадртаной матрицей
import numpy as np


def value_of_solution(matrix):

    matrix_size = np.shape(matrix)
    A = np.zeros((matrix_size[0], matrix_size[0]))
    f = np.zeros((matrix_size[0], 1))

    for i in range(matrix_size[0]):

        f[i] = matrix[i, matrix_size[1] - 1]

        for j in range(matrix_size[1] - 1):
            A[i, j] = matrix[i, j]

    D = np.linalg.det(A)  # Главный определитель
    list_of_Dn = []

    for i in range(matrix_size[0]):
        Dn = A.copy()
        Dn[:, i] = f[:, 0]
        list_of_Dn.append(np.linalg.det(Dn))

    summa = 0

    for i in list_of_Dn:
        summa = summa + abs(i)

    if summa == 0 and D == 0:
        print('Система имеет бесконечно много решений')
    elif D == 0 and summa != 0:
        print('Система не имеет решений')
    else:
        print('Система имеет единственное решение')
