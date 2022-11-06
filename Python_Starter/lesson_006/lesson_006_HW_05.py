# Ready
import random

numbers = int(input("Введите количество чисел в списке: "))
int_list = []
new_list = []

for _ in range(numbers):
    int_list.append(random.randint(1, 100))

for i in int_list:
    if i % 2 == 1:
        new_list.append(i)

repeat = int(input("Сколько раз повторить список с непарными числами: "))

repeated_n = new_list * repeat
int_list.clear()

print(f"\nСодержимое new_list: {repeated_n}.")
print(f"Содержимое int_list: {int_list}.")
