'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем 
нуля в качестве делителя программа должна корректно обработать эту ситуацию и не 
завершиться с ошибкой.
'''

class MyError(Exception):
    def __init__(self, text):
        self.text = text


print('Введите два числа для операции деления')
input_num_1 = input('число первое: ')
input_num_2 = input('число второе: ')

try:
    input_num_1 = int(input_num_1)
    input_num_2 = int(input_num_2)
    if input_num_2 == 0 or input_num_1 == 0:
        raise MyError('На ноль делить нельзя!')
except ValueError:
    print('Вы ввели слово вместо числа!')
except MyError as error_zero:
    print(error_zero)
else:
    print(f'{input_num_1} / {input_num_2} = {input_num_1 / input_num_2}')
