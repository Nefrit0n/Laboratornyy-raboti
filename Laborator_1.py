from random import *

n = [i for i in input('введите слово: ')]
print(*n, sep='')
slovo = [i for i in input('Слово ключ: ')]



def easy_level():  # саммый простой способ
    global s
    s = [i for i in range(len(n))]
    shuffle(s)
    print('Наш ключ: ', *s, sep='')
    new_lst = []
    for i in range(len(n)):
        new_lst.append(n[s[i]])
    print('Что мы зашифровали:', *new_lst, sep='')
    print('\nТеперь дешифруем')
    s.sort()
    print(*s)
    new_lst.clear()
    for i in range(len(n)):
        new_lst.append(n[s[i]])
    print('Результат дешифровки: ', *new_lst, sep='')


def hard_level():  # Теперь мы будем использовать в качестве ключа другое слово
    key = len(slovo)
    stolbci = len(n) // key
    stolbci += 1
    stroka = [[''] * key for i in range(stolbci)]
    count_1 = 0
    for i in range(len(stroka)):
        for j in range(key):
            if count_1 == len(n):
                break
            stroka[i][j] = n[count_1]
            count_1 += 1
    for i in range(len(stroka)):
        print(*stroka[i], sep='')
    key_1 = [i for i in range(key)]
    shuffle(key_1)
    print('Наш ключ: ',*key_1)
    new_stroka = []
    for i in range(len(stroka)):
        for j in range(key):
            new_stroka.append(stroka[i][key_1[j]])
    print('Наше закодированное слово: ',*new_stroka, sep='')
    stolbci_1 = len(n) // key
    stolbci_1 += 1
    stroka_1 = [[''] * key for i in range(stolbci_1)]
    count_2 = 0
    for i in range(len(stroka_1)):
        for j in range(key):
            if count_2 == len(n):
                break
            stroka_1[i][j] = new_stroka[count_2]
            count_2 += 1
    for i in range(len(stroka_1)):
        print(*stroka_1[i], sep='')


while True:
    x=int(input('Куда пойдём 1) простой путь 2)сложный путь'))
    if x == 1:
        easy_level()
    elif x == 2:
        hard_level()
    else:
        print('Такой цыфры нет')