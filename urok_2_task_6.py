#ЗАДАЧА 6

# реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# каждый кортеж хранит информацию об отдельном товаре.
# в кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# cтруктуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]

# необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

list_of_products = []
products_analytics_name = []
products_analytics_amount = []
products_analytics_price = []
products_analytics_unit = []
number_of_products = int(input('Введите количество товаров: '))

for i in range(1, number_of_products + 1):
    list_of_products.append((i, {}))

i = 0
while i < number_of_products:
    try:
        product_number = int(input('Назначьте номер товару: '))
        if product_number < 1 or product_number > number_of_products:
            print('Неверный номер.')
            continue

        product_name = input('Введите название товара: ')
        product_amount = int(input('Введите количество товара: '))
        product_price = float(input('Введите цену товара (в у.е.): '))
        product_unit = input('Введите единицу измерения: ')
        list_of_products[product_number - 1][1]['Название'] = product_name
        list_of_products[product_number - 1][1]['Количество'] = product_amount
        list_of_products[product_number - 1][1]['Цена'] = product_price
        list_of_products[product_number - 1][1]['Единица измерения'] = product_unit
        products_analytics_name.append(product_name)
        products_analytics_amount.append(product_amount)
        products_analytics_price.append(product_price)
        products_analytics_unit.append(product_unit)
        i = i + 1

    except:
        print('Вы ввели что-то не то. Попробуем еще раз.')
        continue

    print(list_of_products)
    print('Следующий товар')

print('Данные по всем товарам заполнены!')
print(list_of_products)
print('Теперь соберем аналитику по товарам.')

print(f'Название: {products_analytics_name}')
print(f'Количество: {products_analytics_amount}')
print(f'Цена: {products_analytics_price}')
print(f'Единица измерения: {products_analytics_unit}')
