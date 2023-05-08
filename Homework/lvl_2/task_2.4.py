# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# def remove_exclamation_marks(s):
#     chars = list(s)
#     for i in chars:
#         if i == '!':
#             chars.remove(i)
#     s = ''.join(chars)
#     return s

# s = "Hi! Hello!"
# print(remove_exclamation_marks(s))



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# def remove_last_em(s):
#     chars = list(s)
#     if chars[-1] == '!':
#         chars.remove(chars[-1])
#     s = ''.join(chars)
#     return s

# str = "!Hi"
# print(remove_last_em(str))


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    new_s = []
    words = s.split(" ")       # разделяем строку на слова по пробелу, засовываем в список
    for i in words:             # для каждого слова в списке
        count = 0
        char = list(i)             # преобразовываем слово в список из символов
        for j in char:             # для каждого символа в списке слова:
            if j == '!':                # если символ равен !, счетчик увеличивается
                count += 1  
        if count != 1:             # если счетчик равен 1, удаляем слово из списка слов 
            new_s.append(i)

    s = ' '.join(new_s)         # преобразовываем список слов в строку
    return s

print(remove_word_with_one_em("Hi Hi! Hi!"))