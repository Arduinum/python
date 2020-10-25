'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) 
и метод running (запуск). Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 
секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении 
выводить соответствующее сообщение и завершать скрипт.
'''

# первый способ

# from time import sleep


# class TrafficLight:
#     __color = 'red', 'yellow', 'green'


#     def running(self, *colors):
#         try:
#             if colors[0] == TrafficLight.__color[0] and colors[1] == TrafficLight.__color[1] and colors[2] == TrafficLight.__color[2]:
#                 print("\033[31m {}" .format('***'))
#                 sleep(7)
#                 print("\033[33m {}" .format('***'))
#                 sleep(2)
#                 print("\033[32m {}" .format('***'))
#                 sleep(7)
#             else:
#                 print('Ошибка - не верный порядок цвета!')
#         except IndexError:
#             print('Ошибка - отсутствует один из цветов!')


# t = TrafficLight()
# t.running('red', 'yellow', 'green')

# второй способ

from time import sleep


class TrafficLight:
    def __init__(self, *color):
        self.__color = color


    def running(self):
        try:
            if self.__color[0] == 'red' and self.__color[1] == 'yellow' and self.__color[2] == 'green':
                print("\033[31m {}" .format('***'))
                sleep(7)
                print("\033[33m {}" .format('***'))
                sleep(2)
                print("\033[32m {}" .format('***'))
                sleep(7)
                print("\033[30m {}" .format(''))
            else:
                print('Ошибка - не верный порядок цвета!')
        except IndexError:
            print('Ошибка - отсутствует один из цветов!')


t = TrafficLight('red', 'yellow', 'green')
t.running()
