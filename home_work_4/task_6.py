'''
Реализовать два небольших скрипта: 
а) итератор, генерирующий целые числа, начиная с указанного, 
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, 
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его 
завершения. 
Например, в первом задании выводим целые числа, начиная с 3, а при достижении 
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, 
при котором повторение элементов списка будет прекращено.
'''

from itertools import count, cycle


def generator():
    for num in count(3): 
        if num >= 10:
            return # выхожу из цикла вместо break!
        yield num
        

g = generator()
list_generate = [num for num in g]

print('часть a):')
for el in list_generate:
    print(el)


def func_cycle(list_el):
    for num, el in enumerate(cycle(list_el), 1):
        if num >= 10:
            return 
        yield el


f_c = func_cycle(list_generate)

print('часть б):')
for num, el in enumerate(f_c, 1):
    print(f'счёт {num} - элемент {el}')







