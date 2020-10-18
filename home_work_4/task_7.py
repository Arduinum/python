'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное 
значение. При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить 
только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, 
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

from math import factorial

number = int(input('Введите число для вычисления его факториала: '))


def fact(num):
    global factorial
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
        yield i


list_result = []

for el in fact(number):
    list_result.append(str(el) + ' *')
str_result = ' '.join(list_result)
print(f'факториал числа {number} = {str_result[:-2]} = {factorial}')