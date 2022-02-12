# Задача 5.
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

first_alphabet_symbol = ord('a')
last_alphabet_symbol = ord('z')

c = int(input("Введите номер буквы английского алфавита: "))

c = c + first_alphabet_symbol - 1

if first_alphabet_symbol <= c <= last_alphabet_symbol:
    print(f"Это буква {chr(c)}")
else:
    print("Вы ввели что-то не то")
