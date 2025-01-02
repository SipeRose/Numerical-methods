# Решение СЛАУ с трехдиагональной матрицей методом прогонки (А — матрица + столбец свободных элементов; а, b - размер матрицы)
import numpy as np


def progonka(A, a, b):

    alpha1 = (-1) * A[0, 1]
    beta1 = A[0, b - 1]
    AlphaBeta = np.zeros((2, a - 1))
    AlphaBeta[0, 0] = alpha1
    AlphaBeta[1, 0] = beta1

    # Прямой ход метода прогонки
    for i in range(1, a - 1):
        AlphaBeta[0, i] = (-1) * (A[i, i + 1] / (A[i, i - 1] * AlphaBeta[0, i - 1] + A[i, i]))
        AlphaBeta[1, i] = (A[i, b - 1] - A[i, i - 1] * AlphaBeta[1, i - 1]) / (A[i, i - 1] * AlphaBeta[0, i - 1] + A[i, i])

    # Обратный ход метода прогонки
    y = np.zeros(a)  # Вектор решений
    k2 = -A[a - 1, b - 3]
    mu2 = A[a - 1, b - 1]
    y[a - 1] = (k2 * AlphaBeta[1, a - 2] + mu2) / (1 - k2 * AlphaBeta[0, a - 2])

    for i in range(a - 2, -1, -1):
        y[i] = AlphaBeta[0, i] * y[i + 1] + AlphaBeta[1, i]

    return y
