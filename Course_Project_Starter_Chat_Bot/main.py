from random import randint
from hello import *
from joke import get_joke
from exit import *
from story import *


logo()
hello()


def menu():
    # Функция меню или навигации по программе.
    print('\nВыберите вариант: \n1. Порекомендовать фильм\n2. Порекомендовать музыку\n3. Порекомендовать игру за жанром'
          '\n4. Рассказать анекдот\n5. Рассказать интересную историю\n6. Поиграть в игру\n7. Выход')
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
    print('Учитывая рейтинг IMDb, и свои предпочтения, могу порекомендовать несколько фильмов.')

    def movie_rec_sys():
        # Система для рекомендации фильма + дополнительное меню.
        movies = [
            ['Побег из Шоушенка', 9.2, 1994, 'Фрэнк Дарабонт', 'Драма'],
            ['Крестный отец', 9.2, 1972, 'Фрэнсис Форд Коппола', 'Детектив, Драма'],
            ['Форрест Гамп', 8.8, 1994, 'Роберт Земекис', 'Драма, Мелодрама'],
            ['Бойцовский клуб', 8.7, 1999, 'Дэвид Финчер', 'Драма, Триллер, Мифический фильм'],
            ['Матрица', 8.7, 1999, 'Энди и Ларри Вачовски', 'Научная фантастика, Приключение, Боевик'],
            ['Назад в будущее', 8.5, 1985, 'Роберт Земекис', 'Научная фантастика, Семейный фильм, Приключение'],
            ['Паразиты', 8.5, 2019, 'Пон Чжун Хо', 'Комедия, Драма, Триллер'],
            ['Престиж', 8.5, 2006, 'Кристофер Нолан', 'Фэнтези, Драма, Мистический фильм'],
            ['ВАЛЛ-И', 8.4, 2008, 'Эндрю Стэнтон', 'Мультфильм, Семейный фильм, Приключение'],
            ['Джокер', 8.3, 2019, 'Тодд Филлипс', 'Детектив, Драмма, Триллер'],
            ['Дюна', 8.0, 2021, 'Дени Вильнёв', 'Эпическая фантастика'],
        ]

        rnd_movie = randint(0, len(movies) - 1)
        print(f'\nРекомендую фильм: {movies[rnd_movie][0]}\nIMDb рейтинг: {movies[rnd_movie][1]}'
              f'\nГод выхода на экран: {movies[rnd_movie][2]}\nРежиссёр: {movies[rnd_movie][3]}'
              f'\nЖанр: {movies[rnd_movie][4]}')


        def movie_menu():
            # Функция меню раздела фильмов
            try:
                ask = int(input('\n1. Отобразить еще один фильм\n2. Выйти в главное меню\n3. Выйти из программы\n>>> '))
                if ask == 1:
                    movie_rec_sys()
                elif ask == 2:
                    menu()
                elif ask == 3:
                    exit_logo()
                    exit()
                elif ask != 1 and ask != 2 and ask != 3:
                    print('Нет, такого пункта меню, попробуйте еще раз.')
                    movie_menu()
                else:
                    print('\nЧто-то случилось. Нужно ввести 1, 2 или 3.')
            except ValueError:
                print('\nОшибка типа вводимых данных. Попробуйте ввести цифры.')
                movie_menu()

        movie_menu()

    movie_rec_sys()


def music_rec():
    # Функция рекомендации музыки
    print('\nУчитывая рейтинг популярных песен, и свои предпочтения в музыке. Рекомендую песню: ')


    def rec_sys():
        # Система рекомендации музыки + дополнительное меню.
        songs = [
            ['Ariana Grande', 'Break up with your girlfried in bored', 2019],
            ['Masked Wolf', 'Astronaut in the Ocean', 2019],
            ['Selena Gomez', 'BoyFriend', 2020],
            ['David Rawlings', 'Cumberland Gap', 2017],
            ['Ooyy', 'Come 2gether', 2020],
            ['Ooyy', 'Faded', 2018],
            ['FanEOne', 'Bre Petrunko', 2020],
            ['Halsey', 'Gasoline', 2015],
            ['Dimitri Vegas & Like Mike vs Diplo Kid', 'Hey Baby', 2016],
            ['Jerry Heil', 'Кохайтеся Чорнобриві', 2022],
            ['Shahmen', 'Mark', 2015],
        ]

        rnd_music = randint(0, len(songs) - 1)
        print(f'\nРекомендую песню: {songs[rnd_music][0]}\nИсполнителя: {songs[rnd_music][1]}'
              f'\nДата выхода: {songs[rnd_music][2]}')

        def music_menu():
            # Функция меню раздела музыки
            try:
                ask = int(input('\n1. Отобразить еще один трек\n2. Выйти в главное меню\n3. Выйти из программы\n>>> '))
                if ask == 1:
                    rec_sys()
                elif ask == 2:
                    menu()
                elif ask == 3:
                    exit_logo()
                    exit()
                elif ask != 1 and ask != 2 and ask != 3:
                    print('Нет, такого пункта меню, попробуйте еще раз.')
                    music_menu()
                else:
                    print('\nЧто-то случилось. Нужно ввести 1, 2 или 3.')
            except ValueError:
                print('\nОшибка типа вводимых данных. Попробуйте ввести цифры.')
                music_menu()

        music_menu()

    rec_sys()


def game_rec():
    # Функция рекомендация игр
    pass


def joke():
    # Функция для рассказа шутки
    get_joke()

    def joke_menu():
        # Функция меню раздела шутки
        try:
            ask = int(input('\n1. Отобразить еще одну шутку\n2. Выйти в главное меню\n3. Выйти из программы\n>>> '))
            if ask == 1:
                joke()
            elif ask == 2:
                menu()
            elif ask == 3:
                exit_logo()
                exit()
            elif ask != 1 and ask != 2 and ask != 3:
                print('Нет, такого пункта меню, попробуйте еще раз.')
                joke_menu()
            else:
                print('\nЧто-то случилось. Нужно ввести 1, 2 или 3.')
        except ValueError:
            print('\nОшибка типа вводимых данных. Попробуйте ввести цифры.')
            joke_menu()

    joke_menu()


def cool_story():
    # Функция для интересных историй
    story_random()

    def story_menu():
        # Функция меню раздела историй
        try:
            ask = int(input('\n1. Отобразить еще одну историю\n2. Выйти в главное меню\n3. Выйти из программы\n>>> '))
            if ask == 1:
                cool_story()
            elif ask == 2:
                menu()
            elif ask == 3:
                exit_logo()
                exit()
            elif ask != 1 and ask != 2 and ask != 3:
                print('Нет, такого пункта меню, попробуйте еще раз.')
                story_menu()
            else:
                print('\nЧто-то случилось. Нужно ввести 1, 2 или 3.')
        except ValueError:
            print('\nОшибка типа вводимых данных. Попробуйте ввести цифры.')
            story_random()

    story_menu()


def game_choice():
    # Функция для выбора игры
    pass


menu()
