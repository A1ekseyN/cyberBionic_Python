# Ready
class Car:
    # Класс для описания автомобиля
    def __init__(self, name, year, color, mileage):
        self.name = name
        self.year = year
        self.color = color
        self._mileage = mileage

    def set_mileage(self, value):
        self._mileage = value

    def __str__(self):
        return f'Модель: {self.name}\nГод: {self.year}\nЦвет: {self.color}\nПробег: {self._mileage} км.\n'


car_01 = Car('BMW e30', '1985', 'red', 260000)

print(car_01)
car_01.set_mileage(400000)
print(car_01)
