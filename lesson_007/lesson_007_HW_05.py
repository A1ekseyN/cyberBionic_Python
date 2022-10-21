# Ready
import random
import time

words_list = []
word = ''
abc_list = 'qwertyuiopasdfghjklzxcvbnm'

words_value = int(input("Рекомендовано к генерации: 10.000 - 30.000 слов.\nГенерируем: "))

start_time = time.time()

for _ in range(words_value):
    for _ in range(5):
        word = (word + random.choice(abc_list))
    words_list.append(word)
    word = ''

duplicate = []

for i in words_list:
    if words_list.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
        if len(duplicate) == 1:
            print(f"\nНайдено совпадения: {i}", end=', ')
        elif len(duplicate) > 1:
            print(i, end=', ')

print(f"\n\nВ словаре повторяются значения:", end='')
for i in sorted(duplicate):
    print(f"\n\t- {i}: {i.count(i)} раз.", end='')

print(f"\n\nСкрипт выполнен за {time.time() - start_time:,.2f} сек.")
