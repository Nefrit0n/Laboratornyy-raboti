from random import *

rus_l = " абвгдежзийклмнопрстуфхцчшщъыьэюя абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_b = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

slovo = input('Вводим слово: ')


def easy_level():
    shifr = []
    deshifr = []
    key = int(input('Длину ключа цыфрами: '))
    while key > 34:
        key -= 34
    for i in range(len(slovo)):
        if slovo[i] in rus_l:
            x = rus_l.find(slovo[i])
            shifr.append(rus_l[x + key])
        elif slovo[i] in rus_b:
            x = rus_b.find(slovo[i])
            shifr.append(rus_b[x + key])
    for i in range(len(shifr)):
        if shifr[i] in rus_l:
            x = rus_l.find(shifr[i])
            deshifr.append(rus_l[x - key])
        elif shifr[i] in rus_b:
            x = rus_b.find(shifr[i])
            deshifr.append(rus_b[x - key])
    return print('Результат шифровки: ', *shifr, '\nРезультат дешифровки: ', *deshifr, sep='')


def hard_level():
    shifr = []
    deshifr = []
    key_1 = []
    for i in range(len(slovo)):
        key = randint(0, 33)
        key_1.append(key)
        if slovo[i] in rus_l:
            x = rus_l.find(slovo[i])
            shifr.append(rus_l[x + key])
        elif slovo[i] in rus_b:
            x = rus_b.find(slovo[i])
            shifr.append(rus_b[x + key])
    print(*key_1)
    for i in range(len(shifr)):
        key = key_1[i]
        if shifr[i] in rus_l:
            x = rus_l.find(shifr[i])
            deshifr.append(rus_l[x - key])
        elif shifr[i] in rus_b:
            x = rus_b.find(shifr[i])
            deshifr.append(rus_b[x - key])
    return print('Результат шифровки: ', *shifr, '\nРезультат дешифровки: ', *deshifr, sep='')


while True:
    x = int(input('Каким путём пойдём:\n1) лёгкий\n2) тяжёлый\n3)Новое слово: '))
    if x == 1:
        easy_level()
    elif x == 2:
        hard_level()
    elif x == 3:
        slovo = input('Новое слово будет: ')
    elif x == 0:
        print('Ну выходим так выходим чо бубнить то')
        break
    else:
        print('Такого варианта нет, может попробовать из того что есть')
        continue
