class Car():
    # Класс для описания автомобиля
    def __init__(self, name, year, color, mileage):
        self.name = name
        self.year = year
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f"Модель: {self.name} \nГод: {self.year} \nЦвет: {self.color} \nПробег: {self.mileage}\n"

    def __str__(self):
        return f"Модель: {self.name} \nГод: {self.year} \nЦвет: {self.color} \nПробег: {self.mileage}\n"


car_01 = Car('BMW e30', '1985', 'red', '260.000')
car_02 = Car('Passat b5', '2003', 'black', '265.000')
car_03 = Car('Passat b8', '2015', 'white', '120.000')
car_04 = Car('Toyota Corolla', '2006', 'silver', '50.000')
cars_showroom = [car_01, car_02, car_03, car_04]


def sell_car():
    # Функция продажи автомобиля.
    while cars_showroom:
        print("--- На диллерской площадке стоят автомобили: ---\n")
        for i in cars_showroom:
            print(i)
        sell_index = int(input(f"Какую по номеру машину вы ходите приобрести? (1 - {len(cars_showroom)}) \n"))
        sell_index -= 1
        del cars_showroom[sell_index]
    print("\n--- Мы продали все автомобили. ---")


sell_car()
