# ЗАДАЧА 2

# реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон;
# функция должна принимать параметры как именованные аргументы;
# реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth_year, city, email, phone_number):
    return f'name: {name}, surname: {surname}, birth year: {birth_year}, city: {city}, email: {email}, phone number: {phone_number}'

name = input('name is: ')
surname = input('surname is: ')
birth_year = input('birth year is: ')
city = input('city is: ')
email = input('email is: ')
phone_number = input('phone number is: ')

print(user_data(name, surname, birth_year, city, email, phone_number))

