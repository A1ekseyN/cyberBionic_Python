# Ready
def operations():
    global operation
    operation = input('\nВиберіть математичу дію:'
                '\n\t1. Додавання\n\t2. Віднімання\n\t3. Множення\n\t4. Ділення'
                '\n\t5. Зведення в ступінь\n\t6. Зведення до квадратного кореня\n\t7. Зведення до'
                      ' кубічного кореня'
                '\n\t8. Для виходу натисніть: 8, "off", "e", "exit"'
                '\n\tВиберіть дію: ')


def numbers():
    global a
    global b
    if operation == '1' or operation == '2' or operation == '3' or operation == '4' or operation == '5':
        try:
            a = int(input('\nВведіть 1-е число: '))
            b = int(input('Введіть 2-е число: '))
        except:
            print("Будь ласка введіть цифри.")
            numbers()
        return a, b
    elif operation == '6' or operation == '7':
        a = int(input('\nВведите 1-е число: '))
        return a


def addition():
    return print(f"\nСумма чисел: {a} + {b} = {a + b}.")


def minys():
    return print(f"\nВіднімання: {a} - {b} = {a - b}.")


def multiplay():
    return print(f"\nМноження: {a} * {b} = {a * b}.")


def devision():
    if b != 0:
        return print(f"\nДілення: {a} / {b} = {int(a / b)}.")
    elif b == 0:
        return print(f'\nНельзя делить на ноль.')


def exponentiation():
    return print(f"\nЗведення в ступінь числа {a} в ступінь {b} = {a ** b:}.")


def square_root():
    return print(f"\nКвадратный корень из числа {a} = {round(a ** (0.5),2)}.")


def cube_root():
    return print(f"\nЗведення дл кубічного кореня {a} = {round(a ** (1. / 3.), 2)}.")


while True:
    operations()
    if operation == '1':
        numbers()
        addition()
    if operation == '2':
        numbers()
        minys()
    if operation == '3':
        numbers()
        multiplay()
    if operation == '4':
        numbers()
        devision()
    if operation == '5':
        numbers()
        exponentiation()
    if operation == '6':
        numbers()
        square_root()
    if operation == '7':
        numbers()
        cube_root()
    if operation == '8' or operation == 'off' or operation == 'e' or operation == 'exit':
        break
