'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на 
наличие только чисел. Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и 
строки. При вводе пользователем очередного элемента необходимо реализовать проверку 
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.
'''

from re import findall

class OnlyNums(Exception):
    def __init__(self, text):
        self.text = text


def filter_int(param):
    if param.isdigit() == True:
        return True

def filter_float(param):
    if findall(r'\b\d+\.\d+\b', param):
        return True


list_new = []

print('Программа для заполнения списка числами.')
print('Для прекращения ввода введите exit.')

while True:
    input_num = input('введите число: ')
    try:
        if input_num == 'exit':
            print(list_new)
            break
        if filter_float(input_num):
            input_num = float(input_num)
        elif filter_int(input_num):
            input_num = int(input_num)
        elif '-' in input_num:
            if filter_float(input_num[1:]):
                input_num = float(input_num)
            elif filter_int(input_num[1:]):
                input_num = int(input_num)
        elif input_num.isdigit() == False:
            raise OnlyNums('Ошибка - в список можно добавить только число!')
    except OnlyNums as only_nums:
        print(only_nums)    
    else:
        list_new.append(input_num)