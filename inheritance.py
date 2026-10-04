class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"Vehicle {self.model} is starting...")

    def stop(self):
        print("Vehicle is stopping...")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels 



class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels



car = Car("Toyota", "Camry", 2022, 4, 4)
bike = Bike("Honda", "CBR500R", 2021, 2)

car.start()
bike.start()