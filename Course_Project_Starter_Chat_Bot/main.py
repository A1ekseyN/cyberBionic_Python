print("logo")
print("Привет. Я чат-бот. Могу предложить несколько варинтов для взаимодействия:\n")

def menu():
    # Функция меню или навигации по программе.
    print('Выберите вариант: \n1. Порекомендовать фильм\n2. Порекомендовать музыку\n3. Порекомендовать игру за жанром'
          '\n4. Рассказать анекдот\n5. Рассказать интересную историю\n6. Поиграть в игру.\n7. Выход')
    try:
        menu_sub = int(input('\nВыберите раздел: \n>>> '))
    except:
        print('Попробуйте ввести цифру.')
        menu()

    if menu_sub == 1:
        movie_rec()
    elif menu_sub == 2:
        music_rec()
    elif menu_sub == 3:
        game_rec()
    elif menu_sub == 4:
        joke()
    elif menu_sub == 5:
        cool_story()
    elif menu_sub == 6:
        game_choice()
    elif menu_sub == 7:
        print('\nЗавершение программы. До новой встречи.')
    else:
        menu()


def movie_rec():
    # Функция для рекомендации фильмов
    pass


def music_rec():
    # Функция рекомендации музыки
    pass


def game_rec():
    # Функция рекомендация игр
    pass


def joke():
    # Функция для рассказа шутки
    pass


def cool_story():
    # Функция для интересных историй
    pass


def game_choice():
    # Функция для выбора игры
    pass


menu()
