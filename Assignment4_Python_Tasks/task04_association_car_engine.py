class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def show_engine(self):
        return f"engine power: {self.horsepower} HP"


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def show_car(self):
        print(f"{self.brand} has {self.engine.show_engine()}")


if __name__ == "__main__":
    engine = Engine(300)
    car = Car("BMW", engine)
    car.show_car()
