# coding=utf-8
# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если
# наибольших элементов несколько, выведите индекс первого из них.

L = [int(i) for i in input().split()]

mx = L[0]

for i in range(1, len(L)):
    if L[i] > mx:
        mx = L[i]

print(mx, L.index(mx))