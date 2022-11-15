# Ready
import re


ask = input('Введите несколько слов через пробел: \n>>> ')


def answer():
    result = re.split(r'[\s,]', ask)
    print(f'\nДля текста {ask}.\nНайдены следующие слова, где содержиться более 3-х символов: ')
    for i in result:
        if len(i) >= 3:
            print(f'{i} --> {i[-3:]}')

answer()
