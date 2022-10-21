# Ready
from sympy import *
import numpy as np

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
result = []

for i in range(a, b + 1):
    if isprime(i):
        result.append(i)

print(f"\nПростые числа в диапазоне {a} - {b}: {result}.")

while True:
    d = input("\n1. Показать сумму чисел"
              "\n2. Показать произведение чисел"
              "\n3. Для выхода нажмите 'e', 'exit', 'q', 'quit', '3'."
              "\n\nВведите 1, 2 или 3: ")
    if d == '1':
        print(f"\nСумма чисел: {sum(result)}.")
    elif d == '2':
        result = np.prod(np.array(result))
        print(f"Произведение чисел: {result:,.0f}.")
    elif d == 'e' or d == 'exit' or d == 'q' or d == 'quit' or d == '3':
        break
    else:
        continue
