# ЗАДАЧА 2

# для списка реализовать обмен значений соседних элементов;
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.;
# при нечетном количестве элементов последний сохранить на своем месте;
# для заполнения списка элементов необходимо использовать функцию input().

list = []
num_of_elements = int(input('Сколько элементов будет в списке? '))

for i in range(num_of_elements):
    new_element = input('Введите любой элемент: ')
    list.append(new_element)

print(f'Ваш список: {list}')

i = 0
while i < num_of_elements - 1:
    add_element = list[i] # что-то вроде буфера обмена
    list[i] = list[i + 1]
    list[i + 1] = add_element
    i = i + 2

print(f'Новый список: {list}')
