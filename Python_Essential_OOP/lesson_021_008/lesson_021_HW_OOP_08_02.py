# Ready
import pickle

a = {
    'gl': 'google.com',
    'vk': 'vkontakte.ru',
    'yt': 'youtube.com',
    'insta': 'instagram',
    'od': 'odnoklassniki',
    'fb': 'facebook',
}

pickle.dump(a, open('02.json', 'wb'))
print('Данные сохранены в файл: 02.json')

b = pickle.load(open('02.json', 'rb'))
print('Данные прочитаны из файла: 02.json. И записаны в переменную: b')

ask = input('\nВведите название сайта:\n>>> ')
www = ask

if ask in b:
    print(f'Вы запросили сайт: {ask}')
    print(f'\n- Короткое название: {ask}\n- Полный адресс сайта: {a.get(www)}')
else:
    print(f'\nСайта который вы запросили, нет в БД. Но, есть: ')
    for i in a.keys():
        print(f'\t- {i}')
