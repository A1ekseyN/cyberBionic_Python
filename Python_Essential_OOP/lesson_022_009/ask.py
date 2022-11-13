import pickle


def ask():
    b = pickle.load(open('01.json', 'rb'))
    print('Данные прочитаны из файла: 01.json. И записаны в переменную: b')

    ask = input('\nВведите название сайта:\n>>> ')
    www = ask

    if ask in b:
        print(f'Вы запросили сайт: {ask}')
        print(f'\n- Короткое название: {ask}\n- Полный адресс сайта: {b.get(www)}')
    else:
        print(f'\nСайта который вы запросили, нет в БД. Но, есть: ')
        for i in b.keys():
            print(f'\t- {i}')
