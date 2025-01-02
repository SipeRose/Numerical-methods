# Метод Гаусса с выбором главного элемента (без использования сторонних библиотек)

def Gauss_method(matrix):

    n = len(matrix)  # Число неизвестных

    # Шаг 1 — выбор главного элемента — находим номер строки, содержащий главный элемента
    def find_main_element(iteration):
        main_element = abs(matrix[iteration][iteration])
        row_number = iteration
        for i in range(iteration, n):
            if abs(matrix[i][iteration]) > main_element:
                main_element = abs(matrix[i][iteration])
                row_number = i

        return row_number

    # Шаг 2 — смена строк местами
    def change_rows(iteration, main_element_row_number):
        current_row = matrix[iteration]
        main_element_row = matrix[main_element_row_number]
        matrix[iteration] = main_element_row
        matrix[main_element_row_number] = current_row

    # Шаг 3 — делим текущую строчку на опроный элемент
    def divide_by_support_element(iteration):
        support_element = matrix[iteration][iteration]
        for i in range(iteration, n + 1):
            matrix[iteration][i] = matrix[iteration][i] / support_element

    # Шаг 4 — вычитаем из оставшихся строк текущую, умноженную на соответствующий коэффициент
    def subtraction(iteration):
        for i in range(iteration + 1, n):
            coefficient = matrix[i][iteration]
            for j in range(iteration, n + 1):
                matrix[i][j] = matrix[i][j] - coefficient * matrix[iteration][j]

    # Прямой ход метода Гаусса
    for i in range(0, n):
        main_element_row_number1 = find_main_element(i)
        change_rows(i, main_element_row_number1)
        divide_by_support_element(i)
        subtraction(i)

    # Обратный ход метода
    solution = []
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            matrix[i][n] = matrix[i][n] - matrix[i][j] * matrix[j][n]
        solution.insert(0, matrix[i][n])

    return solution
