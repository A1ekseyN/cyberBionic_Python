# Ready
def numbers():
    a = int(input('Введите число a: '))
    b = int(input('Введите число a: '))
    c = int(input('Введите число a: '))

    average = (a + b + c) // 3
    return print(f'Среднее арифметическое 3-х чисел: {average:,.0f}.\n')

while True:
    numbers()
