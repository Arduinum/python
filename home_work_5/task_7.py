'''
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка 
должна содержать данные о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь 
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь 
(со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''

# text_8.txt вложил в домашнюю работу, firm_dir.json появиться при выполнении программы

from json import dump

sum_profit = 0
firms_list = [{}, {}]

with open('text_8.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    for i, item in enumerate(content, 1):
        firm = item.split(' ')
        profit = int(firm[2]) - int(firm[3][:-1])
        firms_list[0][firm[0]] = profit
        if profit > 0:
            sum_profit += profit
    aver_profit = sum_profit / i 
    firms_list[1]['average_profit'] = aver_profit
    print(firms_list)
    with open('firm_dir.json', 'w', encoding='utf-8') as file:
        dump(firms_list, file, ensure_ascii=False)
