# Ready
sport_complex = {
    'sports': ['football', 'baseball'],
    'trainer': ['jordan', 'west', 'zidane'],
    'timetable': '9.00',
    'price': '5 $'
}

print('Вы можете выбрать интересующий вас раздел из существующих: '
      '\n1. Виды спорта\n2. Тренеры\n3. Расписание\n4. Цена\n5. Вы ищете конкретного тренера')
a = int(input('\nЧто именно вас интересует? \n>>> '))

def menu():
    if a == 1:
        return print(f'У нас в спортивном комплексе есть секция - {sport_complex.get("sports")}.')
    elif a == 2:
        return print(f'У нас в спортивном комплексе есть тренер - {sport_complex.get("trainer")}.')
    elif a == 3:
        return print(f'У нас в спортивном комплексе тренировки проходят в - {sport_complex.get("timetable")}.')
    elif a == 4:
        return print(f'У нас в спортивном комплексе цена тренировки - {sport_complex.get("price")}.')
    elif a == 5:
        b = input(f'Введите имя тренера, к которому хотите записаться на тренировку: ({sport_complex.get("trainer")})'
                  f'\n>>> ')
        try:
            print(sport_complex[b])
            print(b in sport_complex.items())
            return print('Вы нашли тренера, которого искали.')
        except KeyError:
            return print(f'\nУ нас тренера с именем {b.title()}.'
                         f'\nНо, у нас есть тренера по имени: {sport_complex.get("trainer")}.')


menu()
