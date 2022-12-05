#2) Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
#город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
#данных о пользователе одной строкой.

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
date_of_birth = input("Введите дату рождения: ")
city_of_living = input("Введите город проживания: ")
email = input("Введите адрес электронной почты: ")
telephone = input("Введите номер телефона: ")

def person_data(name_1, surname_1, date_of_birth_1, city_of_living_1, email_1, telephone_1):
    return f"Имя: {name_1}, Фамилия: {surname_1}. Дата рождения: {date_of_birth_1}. Город жительства: {city_of_living_1}. Электронный адрес: {email_1}. Телефон: {telephone_1}"

print(person_data(name_1=name, surname_1=surname, date_of_birth_1=date_of_birth, city_of_living_1=city_of_living, email_1=email, telephone_1=telephone))