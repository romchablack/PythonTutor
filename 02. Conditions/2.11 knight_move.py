# coding=utf-8
# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
# или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на
# вторую одним ходом.

a1 = int(input())
b1 = int(input())

a2 = int(input())
b2 = int(input())

if (abs(a1-a2) == 1 and abs(b1-b2) == 2) or (abs(b1-b2) == 1 and abs(a1-a2) == 2):
    print('YES')
else:
    print('NO')