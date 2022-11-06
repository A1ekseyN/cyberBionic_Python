# Ready
worker = {
    'Alex Berger': {
        'surname': 'berger',
        'experience': '7 years',
        'pirtfolio': 'google',
        'efficiency': '95 %',
        'steck': 'python',
        'salary': '9000 $'
    },
    'Rodger Zet': {
        'surname': 'zet',
        'experience': '5 years',
        'pirtfolio': 'yahooo',
        'efficiency': '75 %',
        'steck': 'c#',
        'salary': '6500 $'
    },
    'Gandi Jordan': {
        'surname': 'jordan',
        'experience': '2 years',
        'pirtfolio': 'ciclum',
        'efficiency': '60 %',
        'steck': 'javasript',
        'salary': '2500 $'
    },
}

print(f'У нас в компании работает - {len(worker)} сотрудника: ')
for i in worker:
    print(f"\t- {i}")

while True:
    temp = input('\nМеню для работы с сотрудниками.'
                 '\n\t1. Показать данные про сотрудников\n\t2. Обновить информацию про сотрудника'
                 '\n\t3. Сортировать за фамилией\n\t4. Сортировать за эффективностью'
                 '\n\t5. Удалить данные про сотрудника'
                 '\n\t6. Выход'
                 '\n\n\tВведите цифру для продолжения: \n')

    if temp == '1':
        for i in worker:
            print(f'\t- {i} - {worker[i].values()}')

    elif temp == '2':
        print('В этом меню вы можете обновить данные сотрудников.')
        temp_worker_name = input('\nВведите имя рабочего, для изменения данных: ')
        temp_data = input('Введите данные: ')
        worker.update({temp_worker_name: temp_data})
        print(f'Данные сотрудника {temp_worker_name} обновлены.')

    elif temp == '3':
        print(f'Сотрудники отсортированы по фамилии: ')
        for i in sorted(worker.keys()):
            print(f"\t- {i}")

    elif temp == '4':
        print('Сотрудники сортированы за эффективностью: ')
        for i in sorted(worker.values(), reverse=True, key=lambda values: values['efficiency']):
            print(f'- {i["surname"].title()} - эффективность: {i["efficiency"]}')

    elif temp == '5':
        delete_worker = input('\nДля удаления сотрудника напишите его имя: ')
        try:
            del worker[delete_worker]
            print(f'Сотрудник {delete_worker} покинул нашу кампанию. Всего у нас осталось {len(worker)} сотрудника.')
        except:
            print(f'\nВы ввели не правильное имя сотрудника. Попробуйте еще раз.')

    elif temp == '6':
        break

    else:
        print('Вы выбрали не правильную цифру.')
