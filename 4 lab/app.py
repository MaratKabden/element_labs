from typing import List


class Person:
    age: int
    fullName: str

    def __str__(self):
        return self.fullName


class Engine:
    power: int
    company: str

    def __init__(self, power, company):
        self.power = power
        self.company = company

    def __str__(self):
        return str(self.power) + "hp " + str(self.company)


class Driver(Person):
    experience: int

    def __init__(self, experience):
        self.experience = experience

    def __str__(self):
        return str(self.experience)


class Car:
    carClass: str
    engine: Engine
    driver: Driver
    marka: str

    def __init__(self, carClass, engine, driver, marka):
        self.carClass = carClass
        self.engine = engine
        self.driver = driver
        self.marka = marka

    def __str__(self):
        return "Вы на " + str(self.marka) + " " + str(self.carClass) + " " + str(self.engine)

    def start(self):
        return "Поехали"

    def stop(self):
        return "Останавливаемся"

    def turnRight(self):
        return "Поворот направо"

    def turnLeft(self):
        return "Поворот налево"


class Lorry(Car):
    carrying: int


class SportCar(Car):
    speed: float


engine = Engine(power=300, company="BMW")
driver = Driver(4)
car = Car("sport", engine, driver, "BMW")

cars: List[Car] = []
cars.append(car)

while (True):
    print("Привет пожайлуйста, выберите ваше действие:")
    print("1. Завести машину")
    print("2. Заглушить машину")
    print("3. Повернуть направо")
    print("4. Повернуть налево")
    print("5. Получить информацию о машине")
    print("0. Завершить поездку")

    action = int(input())
    print()
    if action == 0:
        break
    if action == 1:
        print(car.start())
    if action == 2:
        print(car.stop())
    if action == 3:
        print(car.turnRight())
    if action == 4:
        print(car.turnLeft())
    if action == 5:
        print(car.__str__())
    print()