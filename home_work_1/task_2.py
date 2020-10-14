'''
Задание 2:
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк. 
'''

# конвертер секунд:
# первый вариант:
# seconds_user = int(input('Введите любое колличество секунд для их конвертации'\
# ' в стандартный формат времени: '))

# hours = seconds_user // 3600
# if hours < 10:
#     hours = '0' + str(hours)
# minuts = (seconds_user % 3600) // 60
# if minuts < 10:
#     minuts = '0' + str(minuts)
# seconds = (seconds_user % 3600) % 60
# if seconds < 10:
#     seconds = '0' + str(seconds)

# result = f'{hours}чч:{minuts}мм:{seconds}cc'
# print(f'{str(seconds_user)} секунд =', result)

# второй вариант более правильный:
seconds_user = int(input('Введите любое колличество секунд для их конвертации'\
' в стандартный формат времени: '))

hours = seconds_user // 3600
minuts = (seconds_user % 3600) // 60
seconds = (seconds_user % 3600) % 60

result = f'{hours:02.0f}чч:{minuts:02.0f}мм:{seconds:02.0f}cc'
print(f'{str(seconds_user)} секунд =', result)
