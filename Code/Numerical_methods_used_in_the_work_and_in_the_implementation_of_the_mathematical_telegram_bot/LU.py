#  Решение систем линейных алгебраических уравнений с помощью LU-разложения
import numpy as np


def LU(matrix):
    matrix_size = np.shape(matrix)
    A = np.zeros((matrix_size[0], matrix_size[0]))
    f = np.zeros((matrix_size[0], 1))

    for i in range(matrix_size[0]):

        f[i] = matrix[i, matrix_size[1] - 1]

        for j in range(matrix_size[1] - 1):
            A[i, j] = matrix[i, j]

    for i in range(matrix_size[0]):
        d = A[: i + 1, : i + 1]
        if np.linalg.det(d) == 0:
            print('Невозможно применить LU-разложение, так как есть нулевые главные миноры')
            return

    U = np.zeros(np.shape(A))
    L = np.zeros(np.shape(A))

    for i in range(matrix_size[0]):
        L[i, i] = 1
    U[0, 0] = A[0, 0]

    for i in range(1, matrix_size[0]):
        U[0, i] = A[0, i]
        L[i, 0] = A[i, 0] / U[0, 0]

    for i in range(1, matrix_size[0]):
        lu = 0

        for k in range(i):
            lu = lu + L[i, k] * U[k, i]
        U[i, i] = A[i, i] - lu

    for i in range(1, matrix_size[0]):
        for j in range(i + 1, matrix_size[0]):
            lu = 0
            lu1 = 0

            for k in range(i):
                lu = lu + L[i, k] * U[k, j]
                lu1 = lu1 + L[j, k] * U[k, i]

            U[i, j] = A[i, j] - lu
            L[j, i] = 1 / U[i, i] * (A[j, i] - lu1)
    y = np.linalg.inv(L).dot(f)
    x = np.linalg.inv(U).dot(y)
    return x
