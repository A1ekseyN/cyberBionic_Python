# Ready
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
c = [i for i in a if not i % 2]
d = []

# Цикл
for i in a:
    if not i % 2:
        b.append(i ** 2)

# Генератор
for i in [i ** 2 for i in a if not i % 2]:
    d.append(i)

print(b)
print(d)
