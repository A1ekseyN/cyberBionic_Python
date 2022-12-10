# Ready
# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.

import json


data_cars = {'bmw e30': '3000',
     'subaru wrx sti': '9000',
     }

with open('data_025_03_01.json', 'w') as file:
    json.dump(data_cars, file)

with open('data_025_03_01.json', 'r') as json_file:
    data_loaded_cars = json.load(json_file)
    for i in data_loaded_cars:
        print(f'Цена на автомобиль {i.title()} составляет - {data_loaded_cars[i]} $.')
