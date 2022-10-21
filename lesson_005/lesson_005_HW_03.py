# Ready
from colorama import Fore, Style

print('Введите код цвета в цветовом пространстве RGB. Каждый цвет в диапазоне от 0 до 255.')
r = int(input(f'{Fore.RED}R:{Style.RESET_ALL} '))
g = int(input(f'{Fore.GREEN}G:{Style.RESET_ALL} '))
b = int(input(f'{Fore.LIGHTBLUE_EX}B:{Style.RESET_ALL} '))

if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
    color = (r, g, b)
    print(f'Вы ввели RGB цвет: {color}.')
else:
    print('\nВы ввели не правильные параметры для цвета.')
