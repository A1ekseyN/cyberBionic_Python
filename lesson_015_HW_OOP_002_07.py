# Ready
class Transport():
    # Общий класс для траспорта.
    @staticmethod
    def drive():
        return 'Весь транспорт может передвигаться'


class Car(Transport):
    # Класс для автомобиля.
    @staticmethod
    def drive():
        return 'Машины могут ездить по земле'


class Bike(Car):
    # Класс для велосипедов
    @staticmethod
    def bike():
        return 'Велосипеды, так же, как и машины могут передвигаться по земле. Но, нужно крутить педали'


class Fly(Transport):
    # Класс для самолетов
    @staticmethod
    def fly():
        return 'Самолеты летают по воздуху'


print(f"Транспорт - {Transport.drive()}.")
print(f"Автомобили - {Car.drive()}.")
print(f"Велосипеды - {Bike.bike()}.")
print(f"Самолеты - {Fly.fly()}.")
