# Условие

# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
#
# Для слова из словаря, записанного в последней строке, определите его синоним.

D = dict()
for i in range(int(input())):
    row = input().split()
    D[row[0]] = row[1]
    D[row[1]] = row[0]

print(D[input()])