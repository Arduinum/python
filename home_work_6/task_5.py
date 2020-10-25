'''
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение 
метода draw. Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого 
экземпляра.
'''

class Stationery:
    def __init__(self, title=None):
        self.title = title
    

    def draw(self):
        print('Запуск отрисовки\n')


class Pen(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print("\033[34m {}" .format(self.title))
        print("\033[30m {}" .format('\n'))

class Pencil(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print("\033[35m {}" .format(self.title))
        print("\033[30m {}" .format('\n'))

class Handle(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print("\033[36m {}" .format(self.title))
        print("\033[30m {}" .format('\n'))

s = Stationery()
s.draw()

p = Pen('Пишем ручкой')
p.draw()

penc = Pencil('Пишем цветным карандашём')
penc.draw()

h = Handle('Пишем маркером')
h.draw()