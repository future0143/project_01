import random
from datetime import datetime
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

#пункт D
date_of_sum = datetime.strptime(str(round(new_sum_of_lengs, 2)), '%M.%S').time()
print('Три песни звучат', date_of_sum, 'минут')