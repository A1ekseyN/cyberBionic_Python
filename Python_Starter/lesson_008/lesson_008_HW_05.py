# Ready
from colorama import Fore, Style


print('Индекс массы тела - величина, позволяющая оценить степень соответствия массы человека и его роста'
      ' и тем самым косвенно судить о том, \nявляется ли масса недостаточной, нормальной или избыточной. '
      'Важен при определении показаний для необходимости лечения.'
      '\n\nВведите свой рост и вес, или "off" для выхода из программы.')


def bmi():
    """Функция для калькуляции ИМТ, определения текста, и цвета текста"""
    index_bmi = weight / (growth / 100) ** 2

    if index_bmi < 16:
        index_text = 'Выраженный дефицит массы'
        index_color = Fore.CYAN
    elif 16 < index_bmi < 16.99:
        index_text = 'Умеренный дифицит массы'
        index_color = Fore.LIGHTCYAN_EX
    elif 17 < index_bmi < 18.49:
        index_text = 'Небольшой дефицит массы'
        index_color = Fore.LIGHTGREEN_EX
    elif 18.5 < index_bmi < 24.99:
        index_text = ('Норма')
        index_color = Fore.GREEN
    elif 24.5 < index_bmi < 29.99:
        index_text = 'Избыточная масса тела (предожирение)'
        index_color = Fore.YELLOW
    elif 30 < index_bmi < 34.99:
        index_text = 'Ожирение I степени'
        index_color = Fore.LIGHTYELLOW_EX
    elif 35 < index_bmi < 39.99:
        index_text = 'Ожирение II степени'
        index_color = Fore.RED
    elif 40 < index_bmi:
        index_text = 'Ожирение III степени'
        index_color = Fore.LIGHTRED_EX
    return print(f'\nВаш ИМТ: {index_color}{round(index_bmi, 2)}{Style.RESET_ALL}'
                 f'\nУ вас: {index_color}{index_text}{Style.RESET_ALL}')


while True:
    growth = input('\nВведите ваш рост: ')
    if growth != 'off':
        growth = float(growth)
    else:
        break
    weight = input('Введите ваш вес: ')
    if weight != 'off':
        weight = float(weight)
    else:
        break

    bmi()
