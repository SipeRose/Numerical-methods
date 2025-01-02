#  Решение СЛАУ с СИММЕТРИЧЕСКОЙ матрицей методом квадратного корня (аналог LU для сим. матрицы)
import numpy as np
from math import sqrt


def sqrt_method(matrix):

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
            print('Невозможно применить, так как есть нулевые главные миноры')
            return

    D = np.zeros((matrix_size[0], matrix_size[0]))
    S = np.zeros((matrix_size[0], matrix_size[0]))

    for i in range(matrix_size[0]):
        sd = 0

        for k in range(i):
            sd = sd + abs(S[k, i]) ** 2 * D[k, k]

        D[i, i] = np.sign(A[i, i] - sd)
        S[i, i] = sqrt(abs(A[i, i] - sd))

        for j in range(i + 1, matrix_size[0]):
            ssd = 0

            for k in range(i):
                ssd = ssd + S[k, i] * S[k, j] * D[k, k]

            S[i, j] = (A[i, j] - ssd)/(S[i, i] * D[i, i])

    y = np.linalg.inv(np.transpose(S)).dot(f)
    x = np.linalg.inv(D.dot(S)).dot(y)

    return x
