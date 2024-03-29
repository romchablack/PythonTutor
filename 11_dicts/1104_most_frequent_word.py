# Условие
#
# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом
# тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

n = int(input())
D = dict()

for i in range(n):
    row = input().split()
    for word in row:
        D[word] = D.get(word, 0) + 1

for key in sorted(D):
    if D[key] == max(D.values()):
        print(key)
        break

# ChatGPT
n = int(input())  # количество строк

words_count = {}  # создаем пустой словарь слов и их повторений

for i in range(n):
    line = input().split()  # считываем очередную строку и разбиваем на слова
    for word in line:
        if word not in words_count:  # если слово еще не встречалось, добавляем его в словарь
            words_count[word] = 1
        else:  # иначе увеличиваем количество повторений слова
            words_count[word] += 1

max_count = 0  # переменная для хранения максимального количества повторений слова
min_word = ''  # переменная для хранения слова с максимальным количеством повторений и наименьшим лексикографическим значением

for word in sorted(words_count.keys()):  # сортируем слова по алфавиту
    if words_count[word] > max_count:  # если текущее слово встречается чаще, чем предыдущее максимальное
        max_count = words_count[word]  # обновляем максимальное количество повторений
        min_word = word  # и запоминаем текущее слово
    elif words_count[word] == max_count and (min_word == '' or word < min_word):  # если текущее слово встречается так же часто, как предыдущее максимальное, но имеет меньшее лексикографическое значение
        min_word = word  # обновляем слово с максимальным количеством повторений и наименьшим лексикографическим значением

print(min_word)  # выводим слово, которое встречается чаще всего и имеет наименьшее лексикографическое значение
