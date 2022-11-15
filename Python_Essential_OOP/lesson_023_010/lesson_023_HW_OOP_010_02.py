# Ready
import json
import re


data_frame = []

def data():
    with open('data_02.txt', 'r') as file:
        for row in file:
            if re.match(r'\w+[@]\w+[.]\w+', row):
                print(f'Електронный адресс: {row}')
                data_frame.append(row)
            if re.match(r'[+\]{0}[0-9]{12}', row) and len(row) == 14:
                print(f'Номер телефона: {row}')
                data_frame.append(row)
            if re.match(r'\d{2}.\d{2}.\d{4}', row):
                print(f'Дата рождения: {row}')
                data_frame.append(row)

data()


def save_data():
    # Функция сохранения файла с данными
    with open('../../data_frame_02.json', 'w') as f:
        json.dump(data_frame, f)

save_data()
