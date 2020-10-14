'''
Задание 4:
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

user_number = int(input('Введите целое положительное число (минимум двухзначное): '))

max_num = 0
number = 0
number_print = user_number
while user_number > 0:
    number = user_number % 10
    if number > max_num:
        max_num = number
    user_number = user_number // 10
print(f'Самая большая цифра в числе {number_print} - {max_num}')