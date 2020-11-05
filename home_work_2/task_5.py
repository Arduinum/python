'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. 
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

rating_list = [8, 7, 3, 2]

while True:
    number_user = input('Введите новое число для рейтинга или exit для выхода из добавления: ')

    if number_user == 'exit':
        break
    else:
        number_user = int(number_user)
        if number_user in rating_list:
            index_item = rating_list.index(number_user)
            rating_list.reverse() # добавлена данная строка
            rating_list.insert((index_item - 1), number_user) # исправлена данная строка
            rating_list.reverse() # добавлена данная строка
            print(f'рейтинг: {rating_list}')
        elif min(rating_list) > number_user:
            rating_list.append(number_user)
            print(f'рейтинг: {rating_list}')
        elif max(rating_list) < number_user:
            rating_list.insert(0, number_user)
            print(f'рейтинг: {rating_list}')
