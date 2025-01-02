#  Решение СЛАУ с неквадартаными матрицами, у которых могут быть: 0 и бесконечно много
#  решений (теорема Кронекера-Капелли)
import numpy as np


def non_square_SLAU(matrix):

    size = np.shape(matrix)
    matrix_size = np.shape(matrix)
    A = np.zeros((matrix_size[0], matrix_size[1] - 1))

    for i in range(matrix_size[0]):
        for j in range(matrix_size[1] - 1):
            A[i, j] = matrix[i, j]

    rank1 = np.linalg.matrix_rank(A)
    rank2 = np.linalg.matrix_rank(matrix)

    # Теорема Кронекера-Капелли
    if rank1 != rank2:
        print('Система несовместна')
        return

    for i in range(rank2):

        a1 = matrix[i, i]

        if a1 != 0:

            for j in range(size[1]):
                matrix[i, j] = matrix[i, j] / a1

            for i1 in range(i + 1, size[0]):
                a = matrix[i1, i]
                for j in range(i, size[1]):
                    matrix[i1, j] = matrix[i1, j] - a * matrix[i, j]
        else:

            j = i + 1

            while matrix[i, j] == 0:
                j = j + 1

            a1 = matrix[i, j]

            for j in range(size[1]):
                matrix[i, j] = matrix[i, j] / a1

            for i1 in range(i + 1, size[0]):
                a = matrix[i1, i]
                for j in range(i, size[1]):
                    matrix[i1, j] = matrix[i1, j] - a * matrix[i, j]

    for i in range(rank1):
        for i1 in range(i + 1, rank1):
            a = matrix[i, i1]
            for j in range(i1, size[1]):
                matrix[i, j] = matrix[i, j] - a * matrix[i1, j]

    solution = np.zeros((size[1] - 1, size[1] - rank1))

    for i in range(size[0]):
        for j in range(rank1, size[1]):
            solution[i, j - rank1] = matrix[i, j]

    for i in range(size[1] - 1):
        for j in range(size[1] - 1 - rank1):
            solution[i, j] = -solution[i, j]

    for i in range(size[1] - rank1 - 1):
        solution[i + rank1, i] = 1

    return solution
