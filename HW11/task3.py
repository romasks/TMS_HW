class Car:
    def __init__(self, color, type, year) -> None:
        self.color = color
        self.type = type
        self.year = year

    def start(self) -> None:
        print("Автомобиль заведён")

    def stop(self) -> None:
        print("Автомобиль заглушен")

    def set_color(self, color) -> None:
        self.color = color

    def set_type(self, type) -> None:
        self.type = type

    def set_year(self, year) -> None:
        self.year = year

    def __str__(self) -> str:
        return f"цвет: {self.color}, тип: {self.type}, год выпуска: {self.year}"

car = Car("синий металлик", "седан", "2001")

car.start()
print(car)
car.stop()

car.set_color("красный")
car.set_type("хэтчбек")
car.set_year("2010")

car.start()
print(car)
car.stop()