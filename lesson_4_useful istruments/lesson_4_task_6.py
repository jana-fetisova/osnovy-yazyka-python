from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для генерации числа нажмите enter, для выхода - q: ')

for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа генерирует элементы списка. Для генерации следующего элемента нажмите enter, для выхода - q: ')

u_list = input('Введите элеиенты списка, разделяя их пробелом: ').split
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()


