# Условие
#
# Дан текст: в первой строке записано количество строк в тексте, а затем сами строки. Выведите все слова,
# встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию их количества
# появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
#
# Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости
# слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота
# встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет
# сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму.
# Это почти то, что требуется в задаче.

n = int(input())
words = ""
for i in range(n):
    line = input()
    words = words + " " + line

L = words.split()
D = []

for word in L:
    if (L.count(word), word) not in D:
        D.append((L.count(word), word))
    
my_dict = {}

for tup in D:
    if tup[0] not in my_dict:
        my_dict[tup[0]] = [tup[1]]
    else:
        my_dict[tup[0]].append(tup[1])
        my_dict[tup[0]].sort()

for k in reversed(list(my_dict.keys())):
    for v in my_dict[k]:
        print(v)