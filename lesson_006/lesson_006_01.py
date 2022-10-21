b = []
result = []

for _ in range(10):
    a = int(input('Введите число: '))
    b.append(a)
    d = a ** 3
    result.append(d)

b.sort()
result.sort()

print(f"\nСортированные числа, которые мы ввели с клавиатуры: {b}")
print(f"Сортированные числа, которые вы ввели в степень 3: {result}")

b.sort(reverse=True)
result.sort(reverse=True)

print(b)
print(result)
