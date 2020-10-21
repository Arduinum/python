'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад 
менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины 
дохода сотрудников.
'''

# файл text_3.txt вложил в домашнюю работу

try:
    with open('text_3.txt', 'r', encoding='utf-8') as file:
        salary_sum = 0
        content = file.readlines()
        print('Данные сотрудники имеют окдлад менее 20 тыс:')
        for man in content:
            if '\n' in man:
                salary = float(man.split(' ')[-1][:-1])
            else:
                salary = float(man.split(' ')[-1])
            person = man.split(' ')[0]
            if salary < 20000.00:
                print(person) 
            salary_sum += salary 
        average_salary = salary_sum / len(content)
        print(f'\nСредняя зарплата сотрудников:\n{average_salary:.2f} руб')
except FileNotFoundError:
    print('Ошибка - файл не найден!')