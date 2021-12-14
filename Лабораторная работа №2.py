print('Введите две даты для сравнения какая позже в формате дд.мм.гггг')
while True:
    a = input('первая дата ')
    b = input('вторая дата ')
    if len(a) < 9 or len(a) > 10 or len(b) < 9 or len(b) > 10:
        print('Формат не соответсвует')
        continue
    a1 = a.split('.')
    b1 = b.split('.')
    a1 = list(map(int, a1))
    b1 = list(map(int, b1))
    if a1[0] > 30 or a1[1] > 12 or a1[2] < 0 or b1[0] > 30 or b1[1] > 12 or b1[2] < 0:
        print('Дата введена не верно')
        continue
    break

if a1[2] > b1[2]:
    print('дата', a, 'позже даты', b)
elif a1[2] == b1[2]:
    if a1[1] > b1[1]:
        print('дата', a, 'позже даты', b)
    elif a1[1] == b1[1]:
        if a1[0] > b1[0]:
            print('дата', a, 'позже даты', b)
        elif a1[0] == b1[0]:
            print('Это одна дата')
        else:
            print('дата', b, 'позже даты', a)
    else:
        print('дата', b, 'позже даты', a)
else:
    print('дата', b, 'позже даты', a)
