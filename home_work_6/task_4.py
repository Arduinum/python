'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, 
color, name, is_police (булево).  А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость 
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться 
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
выведите результат. Выполните вызов методов и также покажите результат.
'''

from time import sleep

class Car:
    
    show_speed = 0

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        Car.show_speed += 30
        print(f'{self.name} {self.color} цвета поехала вперёд!')
        print(f'Cкорость {Car.show_speed} км/ч')
    

    def stop(self):
        Car.show_speed = 0
        print(f'{self.name} {self.color} цвета остановилась!')
        print(f'Cкорость {Car.show_speed} км/ч')
    

    def turn(self, rotation):
        self.rotation = rotation
        while True:
            if self.rotation == 'right':
                Car.show_speed += 20
                print(f'{self.name} {self.color} цвета повернула направо!')
                print(f'Cкорость {Car.show_speed} км/ч')
                break
            elif self.rotation == 'left':
                Car.show_speed += 15
                print(f'{self.name} {self.color} цвета повернула на лево!')
                print(f'Cкорость {Car.show_speed} км/ч')
                break
            else:
                print('Поверните машину на лево или направа введя: left или right!')
                break
    

    def auto_character(self):
        print('\nНазвание авто:', self.name)
        print('Цвет:', self.color)
        if self.is_police == True:
            print('Тип авто: полицейское')
        else:
            print('Тип авто: гражданское')


class TownCar(Car):
    
    def __init__(self, color, name, is_police):
        Car.__init__(self, color, name, is_police)

    def max_speed(self):
        if Car.show_speed > 60:
            print('Это полиция! Вы привысели скорость! Остановитесь на обочине!')
            Car.stop(self)
    

class WorkCar(Car):
    def __init__(self, color, name, is_police):
        Car.__init__(self, color, name, is_police)
        

    def max_speed(self):    
        if Car.show_speed > 40:
            print('Это полиция! Вы привысели скорость! Остановитесь на обочине!')
            Car.stop(self)


class SportCar(Car):
    def __init__(self, color, name, is_police):
        Car.__init__(self, color, name, is_police)


    def tricks(self):
        if Car.show_speed > 25 and Car.show_speed < 31:
            print('Дрифтуем по трассе')
        elif Car.show_speed > 31 and Car.show_speed < 100:
            print('Управляемый занос')
            Car.show_speed += 100
        elif Car.show_speed > 150 and Car.show_speed < 180:
            print('Резкое ускорение!')
        elif Car.show_speed > 180:
            print('Оторвало заднее колесо, аварийная остановка!')
            Car.stop(self)


class PoliceCar(Car):
    def __init__(self, color, name, is_police):
        Car.__init__(self, color, name, is_police)

    
    def chase(self):
        if Car.show_speed > 25 and Car.show_speed < 31:
            print('Преследуем нарушителя скорости!')
        elif Car.show_speed > 31 and Car.show_speed < 100:
            print('Немедленно остановите машину или мы открываем огонь!')
            Car.show_speed += 100
        elif Car.show_speed > 150 and Car.show_speed < 180:
            print('Резкое ускорение!')
        elif Car.show_speed > 180:
            print('Отстрелили колесо нарушителю, остановились у обочины!')
            Car.stop(self)

    
    def flasher(self):
        print("\033[31m {}" .format('*'))
        sleep(2)
        print("\033[34m {}" .format('*'))
        sleep(2)
        print("\033[30m {}" .format(''))

# примеры запуска:

# t = TownCar('green', 'bmw-z9', False)
# t.go()
# t.max_speed()
# t.turn('wdwdw')
# t.max_speed()
# t.turn('right')
# t.max_speed()
# t.turn('left')
# t.max_speed()
# p.auto_character()

# w = WorkCar('yellow', 'kamaz', False)
# w.go()
# w.max_speed()
# w.turn('wdwdw')
# w.max_speed()
# w.turn('right')
# w.max_speed()
# w.auto_character()

# s = SportCar('black', 'Mercedes-AMG GT 4', False)
# s.go()
# s.tricks()
# s.turn('wdwdw')
# s.tricks()
# s.turn('right')
# s.tricks()
# s.turn('left')
# s.tricks()
# s.go()
# s.tricks()
# s.auto_character()

p = PoliceCar('white', 'ford focus', True)
p.flasher()
p.go()
p.chase()
p.flasher()
p.turn('wdwdw')
p.chase()
p.flasher()
p.turn('right')
p.chase()
p.flasher()
p.turn('left')
p.chase()
p.flasher()
p.go()
p.chase()
p.auto_character()