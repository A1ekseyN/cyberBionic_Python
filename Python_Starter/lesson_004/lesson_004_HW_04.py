# Ready
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
temp = []
s = 0

for i in range(a, b + 1):
    temp.append(i)

average = sum(temp) // len(temp)

for i in range(a, b + 1):
    if average == 0:
        average = 1
    elif i % average == 0:
        s += i

print(s)
