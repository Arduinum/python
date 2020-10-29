'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса 
(метод __init__()), который должен принимать данные (список списков) для формирования 
матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном 
виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух 
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. 
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой 
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix 
        
    
    def __str__(self):
        return str(self.matrix_output(self.matrix))


    def __add__(self, other):
        return self.matrix_output(self.matrix_sum(self.matrix, other.matrix))
        
    
    def matrix_sum(self, m1, m2):
        self.m1 = m1
        self.m2 = m2 
        if len(self.m1[0]) == len(self.m2[0]):
            for index, els in enumerate(self.m1):
                for i, el in enumerate(els):
                    sum_1 = el + self.m2[index][i]
                    self.m2[index].pop(i)
                    self.m2[index].insert(i, sum_1)
            return self.m2
        else:
            return 'Ошибка - матрицы не одинаковых размерностей!'


    def matrix_output(self, m):
        self.m = m
        if str(type(self.m)) == "<class 'list'>":
            self.result = ''
            max_len = 0
            difference = 0
            for max_list in self.m:
                if len(max_list) > max_len:
                    max_len = len(max_list)
            for item in self.m:
                if len(item) < max_len:
                    difference = max_len - len(item)
                    for _ in range(0, difference):
                        item.append(0)
                for index, _ in enumerate(item):
                    self.result += str(item[index]) + ' '
                self.result += '\n'
            return self.result
        else:
            return self.m


print('Cценарий когда матрицы одинаковых размерностей:\n')
matrix_1 = Matrix([[1, 2, 9], [3, 4, 10], [5], [7, 12, 2, 4]])
print(matrix_1)
matrix_2 = Matrix([[9, 10], [11, 12, 30], [12, 13, 14, 20], [15]])
print(matrix_2)
print('Результат сложения двух матриц:\n')
print(matrix_1 + matrix_2)

print('Cценарий когда матрицы не одинаковых размерностей:\n')
matrix_1 = Matrix([[1, 2, 9], [3, 4, 10], [5], [7, 12, 2, 4]])
print(matrix_1)
matrix_2 = Matrix([[9, 10], [11, 12], [12, 13], [15]])
print(matrix_2)
print(matrix_1 + matrix_2)