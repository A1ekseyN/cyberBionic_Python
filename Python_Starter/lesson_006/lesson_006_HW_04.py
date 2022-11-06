# Ready
import random
import time

numbers = random.randint(10, 100)
a = []

for _ in range(numbers):
    a.append(random.randint(1, 100))

print(f"Количество элементов в списке: {len(a)}")

print(f"Элементы в списке:", end='')
for i in a:
    print(f" {i}", end='')
    if i != a[-1]:
        print("", end=',')
    else:
        print("", end=".")

while True:
    d = input("\n\nОтобразить элементы списка в обратном порядке. Введите: 1"
                  "\nОтобразить элементы по возрастанию. Введите: 2"
                  "\nДля выхода нажмине: 'exit', 'quit', 'e', 'q'."
                  "\nВведите 1 или 2: ")
    if d == '1':
        print(f"Элементы списка в обратном порядке: {a[::-1]}.")
        time.sleep(5)
        continue
    elif d == '2':
        a_copy = a
        a_copy.sort()
        asorted = a_copy
        print(f"Элементы списка сортированы по возрастанию: {asorted}.")
        time.sleep(5)
        continue
    elif d == 'e' or d == 'exit' or d == 'q' or d == 'quit':
        print(f'\nВы завершили выполнение скрипта \U00002665 \U00002665 \U00002665.')
        break
    else:
        continue
