# Ready
a = [0, 1, 2, 3, 4, 5]
b = [i for i in a[::-1]]    # Генератор перевернутого списка
c = range(0, 20)
d = [i for i in c[::-1]]    # Генератор перевернутого списка с использованием range

print(a)
print(b)
print([i for i in c])
print(d)
