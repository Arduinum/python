'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
'''

# файл text_2.txt вложил в домашнюю работу

try:
    with open('text_2.txt', 'r', encoding='utf-8') as file:
        lines_str = file.readlines()
        number_lines = [i for i, _ in enumerate(lines_str, 1)][-1]
        print(f'в текстовом документе - {number_lines} строки')
        for i in lines_str:
            number_words = [i for  i, words in enumerate(i.split(' '), 1) if words.isalpha() == True][-1]
            i = i[:-1]
            print(f'в строке "{i}" - {number_words} слов')
except FileNotFoundError:
    print('Ошибка - файл не найден!')
