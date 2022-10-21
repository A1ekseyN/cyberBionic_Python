# Ready
import math


a = int(input('Введите число - a: '))
b = int(input('Введите число - b: '))
c = int(input('Введите число - c: '))


def quadratic_equation(a, b, c):
    discriminant = 0

    def calc_result(a, b, c):
        global discriminant
        discriminant = b ** 2 - 4 * a * c
        return discriminant

    if calc_result(a, b, c) < 0:
        return "\nКорней нет."
    elif calc_result(a, b, c) == 0:
        return -(b / (2 * a))
    else:
        return (- b + math.sqrt(discriminant)) / (2 * a), (- b - math.sqrt(discriminant)) / (2 * a)


print(quadratic_equation(a, b, c))
