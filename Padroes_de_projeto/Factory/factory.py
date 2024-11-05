from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self,tipo):
        ...
class Cachorro(Animal):
    def falar(self):
        print("AUAUAU")
        
class Gato(Animal):
    def falar(self):
        print("miau")
class Vaca(Animal):
    def falar(self):
        print("MUUUUUUUU")
class Fabrica:
    def criar_animal_falante(self,tipo):
        return eval(tipo+"()").falar()
#Clente
if __name__ == "__main__":
    fab = Fabrica()
    animal = input("Qual animal deve falar?")
    fab.criar_animal_falante(animal)