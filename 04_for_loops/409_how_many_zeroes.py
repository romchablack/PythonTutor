# coding=utf-8
# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди
# введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

n = int(input())
sum = 0
prod = 1
s = ''

for i in range(1, n + 1):
    if int(input()) == 0:
        sum += 1

print(sum)