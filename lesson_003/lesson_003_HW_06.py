# Ready
day = input("Введите день недели: ").lower()

match day:
    case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница':
        print('Сегодня на работу.')
    case 'суббота' | 'воскресение':
        print('Сегодня выходной день.')
    case _:
        print('Такого дня не существует.')
