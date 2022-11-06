# Ready
a = int(input('Введите высоту треугольника: '))
b = int(input('Введите ширину треугольника: '))

if a <= 0 or b <= 0:
    print("\nВведите высоту и ширину треугольника еще раз: ")
    a = int(input('Введите высоту треугольника: '))
    b = int(input('Введите ширину треугольника: '))
    if a <= 0 or b <= 0:
        print('Треугольник не может быть с нулевой стороной.')

else:
    if a < b:
        result = b / a
    elif a > b:
        result = a / b

    for i in range(min(a, b) + 1):
        d = int(i * result)
        for _ in range(d):
            print('*', end='')
        print()
