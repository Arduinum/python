'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, 
surname, position (должность), income (доход). Последний атрибут должен быть 
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, 
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:

    def __init__(self, name, position, **income):
        self.name = name
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, position, experience, **income):
        Worker.__init__(self, name, position, **income)
        self.experience = experience

    def _info_position(self):
        _profit = self._income['wage'] + self._income['bonus']
        print(f'Имя сотрудника: {self.name}')
        print(f'Должность: {self.position}')
        print(f'Доход: оклад {self._income["wage"]} + премия {self._income["bonus"]} = {_profit} руб')
        print(f'Стаж: {self.experience} лет')

p = Position('Alex', 'lawyer', 5, wage=13000, bonus=3000)
p._info_position()


