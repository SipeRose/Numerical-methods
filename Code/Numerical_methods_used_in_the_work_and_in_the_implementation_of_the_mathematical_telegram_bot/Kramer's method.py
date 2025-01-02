#  Решение СЛАУ методом Крамера
import numpy as np


def Kramer(matrix):
    matrix_size = np.shape(matrix)
    A = np.zeros((matrix_size[0], matrix_size[0]))
    f = np.zeros((matrix_size[0], 1))

    for i in range(matrix_size[0]):
        f[i] = matrix[i, matrix_size[1] - 1]

        for j in range(matrix_size[1] - 1):
            A[i, j] = matrix[i, j]

    D = np.linalg.det(A)  # Главный определитель
    if D == 0:  # Невозможность решения
        return

    list_of_Dn = []

    for i in range(matrix_size[0]):
        Dn = A.copy()
        Dn[:, i] = f[:, 0]
        list_of_Dn.append(np.linalg.det(Dn))

    solution = []
    for i in range(matrix_size[0]):
        solution.append(list_of_Dn[i]/D)

    return solution
