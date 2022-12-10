a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
c = [i ** 2 for i in a if i % 2]


def prime():
    for i in a:
        if i % 2 != 0:
            b.append(i ** 2)
    return b


print(prime())
print(c)
