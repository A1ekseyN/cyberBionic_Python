import math


def volume():
    # Функция для расчёта объема цилиндра
    r = 1
    h = 0.6
    v = (math.pi * (r ** 2)) * h
    return f'Объем цилиндра радиусом {v}'
