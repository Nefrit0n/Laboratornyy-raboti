x = int(input('задаём размер массива - '))
lst_1 = [[] for _ in range(x)]  # таблица слов
lst_2 = ['' for _ in range(x)]  # таблица ключей
print(lst_1, lst_2, sep='\n')
count = 0


def dobavit_slovo(slovo_1):  # добавление слова
    global count
    global x
    global lst_1
    global lst_2
    c = hash_function(slovo_1)
    if lst_2[c] == '':
        lst_2[c] = c
        count += 1
    lst_1[c].append(slovo_1)
    if count == round(x / 2):
        proverka_maximum()
    print(lst_1)


def hash_function(slovo):  # рассчёт хэш функции
    h = 0
    a = 127
    for v in range(len(slovo)):
        h = (a * h + (ord(slovo[v]))) % x
    print(h, '-хэш')
    return h


def find_slovo(slovo_4):  # для функции вывода слова и удаления по слову
    for i in range(x):
        for j in range(len(lst_1[i])):
            if slovo_4 == lst_1[i][j]:
                return i


def vivesti_slovo(num):  # Выводим слово по ключу или слову
    if num == 1:
        key = int(input('Ключик который будем выводить - '))
        print(lst_2[key], ':', *lst_1[key])
    elif num == 2:
        slovo_3 = input('Слово которое ищем  - ')
        poisk = find_slovo(slovo_3)
        print(lst_2[poisk], ':', *lst_1[poisk])


def vivesti_vsu_tabel():  # Выводим всю таблицу
    for i in range(len(lst_1)):
        print(lst_2[i], ':', *lst_1[i])


def proverka_maximum():  # Увелечение размера и рехеширование
    global lst_1
    global lst_2
    global x
    global count
    lst_3 = []
    for j in range(x):
        if lst_1[j] != '':
            lst_3.extend(lst_1[j])
    lst_1.clear()
    lst_2.clear()
    lst_1 = [[] for _ in range(x * 2)]
    lst_2 = ['' for _ in range(x * 2)]
    count = 0
    x = len(lst_1)
    for i_1 in range(len(lst_3)):
        c = hash_function(lst_3[i_1])
        if lst_2[c] == '':
            lst_2[c] = c
            count += 1
        lst_1[c].append(lst_3[i_1])


def proverka_minimum():  # Уменьшаем размер и рехеширование
    global lst_1
    global lst_2
    global count
    global x
    lst_3 = []
    for j in range(x):
        if lst_1[j] != '':
            lst_3.extend(lst_1[j])
    lst_1.clear()
    lst_2.clear()
    lst_1 = [[] for _ in range(round(x / 2))]
    lst_2 = ['' for _ in range(round(x / 2))]
    count = 0
    x = len(lst_1)
    for i_1 in range(len(lst_3)):
        c = hash_function(lst_3[i_1])
        if lst_2[c] == '':
            lst_2[c] = c
            count += 1
        lst_1[c].append(lst_3[i_1])


def deleat_slovo(number):  # удаление слова
    global count
    global x
    global lst_2
    global lst_1
    if number == 1:
        key_1 = int(input('ключик - '))
        lst_1[key_1] = []
        lst_2[key_1] = ''
        count -= 1
        if count < x / 2:
            proverka_minimum()
    elif number == 2:
        slovo_3 = input('слово - ')
        x_4 = find_slovo(slovo_3)
        print(x_4)
        lst_2[x_4] = ''
        lst_1[x_4] = []
        count -= 1
        if count < x / 2:
            proverka_minimum()
    elif number == 3:
        lst_1.clear()
        lst_2.clear()
        x = int(input('Новая длина массива - '))
        lst_1 = [[] for _ in range(x)]  # таблица слов
        lst_2 = ['' for _ in range(x)]  # таблица ключей
        print(lst_1, lst_2, sep='\n')
        count = 0


while True:
    choice_variant = (input(
        'Выбор номера задачи:\n1)Добавить слово\n2)Вывести слово'
        '\n3)вывести всю таблицу\n4)удалить слово\n0)закончить выполнение\nчто делаем? - '))
    if choice_variant == '1':
        slovo_2 = input()
        dobavit_slovo(slovo_2)
        continue
    elif choice_variant == '2':
        x_2 = int(input('ищем по слову или ключу - 1)Ключ 2)Слово -'))
        vivesti_slovo(x_2)
        continue
    elif choice_variant == '3':
        vivesti_vsu_tabel()
        continue
    elif choice_variant == '4':
        variant_1 = int(input('Удаляем по ключу или слову? или удалить всю таблицу целиком? -1)2)3) '))
        deleat_slovo(variant_1)
        continue
    elif choice_variant == '0':
        print('Спасибо за внимание, только как нибудь приходите ещё :З')
        break
    else:
        print('Такой команды нет')
        continue
