# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!



def minimum(arr):
    i = -1
    min = arr[0]
    while i < len(arr)-1:
        i += 1
        if(arr[i] < min):
            min = arr[i]
    return min



def maximum(arr):
    i = -1
    max = arr[0]
    while i < len(arr)-1:
        i += 1
        if(arr[i] > max):
            max = arr[i]
    return max


arr = [5]
min = minimum(arr)
max = maximum(arr)
print('min =', min, 'max =', max)
