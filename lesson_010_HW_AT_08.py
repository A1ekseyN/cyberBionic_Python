# Ready
year = int(input('Введите год для проверки или он високосный: '))


def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if leap(year):
    print(f"{year} - год является високосным.")
elif leap(year) == False:
    print(f"{year} - год не является високосным.")

print('Hello')