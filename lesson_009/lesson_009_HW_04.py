# Ready
import sys
sys.setrecursionlimit(2000)


a = int(input('Введите 1-е число: '))
b = int(input('Введите 2-е число: '))
summa = 0


def sum_n():
    if a == b:
        return print(f'Сумма натуральный чисел от {a} до {b} = 0.')
    return print(f'Сумма натуральных чисел от {a} до {b} = {a + sum_numbers(b - 1)}.')


def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

sum_n()
