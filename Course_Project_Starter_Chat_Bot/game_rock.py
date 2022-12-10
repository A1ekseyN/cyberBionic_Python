import random
import time


player_score = 0
pc_score = 0


def game_rock():
    try:
        player_move = int(input('\nВыберите знак: \n1. Камень ✊\n2. Ножницы ✌\n3. Бумага 🤚'
                           '\n\n4. Выход в главное меню\n>>> '))
        pc_move = random.randint(1, 3)
        if player_move == 1 or player_move == 2 or player_move == 3:
            print('Раз!!!')
            time.sleep(0.5)
            print('Два!!!')
            time.sleep(0.5)
            print('Три!!!')
            time.sleep(0.5)
    except:
        print('Введите число ')
        game_rock()


    def player_win():
        global player_score
        player_score += 1
        print('\nПобеда игрока 🏆🏆🏆')
        print(f'Счёт игры: \n-- 😎 Игрок: {player_score}\n-- 🤖 Компьютер: {pc_score}')
        game_rock()

    def pc_win():
        global pc_score
        pc_score += 1
        print('\n🤖 Победа компьютера 🤖')
        print(f'Счёт игры: \n-- 😎 Игрок: {player_score}\n-- 🤖 Компьютер: {pc_score}')
        game_rock()


    if player_move == pc_move:
        print('\n--- Ничья ---')
        print(f'Счёт игры: \n-- 😎 Игрок: {player_score}\n-- 🤖 Компьютер: {pc_score}')
        game_rock()
    elif player_move == 1 and pc_move == 2:
        print('✊ --> ✌')
        player_win()
    elif player_move == 1 and pc_move == 3:
        print('✊ <-- 🤚')
        pc_win()
    elif player_move == 2 and pc_move == 1:
        print('✌ <-- ✊')
        pc_win()
    elif player_move == 2 and pc_move == 3:
        print('✌ --> 🤚')
        player_win()
    elif player_move == 3 and pc_move == 1:
        print('🤚 --> ✊')
        player_win()
    elif player_move == 3 and pc_move == 2:
        print('🤚 <-- ✌')
        pc_win()
    elif player_move == 4:
        pass
    else:
        game_rock()

#game_rock()
