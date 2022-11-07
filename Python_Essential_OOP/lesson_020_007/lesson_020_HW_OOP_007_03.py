# Ready
a = [0, 1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10]
n = int(input('Сколько первых чисел натуральных чисел отобразить?\n>>> '))
cnt = 0

def foo():
    global a
    global cnt
    for i in a:
        if i < 1:
            a.remove(cnt)
            a.insert(cnt, -1)
            cnt += 1
        cnt = 0

    while True:
        try:
            b = [i for i in a if i // 1 == i and i // i == 1 and i > 0]
            print(f'Первые {n} натуральных чисел: {b[0:n]}')
            break
        except ZeroDivisionError:
            print('ZeroDivision')
            continue


foo()
