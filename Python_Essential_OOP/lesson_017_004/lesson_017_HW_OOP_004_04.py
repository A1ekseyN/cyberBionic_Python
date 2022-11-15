# Ready
print('Скрипт определяет или вы ввели число или другие символы.')
a = input("Введите число: ")


class Exept():
    try:
        a = int(a)
        print(f'\nВы ввели число: {a}')
    except:
        print('\nВы ввели либо буквы, либо специальные символы.')


def test():
    try:
        print(f"Вы ввели: {a}.")
    except Exept:
        pass


test()
