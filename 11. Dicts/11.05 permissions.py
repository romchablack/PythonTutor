# Условие

# В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам. Для
# каждого файла известно, с какими действиями можно к нему обращаться:
# запись W,
# чтение R,
# запуск X.
#
# В первой строке содержится число N — количество файлов содержащихся в данной файловой
# системе. В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами. Далее
# указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл. К одному и
# тому же файлу может быть применено любое колличество запросов.
#
# Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого запроса должна будет
# возвращать OK если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима.

D = dict()

N = int(input())
for i in range(N):
    row = input().split()
    for i in range(len(row)):
        if row[i] == 'R': row[i] = 'read'
        elif row[i] == 'W': row[i] = 'write'
        elif row[i] == 'X': row[i] = 'execute'
    txt, *args = row
    D[txt] = args

M = int(input())
for i in range(M):
    request, obj = input().split()
    if request in D[obj]:
        print('OK')
    else:
        print('Access denied')