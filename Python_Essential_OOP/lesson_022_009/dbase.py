import pickle


a = {
    'gl': 'google.com',
    'vk': 'vkontakte.ru',
    'yt': 'youtube.com',
    'insta': 'instagram',
    'od': 'odnoklassniki',
    'fb': 'facebook',
}

def save():
    pickle.dump(a, open('01.json', 'wb'))
    print('Данные сохранены в файл: 01.json')
