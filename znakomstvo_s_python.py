#ПРАКТИЧЕСКОЕ ЗАДАНИЕ 1

print('-' * 100)
print('Задача 1')
print('-' * 100)

#поработайте с переменными, создайте несколько, выведите на экран;
#запросите у пользователя несколько чисел и строк.

print('Вывод заданных мной переменных:')

name = 'Alex'
age = 90
height = 1.78
has_grandchilds = False

print(f'Имя - {name}')
print(f'Возраст - {age} лет')
print(f'Рост в метрах - {height}')
print(f'Есть ли внуки - {has_grandchilds}')

print('*' * 10)

user_name = input('Как вас зовут? ')
user_age = int(input('Сколько вам полных лет? '))
user_height = float(input('Укажите ваш рост в метрах: '))

print(f'Вас зовут - {user_name}')
print(f'Ваш возраст - {user_age}')
print(f'Ваш рост в метрах - {user_height}')

print('-' * 100)
print('Задача 2')
print('-' * 100)

#пользователь вводит время в секундах;
#переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс;
#используйте форматирование строк.

user_time = int(input('Введите время в секундах: '))
time_h = user_time // 3600 #количество полных часов в time_h
time_s = user_time % 3600 #количество секунд, которое не уместилось в часы
time_m = time_s // 60 #количество минут в time_s
time_s = time_s % 60 #перезаписываем значение переменной для вывода в результат

print(f'В часах, минутах и секундах это - {time_h}:{time_m}:{time_s}')

print('-' * 100)
print('Задача 3')
print('-' * 100)

#узнайте у пользователя число n, найдите сумму чисел n + nn + nnn;
#например, пользователь ввёл число 3, считаем 3 + 33 + 333 = 369.

n = input('Введите число: ')
nn = n + n
nnn = n + n + n
print(f'n - {n}')
print(f'nn - {nn}')
print(f'nnn - {nnn}')
sum_n = int(n) + int(nn) + int(nnn)
print(f'Сумма этих чисел - {sum_n}')

print('-' * 100)
print('Задача 4')
print('-' * 100)

#пользователь вводит целое положительное число;
#найдите самую большую цифру в числе;
#для решения используйте цикл while и арифметические операции.

number = input('Введите целое положительное число: ')
max_num = number[0]
i = 1
while i <= len(number) - 1:
    #print(number[i])
    if number[i] > max_num:
        max_num = number[i]
    i = i + 1
print(f'Самая большая цифра в вашем числе - {max_num}')

print('-' * 100)
print('Задача 5')
print('-' * 100)

#запросите у пользователя значения выручки и издержек фирмы;
#определите, с каким финансовым результатом работает фирма;
#прибыль — выручка больше издержек, или убыток — издержки больше выручки;
#выведите соответствующее сообщение;
#если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке);
#далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

vyruchka = float(input('Введите вашу выручку (в у.е.): '))
izderzhki = float(input('Введите ваши издержки (в у.е.): '))

if vyruchka > izderzhki:
    print('Вы в прибыли!')
    pribyl = vyruchka - izderzhki
    rent_vyruchki = round(pribyl / vyruchka, 2)
    print(f'Рентабельность выручки равна {rent_vyruchki}')
    num_employees = int(input('Сколько у вас сотрудников? '))
    pribyl_per_employee = round(pribyl / num_employees, 2)
    print(f'Прибыль в расчете на одного сотрудника равна {pribyl_per_employee} (у.е.)')
elif izderzhki > vyruchka:
    print('Вы в убытке!')
    print('Рентабельность выручки и прибыль на одного сотрудника не рассчитываются по условиям задачи')
else:
    print('Ваши издержки и выручка одинаковы!')
    print('Рентабельность выручки и прибыль на одного сотрудника не рассчитываются по условиям задачи')

print('-' * 100)
print('Задача 6')
print('-' * 100)

#спортсмен занимается ежедневными пробежками;
#в первый день его результат составил a километров;
#каждый день спортсмен увеличивал результат на 10 % относительно предыдущего;
#требуется определить номер дня, на который общий результат спортсмена составил не менее b километров;
#программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Сколько км пробежал спортсмен в первый день? '))
b = int(input('Сколько км в день стремится бегать спортсмен? '))
actual_result = a #сколько км пробежал спортсмен за текущий день

day = 1
while actual_result < b:
    day = day + 1
    actual_result = actual_result * 1.1
    #print(f'{day}, {actual_result}')

print(f'Номер дня, на который результат спортсмена составил не менее {b} км: {day}')