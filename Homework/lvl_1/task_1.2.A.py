import random
# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


#list_of_songs = random.choices(my_favorite_songs, k=3)

#list_of_songs_lengs = [list_of_songs[0][1], list_of_songs[1][1], list_of_songs[2][1]]

#sum_of_lengs = sum(list_of_songs_lengs)

#print('Три песни звучат', sum_of_lengs, 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

new_list_of_songs = list(my_favorite_songs_dict.items())
random_list_of_songs = random.choices(new_list_of_songs, k=3)

new_list_of_songs_lengs = [random_list_of_songs[0][1], random_list_of_songs[1][1], random_list_of_songs[2][1]]

new_sum_of_lengs = sum(new_list_of_songs_lengs)

print('Три песни звучат', new_sum_of_lengs, 'минут')