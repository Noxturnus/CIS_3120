#Example 1: Vehicle Inheritance

# Case class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.!")

    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped.!")


# Subclass 1: Car
class Car(Vehicle):
    def __init__(self, brand, model, door):
        super().__init__(brand, model)
        self.door = door

    def describe(self):
        print(f"This car is {self.brand} {self.model} and has {self.door} doors.")

    def honk(self):
        print("Beep Beep Beep")


# Subclass 2: Bike
class Bike(Vehicle):
    def __init__(self, brand, model, type_bike):
        super().__init__(brand, model)
        self.type_bike = type_bike

    def describe(self):
        print(f"This bike is {self.brand} {self.model} and {self.type_bike} type.")

    def ring(self):
        print("Ring Ring Ring")


#Define the main and create objects


def main():
    car1 = Car("Tesla", "Y", 4)
    bike1 = Bike("Honda", "Air", "road")

    #Use the inheried and subclass methods
    car1.start_engine()
    car1.describe()
    car1.honk()
    car1.stop_engine()

    print("-----------------------------")

    bike1.start_engine()
    bike1.describe()
    bike1.ring()
    bike1.stop_engine()


main()
