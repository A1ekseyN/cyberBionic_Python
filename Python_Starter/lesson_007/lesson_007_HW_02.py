# Ready

a = {
    'gl': 'google.com',
    'vk': 'vkontakte.ru',
    'yt': 'youtube.com',
    'insta': 'instagram',
    'od': 'odnoklassniki',
    'fb': 'facebook',
}

ask = input('Введите название сайта: ')
www = ask

if ask in a:
    print(f'Вы запросили сайт: {ask}.')
    print(f'\n- Короткое название: {ask}\n- Полный адресс сайта: {a.get(www)}')
else:
    print(f'\nСайта который вы запросили, нет в БД. Но, есть: ')
    for i in a.keys():
        print(f'\t- {i}')
