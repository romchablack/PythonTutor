# coding=utf-8 Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов
# этой последовательности больше предыдущего элемента.

n = int(input())
m = int(input())
count = 0

while m != 0:
    if m > n:
        count += 1
    n = m
    m = int(input())

print(count)
