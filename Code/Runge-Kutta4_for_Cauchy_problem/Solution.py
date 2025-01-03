import numpy as np
from math import sin, pi, sqrt
from matplotlib import pyplot as plt
from prettytable import PrettyTable


# f1, f2, f3, f4 — функции правых частей нормальной системы ДУ
def f1(t, x_, x1_, y_, y1_):
    return x1_


def f2(t, x_, x1_, y_, y1_):
    return x_ * y_ * g(t) / (x_ ** 2 + y_ ** 2)


def f3(t, x_, x1_, y_, y1_):
    return y1_


def f4(t, x_, x1_, y_, y1_):
    return y_ ** 2 * g(t) / (x_ ** 2 + y_ ** 2) - g(t)


# Ускорение свободного падения
def g(t):
    return 9.81 + 0.05 * sin(2 * pi * t)


# Таблица численных решений для значений x и y. Ее столбцы: время, координата x, координата y
table = PrettyTable()
table.field_names = ['t', 'X', 'Y']

# Примечание: в данной реализации численного решения не применялось правило Рунге практической оценки погрешности,
# а разбиение временного интервала было постоянным и вводилось пользователем.

# Количество разбиений временного интервала
n = int(input('Введите количество разбиений: '))

# Временной интервал и шаг
a, b = 0, 2  # 100
h = (b-a) / n

# Массивы значений времени и численных решений системы ДУ соответственно
time = np.zeros((n + 1))
x = np.zeros((n + 1))
x1 = np.zeros((n + 1))
y = np.zeros((n + 1))
y1 = np.zeros((n + 1))

# Массив значений sqrt(x^2(t) + y^2(t))
L = np.zeros((n + 1))

# Начальные условия задачи Коши
U = np.array([[3.0],
              [-0.8],
              [-4.0],
              [-0.6]])


# Метод Рунге-Кутта 4-го порядка точности
K1 = np.zeros((4, 1))
K2 = np.zeros((4, 1))
K3 = np.zeros((4, 1))
K4 = np.zeros((4, 1))

for i in range(n + 1):
    table.add_row([f'{a + i*h: .3f}', f'{U[0, 0]: .5f}', f'{U[2, 0]: .5f}'])

    time[i] = a + i*h

    x[i] = U[0, 0]
    x1[i] = U[1, 0]
    y[i] = U[2, 0]
    y1[i] = U[3, 0]
    L[i] = sqrt(x[i] ** 2 + y[i] ** 2)

    K1[0, 0] = h * f1(time[i], x[i], x1[i], y[i], y1[i])
    K1[1, 0] = h * f2(time[i], x[i], x1[i], y[i], y1[i])
    K1[2, 0] = h * f3(time[i], x[i], x1[i], y[i], y1[i])
    K1[3, 0] = h * f4(time[i], x[i], x1[i], y[i], y1[i])

    K2[0, 0] = h * f1(time[i] + h/2, x[i] + K1[0, 0]/2, x1[i] + K1[1, 0]/2, y[i] + K1[2, 0]/2, y1[i] + K1[3, 0]/2)
    K2[1, 0] = h * f2(time[i] + h/2, x[i] + K1[0, 0]/2, x1[i] + K1[1, 0]/2, y[i] + K1[2, 0]/2, y1[i] + K1[3, 0]/2)
    K2[2, 0] = h * f3(time[i] + h/2, x[i] + K1[0, 0]/2, x1[i] + K1[1, 0]/2, y[i] + K1[2, 0]/2, y1[i] + K1[3, 0]/2)
    K2[3, 0] = h * f4(time[i] + h/2, x[i] + K1[0, 0]/2, x1[i] + K1[1, 0]/2, y[i] + K1[2, 0]/2, y1[i] + K1[3, 0]/2)

    K3[0, 0] = h * f1(time[i] + h/2, x[i] + K2[0, 0]/2, x1[i] + K2[1, 0]/2, y[i] + K2[2, 0]/2, y1[i] + K2[3, 0]/2)
    K3[1, 0] = h * f2(time[i] + h/2, x[i] + K2[0, 0]/2, x1[i] + K2[1, 0]/2, y[i] + K2[2, 0]/2, y1[i] + K2[3, 0]/2)
    K3[2, 0] = h * f3(time[i] + h/2, x[i] + K2[0, 0]/2, x1[i] + K2[1, 0]/2, y[i] + K2[2, 0]/2, y1[i] + K2[3, 0]/2)
    K3[3, 0] = h * f4(time[i] + h/2, x[i] + K2[0, 0]/2, x1[i] + K2[1, 0]/2, y[i] + K2[2, 0]/2, y1[i] + K2[3, 0]/2)

    K4[0, 0] = h * f1(time[i] + h, x[i] + K3[0, 0], x1[i] + K3[1, 0], y[i] + K3[2, 0], y1[i] + K3[3, 0])
    K4[1, 0] = h * f2(time[i] + h, x[i] + K3[0, 0], x1[i] + K3[1, 0], y[i] + K3[2, 0], y1[i] + K3[3, 0])
    K4[2, 0] = h * f3(time[i] + h, x[i] + K3[0, 0], x1[i] + K3[1, 0], y[i] + K3[2, 0], y1[i] + K3[3, 0])
    K4[3, 0] = h * f4(time[i] + h, x[i] + K3[0, 0], x1[i] + K3[1, 0], y[i] + K3[2, 0], y1[i] + K3[3, 0])

    U[0, 0] = U[0, 0] + 1/6 * (K1[0, 0] + 2*K2[0, 0] + 2*K3[0, 0] + K4[0, 0])
    U[1, 0] = U[1, 0] + 1/6 * (K1[1, 0] + 2*K2[1, 0] + 2*K3[1, 0] + K4[1, 0])
    U[2, 0] = U[2, 0] + 1/6 * (K1[2, 0] + 2*K2[2, 0] + 2*K3[2, 0] + K4[2, 0])
    U[3, 0] = U[3, 0] + 1/6 * (K1[3, 0] + 2*K2[3, 0] + 2*K3[3, 0] + K4[3, 0])


# Построение графиков и таблицы
print(table)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(time, x)
axs[0, 0].set_title('График x = x(t)')
axs[0, 1].plot(time, y, 'tab:orange')
axs[0, 1].set_title('График y = y(t)')
axs[1, 0].plot(x, y, 'tab:green')
axs[1, 0].set_title('График y = y(x)')
axs[1, 1].plot(time, L, 'tab:red')
axs[1, 1].set_title('График sqrt(x^2 + y^2)')
fig.tight_layout(pad=3.0)
plt.show()
