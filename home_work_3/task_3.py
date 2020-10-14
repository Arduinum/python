'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(var_1, var_2, var_3):
        list_numbers = [var_1, var_2, var_3] 
        min_number = min(var_1, var_2, var_3)    
        list_numbers.remove(min_number)
        return sum(list_numbers)

try:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    num_3 = int(input('Введите третье число: '))
except ValueError:
    print('Ошибка - вы ввели слово вместо цифры!')
else:
    print(my_func(num_1, num_2, num_3))

