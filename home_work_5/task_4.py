'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
'''

# файл text_4.txt прилажу к домашке, а файл text_5.txt появиться при выполнении программы

transfer_dir = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

try:
    with open('text_4.txt', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file.readlines()):
            result = line.split(' ')
            result.insert(0, transfer_dir.get(result.pop(0)))
            result = ' '.join(result)
            with open('text_5.txt', 'a', encoding='utf-8') as f:
                print(result, end='', file=f)
    print('Новый файл text_5.txt создан успешно.')
except FileNotFoundError:
    print('Ошибка - файл не найден!')
