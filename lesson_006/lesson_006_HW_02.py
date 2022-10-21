# Ready
import random

a = int(input("Сколько чисел сгенерировать в 1-м списке: "))
b = int(input("Сколько чисел сгенерировать во 2-м списке: "))

aa = []
bb = []
unique_number = []
not_unique_number = []

for _ in range(a):
    aa.append(random.randint(1, 100))
for _ in range(b):
    bb.append(random.randint(1, 100))

print(aa)
print(bb)

for i in aa:
    for j in bb:
        if i == j:
            if i in enumerate(unique_number):
                continue
        if i == j and i not in unique_number:
            unique_number.append(i)
        elif i != j:
            if i in enumerate(not_unique_number):
                continue
            elif i not in not_unique_number and i not in not_unique_number:
                not_unique_number.append(i)
for j in bb:
    if j not in not_unique_number:
        not_unique_number.append(j)

for i in unique_number:
    for j in unique_number:
        if i == j:
            unique_number.remove(i)

for i in unique_number:
    for j in not_unique_number:
        if i == j:
            not_unique_number.remove(i)

print(f"\nУникальные числа, которые содержаться в двух списках: {sorted(unique_number)}.")
print(f"Числа, которые не содержаться в двух списках: {sorted(not_unique_number)}.")
