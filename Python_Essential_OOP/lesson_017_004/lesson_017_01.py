print('Скрипт определяет или вы ввели число больше или меньше - 0.')
a = input("Введите число: ")


class xept():
    a = input()

class number_less_zero():
    if a >= 0:
        pass
    else:
        print("\nЧисло меньше 0. Сработал exeption.")


def counter():
    try:
        print(a + a)
#        print(f"\nВы ввели число - {a}.")
    except number_less_zero:
        print(f"Введено число меньше 0.")


counter()
