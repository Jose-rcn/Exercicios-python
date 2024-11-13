from abc import ABC, abstractmethod

class velocimetro(ABC):
    def __init__(self):
        self._velocidade = None
    @abstractmethod
    def get_velocidade(self):
        ...
    @abstractmethod
    def set_velocidade(self,value):
        ...
class rodas(ABC):
    def __init__(self):
        self._raio = None
    @abstractmethod
    def get_raio(self):
        ...
    @abstractmethod
    def set_raio(self,value):
        self._raio = value
class velocimetro_aereo(velocimetro):
    def get_velocidade(self):
        return f"{self._velocidade} m/s"
    def set_velocidade(self, value):
        self._velocidade = value
    
class velocimetro_terrestre(velocimetro):
    def get_velocidade(self):
        return f"{self._velocidade}km/h"
    def set_velocidade(self, value):
        self._velocidade = value
        
class rodas_aereo(rodas):
    def get_raio(self):
        return f"{self._raio} cm"
    def set_raio(self, value):
        self._raio = value

class rodas_terrestre(rodas):
    def get_raio(self):
        return f"{self._raio} m"
    def set_raio(self, value):
        self._raio = value
        
class Factory(ABC):
    @abstractmethod
    def criar_rodas(self):
        ...
    @abstractmethod
    def criar_velocimetro(self):
        ...
class Factoy_veiculo_terrestre(Factory):
    def criar_rodas(self):
        roda = rodas_terrestre()
        roda.set_raio(0.15)
        return roda
    def criar_velocimetro(self):
        velocimetro =  velocimetro_terrestre()
        velocimetro.set_velocidade(0)
        return velocimetro

class Factory_veiculo_aereo(Factory):
    def criar_rodas(self):
        roda = rodas_terrestre()
        roda.set_raio(15)
        return roda
    def criar_velocimetro(self):
        velocimetro = velocimetro_aereo()
        velocimetro.set_velocidade(10)
        return velocimetro

if __name__ == "__main__":
    fabrica_aereo = Factory_veiculo_aereo()
    vel = fabrica_aereo.criar_velocimetro()
    roda = fabrica_aereo.criar_rodas()
    vel.set_velocidade(100)
    print(vel.get_velocidade())
    