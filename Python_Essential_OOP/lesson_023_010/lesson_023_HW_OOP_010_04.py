# Ready
import re


ask = input('Введите текст:\n>>> ')
words = []
lst_unique = []


def word_analysis():
    result = re.findall(r'[a-zA-Z]\w+', ask)
    for i in result:
        words.append(i)

    for j in result:
        if j not in lst_unique:
            lst_unique.append(j)

word_analysis()

print(f'\nВсего в тексте - {len(words)} слов.\nИз них - {len(lst_unique)} уникальных слова.')
print(lst_unique)
