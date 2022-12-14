from hello import *
from joke import get_joke
from exit import *
from story import *
from game_recommendation import *
from game_rock import *

# Запуск игры Space Invaders
#import sys
#sys.path.append('./Space')
#from Space import main

#main.AlienInvasion()
#main.ai.run_game()


logo()
hello()


def menu():
    # Функция меню или навигации по программе.
    print('\nВыберите вариант меню: \n1. Порекомендовать фильм\n2. Порекомендовать музыку\n3. Порекомендовать игру за жанром'
          '\n4. Рассказать анекдот\n5. Рассказать интересную историю\n6. Поиграть в игру (Камень-ножницы-бумага)\n7. Выход')
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
        exit_logo()
        exit()
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
    # print() Перенести в функцию
    print('\n--- Система рекомендации игр за жанром. ---')
    game_recommendation()


    def game_menu_items():
        return '\nВыберите жанр:' \
               '\n1. Приключения\n2. Выживание\n3. MMORPG\n4. Шутер' \
               '\n5. Гонки\n6. Стратегии\n7. RPG\n8. Вернуться в Главное меню\n9. Выход из программы'


    def game_genre_recommendation():
        try:
            ask = int(input('\nВыберите жанр:\n>>> '))
            if ask == 1:
                rnd = randint(0, len(games_adventure) - 1)
                print(f'\nВ жанре Приключения, рекомендую: {games_adventure[rnd][0]}'
                      f'\nЖанр: {games_adventure[rnd][1]}\nГод выхода: {games_adventure[rnd][2]}')
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 2:
                rnd = randint(0, len(games_survival) - 1)
                print(f'\nВ жанре "Выживание", рекомендую: {games_survival[rnd][0]}'
                      f'\nЖанр: {games_survival[rnd][1]}\nГод выхода: {games_survival[rnd][2]}')
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 3:
                rnd = randint(0, len(games_mmo) - 1)
                print(f'\nВ жанре "MMORPG", рекомендую: {games_mmo[rnd][0]}'
                      f'\nЖанр: {games_mmo[rnd][1]}\nГод выхода: {games_mmo[rnd][2]}')
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 4:
                rnd = randint(0, len(games_shooter) - 1)
                print(f'\nВ жанре "Шутер", рекомендую: {games_shooter[rnd][0]}'
                      f'\nЖанр: {games_shooter[rnd][1]}\nГод выхода: {games_shooter[rnd][2]}')
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 5:
                rnd = randint(0, len(games_races) - 1)
                print(f'\nВ жанре "Гонки", рекомендую: {games_races[rnd][0]}'
                      f'\nЖанр: {games_races[rnd][1]}\nГод выхода: {games_races[rnd][2]}')
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 6:
                rnd = randint(0, len(games_strategy) - 1)
                print(f'\nВ жанре "Стратегии", рекомендую: {games_strategy[rnd][0]}'
                      f'\nЖанр: {games_strategy[rnd][1]}\nГод выхода: {games_strategy[rnd][2]}')
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 7:
                rnd = randint(0, len(games_rpg) - 1)
                print(f'\nВ жанре "RPG", рекомендую: {games_rpg[rnd][0]}'
                      f'\nЖанр: {games_rpg[rnd][1]}\nГод выхода: {games_rpg[rnd][2]}')
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 8:
                menu()
            elif ask == 9:
                exit_logo()
                exit()
            else:
                print('\nПопробуйте выбрать цифры 1 - 9.\n')
                game_genre_recommendation()
        except:
            print('\nПопробуйте еще раз. И введите цифры.\n')
            game_genre_recommendation()


    def game_rec_menu():
        # Функция меню раздела с рекоммендацией игр.
        try:
            ask = int(input('\n1. Отобразить игру за случайным жанром\n2. Рекомендовать игру за жанром'
                            '\n3. Выйти в главное меню\n4. Выйти из программы\n>>> '))
            if ask == 1:
                game_rec()
            elif ask == 2:
                print(game_menu_items())
                game_genre_recommendation()
            elif ask == 3:
                menu()
            elif ask == 4:
                exit_logo()
                exit()
            elif ask != 1 and ask != 2 and ask != 3 and ask != 4:
                print('\nНет, такого пункта меню, попробуйте еще раз.')
                game_rec_menu()
            else:
                print('\nЧто-то случилось. Нужно ввести 1, 2 или 3.')
        except ValueError:
            print('\nОшибка типа вводимых данных. Попробуйте ввести цифры.')
            game_rec_menu()

    game_rec_menu()


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
    game_rock()
    menu()


menu()
