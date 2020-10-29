'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное 
название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды 
существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные 
числа: V и H, соответственно. 
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто 
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке 
знания: реализовать абстрактные классы для основных классов проекта, проверить 
на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Сlothes(ABC):
    def __init__(self, name=None):
        self.name = name
    
    @abstractmethod
    def outgo_cloth(self):
        pass
    
class Coat(Сlothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def outgo_cloth(self):
        return float(f'{((self.size / 6.5) + 0.5):.2f}')

class Suit(Сlothes):
    def __init__(self, name, rise):
        super().__init__(name)
        self.rise = rise
    
    @property
    def outgo_cloth(self):
        return float(f'{((2 * self.rise) + 0.3):.2f}')

class ClothSum:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
    
    @property
    def outgo_cloth(self):
        return self.param_1 + self.param_2

c = Coat('Inverness', 52) # 52й размер
print('Расход ткани на пальто', c.name, '-', c.outgo_cloth, 'м')
s = Suit('Tuxedo', 1.72) # 1м720см
print('Расход ткани на педжак', s.name, '-', s.outgo_cloth, 'м')
cl = ClothSum(s.outgo_cloth, c.outgo_cloth)
print('Общий расхорд ткани -',  cl.outgo_cloth, 'м')