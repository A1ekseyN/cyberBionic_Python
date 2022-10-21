# Ready
import random

numbers = int(input("Введите количество чисел в списке: "))
new_list = []

for _ in range(numbers):
    new_list.append(random.randint(1, 100))

s_nbr = int(input("Введите число, для проверки его присутствия в new_list: "))
s_nbr_count = 0
s_pos = []
s_pos_count = 0

for i in new_list:
    s_pos_count += 1
    if i == s_nbr:
        s_nbr_count += 1
        s_pos.append(s_pos_count)

if s_nbr_count != 0:
    print(f"\nЧисло {s_nbr} встречается - {s_nbr_count} раз. На ", end='')
    for i in sorted(s_pos):
        print(f"{i}", end='')
        s_nbr_count -= 1
        if s_nbr_count > 0:
            print(end=', ')
    print(" позициях.")
else:
    print(f"\nЧисло {s_nbr} не встречаетс в списке new_list.")
