# Ready
def hello():
    name = input('Как вас зовут? ')
    if len(name) < 3:
        name = input('С первого раза не расслышал. Повторите, пожалуйста, ваше имя: ')
        if len(name) < 3:
            return print('\nПопробуйте еще раз.')
        return print(f'\nДобрый день, {name.title()}. Хорошего вам дня 😘😘😘.')
    else:
        print(f'\nДобрый день, {name.title()}. Хорошего вам дня. 🏕 ⛰ 😘 ')
    return name

hello()
