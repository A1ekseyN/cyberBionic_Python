# Ready
class Worker:
    # Класс для рабочего
    def __init__(self, name, surname, department, year):
        self.name = name
        self.surname = surname
        self.department = department
        self.year = year

    def __str__(self):
        return f'Имя и фамилия: {self.name} {self.surname}\nОтдел: {self.department}\nУстроился в {self.year} году.'


worker_01 = Worker('Beves', 'Budhead', 'farmer', 2020)
print(f'{worker_01}\n')

def add_worker():
    # Функция создания нового рабочего
    global worker_02
    try:
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        department = input('Введите департамент: ')
        year = int(input('Введите год начала работы: \n'))
    except ValueError:
        print('Вы ввели данные не правильного типа.\nПроверьте или вы правильного ввели год.')

    try:
        worker_02 = Worker(name, surname, department, year)
    except UnboundLocalError:
        print('Есть ошибки при вводе данных. Попробуйте еще раз.\n')
        add_worker()


add_worker()

print(worker_02)
