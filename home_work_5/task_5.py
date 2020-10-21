'''
Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее 
на экран.
'''

# text_6.txt появиться при выполнении программы

with open('text_6.txt', 'w', encoding='utf-8') as file:
    numbers_str = '6 7 8 9 10 11 12 21'
    content = file.write(numbers_str)
try:
    with open('text_6.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        numbers_sum = sum([int(num) for num in content.split(' ')])
        print(f'Сумма чисел: {content} = {numbers_sum}')
except FileNotFoundError:
    print('Ошибка - файл не найден!')
