# Задача 1.4.

# Есть словарь кодов товаров 

titles = {'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280'}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store =  {'100000110': [{'количество': 31, 'цена': 1637}],
    '100000146': [ {'количество': 4, 'цена': 45}, {'количество': 10, 'цена': 48}],
    '100000149': [ {'количество': 28, 'цена': 279}, {'количество': 32, 'цена': 291}],
    '100000194': [{'количество': 8, 'цена': 220}, {'количество': 1, 'цена': 170}],
    '100000224': [{'количество': 61, 'цена': 438}, {'количество': 23, 'цена': 302}, {'количество': 50, 'цена': 412}],
    '100000280': [{'количество': 26, 'цена': 175}, ]}

# Рассчитайте на какую сумму лежит каждого товара на складе.
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

for name in titles:
 code = titles[name]
 total_price = 0
 total_count = 0
 for count_price in store[code]:
  total_price = total_price + count_price['количество'] * count_price['цена']
  total_count = total_count + count_price['количество']
 print(name, '-', total_count, 'шт, стоимость', total_price, 'руб')