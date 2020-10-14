'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

list_user = []
list_result = []
info = print('Программа для создания и перемешивания списка из строк')
while True:
    element = input('Введите элемент для списка или введите stop для выхода из наполнения списка: ')
    if element == 'stop':
        break
    else:
        list_user.append(element)
        print(list_user)
item1 = None
item2 = None
list_len = len(list_user)
old_list = list_user.copy()
if len(list_user) % 2 == 0:
    while list_len != 0:
        item2 = list_user[0]
        item1 = list_user[1]
        list_result.append(item1)
        list_result.append(item2)
        list_user.pop(0)
        list_user.pop(0)
        list_len -= 2
else:
    item_end = list_user[-1]
    list_user.pop(-1)
    list_len = list_len - 1
    while list_len != 0:
        item2 = list_user[0]
        item1 = list_user[1]
        list_result.append(item1)
        list_result.append(item2)
        list_user.pop(0)
        list_user.pop(0)
        list_len -= 2
    list_result.append(item_end)
print(f'старый список - {old_list}')
print(f'новый список - {list_result}')