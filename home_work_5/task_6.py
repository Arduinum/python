'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный 
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их 
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

# файл text_7.txt будет в папке с домашней работой

subjects = {}
num_sum = 0

with open('text_7.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    for subj in content:
        subj_list = subj.split(' ')
        for str_obj in subj_list:
            if '(лаб)' in str_obj:
                if '\n' in str_obj:
                    num_sum += int(str_obj[:-6])
                else:
                    num_sum += int(str_obj[:-5])
            elif '(л)' in str_obj:
                num_sum += int(str_obj[:-3])
            elif '(пр)' in str_obj:
                num_sum += int(str_obj[:-4])
        subjects[subj_list[0]] = num_sum
        num_sum = 0
    print(subjects)    