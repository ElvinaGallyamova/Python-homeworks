#Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Осуществить вывод данных о пользователе одной строкой.

name = input('Enter your name')
surname = input('Enter your surname')
year = int(input('Enter year of birth'))
city = input('Enter city of residence')
email = input('Enter your email')
telephone = input('Enter phone number')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Smith', name = 'John', year = '1996', city = 'Vladivostok', email = 'johnsmith22@mail.ru', telephone = '89811100500'))