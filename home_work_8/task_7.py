'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу 
проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение 
созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNum:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return ComplexNum(self.num + other.num)

    def __mul__(self, other):
        return ComplexNum(self.num * other.num)


a = ComplexNum(1 + 1j)
b = ComplexNum(1 + 4j)
print(a + b)
print(a * b)