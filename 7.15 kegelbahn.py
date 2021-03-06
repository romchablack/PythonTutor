# coding=utf-8
# N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров,
# при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на
# месте. Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri,
# при этом 1≤ li≤ ri≤ N. Программа должна вывести последовательность из N символов, где j-й символ есть “I”,
# если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.

N, K = [int(i) for i in input().split()]  # type: (object, object)
L = ['I']*N

for i in range(K):
    lft, rght = [int(j) for j in input().split()]
    
    for i in range(lft-1, rght):
        L[i] = '.'

print(''.join([i for i in L]))
