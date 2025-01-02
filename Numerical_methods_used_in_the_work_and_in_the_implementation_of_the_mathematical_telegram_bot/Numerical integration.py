# Численное интегрирование метода серединных прямоугольников, трапеций, Симпсона с применением правила Рунге
# практической оценки погрешности
from math import sqrt, exp


def function_of_your_variant(x):
    return exp(1/x) / x**2


def rectangles(h, n):
    summa = 0
    x = a  # Начало отрезка

    for i in range(n):
        x = a + (i + 1 / 2) * h
        summa += function_of_your_variant(x)

    return h * summa


def trapezoid(h, n):
    summa = 0
    x = a  # Начало отрезка

    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:  # Если точки — крайние
            summa += function_of_your_variant(x) / 2
        else:  # Если точки — внутренние
            summa += function_of_your_variant(x)

    return h * summa


def simpson(h, n):
    summa = 0
    x = a  # Начало отрезка

    for i in range(1, 2*n):
        x = a + i * h
        if i % 2 == 1:  # Если номер точки — нечетный, то умножаем на 4
            summa += 4 * function_of_your_variant(x)
        else:  # Если номер точки — четный, то умножаем на 2
            summa += 2 * function_of_your_variant(x)

    summa += function_of_your_variant(a) + function_of_your_variant(b)

    return h / 3 * summa


a, b, epsilon = 1, 2, 1e-4

# Cредние прямоугольники
n0 = int((b - a) / sqrt(epsilon)) + 1
h0 = (b - a) / n0  # для средних прямоугольников и трапеций
n1 = 2 * n0
h1 = h0 / 2
I_h = rectangles(h0, n0)
I_halfH = rectangles(h1, n1)
while abs(I_halfH - I_h) / (2 ** 2 - 1) >= epsilon:
    I_h = I_halfH
    h1 /= 2
    n1 *= 2
    I_halfH = rectangles(h1, n1)
print("\n", I_halfH)
print(I_halfH - 0.1, "\n")

# Трапеции
n0 = int((b - a) / sqrt(epsilon)) + 1
h0 = (b - a) / n0  # для средних прямоугольников и трапеций
n1 = 2 * n0
h1 = h0 / 2
I_h = trapezoid(h0, n0)
I_halfH = trapezoid(h1, n1)
while abs(I_halfH - I_h) / (2 ** 2 - 1) >= epsilon:
    I_h = I_halfH
    h1 /= 2
    n1 *= 2
    I_halfH = trapezoid(h1, n1)
print(I_halfH)
print(I_halfH - 0.1, "\n")

# Симпсон
n0 = int((b - a) / (2 * sqrt(sqrt(epsilon)))) + 1
h0 = (b - a) / (2 * n0)  # для метода симпсона
n1 = 2 * n0
h1 = h0 / 2
I_h = simpson(h0, n0)
I_halfH = simpson(h1, n1)
while abs(I_halfH - I_h) / (2 ** 4 - 1) >= epsilon:
    I_h = I_halfH
    h1 /= 2
    n1 *= 2
    I_halfH = simpson(h1, n1)
print(I_halfH)
print(I_halfH - 0.1, "\n")
