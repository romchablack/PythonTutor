# coding=utf-8 Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для
# каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите,
# сколько секунд прошло между двумя моментами времени.
#
# Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых
# числа, задающих второй момент времени.
#
# Выведите число секунд между этими моментами времени.

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

dif = abs((a * 60 * 60 + b * 60 + c) - (d * 60 * 60 + e * 60 + f))

print(dif)
