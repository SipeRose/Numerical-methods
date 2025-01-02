# Нахождение меры обусловленности заданной матрицы
import numpy as np
import math


def measure_of_conditionality(matrix, p):

    x = np.random.randint(1, 5, size=(p, 1))  # Произвольный вектор
    a = x.copy()
    s = 0

    for i in range(p):
        s += x[i, 0]**2

    NormaX = math.sqrt(s)
    epsilon = 1e-6  # Точность
    y = 1 / NormaX * matrix.dot(x)  # Новый вектор (первый) из степенного метода
    z = x.transpose().dot(y)
    z = y - np.sign(z) * x
    s = 0

    for i in range(p):
        s += z[i, 0] ** 2

    NormaX = math.sqrt(s)  # Норма вектора, сравниваемого с epsilon
    if NormaX > epsilon:
        x = y.copy()

    while NormaX > epsilon:   # СТЕПЕННОЙ МЕТОД
        s = 0

        for i in range(p):
           s += x[i, 0] ** 2

        NormaX = math.sqrt(s)
        y = 1 / NormaX * matrix.dot(x)
        z = x.transpose().dot(y)
        z = y - np.sign(z) * x
        s = 0

        for i in range(p):
            s += z[i, 0] ** 2
        NormaX = math.sqrt(s)  # Норма вектора, сравниваемого с epsilon

        if NormaX > epsilon:
            x = y.copy()

    s = 0
    for i in range(p):
        s += x[i, 0] ** 2

    nA = abs((y[0, 0] / x[0, 0] * math.sqrt(s)))  # Норма матрицы А
    x = a.copy()  # Скопированный вначале вектор
    B = np.linalg.inv(matrix)  # Обратная матрица

    s = 0
    for i in range(p):
        s += x[i, 0] ** 2

    NormaX = math.sqrt(s)
    y = 1 / NormaX * B.dot(x)
    z = x.transpose().dot(y)
    z = y - np.sign(z) * x

    s = 0
    for i in range(p):
        s += z[i, 0] ** 2

    NormaX = math.sqrt(s)
    if NormaX > epsilon:
        x = y.copy()

    while NormaX > epsilon:   # СТЕПЕННОЙ МЕТОД
        s = 0

        for i in range(p):
            s += x[i, 0] ** 2
        NormaX = math.sqrt(s)
        y = 1 / NormaX * B.dot(x)
        z = x.transpose().dot(y)
        z = y - np.sign(z) * x

        s = 0
        for i in range(p):
            s += z[i, 0] ** 2

        NormaX = math.sqrt(s)
        if NormaX > epsilon:
            x = y.copy()

    s = 0
    for i in range(p):
        s += x[i, 0] ** 2

    nAm = abs((y[0, 0] / x[0, 0]) * math.sqrt(s))  # Норма обратной матрицы
    return nA * nAm
