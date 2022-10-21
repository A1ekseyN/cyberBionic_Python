# Ready
items = {'item': 'price', 'phone': '200 $'}
flag = True


def add_items():
    global flag
    print('Введите название товара, а затем его цену. Для выхода пишите - "e" или "exit".')
    a = input('Введите название товара: ')
    b = input('Введите цену товара: ')
    print()
    if a == 'exit' or a == 'e' or b == 'e' or b == 'exit':
        flag = False
    else:
        items[a] = b
    print(items)


while flag:
    add_items()

print(items)
