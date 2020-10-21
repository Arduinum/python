'''
Создать программно файл в текстовом формате, записать в него построчно данные, 
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
# text_1.txt создасться при выполнении программы

list_str = []

try:
    with open('text_1.txt', 'x', encoding='utf-8') as file:
        print('Для выхода из ввода нажмите enter.')
        while True:
            content = input('Введите строку данных: ')
            if content != '':
                if not list_str: # если список пуст
                    list_str.append(content)             
                else:
                    list_str.append('\n' + content)
            elif content == '':
                file.writelines(list_str)
                break
except FileExistsError:
    print('Ошибка - файл уже существует!')
