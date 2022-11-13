def ask_number():

    try:
        n = int(input('Начинаем считать с числа - 2.\nДо какого числа считаем простые числа?\n>>> '))
    except:
        ask_number()
    return n
