# Ready
from random import randint


a = []
b = []

while len(a) < 10000:
    a.append(randint(0, 100))

with open('01.txt', 'w') as f:
    for i in a:
        f.write(str(i) + '\n')

with open('01.txt', 'r', encoding='utf-8') as file:
    for row in file:
        b.append(int(row))

print(f'Сумма чисел из файла: {sum(b)}')
