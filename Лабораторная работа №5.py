x = int(input('задаём размер массива - '))
lst_1 = [[] for i in range(x)]  # таблица слов
lst_2 = ['' for i in range(x)]  # таблица ключей
print(lst_1, lst_2, sep='\n')
count = 0


def dobavit_slovo(slovo_1):  # добавление слова
    global count
    global x
    c = hash_function(slovo_1)
    if lst_2[c] == '':
        lst_2[c] = c
        count += 1
    lst_1[c].append(slovo_1)
    if count == x / 2:
        lst_1.append([])
        lst_1.append([])
        lst_2.append('')
        lst_2.append('')
        x = len(lst_1)
    print(lst_1)


def hash_function(slovo):  # рассчёт хэш функции
    h = 0
    a = 127
    for v in range(len(slovo)):
        h = (a * h + (ord(slovo[v]))) % x
    print(h, '-хэш')
    return h


def vivesti_slovo(num):
    print(lst_2[num], ':', lst_1[num])


def vivesti_vsu_tabel():
    for i in range(len(lst_1)):
        print(lst_2[i], ':', *lst_1[i])


def deleat_slovo(number):
    global count
    global x
    global lst_2
    global lst_1
    if number == 1:
        key_1 = int(input('ключик - '))
        lst_1[key_1] = []
        lst_2[key_1] = ''
        count -= 1
    elif number == 2:
        slovo_3 = input('слово - ')
        lst_2[lst_1.index(slovo_3)] = ''
        lst_1[lst_1.index(slovo_3)] = []
        count -= 1
    elif number == 3:
        lst_1.clear()
        lst_2.clear()
        x = int(input('Новая длина массива - '))
        lst_1 = [[] for i in range(x)]  # таблица слов
        lst_2 = ['' for i in range(x)]  # таблица ключей
        print(lst_1, lst_2, sep='\n')


while True:
    choice_variant = (input(
        'Выбор номера задачи:\n1)Добавить слово\n2)Вывести слово по ключу'
        '\n3)вывести всю таблицу\n4)удалить слово\n0)закончить выполнение\nчто делаем? - '))
    if choice_variant == '1':
        slovo_2 = input()
        dobavit_slovo(slovo_2)
        continue
    elif choice_variant == '2':
        key = int(input('номер который будем выводить - '))
        vivesti_slovo(key)
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
        print('Такой команды нет¯\_(ツ)_/¯')
        continue
