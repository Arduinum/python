'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

n = input('Введите любое число от 1 до 9: ')
result = int(n) + int(n + n) + int(n + n + n)
print(result)