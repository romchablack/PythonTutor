# coding=utf-8
# Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

L = input().split()
for i in L:
    if int(i) % 2 == 0:
        print(i)