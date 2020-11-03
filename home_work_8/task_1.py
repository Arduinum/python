'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде 
строки формата «день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
'''

# первый вариант:
# class Date:
#     date = []
#     def __init__(self, date_str):
#         self.date.clear()
#         self.date.append(date_str)
#         self.date_str = date_str

#     @classmethod
#     def get_numbers(cls):     
#         date = [int(num) for num in cls.date[0].split('-')]
#         if Date.date_valid(date):
#             return f'Год: {date[0]:02.0f}, месяц: {date[1]:02.0f}, год: {date[2]:02.0f}'
#         else:
#             return f'Введённая дата: {date[0]:02.0f}-{date[1]:02.0f}-{date[2]:02.0f} невалидна!'

#     @staticmethod
#     def date_valid(date):
#         if date[0] in range(1, 31) and date[1] in range(1, 13) and date[2] in range(20, 22):
#             return True


# d = Date('01-11-20')
# print(d.get_numbers())
# d = Date('01-11-95')
# print(d.get_numbers())

# второй вариант
from datetime import datetime, date as date_t, time

class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def get_numbers(cls, date_str):
        date = [int(num) for num in date_str.split('-')]
        if Date.date_valid(date):
            return f'Год: {date[0]:02.0f}, месяц: {date[1]:02.0f}, год: {date[2]}'
        else:
            return f'Введённая дата: {date[0]:02.0f}-{date[1]:02.0f}-{date[2]} невалидна!'

    @staticmethod
    def date_valid(date):
        try:
            date_input = date_t(date[2], date[1], date[0])
        except ValueError:        
            pass
        else:
            if date_input:
                return True
            
                
d = Date('01-11-20')
print(d.get_numbers('01-11-20'))
print(d.get_numbers('01-11-19985'))