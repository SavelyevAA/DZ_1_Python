x = int(input('Введите координаты x = '))
y = int(input('Введите координаты y = '))
if x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Первая четверть плоскости')
    elif x < 0 and y > 0:
        print('Вторая четверть плоскости')
    elif x < 0 and y < 0:
        print('Третья четверть плоскости')
    elif x > 0 and y < 0:
        print('Четвертая четверть плоскости')
else:
    print('должно быть X ≠ 0 и Y ≠ 0')