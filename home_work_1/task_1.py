'''
Задание 1:
Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в переменные, 
выведите на экран.
'''

my_number = 777
my_str = 'Hello world!'

print(my_number)
print(my_str)

my_number = input('Enter any number: ')
my_str = input('Enter any word: ')

print(f'Вы ввели цифру: {my_number}')
print(f'Вы ввели слово: {my_str}')

my_number = input('Введите ваш год рождения: ')
my_str = input('Введите ваше имя: ')

print(f'Вас зовут {my_str} и вы рождены в {my_number} году.')