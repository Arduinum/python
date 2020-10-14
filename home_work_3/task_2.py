'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def get_data(name, surname, email, phone, city, year):
    data = f'имя: {name}; фамилия: {surname}; год рождения: {year}; город: {city}; почта: {email}; телефон: {phone}'
    return data


name_user = input('Введите имя пользователя: ')
surname_user = input('Введите фамилию пользователя: ')
year_user = input('Введите год рождения пользователя: ')
email_user = input('Введите почту пользователя: ')
phone_user = input('Введите телефон пользователя: ')
city_user = input('Введите город проживания пользователя: ')

print(get_data(surname=surname_user, name=name_user, phone=phone_user, email=email_user, year=year_user, city=city_user))