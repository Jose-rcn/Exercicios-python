from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

# Utilizando as fábricas específicas
car_factory = CarFactory()
car = car_factory.create_vehicle()
print(car.drive())  # Output: Driving a car

bike_factory = BikeFactory()
bike = bike_factory.create_vehicle()
print(bike.drive())  # Output: Riding a bike
