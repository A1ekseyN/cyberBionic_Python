# Ready
import re


ask = input('Введите информацию:\n>>> ')

mail_lst = []
birth_date_lst = []
name_lst = []
comment_lst = []


def data_frame():
    # email
    mail = re.findall(r'\w+[@]\w+[.]\w+', ask)
    for i in mail:
        mail_lst.append(i)

    # Дата рождения
    birth_date = re.findall('\d{2}[.-]\d{2}[.-]\d{4}', ask)
    for i in birth_date:
        birth_date_lst.append(i)

    # Имя и фамилия
    name_en = re.findall(r'[A-Z]\w+\s[A-Z]\w+', ask)
    name_ru = re.findall(r'[А-Я]\w+\s[А-Я]\w+', ask)
    for i in name_en:
        name_lst.append(i)
    for j in name_ru:
        name_lst.append(j)

    # Комментарий
    global comment_en
    comment_en = re.findall(r'[,.a-zA-Z0-9@\s-]+', ask)
    comment_ru = re.findall(r'[,.а-яА-Я0-9@\s-]+', ask)
    for i in comment_en:
        comment_lst.append(i)
    if len(comment_lst) == 0:
        for j in comment_ru:
            comment_lst.append(j)

data_frame()

print(f'Имя и фамилия: {name_lst[0]}')
print(f'Email: {mail_lst[0]}')
print(f'Дата рождения: {birth_date_lst[0]}')
print(f'Комментарий: {comment_lst}')
