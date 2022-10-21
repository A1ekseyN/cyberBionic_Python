# Ready
import random

numbers = random.randint(1, 100)
a = []

for _ in range(numbers):
    a.append(random.randint(1, 100))

print(f"Минимальное число из списка: {min(a)}")
print(f"Максимальное число из списка: {max(a)}")
print(f"Сумма всех чисел из списка: {sum(a):,.0f}")
print(f"Среднее арифметическое чисел из списка: {round(sum(a) / len(a), 1)}")
