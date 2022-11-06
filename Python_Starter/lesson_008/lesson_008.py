import math


a = input('Введите математическое действие: ')

def addition(a, b):
    return a + b


def minys(a, b):
    return a - b


def multiplay(a, b):
    return a * b


def devision(a, b):
    if b != 0:
        return a / b
    else:
        return 'Нельзя делить на ноль.'


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


if a == '+':
    print(addition(3, 5))
elif a == '-':
    print(minys(10, 5))
elif a == '*':
    print(multiplay(5, 5))
elif a == '/':
    print(devision(25, 0))
elif a == 'cos':
    print(cos(5))
elif a == 'sin':
    print(sin(25))
elif a == 'all':
    print(addition(3, 5))
    print(minys(50, 5))
    print(multiplay(5, 5))
    print(devision(25, 0))
    print(cos(5))
    print(sin(100))
