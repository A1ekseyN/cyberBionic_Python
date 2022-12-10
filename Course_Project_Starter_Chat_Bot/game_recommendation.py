from random import randint


games_adventure = [
    ['Subnautica', 'Приключения, симулятор выживания', '2018'],
    ['Subnautica: Below Zero', 'Приключения, симулятор выживания', '2019'],
    ['Fallout 2', 'RPG, Приключения', '1998'],
]
games_survival = [
    ['Subnautica', 'Приключения, симулятор выживания', '2018'],
    ['Subnautica: Below Zero', 'Приключения, симулятор выживания', '2019'],
]
games_mmo = [
    ['Destiny 2', 'Шутер, MMORPG', '2017'],
    ['Deep Rock Galactic', 'Шутер, MMORPG', '2018'],
    ['Eve Online', 'ММОRPG, Песочница, Космический симулятор, Ролевая игра', '2003'],
    ['World of Warcraft', 'MMORPG', '2004']
]
games_shooter = [
    ['Destiny 2', 'Шутер, MMORPG', '2017'],
    ['Deep Rock Galactic', 'Шутер, MMORPG', '2018'],
]
games_races = [
    ['Dirt 2.0', 'Гонки', '2019'],
    ['Gran Turismo 7', 'Гонки', '2022'],
]
games_strategy = [
    ['Frostpunk', 'Стратения, выживание', '2018'],
    ['Warcraft 3', 'Стратегия, RPG', '2002'],
    ['StarCraft', 'Стратегия', '1998'],
    ['StarCraft 2', 'Стратегия', '2010'],
]
games_rpg = [
    ['Destiny 2', 'Шутер, MMORPG', '2017'],
    ['Eve Online', 'ММОRPG, Песочница, Космический симулятор, Ролевая игра', '2003'],
    ['World of Warcraft', 'MMORPG', '2004'],
    ['Warcraft 3', 'Стратегия, RPG', '2002'],
    ['Fallout 2', 'RPG, Приключения', '1998'],
]


def game_recommendation():
    rnd_genr = randint(1, 7)

    if rnd_genr == 1:
        rnd_genr = games_adventure
    elif rnd_genr == 2:
        rnd_genr = games_survival
    elif rnd_genr == 3:
        rnd_genr = games_mmo
    elif rnd_genr == 4:
        rnd_genr = games_shooter
    elif rnd_genr == 5:
        rnd_genr = games_races
    elif rnd_genr == 6:
        rnd_genr = games_strategy
    elif rnd_genr == 7:
        rnd_genr = games_rpg

    rnd_game = randint(0, len(rnd_genr) - 1)
    print(f'Рекомендую игру: {rnd_genr[rnd_game][0]}'
          f'\nЖанр: {rnd_genr[rnd_game][1]}'
          f'\nГод выхода: {rnd_genr[rnd_game][2]}')
