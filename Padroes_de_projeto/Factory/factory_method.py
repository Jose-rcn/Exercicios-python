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

class Motorcicle(Vehicle):
    def drive(self):
        return " Riding a motorcicle"

class Factory(ABC):
    @staticmethod
    @abstractmethod
    def create_vehicle(tipe:str)->Vehicle:
        pass

class Factory_store_A(Factory):
    @staticmethod
    def create_vehicle(tipe:str)->Vehicle:
        if tipe == 'motorcicle':
            return Motorcicle()
        raise NameError(f'No vehicle named "{tipe}"')

class Factory_store_B(Factory):
    @staticmethod
    def create_vehicle(tipe:str)-> Vehicle:
        if tipe == 'motorcicle':
            return Motorcicle()
        if tipe == 'car':
            return Car()
        if tipe == 'bike':
            return Bike()
        raise NameError(f'No vehicle named "{tipe}"')

# Utilizando as fábricas específicas
try:
    car_A = Factory_store_A.create_vehicle('car') #Error
except NameError:
    print('No vehicle with this name in this store')

try:
    car_B = Factory_store_B.create_vehicle('car')
    print(car_B.drive())  # Output: Riding a bike
except NameError:
    print('No vehicle with this name in this store')

