while True:
    vibor = int(input('Выбор задания: '))
    if vibor == 1:
        a = input('Присваиваем строку ')
        while True:
            x = int(input('Введите цыфрву что вы хотите сделать:\n 1)Вывести длину '
                          '\n 2)Присвоить строку\n 3)Сцеплениестрок\n 4)Выделение подстроки\n '
                          '5)Поиск вхождения\n 0)чтобывыйтииз цыкла\n'))
            if x == 1:
                print('Выводим длину строки:', len(a))
            elif x == 2:
                a = input('Введите новую строку: ')
                print(a)
            elif x == 3:
                a += input('Введите строку которую хотите присвоить: ')
                print(a)
            elif x == 4:
                word = input('Подстрока которую надо выделить: ')
                high = word.upper()
                if word in a:
                    print(a.replace(word, high))
                else:
                    print('Такой подстроки нет')
            elif x == 5:
                print(a.find(input('Введите то что хотите найти: ')))
            elif x == 0:
                break
            else:
                print('Такую функцию я ещё не придумал')
                continue
    elif vibor == 2:
        x1 = int(input('Сколько элементов списка будет?: '))
        spisok=[]
        for i1 in range(x1):
            slovo = input('Вводим элемент: ')
            spisok.append(slovo)
        while True:
            x2 = int(input('Введите цыфрву что вы хотите сделать:\n 1)Перебор элементов списка '
                           '\n 2)Операция формирования списка \n 3)Вставка элемента в список\n 4)Удаление элемента\n '
                           '5)Перестановка элементов списка\n 6)Печать односвязного списка\n 0)что-бы выйтииз цыкла\n'))
            if x2 == 1:
                for j1 in range(len(spisok)):
                    print(spisok[j1])
            elif x2 == 2:
                spisok.clear()
                x3 = int(input('Сколько элементов списка будет?: '))
                for j2 in range(x3):
                    slovo = input('Вводим элемент: ')
                    spisok.append(slovo)
            elif x2 == 3:
                element = input('Элемент который мы хотим добавить: ')
                spisok.append(element)
            elif x2 == 4:
                delit = input('элемент который хотите удалить')
                spisok.remove(delit)
            elif x2 == 5:
                pervii = input('Первый элемент')
                vtoroi = input('Второй элемент')
                first = spisok.replace(pervii, vtoroi)
                second = spisok.replace(vtoroi, pervii)
                print(second)
            elif x2 == 6:
                print(spisok)
            elif x2 == 0:
                break
            else:
                print('Такой функции ещё нет')
    elif vibor == 0:
        break
    else:
        print('Такой функции нет')
