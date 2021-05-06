# coding=utf-8
# Условие
# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.

n = int(input())
L = []

for i in range(n):
    N = []
    L.append(N)
    for j in range(n):
        if i + j + 1 == n:
            N.append(1)
        elif i + j >= n:
            N.append(2)
        else:
            N.append(0)

for row in L:
    for elem in row:
        print(elem, end=' ')
    print()